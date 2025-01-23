document.getElementById('identifyButton').addEventListener('click', async () => {
    const textInput = document.getElementById('textInput').value;
    const resultDiv = document.getElementById('result');

    if (!textInput.trim()) {
        resultDiv.textContent = "Please enter some text.";
        return;
    }

    const response = await fetch('/identify', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: textInput })
    });

    const data = await response.json();
    resultDiv.textContent = `The generation is: ${data.generation}`;
});