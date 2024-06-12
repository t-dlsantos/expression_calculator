document.addEventListener('DOMContentLoaded', function () {
    const buttons = document.querySelectorAll('button');
    const visor = document.querySelector('.current-operation');
    const lastOperation = document.querySelector('.last-operation');

    buttons.forEach(button => {
        button.addEventListener('click', () => {
            if (button.classList.contains('all-clear')) {
                visor.textContent = '';
                lastOperation.textContent = '';
            } else if (button.classList.contains('equals')) {
                const expression = visor.textContent;
                fetch('/calculate', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ expression: expression })
                })
                .then(response => response.json())
                .then(data => {
                    lastOperation.textContent = expression;
                    
                    visor.textContent = data.result;
                })
                .catch(error => console.error('Error:', error));
            } else {
                if (button.dataset.number) {
                    visor.textContent += button.dataset.number;
                } else if (button.dataset.operator) {
                    visor.textContent += button.dataset.operator;
                } else if (button.textContent === '.') {
                    visor.textContent += '.';
                }
            }
        });
    });
});


