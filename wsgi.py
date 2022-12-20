import os
from api.app import create_app

env_name = os.getenv('FLASK_ENV')
app = create_app(env_name)

if __name__ == "__main__":
    app.run(port=5000)