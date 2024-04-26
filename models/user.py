from database.db import db

class User(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    company_id = db.Column(db.String(36), db.ForeignKey('company.id'), nullable=False)
    is_boss = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'