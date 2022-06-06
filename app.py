from flask import Flask
from blueprints import index_bl,media_bl,api_resource_bl

app = Flask(__name__)
app.register_blueprint(index_bl)
app.register_blueprint(media_bl)
app.register_blueprint(api_resource_bl)


if __name__ == '__main__':
    app.run(debug=True)
