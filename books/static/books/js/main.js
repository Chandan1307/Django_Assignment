document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/books/recommendations/')
        .then(response => response.json())
        .then(data => {
            const recommendationsDiv = document.getElementById('recommendations');
            data.forEach(book => {
                const bookDiv = document.createElement('div');
                bookDiv.innerHTML = `<h2>${book.title}</h2><p>${book.author}</p>`;
                recommendationsDiv.appendChild(bookDiv);
            });
        });
});
