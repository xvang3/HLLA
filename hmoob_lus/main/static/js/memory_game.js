let flippedCards = [];
let matchedPairs = 0;

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

        // Add a bounce animation and color change
        card1.style.animation = "bounce 0.5s";
        card2.style.animation = "bounce 0.5s";

        // Ensure background color changes are applied last
        setTimeout(() => {
            card1.style.backgroundColor = "#61C865"; // Green for match
            card2.style.backgroundColor = "#61C865";
        }, 500); // Delay to avoid overlap with animation

        document.getElementById('correct-matches').textContent = matchedPairs;

        console.log("Match found! Total matches:", matchedPairs);

        // Check for win condition based on total pairs
        if (matchedPairs === totalPairs) {
            setTimeout(() => displayPlayAgainButton(), 300);
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
function displayPlayAgainButton() {
    const gameContainer = document.querySelector('.container.text-center.my-5');
    const button = document.createElement('button');
    button.textContent = "Play Again";
    button.className = "btn btn-primary mt-4";
    button.onclick = () => location.reload();
    gameContainer.appendChild(button);

    alert("Congratulations! You've matched all pairs!");
