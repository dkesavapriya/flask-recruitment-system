from flask import Flask, render_template, request, redirect, url_for, session, flash
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = os.getenv("app.secret_key")

from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env

mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client["recruitment"]
jobs = db["jobs"]
applicants = db["applicants"]
admins = db["admins"]

@app.route("/")
def home():
    all_jobs = list(jobs.find())
    return render_template("index.html", jobs=all_jobs)

@app.route("/post_job", methods=["GET", "POST"])
def post_job():
    if "admin" not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        job = {"title": request.form["title"], "description": request.form["description"]}
        jobs.insert_one(job)
        flash("JOB posted Successfully")
        return redirect(url_for("home"))
    return render_template("post_job.html")

@app.route("/apply/<job_id>", methods=["GET", "POST"])
def apply(job_id):
    job = jobs.find_one({"_id": ObjectId(job_id)})
    if request.method == "POST":
        application = {
            "job_id": job_id,
            "name": request.form["name"],
            "email": request.form["email"],
            "qualification": request.form["qualification"],
            "status": "Applied",
            "test_score": None,
            "interview_result": None
        }
        applicants.insert_one(application)
        return redirect(url_for("home"))
    return render_template("apply.html", job=job)

@app.route("/admin")
def admin():
    if "admin" not in session:
        return redirect(url_for("login"))
    all_applicants = list(applicants.find())
    return render_template("admin.html", applicants=all_applicants)

@app.route("/shortlist/<applicant_id>")
def shortlist(applicant_id):
    if "admin" not in session:
        return redirect(url_for("login"))
    applicants.update_one({"_id": ObjectId(applicant_id)}, {"$set": {"status": "WaitingList"}})
    return redirect(url_for("admin"))


@app.route("/update_score/<applicant_id>", methods=["POST"])
def update_score(applicant_id):
    if "admin" not in session:
        return redirect(url_for("login"))

    #app_id = request.form["app_id"]
    test_score = int(request.form["Test score"])
    interview_score = int(request.form["Interview score"])

    total_score = test_score + interview_score

    if total_score >= 15:
        status = "Recruited"
    else:
        status = "Rejected"

    applicants.update_one(
        {"_id": ObjectId(applicant_id)},
        {"$set": {
            "test_score": test_score,
            "interview_score": interview_score,
            "status": status  # ✅ this is critical
        }}
    )
    return redirect(url_for("view_applicants"))

@app.route("/admin/applicants")
def view_applicants():
    if "admin" not in session:
        return redirect(url_for("login"))

    all_apps =list(applicants.find())
    recruited = []
    rejected = []
    pending = []
    waitinglist=[]
    for app in all_apps:
        if app.get("status") == "Recruited":
            recruited.append(app)
        elif app.get("status") == "Rejected":
            rejected.append(app)
        elif app.get("status"=="WaitingList"):
            waitinglist.append(app)
        else:
            pending.append(app)

    return render_template("view_applicants.html", recruited=recruited, rejected=rejected, pending=pending,waitinglist=waitinglist)

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session["admin"] = True
            return redirect(url_for("home"))
        else:
            flash("Invalid credentials")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("admin", None)
    return redirect(url_for("home"))
 


if __name__ == "__main__":
    app.run(debug=True)
