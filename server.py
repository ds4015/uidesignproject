# Dallas Scott - ds4015
# Larry Chen - Lc3718
# UI Design - Spring 2024
# HW 11 Main

from flask import Flask
from flask import render_template
from flask import Response, request, jsonify, session, redirect, flash
import random
import datetime
import os
app = Flask(__name__)

app.secret_key = os.urandom(24)

start_time = datetime.datetime.now()
end_time = datetime.datetime.now()


###################   TBC - Dallas  ##################


learn_data = [
 {
        "id": 1,
        "title": "<span class='first-letter'>B</span> <span class='heading'>" +
                    "a s i c s </span>&nbsp;&nbsp;-&nbsp;&nbsp; <span class='first-letter'>" +
                    "C</span> <span class='heading'>e l l s</span>" +
                    "<div class='row mt-0 pt-0'><div class='col-12 mt-0 pt-0'>" +
                    "<span class='sub-heading'>L e s s o n &nbsp;&nbsp; 1 :&nbsp;&nbsp;" +
                    "N e u r o n s &nbsp;&nbsp; a n d &nbsp;&nbsp; t h e i r &nbsp;&nbsp;" +
                    "C o m p o n e n t s</span></div></div>",
        "left_box": "<p><img class='bpoint' src='/static/bulletpoint.png'>The primary cell in the brain is known as a <b>neuron</b>.</p>" +
                    "<p><img class='bpoint' src='/static/bulletpoint.png'>The neuron looks kind of like a scorpion.</p> <p><img class='bpoint' src='/static/bulletpoint.png'>It has a main " +
                    "<b>body</b> with spindly projections called <b>dendrites</b> and a long tail "+
                    "called an <b>axon</b></p>",
        "right_image":"cell.png",
        "model": "/static/models/neuron/scene.gltf",
        "model_bg": "0xDDFFF7",
        "puzzle" : None,
        "solution": ["BUILDING", "BLOCK"],
        "concept_title" : "Neuron",
        "mnemonic":["<span class='first-letter-btn'>N</span>euron - ","<span class='first-letter-btn'>N</span>erve"],
        "next": "/learn/2",
        "back": "/",
        "next_num": "Lesson 2",
        "back_num": "Home",
        "time": None
    }, 
     {
        "id": 2,
        "title": "<span class='first-letter'>B</span> <span class='heading'>" +
                    "a s i c s </span>&nbsp;&nbsp;-&nbsp;&nbsp; <span class='first-letter'>" +
                    "N</span> <span class='heading'>e u r o t r a n s m i s s i o n</span>" +
                    "<div class='row mt-0 pt-0'><div class='col-12 mt-0 pt-0'>" +
                    "<span class='sub-heading'>L e s s o n &nbsp;&nbsp; 2 :&nbsp;&nbsp;" +
                    "C o m m u n i c a t i o n &nbsp;&nbsp; B e t w e e n &nbsp;&nbsp;" +
                    "C e l l s</span></div></div>",
        "left_box": "<br><p><img class='bpoint' src='/static/bulletpoint.png'>At the end of each dendrite is a receptor for a chemical known as a <b>neurotransmitter</b>.</p>" +
                    "<p><img class='bpoint' src='/static/bulletpoint.png'>Cells communicate by passing these neurotransmitters as signals.</p>" +
                    "<p><img class='bpoint' src='/static/bulletpoint.png'>A small gap between neurons known as the <b>synapse</b> is where these transmitters" +
                    " are transferred.</p>",
        "right_image": None,
        "model": "/static/models/synapse/scene.gltf",
        "model_bg": "0xDDFFF7",
        "puzzle" : ["ETFGRRIEFTEH","TGIERWREOHTE"],
        "solution": ["FIRETOGETHER", "WIRETOGETHER"],
        "concept_title" : "Transmission",
        "mnemonic":["<span class='first-letter-btn'>T</span>ransmission - ","<span class='first-letter-btn'>T</span>hinking"],
        "next": "/learn/3",
        "back": "/learn/1",
        "next_num": "Lesson 3",
        "back_num": "Lesson 1",
        "time": None
     },
  {
        "id": 3,
        "title": "<span class='first-letter'>B</span> <span class='heading'>" +
                    "a s i c s </span>&nbsp;&nbsp;-&nbsp;&nbsp; <span class='first-letter'>" +
                    "N</span> <span class='heading'>e u r o t r a n s m i t t e r s</span>" +
                    "<div class='row mt-0 pt-0'><div class='col-12 mt-0 pt-0'>" +
                    "<span class='sub-heading'>L e s s o n &nbsp;&nbsp; 3 :&nbsp;&nbsp;" +
                    "G a m m a - a m i n o b u t y r i c &nbsp;&nbsp; a c i d &nbsp;&nbsp;"
                    "</span></div></div>",
        "left_box": "<p><img class='bpoint' src='/static/bulletpoint.png'>Reduces the amount of activity a cell can transmit</p>",
        "right_image":"gaba.png",
        "model": "/static/models/gaba/scene.gltf",
        "model_bg": "0xDDFFF7",        
        "puzzle" : ["MGMMA","OBCONYMIIART","DCIA"],
        "solution": ["GAMMA", "AMINOBUTYRIC", "ACID"],
        "concept_title" : "GABA",
        "nt_effect": "Stress and anxiety",
        "nt_dir": "Down",
        "mnemonic":["<span class='first-letter-btn'>G</span>ABA - ","<span class='first-letter-btn'>G</span>reatly eases anxiety"],
        "next": "/learn/4",
        "back": "/learn/2",
        "next_num": "Lesson 4",
        "back_num": "Lesson 2",        
        "time": None
    },    
  {
        "id": 4,
        "title": "<span class='first-letter'>B</span> <span class='heading'>" +
                    "a s i c s </span>&nbsp;&nbsp;-&nbsp;&nbsp; <span class='first-letter'>" +
                    "N</span> <span class='heading'>e u r o t r a n s m i t t e r s</span>" +
                    "<div class='row mt-0 pt-0'><div class='col-12 mt-0 pt-0'>" +
                    "<span class='sub-heading'>L e s s o n &nbsp;&nbsp; 4 :&nbsp;&nbsp;" +
                    "S e r o t o n i n  &nbsp;&nbsp; a n d &nbsp;&nbsp; M o o d " +
                    "</span></div></div>",
        "left_box": "<p><img class='bpoint' src='/static/bulletpoint.png'>Regulates mood, sleep and digestion.</p>",
        "right_image":"serotonin.png",
        "model": "/static/models/serotonin2/scene.gltf",
        "model_bg": "0xDDFFF7",
        "puzzle" : ["NROOEINST","OSNTLOCR","ISHPAENPS"],
        "solution": ["SEROTONIN", "CONTROLS", "HAPPINESS"],
        "concept_title" : "Serotonin",
        "nt_effect": "Depression",
        "nt_dir": "Down",
        "mnemonic":["<span class='first-letter-btn'>S</span>erotonin - ","<span class='first-letter-btn'>S</span>adness"],
        "next": "/learn/5",
        "back": "/learn/3",
        "next_num": "Lesson 5",
        "back_num": "Lesson 3",        
        "time": None
    },    
     {
        "id": 5,
        "title": "<span class='first-letter'>B</span> <span class='heading'>" +
                    "a s i c s </span>&nbsp;&nbsp;-&nbsp;&nbsp; <span class='first-letter'>" +
                    "N</span> <span class='heading'>e u r o t r a n s m i t t e r s</span>" +
                    "<div class='row mt-0 pt-0'><div class='col-12 mt-0 pt-0'>" +
                    "<span class='sub-heading'>L e s s o n &nbsp;&nbsp; 5 :&nbsp;&nbsp;" +
                    "D o p a m i n e &nbsp;&nbsp; a n d &nbsp;&nbsp; A t t e n t i o n" +
                    "</span></div></div>",
        "left_box": "<p><img class='bpoint' src='/static/bulletpoint.png'>Associated with attention and reward.</p>",
        "right_image":"dopamine.png",
        "model": "/static/models/dopamine/scene.gltf",
        "model_bg": "0xDDFFF7",
        "puzzle" : ["UIGBNSRT","HWTI", "YREENG"],
        "solution": ["BURSTING", "WITH", "ENERGY"],
        "concept_title" : "Dopamine",
        "nt_effect": "Motivation",
        "nt_dir": "Up",
        "mnemonic":["<span class='first-letter-btn'>D</span>opamaine - ","<span class='first-letter-btn'>D</span>ynamic"],
        "next": "/learn/6",
        "back": "/learn/4",
        "next_num": "Lesson 6",
        "back_num": "Lesson 4",        
        "time": None
    },    
       {
        "id": 6,
        "title": "<span class='first-letter'>S</span> <span class='heading'>" +
                    "e n s e s </span>&nbsp;&nbsp;-&nbsp;&nbsp; <span class='first-letter'>" +
                    "V</span> <span class='heading'>i s i o n</span>" +
                    "<div class='row mt-0 pt-0'><div class='col-12 mt-0 pt-0'>" +
                    "<span class='sub-heading'>L e s s o n &nbsp;&nbsp; 6 :&nbsp;&nbsp;" +
                    "O c c i p i t a l &nbsp;&nbsp; L o b e</span></div></div>",
        "left_box": "<p><img class='bpoint' src='/static/bulletpoint.png'>Recognize faces</p>" +
                    "<p><img class='bpoint' src='/static/bulletpoint.png'>Process input from the eyes</p>" +
                    "<p><img class='bpoint' src='/static/bulletpoint.png'>Color vision</p>" +
                    "<p><img class='bpoint' src='/static/bulletpoint.png'>Shapes and depth</p>",
        "right_image": None,
        "model": "/static/models/occipital_bone/scene.gltf",
        "model_bg": "0xDDFFF7",
        "puzzle" : ["UIGBNSRT","HWTI", "YREENG"],
        "solution": ["BURSTING", "WITH", "ENERGY"],
        "concept_title" : "Occipital Lobe",
        "nt_effect": None,
        "nt_dir": None,
        "mnemonic":["<span class='first-letter-btn'>O</span>occipital - ","<span class='first-letter-btn'>O</span>cular"],
        "next": "/learn/7",
        "back": "/learn/5",
        "next_num": "Lesson 7",
        "back_num": "Lesson 5",        
        "time": None
    },    
       {
        "id": 7,
        "title": "<span class='first-letter'>S</span> <span class='heading'>" +
                    "e n s e s </span>&nbsp;&nbsp;-&nbsp;&nbsp; <span class='first-letter'>" +
                    "T</span> <span class='heading'>o u c h</span>" +
                    "<div class='row mt-0 pt-0'><div class='col-12 mt-0 pt-0'>" +
                    "<span class='sub-heading'>L e s s o n &nbsp;&nbsp; 7 :&nbsp;&nbsp;" +
                    "P a r i e t a l &nbsp;&nbsp; L o b e</span></div></div>",
        "left_box": "<p><img class='bpoint' src='/static/bulletpoint.png'>Sensation of temperature, pressure, vibration, pain</p>" +
                    "<p><img class='bpoint' src='/static/bulletpoint.png'>Writing and precise hand movement</p>" +
                    "<p><img class='bpoint' src='/static/bulletpoint.png'>Symbol recognition - reading and math</p>" +
                    "<p><img class='bpoint' src='/static/bulletpoint.png'>Navigation of physical space</p>",
        "right_image": None,
        "model": "/static/models/parietal_bone/scene.gltf",
        "model_bg": "0xDDFFF7",
        "puzzle" : ["UIGBNSRT","HWTI", "YREENG"],
        "solution": ["BURSTING", "WITH", "ENERGY"],
        "concept_title" : "Parietal Lobe",
        "nt_effect": None,
        "nt_dir": None,
        "mnemonic":["<span class='first-letter-btn'>P</span>arietal - ","<span class='first-letter-btn'>P</span>ain"],
        "next": "/learn/8",
        "back": "/learn/6",
        "next_num": "Lesson 8",
        "back_num": "Lesson 6",        
        "time": None
    },   

       {
        "id": 8,
        "title": "<span class='first-letter'>S</span> <span class='heading'>" +
                    "e n s e s </span>&nbsp;&nbsp;-&nbsp;&nbsp; <span class='first-letter'>" +
                    "H</span> <span class='heading'>e a r i n g</span>" +
                    "<div class='row mt-0 pt-0'><div class='col-12 mt-0 pt-0'>" +
                    "<span class='sub-heading'>L e s s o n &nbsp;&nbsp; 8 :&nbsp;&nbsp;" +
                    "T e m p o r a l &nbsp;&nbsp; L o b e</span></div></div>",
        "left_box": "<p><img class='bpoint' src='/static/bulletpoint.png'>Understand music and harmonies</p>" +
                    "<p><img class='bpoint' src='/static/bulletpoint.png'>Process input from the ears</p>" +
                    "<p><img class='bpoint' src='/static/bulletpoint.png'>Associated with speech</p>" +
                    "<p><img class='bpoint' src='/static/bulletpoint.png'>Located behind the temples</p>",
        "right_image": None,
        "model": "/static/models/temporal_bone/scene.gltf",
        "model_bg": "0xDDFFF7",
        "puzzle" : ["UIGBNSRT","HWTI", "YREENG"],
        "solution": ["BURSTING", "WITH", "ENERGY"],
        "concept_title" : "Temporal Lobe",
        "nt_effect": None,
        "nt_dir": None,
        "mnemonic":["<span class='first-letter-btn'>T</span>temporal - ","<span class='first-letter-btn'>T</span>emples"],
        "next": "/learn/9",
        "back": "/learn/7",
        "next_num": "Lesson 9",
        "back_num": "Lesson 7",        
        "time": None
    },   

       {
        "id": 9,
        "title": "<span class='first-letter'>I</span> <span class='heading'>" +
                    "n t e l l i g e n c e &nbsp;&nbsp; a n d </span>&nbsp;&nbsp; <span class='first-letter'>" +
                    "R</span> <span class='heading'>e a s o n</span>" +
                    "<div class='row mt-0 pt-0'><div class='col-12 mt-0 pt-0'>" +
                    "<span class='sub-heading'>L e s s o n &nbsp;&nbsp; 9 :&nbsp;&nbsp;" +
                    "F r o n t a l &nbsp;&nbsp; L o b e</span></div></div>",
        "left_box": "<p><img class='bpoint' src='/static/bulletpoint.png'>Reasoning and logical arguments</p>" +
                    "<p><img class='bpoint' src='/static/bulletpoint.png'>Planning and making schedules</p>" +
                    "<p><img class='bpoint' src='/static/bulletpoint.png'>Being able to imagine the future</p>" +
                    "<p><img class='bpoint' src='/static/bulletpoint.png'>Storage of information in working memory.</p>",
        "right_image": None,
        "model": "/static/models/frontal_bone/scene.gltf",
        "model_bg": "0xDDFFF7",
        "puzzle" : ["UIGBNSRT","HWTI", "YREENG"],
        "solution": ["BURSTING", "WITH", "ENERGY"],
        "concept_title" : "Frontal Lobe",
        "nt_effect": None,
        "nt_dir": None,
        "mnemonic":["<span class='first-letter-btn'>F</span>rontal - ","<span class='first-letter-btn'>F</span>orethought"],
        "next": "/learn/10",
        "back": "/learn/8",
        "next_num": "Lesson 10",
        "back_num": "Lesson 8",        
        "time": None
    },   
     {
        "id": 10,
        "title": "<span class='first-letter'>E</span> <span class='heading'>" +
                    "m o t i o n s </span>&nbsp;&nbsp; - <span class='first-letter'>" +
                    "F</span> <span class='heading'>e a r</span>" +
                    "<div class='row mt-0 pt-0'><div class='col-12 mt-0 pt-0'>" +
                    "<span class='sub-heading'>L e s s o n &nbsp;&nbsp; 10 :&nbsp;&nbsp;" +
                    "T h e &nbsp;&nbsp; A m y g d a l a &nbsp;&nbsp;</span></div></div>",
        "left_box": "<p><img class='bpoint' src='/static/bulletpoint.png'>Almond-shaped structure in the inner brain</p>" 
                    "<p><img class='bpoint' src='/static/bulletpoint.png'>Located at the end of the hippocampus<p>" +
                    "<p><img class='bpoint' src='/static/bulletpoint.png'>Responsible for fear and aggression</p>",
        "right_image": None,
        "model": "/static/models/amygdala/scene.gltf",
        "model_bg": "0xDDFFF7",
        "puzzle" : ["UIGBNSRT","HWTI", "YREENG"],
        "solution": ["BURSTING", "WITH", "ENERGY"],
        "concept_title" : "Amygdala",
        "nt_effect": None,
        "nt_dir": None,
        "mnemonic":["<span class='first-letter-btn'>A</span>mygdala - ","<span class='first-letter-btn'>A</span>nxiety"],
        "next": "/learn/11",
        "back": "/learn/9",
        "next_num": "Lesson 11",
        "back_num": "Lesson 9",        
        "time": None
    },     
         {
        "id": 11,
        "title": "<span class='first-letter'>E</span> <span class='heading'>" +
                    "m o t i o n s </span>&nbsp;&nbsp; - <span class='first-letter'>" +
                    "L</span> <span class='heading'>o v e</span>" +
                    "<div class='row mt-0 pt-0'><div class='col-12 mt-0 pt-0'>" +
                    "<span class='sub-heading'>L e s s o n &nbsp;&nbsp; 11 :&nbsp;&nbsp;" +
                    "T h e &nbsp;&nbsp; H y p o t h a l a m u s &nbsp;&nbsp;</span></div></div>",
        "left_box": "<p><img class='bpoint' src='/static/bulletpoint.png'>Reward center of the brain</p>" + 
                    "<p><img class='bpoint' src='/static/bulletpoint.png'>Love increases dopamaine</p>" +
                    "<p><img class='bpoint' src='/static/bulletpoint.png'>Processed in hypothalamus as reward</p>" +
                    "<p><img class='bpoint' src='/static/bulletpoint.png'>Also responsible for hunger/thirst/sex drive</p>" +
                    "<p><img class='bpoint' src='/static/bulletpoint.png'>Responsible for releasing hormones",
        "right_image": None,
        "model": "/static/models/hypothalamus/scene.gltf",
        "model_bg": "0xDDFFF7",
        "puzzle" : ["UIGBNSRT","HWTI", "YREENG"],
        "solution": ["BURSTING", "WITH", "ENERGY"],
        "concept_title" : "Hypothalamus",
        "nt_effect": None,
        "nt_dir": None,
        "mnemonic":["<span class='first-letter-btn'>H</span>ypothalamus - ","<span class='first-letter-btn'>H</span>ormones"],
        "next": "/learn/12",
        "back": "/learn/10",
        "next_num": "Lesson 12",
        "back_num": "Lesson 10",        
        "time": None
    },
         {
        "id": 12,
        "title": "<span class='first-letter'>M</span> <span class='heading'>" +
                    "e m o r y </span>&nbsp;&nbsp;" +
                    "<div class='row mt-0 pt-0'><div class='col-12 mt-0 pt-0'>" +
                    "<span class='sub-heading'>L e s s o n &nbsp;&nbsp; 12 :&nbsp;&nbsp;" +
                    "T h e &nbsp;&nbsp; H i p p o c a m p u s &nbsp;&nbsp;</span></div></div>",
        "left_box": "<p><img class='bpoint' src='/static/bulletpoint.png'>Sliver-shaped structure in inner brain</p>" + 
                    "<p><img class='bpoint' src='/static/bulletpoint.png'>Long-term memory</p>" +
                    "<p><img class='bpoint' src='/static/bulletpoint.png'>Spatial/navigational mental maps</p>" +
                    "<p><img class='bpoint' src='/static/bulletpoint.png'>Important in learning</p>",
        "right_image": None,
        "model": "/static/models/hippocampus/scene.gltf",
        "model_bg": "0xDDFFF7",
        "puzzle" : ["UIGBNSRT","HWTI", "YREENG"],
        "solution": ["BURSTING", "WITH", "ENERGY"],
        "concept_title" : "Hippocampus",
        "nt_effect": None,
        "nt_dir": None,
        "mnemonic":["<span class='first-letter-btn'>H</span>ippocampus - ","<span class='first-letter-btn'>H</span>old in Memory"],
        "next": "/learn/f",
        "back": "/learn/11",
        "next_num": "Quiz",
        "back_num": "Lesson 11",        
        "time": None
    },
]


