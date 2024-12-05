from app import db

class Group(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    budget = db.Column(db.Integer, unique=False, nullable=False)


    def __repr__(self,):
        return {
            'id'    :self.id,
            "name"  :self.name,
            "budget":self.budget 
            
        }

class User(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return {
            'id'    :self.id,
            "name"  :self.name
        }


class UserGroup(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)

class UserSanta(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer)
    santa_id = db.Column(db.Integer)
    recipient_id = db.Column(db.Integer)