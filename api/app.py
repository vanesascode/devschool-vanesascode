from flask import Flask, render_template, jsonify

app = Flask(__name__)

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


@app.route("/")
def home():
    return render_template("home.html", jobs=JOBS, company_name="Dev")


@app.route("/api/jobs")
def list_jobs():

    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(debug=True, port=4000)

# http://localhost:4000/
