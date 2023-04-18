from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {'id': 1, 'name': 'Richard P.', 'email': 'ric.ric@example.com'},
    {'id': 2, 'name': 'Jhow Jhow', 'email': 'jhow.jhow@example.com'},
    {'id': 3, 'name': 'Bob', 'email': 'bob.smith@example.com'}
]

@app.route('/')
def hello_world():
    return 'Página inicial!'

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for user in users:
        if user['id'] == user_id:
            return jsonify(user), 200
    return jsonify({'error': 'User not found'}), 404

@app.route('/api/users', methods=['GET'])
def get_users():
    response = {'users': users}
    return jsonify(response), 200

if __name__ == '__main__':
    app.run()
