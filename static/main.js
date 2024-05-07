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
if (puzzleType == "Word") {

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

// --------------- DRAG/DROP ---------------- \\

if (puzzleType == "Match") {

    $(document).ready(function () {
        var correctPlacements = 0;
        var totalBlanks = $(".blank").length;
        $(".draggable").draggable({
            revert: "invalid",
            containment: ".right-box",
        });

        $(".blank").droppable({
            accept: ".draggable",
            drop: function (event, ui) {
                var $droppable = $(this);
                var $draggedWord = ui.draggable;
                var correctAnswer = $droppable.data("correct");

                if (correctAnswer === $draggedWord.text()) {
                    // Correct drop
                    $droppable.text($draggedWord.text());
                    $droppable.css("background-color", "green");
                    $draggedWord.hide();
                    correctPlacements++;

                    console.log(correctPlacements);

                    if (correctPlacements === totalBlanks) {
                        // All boxes are correct, show message
                        var puzzleDiv = document.getElementById('puz-container');
                        var statusRowDiv = document.createElement('div');
                        var statusColDiv = document.createElement('div');
                        statusRowDiv.classList.add("row");
                        statusRowDiv.classList.add("justify-content-center");
                        statusColDiv.classList.add("col-7");
                        statusColDiv.classList.add("box-left");
                        statusColDiv.classList.add("text-center");
                        statusColDiv.classList.add("mb-1");
                        statusColDiv.classList.add("mt-0");
                        statusColDiv.classList.add("p-2");
                        statusColDiv.classList.add("viaoda-libre-regular")
                        statusColDiv.textContent = "Great Job!";
                        statusRowDiv.appendChild(statusColDiv);
                        puzzleDiv.appendChild(statusRowDiv);

                    }
                } else {
                    // Incorrect drop
                    $droppable.text("Wrong!");
                    $droppable.css("background-color", "#FF7377");
                    $draggedWord.draggable("option", "revert", true);
                    setTimeout(function () {
                        $droppable.text("");
                        $droppable.css("background-color", "");
                    }, 2000);
                }
            }
        });


        $("#check-answer").on("click", function () {
            var userAnswer = $("#answer").val().trim().toLowerCase();
            var correctWords = ["information", "signal", "transmit", "transmission", "transmitting", "process", "processing", "communicate", "communication", "neurons"];

            var isCorrect = correctWords.some(function (correctWord) {
                return userAnswer.includes(correctWord.toLowerCase());
            });

            if (isCorrect) {
                $("#result").text("Correct!");
            } else {
                $("#result").text("Try again!");
            }
        });
    });
}




// Cup game  


if (puzzleType == "Cup") {
    const cups = document.querySelectorAll('.cup');
    let gameEnded = false;

    function random(min, max) {
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }

    function swapCups() {
        let interval = setInterval(function () {
            // Generate random indices
            if (swapCounter > 0) {
                let index1 = Math.floor(Math.random() * 3); // 0, 1, or 2
                let index2 = Math.floor(Math.random() * 3); // 0, 1, or 2

                // Ensure the indices are different
                while (index1 === index2) {
                    index2 = Math.floor(Math.random() * 3);
                }

                // Get the cup elements
                let cup1 = $(".cups-container .cup[data-index='" + index1 + "']");
                let cup2 = $(".cups-container .cup[data-index='" + index2 + "']");

                // Animate the swap
                let tempLeft = cup1.position().left;
                cup1.animate({ left: cup2.position().left }, 300);
                cup2.animate({ left: tempLeft }, 300);

                // Update indices for next swap
                cup1.attr("data-index", index2);
                cup2.attr("data-index", index1);

                console.log("cups: ", index1, " ", index2);

                if (currentHippoIndex === index1) {
                    currentHippoIndex = index2;
                } else if (currentHippoIndex === index2) {
                    currentHippoIndex = index1;
                }

                console.log("current hippo index: ", currentHippoIndex);

                // Decrement the swap counter
                swapCounter--;
            } else {
                // Check if the swaps should stop
                clearInterval(interval);
                setTimeout(function () {
                    $("#startButton").prop("disabled", false);
                    $(".message").text("Please select a cup.");
                    selectCup();
                }, 100);

            }
        }, speed);
    }


    // Initially, cups are parallel along the x-axis
    cups[0].style.left = '0%'; 
    cups[0].style.top = '0px'; 

    cups[1].style.left = '38%'; 
    cups[1].style.top = '0px'; 

    cups[2].style.left = '78%'; 
    cups[2].style.top = '0px'; 

    let originalHippoIndex = 0;
    let currentHippoIndex = originalHippoIndex;
    let swapCounter = 6;
    let numSwaps = 6;
    let hippoFound = false;
    let speed = 1000;
    let speedSetting = 1000;


    function updateSpeedDisplay() {
        $("#speed").text((1000 - speedSetting)/100 + 1);
    }

    function updateSwapsDisplay() {
        $("#swaps").text(numSwaps);
    }

    $("#speedDown").click(function () {
        speed += 100;
        speedSetting += 100;
        if (speedSetting > 1000) {
            speed = 1000;
            speedSetting =1000;
        }
        updateSpeedDisplay();
    });

    $("#speedUp").click(function () {
        speed -= 100;
        speedSetting -= 100;        
        if (speedSetting <= 200) {
            speed = 300;
            speedSetting = 300;
        }
        updateSpeedDisplay();
    });

    $("#swapsDown").click(function () {
        swapCounter--;
        numSwaps--;
        if (numSwaps < 1) {
            swapCounter = 1;
            numSwaps = 1;
        }
        updateSwapsDisplay();
    });

    $("#swapsUp").click(function () {
        swapCounter++;
        numSwaps++;
        if (numSwaps > 15) {
            swapCounter = 15;
            numSwaps = 15;
        }
        updateSwapsDisplay();
    });


    function placeHippo() {
        // Generate a random index for the cup
        originalHippoIndex = Math.floor(Math.random() * 3); // 0, 1, or 2
        currentHippoIndex = originalHippoIndex;
        hipResult.addClass("no-border");
        // Get the cup element at the random index
        let cupWithHippo = $(".cups-container .cup[data-index='" + originalHippoIndex + "']");

        // Get the hippo element
        let hippo = $("<img src='/static/hippo.png' class='hippo' alt='Hippo'>");

        // Append the hippo to the cup
        cupWithHippo.append(hippo);

        // Position the hippo a little lower
        hippo.css("margin-top", "30px");
        hippo.css("margin-left", "0%");

        cupWithHippo.css("opacity", "0.7");

        // Wait for a few seconds before making the cup opaque again

        setTimeout(function () {
            cupWithHippo.css("opacity", "1")
            hippo.css("opacity", "0");
            swapCups();
        }, 2000); // 500 milliseconds = 0.5 seconds
    }

    function resetGame() {
        // Reset the game state
        $(".hippo").remove(); // Remove the hippo from the cup
        $(".cup").css("opacity", "1"); // Make all cups opaque again
        swapCounter = numSwaps; // Reset the swap counter
        speed = speedSetting;
        hippoFound = false; // Reset the hippoFound flag
        $(".message").text(""); // Clear any message
        $(".hipResult").text("");
        hipResult.addClass("no-border");
        hipResult.css("background-color", "");        
        cups[0].style.left = '0%'; 
        cups[0].style.top = '0px'; 
    
        cups[1].style.left = '38%'; 
        cups[1].style.top = '0px'; 
    
        cups[2].style.left = '78%'; 
        cups[2].style.top = '0px'; 
    }

    var hipResult = $(".hipResult");
    if (hipResult.text().trim() === "") {
      hipResult.addClass("no-border");
    }

    // Call placeHippo to place the hippo in a random cup
    $("#startButton").click(function () {
        resetGame();
        $(".message").text("");
        gameEnded = false;
        $("#startButton").prop("disabled", true);        
        placeHippo();
    });    
    function selectCup() {
    $(".cup").click(function () {
        if (!hippoFound && !gameEnded) {
            // Check if the hippo is under the clicked cup
            let clickedIndex = $(this).data("index");
            $(".hipResult").css("background-color:", "");                       
            if (clickedIndex === currentHippoIndex) {
                // Make the cup transparent to reveal the hippo
                $(".hipResult").removeClass("no-border");   
                $(this).find(".hippo").css("opacity", "0.8");
                $(this).css("opacity", "0.8");         
                hipResult.css("background-color", "green");
                hipResult.css("color", "white");   
                $(".hipResult").text("You found the hippo!");        
                gameEnded = true;
            } else {
                $(".cup[data-index='" + currentHippoIndex + "']").css("opacity", "0.8");
                $(".cup[data-index='" + currentHippoIndex + "']").find(".hippo").css("opacity", "0.8");
                $(this).css("opacity", "0.8");         
                $(".hipResult").removeClass("no-border");                   
                $(".hipResult").text("Try again!");    
                hipResult.css("background-color", "lightcoral");
                hipResult.css("color", "white");   
                gameEnded = true;                
            }
            hippoFound = true;

            setTimeout(resetGame, 3000);
        }
    });
}
}