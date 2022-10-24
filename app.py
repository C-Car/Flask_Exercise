import datetime
from datetime import date
from urllib import request

from flask import Flask, Response, render_template, request

app = Flask(__name__)
global studentOrganisationDetails
studentOrganisationDetails = {'name': 'Football', 'name2': 'Baseball', 'name3': 'Soccer', 'name4': 'Tennis', 'name5': 'Basketball'}
# Assign default 5 values to studentOrganisationDetails for Application  3.


@app.get('/')
def index():
    currentDate = datetime.datetime.now()

    return render_template('index.html', currentDate=currentDate)


@app.get('/calculate')
def displayNumberPage():
    
    # Complete this function to display form.html page
    return render_template('form.html')


@app.route('/calculate', methods=['POST'])
def checkNumber():
    global num
    num = request.form.get("number")

    # Get Number from form and display message according to number
    if not num: 
        return 'No Number Provided.<br><a href="/">Back to Home</a>'
    elif num.isalpha():
        return f'{num} is not an integer!<br><a href="/">Back to Home</a>'
    
    if int(num) % 2 == 0:
        return f'{num} is even.<br><a href ="/">Back to Home</a>'

    else: 
        return f'{num} is odd.<br><a href="/">Back to Home</a>'
    # Display "Number {Number} is even" if given number is even on result.html page
    # Display "Number {Number} is odd" if given number is odd on result.html page
    # Display "No number provided" if value is null or blank on result.html page
    # Display "Provided input is not an integer!" if value is not a number on result.html page

    # Write your to code here to check whether number is even or odd and render result.html page


@app.get('/addStudentOrganisation')
def displayStudentForm():
    # Complete this function to display studentFrom.html page
    
    return render_template('studentForm.html')


@app.route('/addStudentOrganisation', methods=['POST'])
def displayRegistrationPage():
    # Get student name and organisation from form.
    studentName = request.form['name']
    studentOrg = request.form['Organisation']
    studentOrganisationDetails[studentName] = studentOrg
    # Append this value to studentOrganisationDetails
    return render_template('StudentDetails.html', studentOrganisationDetails = studentOrganisationDetails)
    # Display studentDetails.html with all students and organisations
