# Dallas Scott - ds4015
# Larry Chen
# UI Design - Spring 2024
# HW 10 Main

from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)
import random
import datetime


learn_data = ["This is the learn data"]
quiz_data = ["This is the quiz data"]


# ROUTES

@app.route('/')
def welcome():
    access_time = datetime.datetime.now()
    print(access_time)
    access_time = access_time.strftime("%m/%d/%Y at %H:%M")
    learn_data.append(access_time)
    return render_template('welcome.html', data=access_time)   


@app.route('/learn/<int:lesson_id>')
def learn(lesson_id):
    return render_template('learn.html', data=learn_data) 

@app.route('/quiz/<int:question_id>')
def quiz(question_id):
    return render_template('quiz.html', data=quiz_data) 



if __name__ == '__main__':
   app.run(debug = True)