learn_puzzles = [
    {
        "id": 1,
        "html": """ 
            <script>
      var puzzleList = "No puzzle";</script>
    <div class="col-12 col-md-6 col-lg-3 p-4">
      <div class="row box-right">
    <div class="puz-container p-4" id="puz-container">
      <div class="image-container">
        <img src="/static/neuron_small.png" alt="Neuron" id="puz1">
        <div class="blank-field-body newsreader-400 p-2 white-text text-center" data-correct="Cell Body"></div>
        <div class="blank-field-axon newsreader-400 p-2 white-text text-center" data-correct="Axon"></div>
        <div class="blank-field-dendr newsreader-400 p-2 white-text text-center" data-correct="Dendrites"></div>

        <!-- Add more blank fields as needed -->
      </div>       
      <div class="boxes-container">
        <div class="box" id="axon-box"></div>
        <div class="box" id="dendr-box"></div>
        <div class="box" id="body-box"></div>
      </div>     
      <div class="words-container">
        <div class="word-box draggable newsreader-400">Axon</div>
        <div class="word-box draggable newsreader-400">Dendrites</div>
        <div class="word-box draggable newsreader-400">Cell Body</div>
        <!-- Add more draggable words as needed -->
      </div>
    </div>
    </div>"""
    },
    { "id": 2,
        "html": """ 
            <script>
      var puzzleList = "No puzzle";</script>
    <div class="col-12 col-md-6 col-lg-3 p-4">
      <div class="row box-right">
    <div class="puz-container p-4" id="puz-container">
      <div class="image-container">
        <img src="/static/synapse_small.png" alt="Synapse" id="puz1">'
        <div class="blank-field-body newsreader-400 p-2 white-text text-center" data-correct="Neurotransmiters"></div>
        <div class="blank-field-axon newsreader-400 p-2 white-text text-center" data-correct="Synapse"></div>
        <div class="blank-field-dendr newsreader-400 p-2 white-text text-center" data-correct="Receptors"></div>
        <div class="blank-field-vesicle newsreader-400 p-2 white-text text-center" data-correct="Vesicle"></div>

        <!-- Add more blank fields as needed -->
      </div>  
      <div class="boxes-container">
        <div class="box" id="nt-box"></div>
        <div class="box" id="syn-box"></div>
        <div class="box" id="recept-box"></div>
        <div class="box" id="vesicle-box"></div>
      </div>     
      <div class="words-container">
        <div class="word-box draggable newsreader-400">Neurotransmitters</div>
        <div class="word-box draggable newsreader-400">Synapse</div>
        <div class="word-box draggable newsreader-400">Receptors</div>
        <div class="word-box draggable newsreader-400">Vesicles</div>        
        <!-- Add more draggable words as needed -->
      </div>
      <div>What purpose does neurotransmission serve?</div>
    </div>
    </div>"""
    },
    

]



