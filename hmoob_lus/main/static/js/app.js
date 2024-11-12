/* animate toggle nav */
const toggleButton = document.getElementById('toggle-btn')
const sidenav = document.getElementById('toggle-nav')

function toggleSideNav(){
    sidenav.classList.toggle('close')
    toggleButton.classList.toggle('rotate')

    Array.from(sidenav.getElementsByClassName('show')).forEach(ul => {
        ul.classList.remove('show')
        ul.previousElementSibling.classList.remove('rotate')
    })

}

function toggleSubMenu(button){
    button.nextElementSibling.classList.toggle('show')
    button.classList.toggle('rotate')

    if(sidenav.classList.contains('close')){
        sidenav.classList.toggle('close')
        toggleButton.classList.toggle('rotate')
    }
}

/* Handling Course Unit Vocab Cards */

// Function to play audio by source URL
function playAudio(audioUrl) {
    const audio = new Audio(audioUrl);
    audio.play().catch((error) => {
        console.error("Audio playback error:", error);
    });
}

/* Handling audio record and playback and random word selection for Pronunciation Practice */

// DOM elements
const hmongWordDisplay = document.getElementById("hmong-word");
const playMaleButton = document.getElementById("play-male-audio");
const playFemaleButton = document.getElementById("play-female-audio");
const newWordButton = document.getElementById("new-word");
const startRecordingButton = document.getElementById("start-recording");
const playRecordingButton = document.getElementById("play-recording");

let mediaRecorder;
let recordedChunks = [];
let wordList = [];
let currentMaleAudio = new Audio();
let currentFemaleAudio = new Audio();

// Load words from the hidden list
document.querySelectorAll("#word-list li").forEach(li => {
    wordList.push({
        english: li.getAttribute("data-english"),
        hmong: li.getAttribute("data-hmong"),
        maleAudioUrl: li.getAttribute("data-male-audio"),
        femaleAudioUrl: li.getAttribute("data-female-audio"),
    });
});

// Function to select a new word
newWordButton.addEventListener("click", () => {
    if (wordList.length > 0) {
        const randomWord = wordList[Math.floor(Math.random() * wordList.length)];
        hmongWordDisplay.textContent = `${randomWord.english} - ${randomWord.hmong}`;

        // Set audio sources
        currentMaleAudio.src = randomWord.maleAudioUrl;
        currentFemaleAudio.src = randomWord.femaleAudioUrl;

        // Enable audio play buttons
        playMaleButton.disabled = false;
        playFemaleButton.disabled = false;
    }
});

// Play male audio
playMaleButton.addEventListener("click", () => {
    currentMaleAudio.play();
});

// Play female audio
playFemaleButton.addEventListener("click", () => {
    currentFemaleAudio.play();
});

// Start recording functionality
startRecordingButton.addEventListener("click", () => {
    if (startRecordingButton.innerText === "🔴 Record") {
        navigator.mediaDevices.getUserMedia({ audio: true })
            .then(stream => {
                mediaRecorder = new MediaRecorder(stream);
                recordedChunks = [];

                mediaRecorder.ondataavailable = event => {
                    if (event.data.size > 0) recordedChunks.push(event.data);
                };

                mediaRecorder.onstop = () => {
                    const audioBlob = new Blob(recordedChunks, { type: "audio/wav" });
                    const audioUrl = URL.createObjectURL(audioBlob);
                    playRecordingButton.src = audioUrl;
                    playRecordingButton.disabled = false;
                };

                mediaRecorder.start();
                startRecordingButton.innerText = "⏹️ Stop Recording";
            })
            .catch(error => console.error("Error accessing microphone:", error));
    } else {
        mediaRecorder.stop();
        startRecordingButton.innerText = "🔴 Record";
    }
});

// Play user recording
playRecordingButton.addEventListener("click", () => {
    const userRecording = new Audio(playRecordingButton.src);
    userRecording.play();
});
