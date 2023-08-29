# Dev School: fictional coding school with blog by vanesascode (UNDER CONSTRUCTION)

### Site using Python Flask stack and rendered with Vercel

ONGOING project for a complete website in which I keep sharing new knowlege about programming and development.

See here the [PROGRESS](https://devschool-vanesascode.vercel.app/)

# 💥 BACKEND 💥

### This is a totally "self-managed" database and backend management.

Flask is a lightweight web framework in Python.

## Creating a new Flask app:

First you have to have Python installed.

Install pip:

- [x] `python -m pip install --upgrade pip`

Then, you create an environment (imagine you want to call it 'myenv'):

- [x] run: `pip install pipenv`
- [x] `pipenv shell` (it creates a `pipfile`)
- [x] `pipenv install` (Install all dependencies of your project)

Then, you install and set Flask:

- [x] run: `pip install Flask`
- [ ] import Flask in app.py: `from flask import Flask`
- [ ] start the Flask app: `app = Flask(__name__)`
- [ ] run the Flask app in the browser:

```
if __name__ == "__main__":
    app.run(debug=True, port=4000)
```

The previous code is checking if the current module is being run directly (as opposed to being imported by another module). If it is being run directly, it runs the Flask application with debug mode enabled and listens on port 4000.

To see all the pip packages installed in the environment run:

- [x] `pip freeze`

If you don't have an environment:

- [x] `pip list`

## To run the app in development:

1. In the terminal run: `python app.py` If you are in VSCode, within the file app.py just click on the triangle button on the top right.
2. Open http://localhost:4000/ in the browser.

## Route handlers

This is our main route handler, since we only have a page in this app:

```
@app.route("/")
def home():
    return render_template("home.html", jobs=JOBS, company_name="Dev")
```

When a user accesses the root URL ("/"), the home() function is executed.

The function returns the rendered template "home.html" using the render_template() function from Flask. It passes the JOBS variable (the name of the database, in fact) as a parameter to the template, which can be accessed within the template. Additionally, it passes the value "Dev" as the company_name parameter to the template.

## MongoDB Atlas database

First create a new cluster, a database and a collection in your MongoDB Atlas account.
Click on "connect" and in the section of drivers you have some instructions (check them in case the ones here are old already):

- Install: `pip install pymongo`
- Follow the instructions to get a connection.

### .env

Then, you can install `pip install python-dotenv` to make your connection string save. Create an `.env` file and import it in the `app.py` :

```
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Connect to MongoDB using the URI: Retrieving the MongoDB URI from the environment
mongodb_uri = os.getenv("MONGODB_URI")
```

Instead of using `uri` as the instructions in the MongoDB docs tells you, you'll be using `mongodb_uri` in your code, if that is the name you gave to your variable in the .env file when you recorded your connection string there.

Remember to put your .env file in the `.gitignore` file.

## Deployment

Prepare your Flask application:

- [x] Fit everything in an API folder
- [x] In the root folder create a requirements.txt file. You can automatically create it with this command: `pip freeze > requirements.txt`

- [x] In the root folder create a vercel.json file (make it look like the one in this project)

Prepare Vercel:

- [x] Create an account in Vercel.com
- [x] Install the Now package in the terminal, globally: `npm install now -g`

Sign in into the project:

- [x] Run: `now` in the terminal, inside the root folder of the project.
- [x] The terminal will ask you your email.
- [x] Then, you'll receive an email in which you will have to verify your credentials.

Deploy:

- [x] Run: now again.
- [x] It will ask you if you want to deploy. You say Y
- [x] Asks the scope (your name)
- [x] Asks if you want to link to existing project. You say N
- [x] In which directory is your code located? If it's in the root folder just leave it like this: ./
- [x] You want to override the settings? You say N
- [x] You can now get the URL that is in the ✅ production line. It's live!

Add new changes to the live URL

- [x] Run: `now --prod` Then, changes are saved in the same URL you published before.

## See all your pip packages installed so far and versions:

- [x] Run: `py -m pip list`

# 💥 FRONTEND 💥

## Templates

In Flask, templates are used to generate dynamic HTML pages. Templates allow you to separate the structure of your web pages from the logic in your Python code. Flask uses a templating engine called `Jinja2` by default.

We then render these templates using the `render_template`(see it imported in the app.py file) function provided by Flask. This function takes the name of the template file as an argument and can also accept additional parameters to pass data to the template (for example, the value "Dev" as the company_name parameter, as seen in the route handler above).

Jinja2 is inspired by Django's template engine but offers more flexibility and features. It allows you to generate dynamic content by combining HTML code with expressions, control structures, and filters.

As mentioned before, in this particular project we just have a page (home, "/"). However, inside this home template, we include the 'nav' template like this, thanks to the Jinja2 syntax:

`{% include "nav.html" %}`

We can also get every item from the fetched 'jobs' MySQL table like this:

`{% for job in jobs %} {% include "jobitems.html" %} {% endfor %}`

The construction of every item in the jobs table is going to be indicated in the template 'jobitems'

## CSS and pictures

In Flask, the "static" folder is a special directory where you have to store static files such as CSS stylesheets, JavaScript files, images, and other assets that are used by your web application

It is typically placed in the root directory of your Flask project alongside the application code. Flask automatically recognizes and serves the files from this folder when they are requested by the client.

You import a CSS file like this in the head of your html file:

```
<link
      rel="stylesheet"
      type="text/css"
      href="{{ url_for('static', filename='transitions.css') }}"
    />
```

## SASS & Bootstrap customization

I made most of the styling with Bootstrap, but I had to adapt certain details with SASS in order to customize the components as I wanted. To get ready to do so, follow these steps:

- [x] Create a package.json file if you haven't one yet. (In the terminal run `npm init -y`)
- [ ] Install Bootstrap: `npm install bootstrap@5.3.0`
- [ ] Create a file called: 'styles.scss' in the 'static folder'
- [ ] Import Bootstrap in the file: `@import "../node_modules/bootstrap/scss/bootstrap.scss";`
- [ ] Install extension 'Live Sass Compiler' by Ritwick Dey in VsCode.
- [ ] Press the button at the bottom that says 'Watch Sass' and save something in your scss file. You'll see that a styles.css file and a styles.css.map files are created. Sass has been compiled into a CSS file and now we can import it into our project.

## Mailto links

In every position from the jobs table there is a button that says 'Apply'. The mailto link it contains opens the user's default email client with a new email composition window, with the recipient's email address, subject line, and optionally, the body of the email pre-filled.

In this case it has been done with the app https://mailtolink.me/:

```
href="mailto:devjobs@devjobs.com?subject=Application%20to%20{{ job['title']|urlencode }}&body=My%20name%3A%0D%0A%0D%0AMy%20CV%3A%0D%0A%0D%0AMy%20Linkedin%3A"
```

- Mailto:devjobs@devjobs.com" specifies the recipient's email address (it is invented)
- The "{{ job['title']|urlencode }}" part is a placeholder that will be replaced with the URL-encoded version of the job title.
- "|urlencode" is used in URL encoding. It is used to ensure that URLs are properly formatted and can be transmitted correctly over the internet.
