from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/greeting', methods=['POST'])
def greeting():
    data = request.get_json()
    name = data['name']
    message = f'Hello, {name}!'
    return jsonify({'message': message})

if __name__ == '__main__':
    app.run()

