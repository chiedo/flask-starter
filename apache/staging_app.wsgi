import sys
os.environ["FLASK_ENV"] = "staging"
#sys.path.insert(0, '/path/to/the/application')
from webapp import app as application
