from flask import Flask
import config


app = Flask(__name__)


if __name__ == '__main__':
    app.run(host=config.API_HOST, port=config.API_PORT, debug=config.DEBUG)