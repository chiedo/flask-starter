# This may not be relevant if deployed with something like AWS
import sys
os.environ["FLASK_ENV"] = "production"
#sys.path.insert(0, '/path/to/the/application')
from webapp import app as application
