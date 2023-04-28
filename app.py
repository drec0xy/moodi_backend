import os 
from flask import Flask, jsonify


app = Flask(__name__)
 
"""
from firebase_admin import credentials, firestore, initialise_app 

moodi = credentials.Certificate('key.json')
default_app = initialise_app(moodi)
db = firestore.client()
todo_ref = db.collection('todo')
"""

@app.route('/add', methods=['POST'])
def create():
    """
        create() : Add document to Firestore collection with request body.
        Ensure you pass a custom ID as part of json body in post request,
        e.g. json={'id': '1', 'title': 'Write a blog post'}
    """
    return jsonify({"Post-success🚀":"True"})

@app.route('/list', methods=['GET'])
def read():
    """
        read() : Fetches documents from Firestore collection as JSON.
        todo : Return document that matches query ID.
        all_todos : Return all documents.
    """
    return "Get-success🚀 True"

@app.route('/update', methods=['POST', 'PUT'])
def update():
    """
        update() : Update document in Firestore collection with request body.
        Ensure you pass a custom ID as part of json body in post request,
        e.g. json={'id': '1', 'title': 'Write a blog post today'}
    """
    return jsonify({"Update-success🚀":"True"})

@app.route('/delete', methods=['GET', 'DELETE'])
def delete():
    """
        delete() : Delete a document from Firestore collection.
    """
    return "Delete-success🚀 True"

port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)

