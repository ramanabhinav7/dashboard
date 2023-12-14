from flask import Flask, render_template, request, Response
from flask_pymongo import PyMongo
from bson import ObjectId
import json
from simplejson import JSONEncoder

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)  # Convert ObjectId to its string representation
        return super().default(obj)

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://jaishreemahakal:12345@cluster0.vmunvmt.mongodb.net/blackoffer'
mongo = PyMongo(app)
app.json_encoder = CustomJSONEncoder

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data', methods=['GET'])
def get_data():
    filter_params = request.args.to_dict()
    data = list(mongo.db.data1.find(filter_params))
    json_data = json.dumps(data, cls=CustomJSONEncoder)
    return Response(json_data, content_type='application/json')

if __name__ == '__main__':
    app.run(debug=True)
