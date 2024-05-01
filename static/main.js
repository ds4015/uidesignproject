// --- Dallas Scott - ds4015 ---
// JavaScript for both models and puzzle solving



// three.JS for 3D modeling
import * as THREE from 'three';

import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';


var lessonModel = document.querySelector('#modelTest').value;

if (lessonModel !== "no_model") {
    const scene = new THREE.Scene();

    const renderer = new THREE.WebGLRenderer({ antialias: true });

    document.getElementById('model').appendChild(renderer.domElement);
    const width = model.clientWidth;
    const height = model.clientHeight;
    const camera = new THREE.PerspectiveCamera(75, width / height, 0.1, 1000);

    var modelBgColor = document.querySelector('#modelBg').value;
    var rotationSpeed = document.querySelector('#rotSpeed').value;
    var color = new THREE.Color().setHex(modelBgColor);
    renderer.setClearColor(color);


    renderer.setSize(width, height);

    const mpath = document.getElementById('model').getAttribute('data-path');

    const loader = new GLTFLoader();
    loader.load(mpath, function (gltf) {
        let model = gltf.scene;
        if (window.innerWidth < 810) {
            model.scale.set(6, 6, 6);
        } else {
            model.scale.set(2.5, 2.5, 2.5);
        }
        scene.add(model);
        function animate() {
            requestAnimationFrame(animate);
            renderer.render(scene, camera);
            if (rotateEnabled) {
                model.rotation.y -= rotationSpeed;
            }
            controls.update();
        }
        animate();
    }, undefined, function (error) {
        console.error(error);
    });


    camera.position.set(0, 0, 0);
    camera.position.z = 0.3;
    const ambLight = new THREE.AmbientLight(0x404040);
    scene.add(ambLight);

    const spotLight = new THREE.SpotLight(0xffffff);
    const spotLight2 = new THREE.SpotLight(0xffffff);
    const spotLight3 = new THREE.SpotLight(0xffffff);
    const spotLight4 = new THREE.SpotLight(0xffffff);    
    spotLight.position.set(1, 1, 0);
    spotLight2.position.set(1, -1, 0)
    spotLight3.position.set(-1, 1, 0);
    spotLight4.position.set(-1, -1, 0)

    spotLight.intensity = 3;
    spotLight2.intensity = 3;
    spotLight3.intensity = 2;
    spotLight4.intensity = 2;

    spotLight.castShadow = true;


    scene.add(spotLight);
    scene.add(spotLight2);
    scene.add(spotLight3);
    scene.add(spotLight4);



    const controls = new OrbitControls(camera, renderer.domElement);
    controls.target.set(0, 0, 0);
    controls.enableDamping = true;
    controls.dampingFactor = 0.25;
    controls.zoomSpeed = 0.5;

    let isFirstClick = true;
    const minDistance = 0.25;


    controls.addEventListener('change', () => {

        const distance = controls.object.position.distanceTo(controls.target);
        if (distance <= minDistance) {
            controls.object.position.setLength(minDistance);
        }
    });


    function updateCameraPosition() {
        if (window.innerWidth <= 1280 && window.innerWidth > 810) {
            camera.position.z = 0.34;
        } else if (window.innerWidth <= 810) {
            camera.position.z = 0.5;
        } else if (window.innerWidth > 810 && window.innerWidth < 1280) {
            camera.position.z = 0.35;
        } else {
            camera.position.z = 0.3;
        }
        camera.updateProjectionMatrix();
    }

    updateCameraPosition();

    window.addEventListener('resize', updateCameraPosition);


    let rotateEnabled = true;


    document.addEventListener('mousedown', () => {
        rotateEnabled = !rotateEnabled;
    });
    document.addEventListener('mouseup', () => {
        rotateEnabled = !rotateEnabled;
    });

    controls.update();

}


