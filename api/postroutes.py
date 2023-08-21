from flask import Blueprint, request, redirect
from datetime import datetime
from database import typescriptindexsignaturescomments_collection, javascriptclassescomments_collection, javascriptarraymethodspartonecomments_collection, typescriptrecordutilitytypecomments_collection, javascriptarraymethodsparttwocomments_collection

# Create a Blueprint object
postroutes_blueprint = Blueprint("postroutes", __name__)



################## BLOG COMMENTS ###################

# Define the postroutes to handle the submission of comments:

### TYPESCRIPT INDEX SIGNATURES:
@postroutes_blueprint.route("/submit_typescriptindexsignaturescomment", methods=["POST"])
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
@postroutes_blueprint.route("/submit_javascriptclassescomment", methods=["POST"])
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
@postroutes_blueprint.route("/submit_javascriptarraymethodspartonecomment", methods=["POST"])
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


@postroutes_blueprint.route("/submit_typescriptrecordutilitytypecomment", methods=["POST"])
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

@postroutes_blueprint.route("/submit_javascriptarraymethodsparttwocomment", methods=["POST"])
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









