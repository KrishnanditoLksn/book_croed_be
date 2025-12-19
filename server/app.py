from flask  import Flask,jsonify
from flask_cors import CORS
from utils.util import BOOKS
# from urllib.parse import quote as url_quote


app = Flask(__name__)
app.config.from_object(__name__)


CORS(app, resources={r'/*': {'origins': '*'}})




@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/books' , methods=['GET'])
def getAllBooks():
    return jsonify({
        'status':'Success',
        'books' : BOOKS
    })

if __name__ == '__main__':
    app.run()
