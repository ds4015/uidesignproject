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


learn_data = []
quiz_data = []


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
    film = data[film_id - 1]
    return render_template('film.html', film=film) 

@app.route('/quiz/<int:question_id>')
def quiz(question_id):
    results = []
    for film in data:
        print(film)
        print(term.lower())
        print(film['title'])
        if (term.lower() in film['title'].lower()):
            results.append( (film['id'], film['title'], film['year'], film['director']) )
            print(results)
    return render_template('results.html', data=results, query=term) 



if __name__ == '__main__':
   app.run(debug = True)