###################   TBC - Larry  ##################


quiz_questions = {
    "1": {
        "quiz_id": "1",
        "image": "",
        "question": "Match the neurotransmitters with their functions:",
        "options": ["Serotonin", "Norepinephrine", "GABA", "Dopamine"],
        "descriptions": [
            "Regulates mood, sleep, and digestion",
            "Increases alertness and arousal",
            "Reduces stress and anxiety",
            "Associated with pleasure and motivation"
        ],
        "correct_matches": {
            "Serotonin": "Regulates mood, sleep, and digestion",
            "Norepinephrine": "Increases alertness and arousal",
            "GABA": "Reduces stress and anxiety",
            "Dopamine": "Associated with pleasure and motivation"
        },
        "next_question": "2",
        # go back to last learning page
        "previous_question": '/learn/12',
        "title" : "<span class='first-letter'>Q</span> <span class='text-lg'>" +  
          "u i z </span>&nbsp;&nbsp;-&nbsp;&nbsp; <span class='first-letter'>Q</span> <span class='text-lg'>" +
          "u e s t i o n &nbsp;&nbsp;N o .&nbsp;1</span>" +
          "<div class='row mt-0 pt-0'><div class='col-12 mt-0 pt-0'>" + 
          "<span class='sub-heading'></span></div></div>",
    },
    "2": {
        "quiz_id": "2",
        "model": '/models/neuron_quiz/scene.gltf',
        "image": 'dendrites.png',
        "question": "What are these called?",
        "options" : ['Neurons', 'Dendrites', 'Limbic System', 'Axons' ],
        "answer" : "Dendrites",
        "next_question": "3",
         "previous_question": "1",
         "title" : "<span class='first-letter'>Q</span> <span class='text-lg'>" +  "u i z </span>&nbsp;&nbsp;-&nbsp;&nbsp; <span class='first-letter'>Q</span> <span class='text-lg'>" +
              "u e s t i o n &nbsp;&nbsp;N o .&nbsp;2</span>" +
               "<div class='row mt-0 pt-0'><div class='col-12 mt-0 pt-0'>" + 
          "<span class='sub-heading'></span></div></div>"
    },
    "3": {
        "quiz_id": "3",
        "model": "models/frontal_quiz/scene.gltf",
        "image": "frontal_lobe.png",
        "question": "Which area of the brain is highlighted here?  What is its function?",
        "options" : ['Occipital lobe - hearing', 'Temporal lobe - sound', 'Occipital lobe - vision', 'Frontal lobe - reasoning'],
        "answer" : "Frontal lobe - reasoning", 
        "next_question": "4",
        "previous_question" : "2",
        "title" : "<span class='first-letter'>Q</span> <span class='text-lg'>" +  "u i z </span>&nbsp;&nbsp;-&nbsp;&nbsp; <span class='first-letter'>Q</span> <span class='text-lg'>" +
              "u e s t i o n &nbsp;&nbsp;N o .&nbsp;3</span>" +
               "<div class='row mt-0 pt-0'><div class='col-12 mt-0 pt-0'>" + 
          "<span class='sub-heading'></span></div></div>"
    },
    "4": {
        "quiz_id": "4",
        "image": "",
        "question": "Where is the hypothalamus and what does it do",
        "options" : ['Midbrain - processes memory',
'Limbic System - controls hunger', 'Temporal lobe - controls body temperature', 'Thalamus - processes emotion'],
        "answer" : "Limbic System - controls hunger",
        "next_question": "5",
        "previous_question" : "3",
        "title" : "<span class='first-letter'>Q</span> <span class='text-lg'>" +  "u i z </span>&nbsp;&nbsp;-&nbsp;&nbsp; <span class='first-letter'>Q</span> <span class='text-lg'>" +
              "u e s t i o n &nbsp;&nbsp;N o .&nbsp;4</span>" +
               "<div class='row mt-0 pt-0'><div class='col-12 mt-0 pt-0'>" + 
          "<span class='sub-heading'></span></div></div>"
    },
    "5": {
        "quiz_id": "5",
        "image": "amygdala_quiz.png",
        "question": "What is this structure called?",
        "options" : ['Amygdala', 'Cell Body', 'Thalamus ', 'Hippocampus'],
        "answer" : "Amygdala",
        "next_question": "6",
        "previous_question" : "4",
        "title" : "<span class='first-letter'>Q</span> <span class='text-lg'>" +  "u i z </span>&nbsp;&nbsp;-&nbsp;&nbsp; <span class='first-letter'>Q</span> <span class='text-lg'>" +
              "u e s t i o n &nbsp;&nbsp;N o .&nbsp;5</span>" +
               "<div class='row mt-0 pt-0'><div class='col-12 mt-0 pt-0'>" + 
          "<span class='sub-heading'></span></div></div>"
    },
    "6": {
        "quiz_id": "6",
        "image": "",
        "question": "A young man presents to the hospital saying he cannot see.  Which part of of the brain did he injure?",
        "options" : ['Temporal Lobe', 'Hippocampus', 'Occipital Lobe', 'Frontal Lobe'],
        "answer" : "Occipital Lobe",
        "next_question": "7",
        "previous_question" : "5",
         "title" : "<span class='first-letter'>Q</span> <span class='text-lg'>" +  "u i z </span>&nbsp;&nbsp;-&nbsp;&nbsp; <span class='first-letter'>Q</span> <span class='text-lg'>" +
              "u e s t i o n &nbsp;&nbsp;N o .&nbsp;6</span>" +
               "<div class='row mt-0 pt-0'><div class='col-12 mt-0 pt-0'>" + 
          "<span class='sub-heading'></span></div></div>"
    },
    "7": {
        "quiz_id": "7",
        "image": "",
        "question": "What types of cells are found in the brain?",
        "options" : ['Axons', 'Dendrites', 'Neurons', 'Neurotransmitters'],
        "answer" : "Neurons",
        "next_question": "8",
         "previous_question" : "6",
          "title" : "<span class='first-letter'>Q</span> <span class='text-lg'>" +  "u i z </span>&nbsp;&nbsp;-&nbsp;&nbsp; <span class='first-letter'>Q</span> <span class='text-lg'>" +
              "u e s t i o n &nbsp;&nbsp;N o .&nbsp;7</span>" +
               "<div class='row mt-0 pt-0'><div class='col-12 mt-0 pt-0'>" + 
          "<span class='sub-heading'></span></div></div>"
    },
    "8": {
        "quiz_id": "8",
        "image": "temporal_lobe.png",
        "question": "Which area of the brain is highlighted here?  What is its function?",
        "options" : ['Occipital lobe - hearing', 'Temporal lobe - sound', 'Occipital lobe - vision', 'Frontal lobe - reasoning'],
        "answer" : "Temporal lobe - sound",
        "next_question": "end",
         "previous_question" : "7",
         "title" : "<span class='first-letter'>Q</span> <span class='text-lg'>" +  "u i z </span>&nbsp;&nbsp;-&nbsp;&nbsp; <span class='first-letter'>Q</span> <span class='text-lg'>" +
              "u e s t i o n &nbsp;&nbsp;N o .&nbsp;8</span>" +
               "<div class='row mt-0 pt-0'><div class='col-12 mt-0 pt-0'>" + 
          "<span class='sub-heading'></span></div></div>"
         
    },
    
}
    


