from apis import v1
from flask import Flask

app = Flask(__name__)
app.register_blueprint(v1)
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=5000)
