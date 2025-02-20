import requests
import json
import os

def create_new_relic_event(message, outcome, step):
    # Get the environment variables
    environment_name = os.getenv('ENVIRONMENT_PROPERTY')
    new_relic_acc_id = os.getenv('NEWRELIC_ACCOUNTID')
    nr_password = os.getenv('NEWRELIC_PASSWORD')
    operation_name = os.getenv('TEST_DIR_TO_RUN')

    url = "https://insights-collector.newrelic.com/v1/accounts"+str(new_relic_acc_id)+"/events"

    headers = {
        "Content-Type": "application/json",
        "X-Insert-Key": str(nr_password)
    }

    event_payload = {
        "eventType": "Your_NR_Table",
        "process": "Scryptonite QA Testing",
        "Test Set": operation_name,
        "scenario": message,
        "outcome": outcome,
        "step failed": step,
        "environment": environment_name
    }

    nr_response=requests.post(url, headers=headers, data=json.dumps(event_payload))

    if nr_response.status_code == 200:
        print("NR Event sent successfully")
    else:
        print(f"Failed to send NR Event: {nr_response.status_code} - {nr_response.text}")