from blog.security import flask_bcrypt
from sqlalchemy import Column, Integer, String, Boolean, LargeBinary
from blog.models.database import db

from flask_login import UserMixin
from sqlalchemy.orm import relationship


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(120), unique=False, nullable=False, default="", server_default="")
    last_name = Column(String(120), unique=False, nullable=False, default="", server_default="")
    username = Column(String(80), unique=True, nullable=False)
    is_staff = Column(Boolean, nullable=False, default=False)
    email = Column(String(255), unique=True, nullable=False, default="", server_default="")
    #email = Column(String(250), unique=True)
    #password = Column(String(250))
    _password = Column(LargeBinary, nullable=True)
    # Нужен для security!
    #active = db.Column(db.Boolean())
    author = relationship('Author', uselist=False, back_populates='user')

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = flask_bcrypt.generate_password_hash(value)

    def validate_password(self, password) -> bool:
        return flask_bcrypt.check_password_hash(self._password, password)


def __repr__(self):
    return f"<User #{self.id} {self.username!r} {self.password}>"
