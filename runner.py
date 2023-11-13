# import subprocess
# if __name__ == '__main__':
# #command line args along with error capture on failure with check true
#       s = subprocess.run('behave --no-capture',shell=True, check=True)

# to run specifying feature path at testdir: python runner.py --testdir=features
# for example:python runner.py --testdir=features/feature_scenarios/second ; this runs only features in this given path
#-----------------------------------------------------------------------------------------------
import argparse
import subprocess

from features import environment

import argparse
import subprocess

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--testdir', required=False, help="File path")
    parser.add_argument('--env-file', required=False, help="Path to environment properties file")
    args = parser.parse_args()

    testdir = args.testdir
    env_file = args.env_file

    print("Test Directory Path:", testdir)
    print("Environment Properties File:", env_file)

    # Prepare the Behave command
    c = f'behave --no-capture --junit --define env_file={env_file} {testdir}'
    subprocess.run(c, shell=True, check=True)


# python runner.py --testdir features/feature_scenarios/Sample_feature --env-file production.properties
#
#
# python runner.py --testdir features/feature_scenarios/Sample_feature --env-file development.properties


