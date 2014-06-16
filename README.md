First set up your virtualenv

Run pip install -r requirements.txt to get all packages.

Be sure to add the following to venv/bin/activate so you can run tests from the home directory of the app:
export PYTHONPATH="PATHTOYOURAPP:$PYTHONPATH"
