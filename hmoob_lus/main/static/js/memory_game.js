let flippedCards = [];
let matchedPairs = 0;
let matchColors = ["#FF6B6B", "#E6E6FA", "#87CEEB" , "#98FF98", "#DAA520", "#F08080", "#61C865", "#FFE066", "#6CCFF6", "#FFA573", "#FF9DE5", "#C69DF1", "#7CDEDC", "#FFD7B5", "#87CEEB"];

function flipCard(card) {
    // Prevent flipping more than two cards or flipping an already matched card
    if (flippedCards.length < 2 && !card.classList.contains('flipped') && !card.classList.contains('matched')) {
        card.classList.add('flipped');
        flippedCards.push(card);

        // play audio if the cards are Hmong words, using the audio "url"
        const cardType = card.getAttribute('data-type');
        const audioUrl = card.getAttribute('data-audio-url');

        if (cardType === 'hmong' && audioUrl) {
            const audio = new Audio(audioUrl);
            audio.play();
        }

        // If two cards are flipped, check for a match
        if (flippedCards.length === 2) {
            setTimeout(checkForMatch, 2000); //added delay
        }
    }
}

function checkForMatch() {
    const [card1, card2] = flippedCards;
    const id1 = card1.getAttribute('data-id').split('-')[0]; // Get the base ID before '-hmong' or '-english'
    const id2 = card2.getAttribute('data-id').split('-')[0];

    console.log("Checking match between card IDs:", id1, "and", id2);

    if (id1 === id2) {
        // IDs match, so we have a correct Hmong-English pair
        matchedPairs += 1;
        card1.classList.add('matched');
        card2.classList.add('matched');

        const color = matchColors.length > 0 ? matchColors.shift() : "#D3D3D3"; // Default color
        card1.style.setProperty('--match-color', color);
        card2.style.setProperty('--match-color', color);

        // Add a bounce animation and color change
        card1.style.animation = "bounce 0.5s";
        card2.style.animation = "bounce 0.5s";

        // Ensure background color changes are applied last
        setTimeout(() => {
            card1.classList.add('matched');
            card2.classList.add('matched');
        }, 500); // Apply after animations
        

        document.getElementById('correct-matches').textContent = matchedPairs;

        console.log("Match found! Total matches:", matchedPairs);

        // Check for win condition based on total pairs
        if (matchedPairs === totalPairs) {
            setTimeout(() => displayPlayAgainPopup(), 300);
        }
    } else {
        // No match, flip back after a short delay
        card1.classList.remove('flipped');
        card2.classList.remove('flipped');

        console.log("No match, cards flipped back.");
    }

    // Reset flipped cards array for the next turn
    flippedCards = [];
}

// added a play again button just to formally reset instead of just refreshing the page manually
function displayPlayAgainPopup() {
    // Create popup container
    const popup = document.createElement('div');
    popup.className = 'popup-container';

    // Add avatar image
    const img = document.createElement('img');
    img.src = "/static/images/rep_talking.PNG";
    img.alt = "Congratulations Avatar";

    // Add message
    const message = document.createElement('div');
    message.className = 'message';
    message.textContent = "Great Job! Play Again?";

    // Add play again button
    const button = document.createElement('button');
    button.className = 'play-again-btn';
    button.textContent = "Play Again";
    button.onclick = () => location.reload(); // Reload page to start again

    // Append elements to popup
    popup.appendChild(img);
    popup.appendChild(message);
    popup.appendChild(button);

    // Append popup to the game-board for relative positioning
    const gameBoard = document.getElementById('game-board');
    gameBoard.appendChild(popup);

    // Adjust popup position dynamically
    const boardRect = gameBoard.getBoundingClientRect();
    popup.style.left = `${boardRect.width / 2 - popup.offsetWidth / 2}px`;
    popup.style.top = `${boardRect.top + boardRect.height / 3 - 500}px`;


}

// Update the win condition to call the new popup
if (matchedPairs === totalPairs) {
    setTimeout(() => displayPlayAgainPopup(), 300);
}
