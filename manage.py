from project import app
import os

if __name__ == '__main__':
    if os.environ['FLASK_ENV'] == 'development':
        app.run(host='0.0.0.0', debug=True)
    elif os.environ['FLASK_ENV'] == 'staging':
        app.run(host='0.0.0.0', debug=True)
    elif os.environ['FLASK_ENV'] == 'production':
        app.run(host='0.0.0.0', debug=False)
