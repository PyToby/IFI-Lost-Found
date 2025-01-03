const hamburgerIcon = document.getElementById('hamburger-icon');
const mobileMenu = document.getElementById('mobile-menu');
const hamburger = document.getElementById('hamburger');
const closeIcon = document.getElementById('close-icon');

hamburgerIcon.addEventListener('click', () => {
    // Toggle the visibility of the mobile menu
    mobileMenu.classList.toggle('hidden');
    
    // Toggle between the hamburger icon and the close icon
    hamburger.classList.toggle('hidden');
    closeIcon.classList.toggle('hidden');
});


const navbar = document.getElementById('navbar');
const divider = document.getElementById('divider');

window.addEventListener('scroll', () => {
    if (window.scrollY > 0) {
        navbar.classList.remove('bg-transparent');
        navbar.classList.add('bg-white', 'shadow-sm');
        divider.classList.remove('border-transparent');
        divider.classList.add('border-gray-200');
    } else {
        navbar.classList.remove('bg-white', 'shadow-sm');
        navbar.classList.add('bg-transparent');
        divider.classList.remove('border-gray-200');
        divider.classList.add('border-transparent');
    }
});
