let flippedCards = [];
let matchedPairs = 0;
let audioPlaying = false;  // Flag to indicate if audio is currently playing

function flipCard(card) {
    // Prevent flipping more than two cards, flipping an already matched card, or flipping during audio playback
    if (flippedCards.length < 2 && !card.classList.contains('flipped') && !card.classList.contains('matched') && !audioPlaying) {
        card.classList.add('flipped');
        flippedCards.push(card);

        // Play audio if it's a Hmong word and has an audio URL
        const audioUrl = card.getAttribute('data-audio-url');
        if (audioUrl && card.getAttribute('data-id').includes('hmong')) {
            playAudio(audioUrl);
        }

        // If two cards are flipped, check for a match after audio finishes
        if (flippedCards.length === 2) {
            setTimeout(() => {
                // Wait until audio is done before checking for a match
                if (!audioPlaying) checkForMatch();
            }, 500);
        }
    }
}

function checkForMatch() {
    const [card1, card2] = flippedCards;
    const id1 = card1.getAttribute('data-id').split('-')[0];
    const id2 = card2.getAttribute('data-id').split('-')[0];

    if (id1 === id2) {
        matchedPairs += 1;
        card1.classList.add('matched');
        card2.classList.add('matched');
        document.getElementById('correct-matches').textContent = matchedPairs;

        if (matchedPairs === totalPairs) {
            setTimeout(() => alert('Congratulations! You matched all pairs!'), 300);
        }
    } else {
        // No match, flip back after audio completes
        setTimeout(() => {
            card1.classList.remove('flipped');
            card2.classList.remove('flipped');
        }, 500);
    }

    flippedCards = [];
}

// Function to play audio and set the audioPlaying flag
function playAudio(audioUrl) {
    audioPlaying = true;
    const audio = new Audio(audioUrl);
    audio.play();

    // When the audio finishes, reset the audioPlaying flag
    audio.onended = () => {
        audioPlaying = false;
        // Check if two cards are flipped and the audio just ended, then check for a match
        if (flippedCards.length === 2) {
            checkForMatch();
        }
    };
}

function newGame() {
    flippedCards.forEach(card => card.classList.remove('flipped'));
    document.querySelectorAll('.card').forEach(card => card.classList.remove('matched'));
    flippedCards = [];
    matchedPairs = 0;
    document.getElementById('correct-matches').textContent = matchedPairs;
    window.location.href = window.location.pathname + "?newGame=true";
}

function shuffle() {
    window.location.href = window.location.pathname + "?shuffle=true";
}

// Function to reveal all cards
function revealCards() {
    document.querySelectorAll('.card').forEach(card => card.classList.add('flipped'));
}
