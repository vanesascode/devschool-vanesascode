from flask import Flask, render_template, jsonify, request, redirect

# Flask instance
app = Flask(__name__)

# Import MongoClient & Api
from pymongo import MongoClient
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

# Access to the collection
comments_collection = db["comments"]

# Define a route to handle the submission of comments
@app.route("/submit_comment", methods=["POST"])
def submit_comment():
    # Get the comment data from the request form
    comment = request.form.get("comment")

    # Insert the comment into the collection
    comment_doc = {"comment": comment}
    result = comments_collection.insert_one(comment_doc)

    # Redirect back to the article page
    return redirect("/blog/typescript-index-signatures")

@app.route("/blog/typescript-index-signatures")
def typescriptindexsignatures():
    # Retrieve the comments from the collection
    comments = comments_collection.find()
    # Pass the comments to the article template for rendering
    return render_template("typescript/typescript-index-signatures.html", comments=comments)


# JOBS LIST ( expected to take it to an external cloud database)

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

# Route decorators: 

# HOME PAGE

@app.route("/")
def school():
    return render_template("school/index-school.html")

# JOBS PAGE

@app.route("/jobs")
def jobs():
    return render_template("jobs/index-jobs.html", jobs=JOBS)

# BLOG ARTICLES

@app.route("/blog")
def blog():
    return render_template("blog/index-blog.html")

@app.route("/blog/javascript-interview-questions")
def javascriptinterviewquestions():
    return render_template("javascript/javascript-interview-questions.html")

@app.route("/blog/javascript-classes-booklist")
def javascriptclassesbooklist():
    return render_template("javascript/javascript-classes-booklist.html")

@app.route("/blog/javascript-array-methods-part-one")
def javascriptarraymethodspartone():
    return render_template("javascript/javascript-array-methods-part-one.html")

@app.route("/blog/javascript-array-methods-part-two")
def javascriptarraymethodsparttwo():
    return render_template("javascript/javascript-array-methods-part-two.html")

@app.route("/blog/typescript-record-utiliy-type")
def typescriptrecordutiliytype():
    return render_template("typescript/typescript-record-utiliy-type.html")

# FORM AND PRIVACY POLICY:

@app.route("/apply")
def apply():
    return render_template("apply/index-apply.html")

@app.route("/privacy-policy")
def privacypolicy():
    return render_template("privacy-policy.html")

# API WITH JOBS LIST:

@app.route("/api/jobs")
def list_jobs():

    return jsonify(JOBS)

# TO RUN THE APP: 

if __name__ == "__main__":
    app.run(debug=True, port=4000)

# http://localhost:4000/
