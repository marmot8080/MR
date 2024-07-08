document.addEventListener('DOMContentLoaded', function() {
    const starRatings = document.querySelectorAll('.star-rating');

    starRatings.forEach(starRating => {
        const rating = parseFloat(starRating.getAttribute('data-rating'));
        const percentage = (rating / 10) * 100;
        starRating.style.setProperty('--rating-width', `${percentage}%`);
    });
});

function login() {
    alert('Login functionality coming soon!');
}

function register() {
    alert('Register functionality coming soon!');
}
