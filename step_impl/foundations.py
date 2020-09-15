import boto3
import csv, json
from getgauge.python import after_spec, before_spec, data_store, registry, step, Messages
from getgauge.registry import _get_step_value
from io import StringIO
from tabulate import tabulate
from time import sleep

from pprint import pprint


# --------------------------
# Gauge step implementations
# --------------------------

@step("Find users in credential report with: <table>")
def all_users_in_credential_report_have(table):
    # Get credential report generated at Spec start
    report = data_store.spec['credential_report']

    # Create a dict from the table values, splitting the comma-separated
    # "Value" column into a list.
    # Ex: {'password_enabled': ['true','not_supported], 'mfa_active': ['false']}
    non_compliant_field_values = {row[0]: ','.split(row[1]) for row in table}

    # Check report for records matching ALL values in the table
    non_compliant_creds = []
    for record in report:
        for field in non_compliant_field_values:
            if record[field] not in non_compliant_field_values[field]:
                break
        else:
            non_compliant_creds.append(record)

    # Create Markdown-based table to output if test fails
    # FIXME: Limit output to just the fields in the table plus the 'user' column
    fail_output = tabulate(non_compliant_creds, headers='keys', tablefmt='github')

    assert len(non_compliant_creds) == 0, f"Non-compliant credentials:\n{fail_output}"


@step("Managed Config Rule <rule_source_id> must be enabled")
def confirm_managed_config_rule_enabled(rule_source_id):
    # Get config rule from lookup generated at Spec start
    rules = data_store.spec['managed_config_rules']
    rule = rules.get(rule_source_id)

    assert rule is not None, f"Managed Config Rule {rule_source_id} is not installed"

    rule_state = rule['ConfigRuleState']

    assert rule_state == 'ACTIVE', f"Managed Config Rule {rule_source_id} is in {rule_state} state"


@step("Managed Config Rule <rule_source_id> parameters must <match_type>: <table>")
def confirm_managed_config_rule_parameters(rule_source_id, match_type, table):
    # Get config rule from lookup generated at Spec start
    rules = data_store.spec['managed_config_rules']
    rule = rules.get(rule_source_id)

    expected_params = {row[0]:row[1] for row in table}
    actual_params = json.loads(rule['InputParameters'])

    merged_params = []
    for row in table:
        param = {
            'Parameter': row[0],
            'Expected': row[1],
            'Actual': actual_params.get(row[0], None)
        }
        merged_params.append(param)

    fail_msg_table = tabulate(merged_params, headers='keys', tablefmt='github')
    fail_msg = f"Non-compliant Parameters:\n{fail_msg_table}"

    # FIXME: Split this into separate functions
    if match_type == 'match':
        assert actual_params == expected_params, fail_msg
    elif match_type == 'contain':
        for mp in merged_params:
            assert mp['Actual'] == mp['Expected'], fail_msg
    else:
        raise ValueError(f'Invalid match_type "{match_type}". Supported values: contain, match')


# ---------------
# Execution Hooks
# ---------------

@step('Load credentials report.')
def load_credentials_report():

    # Don't re-run report if it's already loaded
    if data_store.spec.get('credential_report', None):
        return

    client = boto3.client('iam')

    report_req = client.generate_credential_report()

    # AWS does not provide a mechanism to check the status of a
    # credential report, so if it is not yet ready, wait few seconds.
    # ¯\_(ツ)_/¯
    if not report_req['State'] == 'COMPLETE':
        sleep(5)

    # Retrieve credential report
    report_resp = client.get_credential_report()

    # Get the CSV report as a string
    report_csv = report_resp['Content'].decode("utf-8")
    
    # Transform CSV string into a Python dict
    csv_sio = StringIO(report_csv)
    report_dicts = list(csv.DictReader(csv_sio))

    # Stash credential report for use in scenarios
    data_store.spec['credential_report'] = report_dicts


@before_spec()
def load_config_rules():
    client = boto3.client('config')

    config_rules_resp = client.describe_config_rules()

    all_rules = config_rules_resp['ConfigRules']

    # Create a lookup of Managed Rules by SourceIdentifier (ex: IAM_PASSWORD_POLICY)
    managed_rules = {
        rule['Source']['SourceIdentifier']:rule for rule in all_rules if rule['Source']['Owner'] == 'AWS'
    }

    # Stash credential report for use in scenarios
    data_store.spec['managed_config_rules'] = managed_rules

@after_spec
def what_in_the_registry(context):
    import inspect

    for step_text in registry.steps():
        step_info = registry.get_info_for(_get_step_value(step_text))
        print(f'step_info.step_text: {step_info.step_text}')
        print(f'step_info.parsed_step_text: {step_info.parsed_step_text}')
        print('step_info.impl:')
        lines, line_no = inspect.getsourcelines(step_info.impl)
        pprint(lines)
        print(f'step_info.instance: {step_info.instance}')
        print(f'step_info.aliases: {step_info.aliases}')
        print(f'step_info.span: {step_info.span}')

