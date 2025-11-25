from flask import Flask, render_template

app = Flask(__name__) #this program is a flask application, tells flask that this is the main application program

@app.route("/") #THis will send them to the first thing, backslash is a default which normally sends people to the index
def indexpage():
    return render_template("index.html")  #this will send them to the index page


@app.route("/portfolio") #THis will send them to the first thing, backslash is a default which normally sends people to the portfolio
def portfoliopage():
    return render_template("portfolio.html")  #this will send them to the portfolio page

@app.route("/projects") #THis will send them to the first thing, backslash is a default which normally sends people to the projects
def projectspage():
    return render_template("projects.html")  #this will send them to the projects page

@app.route("/blog") #THis will send them to the first thing, backslash is a default which normally sends people to the blog
def blogpage():
    return render_template("blog.html")  #this will send them to the blog page

@app.route("/cv") #THis will send them to the first thing, backslash is a default which normally sends people to the cvpage
def cvpage():
    return render_template("cv.html")  #this will send them to the cv page

@app.route("/contactpage") #THis will send them to the first thing, backslash is a default which normally sends people to the contactpage
def contactpage():
    return render_template("contactpage.html")  #this will send them to the contactpage


@app.route("/zork") #THis will send them to the first thing, backslash is a default which normally sends people to the zork
def zorkpage():
    return render_template("zork.html")  #this will send them to the zork game

#This is should allow me to update python - Automatic Restarts (Reloader): When you save a change to a Python file (.py), the server automatically detects the change and reloads itself. This is what stops you from having to constantly stop and start Flask manually.
if __name__ == "__main__":
    app.run(debug=True)