import os
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# In-memory data stores
work_experience = [
    {
        "job_title": "Software Engineer",
        "company": "StoreHub",
        "dates": "2023 - Present",
        "description": "Developed a service that helps with inventory management and handles inventory synchronization with Shopify and other ecommerce stores, alerting customers on WhatsApp when an order is made with Express, React, Typescript, Postgres, and Tailwind",
    },
    {
        "job_title": "Frontend Engineer",
        "company": "Drawstring",
        "dates": "2022 - 2023",
        "description": "Took charge of the integration of all smart contract APIs by making sure the smart contract data was aligned with data from the backend while smart contract remained our single source of truth.",
    },
]
education_data = [
    {
        "degree": "Bachelor of Science in Computer Science",
        "university": "University of Port-Harcourt",
        "dates": "2021 - 2025",
        "description": "Graduated with 4.1 GPA.",
    }
]
hobbies_data = [
    {
        "name": "Photography",
        "image": "hobby1.jpg",
        "description": "I love capturing moments and telling stories through my photos.",
    }
]


@app.route("/")
def index():
    return render_template(
        "index.html",
        title="MLH Fellow",
        url=os.getenv("URL"),
        work_experience=work_experience,
        education_data=education_data,
    )


@app.route("/hobbies")
def hobbies():
    return render_template("hobbies.html", title="My Hobbies", url=os.getenv("URL"))


@app.route("/add/work", methods=["GET", "POST"])
def add_work():
    if request.method == "POST":
        new_work = {
            "job_title": request.form["job_title"],
            "company": request.form["company"],
            "dates": request.form["dates"],
            "description": request.form["description"],
        }
        work_experience.append(new_work)
        return redirect(url_for("index"))
    return render_template(
        "add_form.html",
        form_type="Work Experience",
        fields=["job_title", "company", "dates", "description"],
    )


@app.route("/add/education", methods=["GET", "POST"])
def add_education():
    if request.method == "POST":
        new_education = {
            "degree": request.form["degree"],
            "university": request.form["university"],
            "dates": request.form["dates"],
            "description": request.form["description"],
        }
        education_data.append(new_education)
        return redirect(url_for("index"))
    return render_template(
        "add_form.html",
        form_type="Education",
        fields=["degree", "university", "dates", "description"],
    )


@app.route("/add/hobby", methods=["GET", "POST"])
def add_hobby():
    if request.method == "POST":
        new_hobby = {
            "name": request.form["name"],
            "image": request.form["image"],
            "description": request.form["description"],
        }
        hobbies_data.append(new_hobby)
        return redirect(url_for("hobbies"))
    return render_template(
        "add_form.html", form_type="Hobby", fields=["name", "image", "description"]
    )
