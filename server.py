from flask import Flask, request, jsonify, send_from_directory, render_template
from main import ExpressionAnalyzer 

app = Flask(__name__, static_folder='static')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expression = data['expression']

    analyzer = ExpressionAnalyzer()
    result = analyzer.evaluate_expression(expression)

    return jsonify({'result': result})

@app.route('/index.html')
def serve_html():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5000)
