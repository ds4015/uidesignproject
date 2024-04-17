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


learn_data = [
    {
        "id": 1,
        "title": "Basics - Cells",
        "left_box": "<p>The primary cell in the brain is known as a neuron.</p>" +
                    "<p>The neuron looks kind of like a scorpion. It has a main" +
                    "body with spindly projections called dendrites and a long tail "+
                    "called an axon</p>",
        "right_image":"cell.png",
        "concept_title": "Neuron",
        "concept_descr": "The main cell of the brain.",
        "concepts": ["Body","Axon","Dendrites"],
        "next": "/learn/2",
        "back": "/",
        "time": None
    },
   {
        "id": 2,
        "title": "Basics - Neurotransmission",
        "left_box": "<br><p>At the end of each dendrite is a receptor for a chemical known as a neurotransmitter</p>" +
                    "<p>Cells communicate by passing these neurotransmitters as signals.</p>",
        "video":"https://www.youtube.com/embed/cNaFnRKwpFk?si=m4ffjoYmlKQMhbmq",
        "concept_title": None,
        "concepts":None,
        "next": "/learn/3",
        "back": "/learn/1",
        "time": None
    },    
   {
        "id": 3,
        "title": "Basics - Neurotransmitters",
        "left_box": "<p class='sub-heading'>GABA</p>" + 
                    "<p>Reduces the amount of activity a cell can transmit.</p>" +
                    "<p>An increase in GABA reduces stress and anxiety.</p>",
        "right_image":"gaba.png",
        "concept_title": "GABA",
        "concept_descr": "Slows down brain activity.",
        "concepts":["stress","anxiety"],
        "next": "/learn/4",
        "back": "/learn/2",
        "time": None
    },    
  {
        "id": 4,
        "title": "Basics - Neurotransmitters",
        "left_box": "<p class='sub-heading'>Serotonin</p>" + 
                    "<p>Regulates mood, sleep and digestion.</p>" +
                    "<p>An increase in serotonin alleviates depression, improves sleep and bowel function.</p>",
        "right_image":"serotonin.png",
        "concept_title": "Serotonin",
        "concept_descr": "Regulates mood.",
        "concepts":["depression","sleep"],
        "next": "/learn/5",
        "back": "/learn/3",
        "time": None
    },    
   {
        "id": 5,
        "title": "Basics - Neurotransmitters",
        "left_box": "<p class='sub-heading'>Dopamine</p>" + 
                    "<p>Associated with attention and reward.</p>" +
                    "<p>An increase in dopamaine increases motivation, alertness, and makes you feel good.</p>",
        "right_image":"dopamine.png",
        "concept_title": "Dopamine",
        "concept_descr": "Reward center.",
        "concepts":["motivation","alertness"],
        "next": "/learn/6",
        "back": "/learn/4",
        "time": None
    },           
   {
        "id": 6,
        "title": "Senses - Vision",
        "left_box": "<p class='sub-heading'>Occipital Lobe</p>" + 
                    "<p>→ Recognize faces</p>" +
                    "<p>→ Process input from the eyes</p>" +
                    "<p>→ Color vision</p>" +                                        
                    "<p>→ Shapes and depth</p>",
        "right_image":"occipital.png",
        "concept_title": "Vision",
        "concept_descr": "Occipital Lobe",
        "concepts":["faces","colors","shapes"],
        "next": "/learn/7",
        "back": "/learn/5",
        "time": None
    },  
   {
        "id": 7,
        "title": "Senses - Hearing",
        "left_box": "<p class='sub-heading'>Temporal Lobe</p>" + 
                    "<p>→ Understand music and harmonies</p>" +
                    "<p>→ Process input from the ears</p>" +
                    "<p>→ Associated with speech</p>" +                                        
                    "<p>→ Located behind the ears</p>",
        "right_image":"temporal.png",
        "concept_title": "Hearing",
        "concept_descr": "Temporal Lobe",
        "concepts":["music","speech","hearing"],
        "next": "/learn/8",
        "back": "/learn/6",
        "time": None
    },  
   {
        "id": 8,
        "title": "Senses - Touch",
        "left_box": "<p class='sub-heading'>Parietal Lobe</p>" + 
                    "<p>→ Sensation of temperature, pressure, vibration, pain</p>" +
                    "<p>→ Writing and precise hand movements</p>" +
                    "<p>→ Symbol recognition - reading and math</p>" +                                        
                    "<p>→ Navigation of physical space</p>",
        "right_image":"parietal.png",
        "concept_title": "Touch",
        "concept_descr": "Parietal Lobe",
        "concepts":["pain","writing","symbols"],
        "next": "/learn/9",
        "back": "/learn/7",
        "time": None
    },  
   {
        "id": 9,
        "title": "Intelligence",
        "left_box": "<p class='sub-heading'>Frontal Lobe</p>" + 
                    "<p>→ Reasoning and Logical Arguments</p>" +
                    "<p>→ Planning and making schedules</p>" +
                    "<p>→ Being able to imagine the future</p>" +                                        
                    "<p>→ Storage of information in working memory.</p>",
        "right_image":"frontal.png",
        "concept_title": "Intelligence",
        "concept_descr": "Frontal Lobe",
        "concepts":["reason","planning","imagination"],
        "next": "/learn/10",
        "back": "/learn/8",
        "time": None
    },
   {
        "id": 10,
        "title": "Emotions - Fear",
        "left_box": "<p class='sub-heading'>Amygdala</p>" + 
                    "<p>→ Small structure in the inner brain</p>" +
                    "<p>→ Responsible for fear and aggression</p>",
        "right_image":"amygdala.png",
        "concept_title": "Emotions",
        "concept_descr": "Amygdala",
        "concepts":["fear","anxiety","aggression"],
        "next": "/learn/11",
        "back": "/learn/9",
        "time": None
    },    
   {
        "id": 11,
        "title": "Emotions - Love",
        "left_box": "<p class='sub-heading'>Hypothalams</p>" + 
                    "<p>→ Reward center of the brain</p>" +
                    "<p>→ Love increases dopamine</p>" +
                    "<p>→ Processed in hypothalamus as reward</p>" +                                        
                    "<p>→ Also responsible for hunger/thirst</p>",
        "right_image":"hypothalamus.png",
        "concept_title": "Emotions",
        "concept_descr": "Hypothalamus",
        "concepts":["love","reward","hunger"],
        "next": "/learn/12",
        "back": "/learn/10",
        "time": None
    },    
   {
        "id": 12,
        "title": "Memory",
        "left_box": "<p class='sub-heading'>Hippocampus</p>" + 
                    "<p>→ Long-term memory</p>" +
                    "<p>→ Spatial/navigational mental maps</p>" +
                    "<p>→ Important in learning</p>",                                        
        "right_image":"hippocampus.png",
        "concept_title": "Memory",
        "concept_descr": "Hippocampus",
        "concepts":["mental maps","learning","long-term memory"],
        "next": "/quiz/1",
        "back": "/learn/11",
        "time": None
    }

]

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
        "image": "amygdala_quiz.png",
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
    int(lesson_id)
    next_text = "Next"
    access_time = datetime.datetime.now()
    access_time = access_time.strftime("%m/%d/%Y at %H:%M")
    data = next((item for item in learn_data if item['id'] == lesson_id), None)
    data['time'] = access_time
    if (lesson_id == len(learn_data)):
        next_text = "Quiz Me"
    return render_template('learn.html', lesson=data, next_text=next_text) 

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
            return render_template('quiz.html', question=question, qnum=quiz_id)
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



