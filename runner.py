import os
import argparse
import subprocess
from features import environment
import argparse
import subprocess
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--testdir', required=False, help="File path")
    parser.add_argument('--env-file', required=False, help="Path to environment properties file")
    args = parser.parse_args()

    os.environ['ENVIRONMENT_PROPERTY'] = args.env_file

    testdir = args.testdir
    env_file = 'properties/' + args.env_file +'.properties'

    print("Test Directory Path:", testdir)
    print("Environment Properties File:", env_file)

    # Prepare the Behave command
    c = f'behave --no-capture --junit --junit-directory=reports --define env_file={env_file} {testdir}'
    # subprocess.run(c, shell=True, check=True)

    try:
        # Run the behave command
        result = subprocess.run(c, shell=True, check=True)
        return_code = result.returncode
        print(f"Command executed successfully with return code: {return_code}.")
    except subprocess.CalledProcessError as e:
        print(f"Command '{e.cmd}' returned non-zero exit status {e.returncode}.")
        sys.exit(e.returncode)



# Examples how to run tests:
# python runner.py --testdir features/feature_scenarios/Sample_feature --env-file production.properties
# python runner.py --testdir features/feature_scenarios/Sample_feature --env-file development.properties


