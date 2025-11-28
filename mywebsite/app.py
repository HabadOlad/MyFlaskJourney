from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__) #this program is a flask application, tells flask that this is the main application program

# Configure the database URI (using a local SQLite file for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) # Initialize SQLAlchemy

# --- Database Model ---
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'Post({self.title}, {self.date_posted})'

@app.route("/") #THis will send them to the first thing, backslash is a default which normally sends people to the index
def indexpage():
    return render_template("index.html")  #this will send them to the index page


@app.route("/portfolio") #THis will send them to the first thing, backslash is a default which normally sends people to the portfolio
def portfoliopage():
    return render_template("portfolio.html")  #this will send them to the portfolio page

@app.route("/projects") #THis will send them to the first thing, backslash is a default which normally sends people to the projects
def projectspage():
    return render_template("projects.html")  #this will send them to the projects page

@app.route("/blog")
def blogpage():
    # Query the database to get all posts, ordered by the most recent one first
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    # Pass the list of posts to the blog.html template
    return render_template("blog.html", posts=posts)

@app.route("/cv") #THis will send them to the first thing, backslash is a default which normally sends people to the cvpage
def cvpage():
    return render_template("cv.html")  #this will send them to the cv page

@app.route("/contactpage") #THis will send them to the first thing, backslash is a default which normally sends people to the contactpage
def contactpage():
    return render_template("contactpage.html")  #this will send them to the contactpage


@app.route("/zork") #THis will send them to the first thing, backslash is a default which normally sends people to the zork
def zorkpage():
    return render_template("zork.html")  #this will send them to the zork game

@app.route("/new_post", methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        # Get data from the submitted form
        post_title = request.form['title']
        post_content = request.form['content']
        
        # Create a new Post object
        new_post = Post(title=post_title, content=post_content)
        
        try:
            # Add to the database session, commit, and redirect to the blog index
            db.session.add(new_post)
            db.session.commit()
            return redirect(url_for('blogpage'))
        except:
            return "There was an issue adding your post"
    else:
        # If it's a GET request, just render the creation form
        return render_template("create_post.html")
    
@app.route("/post/<int:post_id>")
def post_detail(post_id):
    # Query the database for a post with the matching ID, or return 404 if not found
    post = Post.query.get_or_404(post_id)
    return render_template('post_detail.html', post=post)

# app.py

# Add the route without the ID, and make post_id accept a default value of None
@app.route("/edit", methods=['GET']) # New route for the index/list page
@app.route("/edit/<int:post_id>", methods=['GET', 'POST']) 
def edit_post(post_id=None):  # Make the ID optional by default
    
    # --- Start of New Logic ---
    if post_id is None:
        # If no ID is provided (user navigated to /edit), 
        # render a page showing all posts to choose from.
        all_posts = Post.query.order_by(Post.date_posted).all()
        return render_template('edit_list.html', posts=all_posts)
    # --- End of New Logic ---

    # Original logic for editing a specific post starts here
    # Retrieve the post to be edited, or return 404 if it doesn't exist
    post = Post.query.get_or_404(post_id)

    if request.method == 'POST':
        # ... (POST request handling for saving the edited post) ...
        post.title = request.form['title']
        post.content = request.form['content']

        try:
            db.session.commit()
            return redirect(url_for('post_detail', post_id=post.id))
        except:
            return "There was an issue updating your post"
    else:
        # If it's a GET request for a specific ID, render the edit form
        return render_template('edit_post.html', post=post)

@app.route("/delete/<int:post_id>", methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    
    try:
        # Delete the post object
        db.session.delete(post)
        # Commit the deletion
        db.session.commit()
        # Redirect back to the main blog page
        return redirect(url_for('blogpage'))
    except:
        return "There was a problem deleting that post"
    


#This is should allow me to update python - Automatic Restarts (Reloader): When you save a change to a Python file (.py), the server automatically detects the change and reloads itself. This is what stops you from having to constantly stop and start Flask manually.
if __name__ == "__main__":
    app.run(debug=True)