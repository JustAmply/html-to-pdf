function convertToPdf() {
    fetch('/api/html-to-pdf', {
        method: 'POST',
        headers: { 'Content-Type': 'text/plain' },
        body: document.getElementById('html-input').value
    })
    .then(response => response.blob())
    .then(blob => {
        const a = document.createElement('a');
        a.style.display = 'none';
        a.href = window.URL.createObjectURL(blob);
        a.download = 'output.pdf';
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(a.href);
    })
    .catch(error => console.error('Error:', error));
}
