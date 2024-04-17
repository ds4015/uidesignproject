# Dallas Scott - ds4015
# Larry Chen - Lc3718
# UI Design - Spring 2024
# HW 10 Main

from flask import Flask
from flask import render_template
from flask import Response, request, jsonify, session, redirect
import random
import datetime
import os
app = Flask(__name__)

app.secret_key = os.urandom(24)


learn_data = ["This is the learn data"]

quiz_questions = {
    "1": {
        "quiz_id": "1",
        "image": "",
        "question": "Which neurotransmitter reduces anxiety and stress?",
        "options" : ['Serotonin', 'Norepinerpheine', 'GABA', 'Thalamus'],
        "answer" : "GABA",
        "next_question": "2"
    },
    "2": {
        "quiz_id": "2",
        "image": 'dendrites.png',
        "question": "What are these called?",
        "options" : ['Neurons', 'Dendrites', 'Limbic System', 'Axons' ],
        "answer" : "Dendrites",
        "next_question": "3"
    },
    "3": {
        "quiz_id": "3",
        "image": "frontal_lobe.png",
        "question": "Which area of the brain is highlighted here?  What is its function?",
        "options" : ['Occipital lobe - hearing', 'Temporal lobe - sound', 'Occipital lobe - vision', 'Frontal lobe - reasoning'],
        "answer" : "Frontal lobe - reasoning", 
        "next_question": "4"
    },
    "4": {
        "quiz_id": "4",
        "image": "",
        "question": "Where is the hypothalamus and what does it do",
        "options" : ['Midbrain - processes memory',
'Limbic System - controls hunger', 'Temporal lobe - controls body temperature', 'Thalamus - processes emotion'],
        "answer" : "Limbic System - controls hunger",
        "next_question": "5"
    },
    "5": {
        "quiz_id": "5",
        "image": "amygdala.png",
        "question": "What is this structure called ",
        "options" : ['Amygdala', 'Cell Body', 'Thalamus ', 'Hippocampus'],
        "answer" : "Amygdala",
        "next_question": "6"
    },
    "6": {
        "quiz_id": "6",
        "image": "",
        "question": "A young man presents to the hospital saying he cannot see.  Which part of of the brain did he injure?",
        "options" : ['Temporal Lobe', 'Hippocampus', 'Occipital Lobe', 'Frontal Lobe'],
        "answer" : "Occipital Lobe",
        "next_question": "7"
    },
    "7": {
        "quiz_id": "7",
        "image": "",
        "question": "What types of cells are found in the brain?",
        "options" : ['Axons', 'Dendrites', 'Neurons', 'Neurotransmitters'],
        "answer" : "Neurons",
        "next_question": "8"
    },
    "8": {
        "quiz_id": "8",
        "image": "temporal_lobe.png",
        "question": "Which area of the brain is highlighted here?  What is its function?",
        "options" : ['Occipital lobe - hearing', 'Temporal lobe - sound', 'Occipital lobe - vision', 'Frontal lobe - reasoning'],
        "answer" : "Temporal lobe - sound",
        "next_question": "end"
    },
    
}
    


# ROUTES

@app.route('/')
def welcome():
    session.clear()
    access_time = datetime.datetime.now()
    print(access_time)
    access_time = access_time.strftime("%m/%d/%Y at %H:%M")
    learn_data.append(access_time)
    return render_template('welcome.html', data=access_time)   


@app.route('/learn/<int:lesson_id>')
def learn(lesson_id):
    return render_template('learn.html', data=learn_data) 

@app.route('/quiz/<quiz_id>', methods=['GET', 'POST'])
def quiz(quiz_id):
    if request.method == 'POST':
        user_answer = request.form['option']
        correct_answer = quiz_questions[quiz_id]['answer']
        # Increment the correct answers count if user answered correctly
        if user_answer == correct_answer:
            session['score'] = session.get('score', 0) + 1
        next_question = quiz_questions[quiz_id]['next_question']
        next_question = quiz_questions[quiz_id]['next_question']
        if next_question == "end":
            return redirect('/results')
        else:
            return redirect(f"/quiz/{next_question}")
    else:
        question = quiz_questions.get(quiz_id)
        if question:
            return render_template('quiz.html', question=question)
        else:
            return "Question not found", 404

@app.route('/results')
def results():
    score = session.get('score', 0)
    total = 8
    return render_template('results.html', score=score, 
                          total=total)

@app.route('/answers')
def answers():
    score = session.get('score', 0)
    total = 8
    return render_template('answers.html',questions=quiz_questions)


if __name__ == '__main__':
    app.run(debug=True)



