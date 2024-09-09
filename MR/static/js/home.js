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

function decreaseValue() {
    const slider = document.getElementById('slider');
    slider.value = Math.max(slider.min, slider.value - 10);
}

function increaseValue() {
    const slider = document.getElementById('slider');
    slider.value = Math.min(slider.max, slider.value + 10);
}
