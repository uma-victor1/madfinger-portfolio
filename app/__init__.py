import os
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# In-memory data stores
work_experience = [
    {
        'job_title': 'Software Engineer',
        'company': 'Company A',
        'dates': '2020 - Present',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum vestibulum.'
    }
]
education_data = [
    {
        'degree': 'Bachelor of Science in Computer Science',
        'university': 'University of Example',
        'dates': '2016 - 2020',
        'description': 'Graduated with honors, focusing on software development and artificial intelligence.'
    }
]
hobbies_data = [
    {
        'name': 'Photography',
        'image': 'hobby1.jpg',
        'description': 'I love capturing moments and telling stories through my photos.'
    }
]

@app.route('/')
def index():
    return render_template('index.html', 
                           title="MLH Fellow", 
                           url=os.getenv("URL"),
                           work_experience=work_experience,
                           education_data=education_data)

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', 
                           title="My Hobbies", 
                           url=os.getenv("URL"),
                           hobbies=hobbies_data)

@app.route('/add/work', methods=['GET', 'POST'])
def add_work():
    if request.method == 'POST':
        new_work = {
            'job_title': request.form['job_title'],
            'company': request.form['company'],
            'dates': request.form['dates'],
            'description': request.form['description']
        }
        work_experience.append(new_work)
        return redirect(url_for('index'))
    return render_template('add_form.html', form_type='Work Experience', fields=['job_title', 'company', 'dates', 'description'])

@app.route('/add/education', methods=['GET', 'POST'])
def add_education():
    if request.method == 'POST':
        new_education = {
            'degree': request.form['degree'],
            'university': request.form['university'],
            'dates': request.form['dates'],
            'description': request.form['description']
        }
        education_data.append(new_education)
        return redirect(url_for('index'))
    return render_template('add_form.html', form_type='Education', fields=['degree', 'university', 'dates', 'description'])

@app.route('/add/hobby', methods=['GET', 'POST'])
def add_hobby():
    if request.method == 'POST':
        new_hobby = {
            'name': request.form['name'],
            'image': request.form['image'],
            'description': request.form['description']
        }
        hobbies_data.append(new_hobby)
        return redirect(url_for('hobbies'))
    return render_template('add_form.html', form_type='Hobby', fields=['name', 'image', 'description'])
