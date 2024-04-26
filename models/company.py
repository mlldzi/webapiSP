from database.db import db


class Company(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    big_boss = db.Column(db.String(36), nullable=False)
    country = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Company {self.name}>'
