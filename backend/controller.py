from flask import Blueprint, jsonify
from service import get_all_users

user_controller = Blueprint('user_controller', __name__)

@user_controller.route('/users', methods=['GET'])
def list_users():
    users = get_all_users()
    return jsonify(users)