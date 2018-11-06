from flask import Flask
from flask_restful import Api
from flask_uploads import UploadSet, IMAGES, configure_uploads

from resources.upload import UploadFile

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOADED_PHOTOS_DEST'] = 'img'
app.secret_key = 'jose'
api = Api(app)
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(UploadFile, '/upload', resource_class_kwargs={'avatar': photos})


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)