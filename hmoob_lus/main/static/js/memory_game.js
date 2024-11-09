let flippedCards = [];
let matchedPairs = 0;

function flipCard(card) {
    // Prevent flipping more than two cards or flipping an already matched card
    if (flippedCards.length < 2 && !card.classList.contains('flipped') && !card.classList.contains('matched')) {
        card.classList.add('flipped');
        flippedCards.push(card);

        // If two cards are flipped, check for a match
        if (flippedCards.length === 2) {
            setTimeout(checkForMatch, 500);
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
        document.getElementById('correct-matches').textContent = matchedPairs;

        console.log("Match found! Total matches:", matchedPairs);

        // Check for win condition based on total pairs
        if (matchedPairs === totalPairs) {
            setTimeout(() => alert('Congratulations! You matched all pairs!'), 300);
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
