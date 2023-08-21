# Import MongoClient & Api
from pymongo import MongoClient
# from pymongo.mongo_client import MongoClient ###
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