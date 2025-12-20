from flask  import Flask,jsonify , request
from flask_cors import CORS
from utils.util import BOOKS
import requests

app = Flask(__name__)
app.config.from_object(__name__)


CORS(
    app, 
    resources={r'/*': {'origins': '*'}}
)



@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/books' , methods=['GET'])
def getAllBooks():
    return jsonify({
        'status':'Success',
        'books' : BOOKS
    })

@app.route('/books/add' , methods=['POST'])
def postBook():
    book_request =  request.get_json()
    
    BOOKS.append({
        'title':book_request.get('title'),
        'author':book_request.get('author'),
        'read':False
    })
    
    return jsonify({
        'status':'Success',
        'messsage':'Book Successfully Added to List'
    })



if __name__ == '__main__':
    app.run()
