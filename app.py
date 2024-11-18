from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'hrmant@12'

# Configure MongoDB
app.config['MONGO_URI'] = 'mongodb://localhost:27017/forumapp'
mongo = PyMongo(app)

# Routes
@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        
        # Check if user already exists
        if mongo.db.users.find_one({'username': username}):
            flash('Username already exists')
            return redirect(url_for('register'))
        
        # Create new user
        mongo.db.users.insert_one({'username': username, 'password': password, 'likes': []})
        flash('Registration successful. Please log in.')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = mongo.db.users.find_one({'username': username})
        
        if user and check_password_hash(user['password'], password):
            session['username'] = username
            session['user_id'] = str(user['_id'])
            flash('Login successful!')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    posts = list(mongo.db.posts.find())
    return render_template('dashboard.html', posts=posts)

@app.route('/like/<post_id>')
def like(post_id):
    if 'username' not in session:
        return redirect(url_for('login'))
    
    user_id = session['user_id']
    post = mongo.db.posts.find_one({'_id': ObjectId(post_id)})
    
    if user_id not in post['likes']:
        mongo.db.posts.update_one({'_id': ObjectId(post_id)}, {'$push': {'likes': user_id}})
        flash('Post liked!')
    else:
        flash('You have already liked this post.')
    
    return redirect(url_for('dashboard'))

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    user = mongo.db.users.find_one({'username': session['username']})
    
    if request.method == 'POST':
        new_username = request.form['username']
        new_password = generate_password_hash(request.form['password']) if request.form['password'] else user['password']
        
        # Update user details
        mongo.db.users.update_one(
            {'_id': user['_id']},
            {'$set': {'username': new_username, 'password': new_password}}
        )
        
        session['username'] = new_username
        flash('Profile updated successfully!')
        return redirect(url_for('profile'))
    
    return render_template('profile.html', user=user)

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