# ROUTES

###################   TBC - Dallas  ###################


@app.route('/')
def welcome():
    title = ('<div class="row m-0 p-0"><div class="col-12 m-0 p-0 reduce-space">' +
              '<b><span class="first-letter">B</span>'+
                '<span class="bullet1">&bull;</span>' + 
            'r <span class="bullet1">&bull;</span>' +
            'a <span class="bullet1">&bull;</span>' +
            'i <span class="bullet1">&bull;</span>' +
            'n &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;' +
            '<span class="first-letter">B</span>' +
            '<span class="bullet2">&bull;</span>' +
            'u <span class="bullet2">&bull;</span>' +
            'i <span class="bullet2">&bull;</span>' +
            'l <span class="bullet2">&bull;</span>' +
            'd</b></div></div>' +
            '<div class="row mt-0 pt-0"><div class="col-12 mt-0 pt-0">' +
            '<span class="sub-heading">T h e &nbsp;&nbsp;' +
            'A n a t o m y &nbsp;&nbsp;a n d &nbsp;&nbsp;' +
            'F u n c t i o n &nbsp;&nbsp;o f &nbsp;&nbsp;' +
            't h e &nbsp;&nbsp;H u m a n &nbsp;&nbsp;B r a i n</span></div></div>')
    session.clear()
    start_time = datetime.datetime.now()
    access_time = start_time.strftime("%B %d, %Y at %I:%M %p")
    model = "/static/models/human_brain/scene.gltf"
    return render_template('welcome.html', data=access_time, title=title, model=model)   


