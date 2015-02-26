General
=====================
The code should be commented pretty thouroughly. If anything is unclear, please let me know. The goal of these examples is to make it much easier to start testing with rspec. These are not perfect tests nor are they exhaustive. You will want to write beter tests than these that covers more test cases. This is a great start though, and the other test cases should be trivial.

Testing concept examples
=====================
- Models
-- project/tests/models/test_people.py
- Views
-- project/tests/views/test_basic_pages.py
-- project/tests/views/test_people.py
- Misc classes
-- project/tests/extras/test_example_class.py
- Stubs (pretend)
-- project/tests/extras/test_example_class.py
- Mocks (mock)
-- project/tests/extras/test_example_class.py

Testing resources
=====================
- Official Flask-Testing Docs: 
-- https://pythonhosted.org/Flask-Testing/ (I will not repeat what is already in this documentation.)
- Official mock documentation
-- https://pypi.python.org/pypi/mock
- Pretend documentation
-- https://github.com/alex/pretend
