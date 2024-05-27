document.getElementById('analyze-btn').addEventListener('click', function() {
    const text = document.getElementById('text-input').value;

    fetch('/analyze', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: text, user_id: 1 }), // user_id seria obtido através de login/autenticação
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerHTML = `
            <p>Sentimento: ${data.label}</p>
            <p>Confiança: ${data.score.toFixed(2)}</p>
        `;
    });

    fetch('/entries/1')
    .then(response => response.json())
    .then(data => {
        const entriesContainer = document.getElementById('entries');
        entriesContainer.innerHTML = '<h3>Histórico de Entradas</h3>';
        data.forEach(entry => {
            entriesContainer.innerHTML += `
                <div>
                    <p>${entry.date}</p>
                    <p>${entry.text}</p>
                    <p>Sentimento: ${entry.sentiment}</p>
                </div>
            `;
        });
    });
});
