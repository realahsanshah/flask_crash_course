from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'

db = SQLAlchemy(app)

todoList = []
class Todo(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.String(200),nullable=False)
    completed = db.Column(db.Integer,default=0)
    date_created = db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self):
        return f"<Task {self.id}>"


@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        print(task_content)
        data = dict()
        data['id'] = len(todoList)+1
        data['content'] = task_content
        data['completed'] = False
        data['date_created'] = datetime.utcnow()

        todoList.append(data)
        return redirect('/')
    else:
        return render_template('index.html')


@app.route('/getdata',methods=['GET'])
def getData():
    print(todoList)
    return todoList[0]['content']

print("App is ready")

if __name__ == "__main__":
    app.run(debug=True)