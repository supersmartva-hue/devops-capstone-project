from flask import Blueprint, jsonify, request
from .models import accounts, create_account, list_accounts, read_account, update_account, delete_account

api_bp = Blueprint('api', __name__)

@api_bp.route('/', methods=['POST'])
def create():
    data = request.json
    account = create_account(data)
    return jsonify(account), 201

@api_bp.route('/', methods=['GET'])
def list_all():
    return jsonify(list_accounts()), 200

@api_bp.route('/<int:account_id>', methods=['GET'])
def read(account_id):
    acc = read_account(account_id)
    if acc:
        return jsonify(acc), 200
    return jsonify({"error": "Not found"}), 404

@api_bp.route('/<int:account_id>', methods=['PUT'])
def update(account_id):
    data = request.json
    acc = update_account(account_id, data)
    if acc:
        return jsonify(acc), 200
    return jsonify({"error": "Not found"}), 404

@api_bp.route('/<int:account_id>', methods=['DELETE'])
def delete(account_id):
    delete_account(account_id)
    return jsonify({"message": "Deleted"}), 200
