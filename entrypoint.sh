#!/bin/bash

# Activate virtual environment
source /opt/venv/bin/activate

export TZ = Australia/Sydney

fail_count=0
TEST_DIR_TO_RUN="${TEST_DIR_TO_RUN}"

# Some log output
echo "_____________"
pwd
echo "_____________"
ls -la

python runner.py --testdir features/feature_scenarios/"$TEST_DIR_TO_RUN" --env-file "$ENVIRONMENT_PROPERTY"
exit_code=$?
echo "$exit_code"
if [ $exit_code -ne 0 ]; then
    echo "Python runner script failed with exit code: $exit_code"
    # Exit bash script with the same exit code
    fail_count=$((fail_count + 1))
else
    echo "Python runner script ran successfully!"
fi

# Prepare files to be retained as artifacts
cp -r /usr/src/SCRYPTONITE_QA/screenshots /usr/src/SCRYPTONITE_QA/artifacts
cp -r /usr/src/SCRYPTONITE_QA/reports /usr/src/SCRYPTONITE_QA/artifacts

cd /usr/src/SCRYPTONITE_QA/artifacts
ls

if [ $fail_count -ne 0 ]; then
    echo "$fail_count Environment/s had failures"
    exit 1
else
    echo "All tests succeeded"
fi

