const hamburgerIcon = document.getElementById('hamburger-icon');
const mobileMenu = document.getElementById('mobile-menu');

hamburgerIcon.addEventListener('click', () => {
    mobileMenu.classList.toggle('hidden');
});