@app.route('/learn/<int:lesson_id>')
def learn(lesson_id):
    int(lesson_id)
    end_time = datetime.datetime.now()
    access_time = end_time.strftime("%B %d, %Y at %I:%M %p")
    data = next((item for item in learn_data if item['id'] == lesson_id), None)
    puzzle_data = next((item for item in learn_puzzles if item['id'] == lesson_id), None)
    duration = end_time - start_time
    duration = round(duration.seconds/60)
    durPrint = 'It is currently ' + access_time + '.  You have been learning' + ' for <b>' + str(duration) + '</b> minutes.'
    model = data['model']    
    title = data['title'] 
    if (puzzle_data):
        puzzle_data = puzzle_data['html'].replace("\n", "")    
        print(puzzle_data)
    if (lesson_id == len(learn_data)):
        next_text = "Quiz Me"
    return render_template('learn.html', lesson=data, duration=durPrint, title=title, model=model, puzzle=puzzle_data) 

@app.route('/learn/f')
def learn_done():
    end_time = datetime.datetime.now()
    access_time = end_time.strftime("%B %d, %Y at %I:%M %p")
    duration = end_time - start_time
    duration = round(duration.seconds/60)
    title = ('<span class="first-letter">E</span>n d  &nbsp;&nbsp;of' +
            '&nbsp;&nbsp;<span class="first-letter">L</span> e a r n i n g')
    return render_template('learn_done.html', minutes=duration, title=title)



