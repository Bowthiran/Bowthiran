from flask import Flask,render_template,request
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

def connect_MongoDB():
    client = MongoClient("mongodb://localhost:27017")
    db = client['collage']
    return db

@app.route('/<value>')
def wellcome_msg(value):
    return "Hello "+str(value.capitalize())

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/home',methods=['POST'])
def home_post():
    db = connect_MongoDB()
    user_data = db['student']
    name = request.form["name"]
    age = request.form["age"]
    Group = request.form["Group"]
    Depart = request.form["Depart"]
    user_data.insert_one({"name":name,"age":age,"Group":Group,"Depart":Depart})
    return render_template('add data.html')

@app.route('/add data')
def add_data():
    return render_template('add data.html')

@app.route('/show data',methods=['GET'])
def show_data():
    db = connect_MongoDB()
    collection = db['student']
    user_data = list(collection.find())
    for data in user_data:
        data["_id"] = str(data["_id"])
    return render_template('show data.html',data=user_data)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)