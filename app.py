from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Routes
@app.route('/', methods=['GET'])
def index():
    if 'user_id' in session:
        todos = Todo.query.filter_by(user_id=session['user_id']).all()
        return render_template('index.html', todos=todos, user=session['username'])
    return render_template('index.html', todos=[], user=None)

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    if User.query.filter_by(username=username).first():
        return 'Username already exists'
    hashed_pw = generate_password_hash(password)
    user = User(username=username, password=hashed_pw)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        session['user_id'] = user.id
        session['username'] = user.username
        return redirect(url_for('index'))
    return 'Invalid credentials'

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/add', methods=['POST'])
def add():
    if 'user_id' in session:
        content = request.form['todo']
        if content.strip():
            new_todo = Todo(content=content.strip(), user_id=session['user_id'])
            db.session.add(new_todo)
            db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    if 'user_id' in session:
        todo = Todo.query.get_or_404(id)
        if todo.user_id == session['user_id']:
            db.session.delete(todo)
            db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    new_content = request.form['updated_todo']
    todo = Todo.query.get_or_404(id)
    todo.content = new_content
    db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
