from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # __name__ just allows us to tell Flask name of file
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/todos'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(), nullable = False)

    def __repr__(self):
        return f'<Todo {self.id} {self.description}'

db.create_all()

@app.route('/') 
def index(): 
    return render_template('index.html', data = Todo.query.all())

@app.route('/create', methods=['POST'])
def create_todo():
    description = request.form.get('description', '')
    create_row = Todo(description=description)
    db.session.add(create_row)
    db.session.commit()
    return redirect(url_for('index'))


