from flask import Flask, render_template, request, redirect

# Flask instance
app = Flask(__name__)

########################## DATABASE CONNECTION #############################

# Import MongoClient & Api
# from pymongo import MongoClient
from pymongo.mongo_client import MongoClient 
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv() 

# Connect to MongoDB using the URI: Retrieving the MongoDB URI from the environment
mongodb_uri = os.getenv("MONGODB_URI")

# Create a new client and connect to the server
client = MongoClient(mongodb_uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Connect to the database
db = client["devschool-blog-comments"]

# Access to the collections
typescriptindexsignaturescomments_collection = db["typescriptindexsignaturescomments"]

javascriptclassescomments_collection = db["javascriptclassescomments"]

javascriptarraymethodspartonecomments_collection = db["javascriptarraymethodspartonecomments"]

typescriptrecordutilitytypecomments_collection = db["typescriptrecordutilitytypecomments"]

javascriptarraymethodsparttwocomments_collection = db["javascriptarraymethodsparttwocomments"]


########################## WEBSITE ROUTES ########################################

#### HOME PAGE

@app.route("/")
def school():
    return render_template("school/index-school.html")


#### JOBS PAGE

JOBS = [
    {
        "id": 1,
        "title": "Junior Full Stack JavaScript",
        "location": "Singapore, Hong Kong",
        "description": "As a Junior Full Stack JavaScript Developer, you will be responsible for assisting in the development, implementation, and maintenance of web applications. You will work closely with senior developers and cross-functional teams to create efficient and scalable software solutions. This is an excellent opportunity to gain hands-on experience and grow your skills in full stack JavaScript development, with a focus on Next.js and GraphQL.",
    },
    {
        "id": 2,
        "title": "Node.js Backend Developer",
        "location": "Remote",
        "description": "We are seeking a highly skilled Senior Backend Node.js Developer to join our dynamic team. The ideal candidate should be passionate about developing high-quality, scalable, and maintainable software solutions. As a Senior Backend Node.js Developer, you will be responsible for designing, developing, and maintaining server-side applications, databases, and APIs. You will work closely with cross-functional teams, including front-end developers, designers, and product managers, to deliver exceptional software solutions.",
    },
    {
        "id": 3,
        "title": "Data Analyst",
        "location": "Remote",
        "description": "We are looking for a data analyst to help our client make smart, data-driven business decisions. As a Data Analyst, you'll be responsible to help build and ensure the data solutions are optimized for speed, reliability, and accuracy. You'll work with cross-functional teams to identify data requirements and develop innovative solutions to address their needs.",
    },
    {
        "id": 4,
        "title": "Senior Full stack Engineer",
        "location": "Remote",
        "description": "We're looking for product-obsessed individuals with early-stage startup experience who want to work with a dynamic fast-moving team and build the roadmap for RabbitHole to become the best way for protocols to distribute their token and engage their users. If this is you, we are super excited to meet you and learn more.",
    },
    {
        "id": 5,
        "title": "Full Stack Software Engineer",
        "location": "San Francisco, US",
        "description": "We are looking for a developer who is detail oriented and can work through complex issues to find elegant solutions.  Key technical skills include: Python",
    },
    {
        "id": 6,
        "title": "Senior WordPress Developer",
        "location": "Remote",
        "description": "If you are an enthusiastic person who wants to learn and explore the various possibilities and magic you can create using WordPress, come to join our WordPress Developers team.",
    },
]

@app.route("/jobs")
def jobs():
    return render_template("jobs/index-jobs.html", jobs=JOBS)


#### FORM AND PRIVACY POLICY:

@app.route("/apply")
def apply():
    return render_template("apply/index-apply.html")

@app.route("/privacy-policy")
def privacypolicy():
    return render_template("privacy-policy.html")


#### BLOG ARTICLES


# BLOG MAIN PAGE

@app.route("/blog")
def blog():
    return render_template("blog/index-blog.html")


# TYPESCRIPT INDEX SIGNATURES

@app.route("/blog/typescript-index-signatures")
def typescriptindexsignatures():
    # Retrieve the comments from the collection
    # convert the Cursor object to a list before passing it to the template (so I can count comments in the article dynamically)
    typescriptindexsignaturescomments = list(typescriptindexsignaturescomments_collection.find())
    # Pass the comments to the article template for rendering
    return render_template("typescript/typescript-index-signatures.html", typescriptindexsignaturescomments=typescriptindexsignaturescomments)

# JAVASCRIPT CLASSES

@app.route("/blog/javascript-classes-booklist")
def javascriptclassesbooklist():
    javascriptclassescomments = list(javascriptclassescomments_collection.find())
    return render_template("javascript/javascript-classes-booklist.html", javascriptclassescomments=javascriptclassescomments)

# JAVASCRIPT ARRAY METHODS PART ONE

@app.route("/blog/javascript-array-methods-part-one")
def javascriptarraymethodspartone():
    javascriptarraymethodspartonecomments = list(javascriptarraymethodspartonecomments_collection.find())
    return render_template("javascript/javascript-array-methods-part-one.html", javascriptarraymethodspartonecomments=javascriptarraymethodspartonecomments)


# TYPESCRIPT RECORD UTILITY TYPE

@app.route("/blog/typescript-record-utiliy-type")
def typescriptrecordutiliytype():
    typescriptrecordutilitytypecomments = list(typescriptrecordutilitytypecomments_collection.find())
    return render_template("typescript/typescript-record-utiliy-type.html", typescriptrecordutilitytypecomments=typescriptrecordutilitytypecomments)


# JAVASCRIPT ARRAY METHODS PART TWO

@app.route("/blog/javascript-array-methods-part-two")
def javascriptarraymethodsparttwo():
    javascriptarraymethodsparttwocomments = list(javascriptarraymethodsparttwocomments_collection.find())
    return render_template("javascript/javascript-array-methods-part-two.html", javascriptarraymethodsparttwocomments=javascriptarraymethodsparttwocomments)



################################## TO RUN THE APP IN DEVELOPMENT MODE ############################ 

if __name__ == "__main__":
    app.run(debug=True, port=4000)

# http://localhost:4000/

###################################### POSTROUTES #####################################################


from datetime import datetime



######################################## BLOG COMMENTS #############################################

# The postroutes to handle the submission of comments:

### TYPESCRIPT INDEX SIGNATURES:
@app.route("/submit_typescriptindexsignaturescomment", methods=["POST"])
def submit_typescriptindexsignaturescomment():
    # Get the comment data from the request form
    comment = request.form.get("comment")
    name = request.form.get("name")

    # Add the current date and time to the comment
    current_datetime = datetime.now().strftime("%B %d, %Y at %I:%M %p")
    typescriptindexsignaturescomment_doc = {"comment": comment, "name": name, "posted_at": current_datetime}
     # Insert the comment into the collection
    result = typescriptindexsignaturescomments_collection.insert_one(typescriptindexsignaturescomment_doc)

    # Redirect back to the article page
    return redirect("/blog/typescript-index-signatures")


### JAVASCRIPT CLASSES:
@app.route("/submit_javascriptclassescomment", methods=["POST"])
def submit_javascriptclassescomment():
    # Get the comment data from the request form
    comment = request.form.get("comment")
    name = request.form.get("name")

    # Add the current date and time to the comment
    current_datetime = datetime.now().strftime("%B %d, %Y at %I:%M %p")
    javascriptclassescomment_doc = {"comment": comment, "name": name, "posted_at": current_datetime}
     # Insert the comment into the collection
    result = javascriptclassescomments_collection.insert_one(javascriptclassescomment_doc)

    # Redirect back to the article page
    return redirect("/blog/javascript-classes-booklist")


### JAVASCRIPT ARRAY METHODS PART ONE:
@app.route("/submit_javascriptarraymethodspartonecomment", methods=["POST"])
def submit_javascriptarraymethodspartonecomment():
    # Get the comment data from the request form
    comment = request.form.get("comment")
    name = request.form.get("name")

    # Add the current date and time to the comment
    current_datetime = datetime.now().strftime("%B %d, %Y at %I:%M %p")
    javascriptarraymethodspartonecomment_doc = {"comment": comment, "name": name, "posted_at": current_datetime}
     # Insert the comment into the collection
    result = javascriptarraymethodspartonecomments_collection.insert_one(javascriptarraymethodspartonecomment_doc)

    # Redirect back to the article page
    return redirect("/blog/javascript-array-methods-part-one")


### TYPESCRIPT RECORD UTILITY TYPE:


@app.route("/submit_typescriptrecordutilitytypecomment", methods=["POST"])
def submit_typescriptrecordutilitytypecomment():
    # Get the comment data from the request form
    comment = request.form.get("comment")
    name = request.form.get("name")

    # Add the current date and time to the comment
    current_datetime = datetime.now().strftime("%B %d, %Y at %I:%M %p")
    typescriptrecordutilitytypecomment_doc = {"comment": comment, "name": name, "posted_at": current_datetime}
     # Insert the comment into the collection
    result = typescriptrecordutilitytypecomments_collection.insert_one(typescriptrecordutilitytypecomment_doc)

    # Redirect back to the article page
    return redirect("/blog/typescript-record-utiliy-type")


### JAVASCRIPT ARRAY METHODS PART TWO:

@app.route("/submit_javascriptarraymethodsparttwocomment", methods=["POST"])
def submit_javascriptarraymethodsparttwocomment():
    # Get the comment data from the request form
    comment = request.form.get("comment")
    name = request.form.get("name")

    # Add the current date and time to the comment
    current_datetime = datetime.now().strftime("%B %d, %Y at %I:%M %p")
    javascriptarraymethodsparttwocomment_doc = {"comment": comment, "name": name, "posted_at": current_datetime}
     # Insert the comment into the collection
    result = javascriptarraymethodsparttwocomments_collection.insert_one(javascriptarraymethodsparttwocomment_doc)

    # Redirect back to the article page
    return redirect("/blog/javascript-array-methods-part-two")



######################################## JOBS list #############################################


# JOBS LIST ( expected to take it to an external cloud database)

