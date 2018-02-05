from app import db
from hashlib import md5
from werkzeug.security import generate_password_hash

class UserToken(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(64), index=True, unique=True)
    user_token = db.Column(db.String(128), index=True, unique=True)
    bot_id = db.Column(db.String(64), index=True, unique=True)
    bot_token = db.Column(db.String(128), index=True, unique=True )
    

    def __repr__(self):
        return '<User {}>'.format(self.user_id)

    # def set_user_token(self, user_token):
    #     self.user_token_hash = generate_password_hash(user_token)

    # def set_bot_token(self, bot_token):
    #     self.bot_token_hash = generate_password_hash(bot_token)