// puzzle display and solving
if (puzzleList != "No puzzle") {

var wordBlanks = puzzleList.map(function (word) {
    return Array(word.length).fill('_');
});


function displayWordsAndBlanks() {
    var wordsDiv = document.getElementById('puzzle');
    wordsDiv.innerHTML = '';
    var wordDivs = [];
    var blankDivs = [];
    var spanList = [];

    var lettersFound = 0;
    var totalLetters = 0;

    puzzleList.forEach(function (word, index) {
        totalLetters += word.length;
    });

    puzzleList.forEach(function (word, index) {
        var wordDiv = document.createElement('div');
        wordDiv.classList.add("p-2");
        wordDiv.classList.add("text-center");
        wordDiv.classList.add("text-md");
        wordDivs.push(wordDiv);
        var blanksDiv = document.createElement('div');
        blanksDiv.classList.add("p-2");
        blanksDiv.classList.add("p-2");
        blanksDiv.classList.add("pb-0");
        blanksDiv.classList.add("text-center");
        blanksDiv.classList.add("mb-4");

        blanksDiv.classList.add('blanks');

        word.split('').forEach(function (letter) {
            var span = document.createElement('span');
            span.textContent = letter;
            wordDiv.appendChild(span);
        });

        wordBlanks[index].forEach(function (blank, i) {
            var input = document.createElement('input');
            input.classList.add('puzzle');
            input.classList.add('blank');
            input.setAttribute('type', 'text');
            input.setAttribute('maxlength', '1');
            input.setAttribute('size', '1');

            input.addEventListener('keydown', function (event) {

                if (event.key === 'Backspace' && this.value === '') {
                    var inputs = blanksDiv.children;
                    var currentIndex = 0;
                    for (var j = 0; j < inputs.length; j++) {
                        var input2 = inputs[j];
                        if (input2 === this) {
                            currentIndex = j;
                            break;
                        }
                    }
                    var previousIndex = currentIndex - 1;
                    while (previousIndex >= 1) {
                        if (inputs[previousIndex].tagName.toLowerCase() === 'input') {
                            break;
                        }
                        previousIndex--;
                    }
                    if (previousIndex > 0) {
                        inputs[previousIndex].value = '';
                        inputs[previousIndex].classList.remove('correct');
                        inputs[previousIndex].classList.remove('incorrect');
                        wordBlanks[index][previousIndex] = '_';
                        blanksDiv.children[previousIndex].focus();

                    } else {
                        inputs[0].value = '';
                        inputs[0].classList.remove('correct');
                        inputs[0].classList.remove('incorrect');
                        wordBlanks[index][0] = '_';
                        blanksDiv.children[0].focus();
                    }

                    event.preventDefault();
                } else if (event.key === 'Backspace') {
                    var inputs = blanksDiv.children;
                    var currentIndex = 0;
                    for (var j = 0; j < inputs.length; j++) {
                        var input2 = inputs[j];
                        if (input2 === this) {
                            currentIndex = j;
                            break;
                        }
                    }

                    var previousIndex = currentIndex - 1;
                    while (previousIndex >= 1) {
                        if (inputs[previousIndex].tagName.toLowerCase() === 'input') {
                            break;
                        }
                        previousIndex--;
                    }

                    if (previousIndex > 0) {
                        blanksDiv.children[previousIndex].focus();
                    }
                    inputs[currentIndex].value = '';
                    inputs[currentIndex].classList.remove('correct');
                    inputs[currentIndex].classList.remove('incorrect');
                    wordBlanks[index][i] = '_';
                    event.preventDefault();
                }

                if (event.key === 'ArrowRight') {
                    var inputs = blanksDiv.children;
                    var currentIndex = 0;
                    for (var j = 0; j < inputs.length; j++) {
                        var input2 = inputs[j];
                        if (input2 === this) {
                            currentIndex = j;
                            break;
                        }
                    }

                    var nextIndex = currentIndex + 1;
                    while (nextIndex < inputs.length) {
                        if (inputs[nextIndex].tagName.toLowerCase() === 'input') {
                            inputs[nextIndex].focus();
                            break;
                        }
                        nextIndex++;
                    }

                } else if (event.key === 'ArrowLeft') {
                    var inputs = blanksDiv.children;
                    var currentIndex = 0;
                    for (var j = 0; j < inputs.length; j++) {
                        var input2 = inputs[j];
                        if (input2 === this) {
                            currentIndex = j;
                            break;
                        }
                    }
                    var previousIndex = currentIndex - 1;
                    while (previousIndex >= 0) {
                        if (inputs[previousIndex].tagName.toLowerCase() === 'input') {
                            inputs[previousIndex].focus();
                            break;
                        }
                        previousIndex--;
                    }

                }
            });

            input.addEventListener('input', function () {
                this.value = this.value.toUpperCase().replace(/[^A-Z]/g, '');
                var letter = this.value;
                var inputs = blanksDiv.children;
                var currentIndex = Array.from(this.parentNode.children).indexOf(this);

                var nextIndex = currentIndex + 1;
                if (solution[index][currentIndex] != letter) {
                    this.classList.add('incorrect');

                    while (nextIndex < inputs.length) {
                        if (inputs[nextIndex].tagName.toLowerCase() === 'input') {
                            inputs[nextIndex].focus();
                            break;
                        }
                        nextIndex++;
                    }
                }

                if (solution[index][currentIndex] === letter) {
                    var span = document.createElement('span');
                    span.classList.add("d-inline-block");                    
                    span.classList.add("p-2");
                    span.textContent = letter;
                    for (var j = 0; j < solution[index].length; j++) {
                        if (wordDiv.querySelector('span:nth-child(' + (j + 1) + ')').textContent === letter && !wordDiv.querySelector('span:nth-child(' + (j + 1) + ')').classList.contains('crossed')) {
                            wordDiv.querySelector('span:nth-child(' + (j + 1) + ')').classList.add('crossed');
                            break;
                        }

                    }
                    var inputs = blanksDiv.children;
                    var nextIndex = currentIndex + 1;
                    while (nextIndex < inputs.length) {
                        if (inputs[nextIndex].tagName.toLowerCase() === 'input') {
                            inputs[nextIndex].focus();
                            break;
                        }
                        nextIndex++;
                    }
                    spanList.push(span);
                    this.parentNode.replaceChild(span, this);
                    lettersFound++;

                    var inputs = blanksDiv.querySelectorAll('input');

                    if (totalLetters == lettersFound) {
                        var puzzleDiv = document.getElementById('puzzle');
                        var statusRowDiv = document.createElement('div');
                        var statusColDiv = document.createElement('div');
                        statusRowDiv.classList.add("row");
                        statusRowDiv.classList.add("justify-content-center");
                        statusColDiv.classList.add("col-5");
                        statusColDiv.classList.add("box-left");
                        statusColDiv.classList.add("text-center");
                        statusColDiv.classList.add("mb-4");
                        statusColDiv.classList.add("p-2");                        
                        statusColDiv.classList.add("viaoda-libre-regular")
                        statusColDiv.textContent = "Great Job!";
                        statusRowDiv.appendChild(statusColDiv);
                        puzzleDiv.appendChild(statusRowDiv);
                    }

                    if (inputs.length === 0) {
                        for (var s = 0; s < spanList.length; s++) {
                            spanList[s].classList.add('green');
                        }
                    }

                    if (nextIndex < inputs.length) {
                        blanksDiv.children[nextIndex].focus();
                    } else {
                        blanksDiv.children[currentIndex].focus();
                    }

                } else {
                    wordBlanks[index][currentIndex] = letter;

                }

            });

            blanksDiv.appendChild(input);
        });
        blankDivs.push(blanksDiv);
    });
    wordDivs.forEach(function (wordDiv) {
        wordsDiv.appendChild(wordDiv);
    });
    blankDivs.forEach(function (blankDiv) {
        wordsDiv.appendChild(blankDiv);
    });
}


displayWordsAndBlanks();
}
