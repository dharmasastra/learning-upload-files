from flask import request
from flask_restful import Resource, reqparse
from models.upload import UploadModel


class UploadFile(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help="This field cannot be blank.")

    def __init__(self, avatar):
        self.image = avatar

    def post(self):
        ALLOWED_EXTENSION = {'png', 'jpeg', 'jpg'}

        data = UploadFile.parser.parse_args()

        file = request.files['avatar']
        format = file.filename.rsplit('.', 1)[1].lower()
        file.filename = data['name'] + '.' + format
        if format not in ALLOWED_EXTENSION:
            return {"message": "Format Invalid"}, 400
        fileSave = self.image.save(file)
        upload = UploadModel(**data)
        upload.save_image(fileSave)
        upload.save_to_db()

        return upload.json()

