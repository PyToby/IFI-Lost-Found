const hamburgerIcon = document.getElementById('hamburger-icon');
const hamburger = document.getElementById('hamburger');
const closeIcon = document.getElementById('close-icon');
const mobileMenu = document.getElementById('mobile-menu');
const content = document.getElementById('content');

hamburgerIcon.addEventListener('click', () => {
const isMenuHidden = mobileMenu.classList.contains('hidden');

// Toggle menu visibility
mobileMenu.classList.toggle('hidden', !isMenuHidden);
mobileMenu.classList.toggle('block', isMenuHidden);

// Toggle icon
hamburger.classList.toggle('hidden', isMenuHidden);
closeIcon.classList.toggle('hidden', !isMenuHidden);

// Push content below menu
content.style.marginTop = isMenuHidden ? `${mobileMenu.offsetHeight}px` : '0';
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

// Toggle dropdown menu on click (PC version)
const profileButton = document.getElementById('profile-btn');
const dropdownMenu = document.getElementById('dropdown-menu');

profileButton.addEventListener('click', () => {
    dropdownMenu.classList.toggle('hidden'); // Toggle visibility
});

// Mobile dropdown toggle
const mobileToggleButton = document.getElementById('mobile-profile-toggle');
const mobileDropdown = document.getElementById('mobile-dropdown');
const mobileArrow = document.getElementById('mobile-arrow');

mobileToggleButton.addEventListener('click', () => {
    const isHidden = mobileDropdown.classList.contains('hidden');
    mobileDropdown.classList.toggle('hidden', !isHidden);
    mobileArrow.classList.toggle('rotate-180', isHidden);
});
