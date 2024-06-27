from flask import Flask

app = Flask(__name__)


if __name__ == '__main__':
    print("Uruchamianie aplikacji Flask...")
    app.run(debug=True)

from app import routes
