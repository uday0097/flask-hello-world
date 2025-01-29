from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to the Greeting API</h1><p>Use the <code>/greet</code> endpoint to get a greeting message.</p><p>For API documentation, visit <a href='/api-docs'>/api-docs</a>.</p>"

@app.route('/greet', methods=['GET'])
def greet():
    
    name = request.args.get('name')
    
    if name:
        return jsonify({"message": f"Hi, {name}!"})
    else:
        return jsonify({"error": "Please specify a name in the 'name' query parameter."}), 400

@app.route('/api-docs', methods=['GET'])
