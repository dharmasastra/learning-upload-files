from db import db


class UploadModel(db.Model):
    __tablename__ = 'upload'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    avatar = db.Column(db.String(300), nullable=False)

    def __init__(self, name):
        self.name = name

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'avatar': self.avatar
        }

    def save_image(self, avatar):
        self.avatar = avatar

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()