from flask import redirect,flash,request, render_template, session, make_response
from app import app
from app import db_ops
import random

@app.route("/group/<id>", methods = ["GET"])
def get_group_by_id(id):
    return db_ops.get_group_by_id(id).__repr__()

@app.route("/group/new/", methods = ["POST"])
def create_group():
    name = request.args["name"]
    budget = request.args["budget"]

    id = db_ops.create_group(name, budget)

    return str(id) 

@app.route("/group/participants/<id>")
def get_participants(id):
    return str([ db_ops.get_user_by_id(i.user_id).__repr__() for i in db_ops.get_users_in_group(id)])

@app.route("/group/add", methods = ["POST"])
def add_participants():
    group_id = request.args["group_id"]
    user_id = request.args['user_id']

    db_ops.add_user_to_group(group_id, user_id)

    return "sucess"

@app.route("/group/price-limit/<id>")
def get_price_limit(id):
    return str(get_group_by_id(id).budget)

@app.route("/group/generate/<id>", methods = ["POST"])
def generate(id):
    
    users_in_group = [i.user_id for i in db_ops.get_users_in_group(id)]
    random.shuffle(users_in_group)

    [db_ops.add_santa(users_in_group[i], users_in_group[i+1 % (len(users_in_group)-1)], id) for i in range(len(users_in_group))]

    return "succses"


@app.route("/user/new", methods = ["POST"])
def new_user():
    name = request.args["name"]
    return str(db_ops.create_user(name, ))

@app.route("/user/<id>")
def get_user_by_id(id):
    return db_ops.get_user_by_id(id).__repr__()

@app.route("/secret-santa/get/<id>")
def get_recipient(id):
    return str([db_ops.get_user_by_id(i.recipient_id).__repr__() for i in db_ops.get_by_santa(id)])