from flask import Flask, Blueprint, jsonify, request

# In-memory storage
accounts = []

# Helper functions
def create_account(data):
    accounts.append(data)
    return data

def list_accounts():
    return accounts

def read_account(account_id):
    for acc in accounts:
        if acc["id"] == account_id:
            return acc
    return None

def update_account(account_id, data):
    for i, acc in enumerate(accounts):
        if acc["id"] == account_id:
            accounts[i].update(data)
            return accounts[i]
    return None

def delete_account(account_id):
    global accounts
    accounts = [acc for acc in accounts if acc["id"] != account_id]

# Blueprint
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

# Flask app
app = Flask(__name__)
app.register_blueprint(api_bp, url_prefix='/accounts')

if __name__ == "__main__":
    app.run(debug=True)