###################   TBC - Larry  ####################

@app.route('/quiz/models')
def quiz_models():
        return render_template('quiz_models.html', title="Quiz Models")    


@app.route('/quiz/<quiz_id>', methods=['GET', 'POST'])
def quiz(quiz_id):
    question = quiz_questions.get(quiz_id)

    if request.method == 'POST':
        feedback = ""
        feedback_class = ""
        submitted_answers = {}

        if quiz_id == "1":
            correct_matches = question["correct_matches"]
            score = 0
            for neurotransmitter, description in correct_matches.items():
                user_answer = request.form.get(neurotransmitter)
                submitted_answers[neurotransmitter] = user_answer
                if user_answer == description:
                    score += 1

            if score == len(correct_matches):
                feedback = 'Correct! Good job.'
                feedback_class = 'correct-feedback'
            else:
                matches_str = '<br>'.join([f'<strong>{nt}</strong>: {desc}' for nt, desc in correct_matches.items()])
                flash(f'Incorrect! The correct matches are:<br>{matches_str}', 'incorrect-feedback')

        else:
            user_answer = request.form.get('option')
            submitted_answers['option'] = user_answer
            correct_answer = question['answer']
            if user_answer == correct_answer:
                session['score'] = session.get('score', 0) + 1
                feedback = 'Correct! Good job.'
                feedback_class = 'correct-feedback'
            else:
                feedback = f'Incorrect! The correct answer is <strong>{correct_answer}</strong>.'
                feedback_class = 'incorrect-feedback'

        question['submitted'] = True
        question['submitted_answers'] = submitted_answers
        question['feedback'] = feedback
        question['feedback_class'] = feedback_class

        return render_template('quiz.html', question=question, quiz=question, title=question.get('title', 'Quiz Question'))

    else:
        question['submitted'] = False
        question['submitted_answers'] = {}
        question['feedback'] = ''
        question['feedback_class'] = ''

        return render_template('quiz.html', question=question, quiz=question, title=question.get('title', 'Quiz Question'))

@app.route('/results')
def results():
    title = ("<span class='first-letter'>Q</span> <span class='text-lg'>u i z </span>&nbsp;&nbsp;-&nbsp;&nbsp; " +
         "<span class='first-letter'>R</span> <span class='text-lg'>e s u l t s</span>" +
         "<div class='row mt-0 pt-0'><div class='col-12 mt-0 pt-0'><span class='sub-heading'></span></div></div>")
    score = session.get('score', 0)
    total = 8
    return render_template('results.html', score=score, 
                          total=total, title=title)

@app.route('/answers')
def answers():
    score = session.get('score', 0)
    total = 8
    return render_template('answers.html',questions=quiz_questions)


if __name__ == '__main__':
    app.run(debug=True)



