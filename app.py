from flask import flask, render_template

app = Flask(__name__) #this program is a flask application, tells flask that this is the main application program

@app.route("/") #THis will send them to the first thing, backslash is a default which normally sends people to the index
def indexpage():
    return render_template("index.html")  #this will send them to the index page


@app.route("/portfolio") #THis will send them to the first thing, backslash is a default which normally sends people to the index
def portfoliopage():
    return render_template("portfolio.html")  #this will send them to the index page

@app.route("/projects") #THis will send them to the first thing, backslash is a default which normally sends people to the index
def projectspage():
    return render_template("projects.html")  #this will send them to the index page

@app.route("/blog") #THis will send them to the first thing, backslash is a default which normally sends people to the index
def blogpage():
    return render_template("blog.html")  #this will send them to the index page

@app.route("/cv") #THis will send them to the first thing, backslash is a default which normally sends people to the index
def cvpage():
    return render_template("cv.html")  #this will send them to the index page

@app.route("/contact") #THis will send them to the first thing, backslash is a default which normally sends people to the index
def contactpage():
    return render_template("contactpage.html")  #this will send them to the index page
