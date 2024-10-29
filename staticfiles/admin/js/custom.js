document.addEventListener('DOMContentLoaded', function() {
    const themeToggleButton = document.querySelector('.theme-toggle');
    const body = document.body;

    themeToggleButton.addEventListener('click', function() {
        if (body.classList.contains('dark-mode')) {
            body.classList.remove('dark-mode');
            body.classList.add('light-mode');
        } else {
            body.classList.remove('light-mode');
            body.classList.add('dark-mode');
        }
    });
});