from app import app, db
from app.model import *

def get_group_by_id(id):
    return Group.query.filter_by(id = id).first()

def create_group(name, budget):
    group = Group(
        name = name,
        budget = budget
    )

    db.session.add(group)
    db.session.commit()

    return group.id

def get_user_by_id(id):
    return User.query.filter_by(id = id).first()


def create_user(name, ):
    user = User(name = name)

    db.session.add(user)
    db.session.commit()

    return user.id

def add_user_to_group(group_id, user_id):
    log = UserGroup(
        group_id = group_id,
        user_id = user_id
    )

    db.session.add(log)
    db.session.commit()

def get_users_in_group(group_id):
    return UserGroup.query.filter_by(group_id = group_id).all()

def add_santa(santa_id, recipient_id, group_id):
    log =  UserSanta(
        santa_id = santa_id,
        recipient_id = recipient_id,
        group_id = group_id
    )

    db.session.add(log)
    db.session.commit()

def get_by_santa(santa_id):
    return UserSanta.query.filter_by(santa_id = santa_id).all()