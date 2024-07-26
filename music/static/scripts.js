document.addEventListener('DOMContentLoaded', function () {
    const scrollElements = document.querySelectorAll('.card-animate');

    const elementInView = (el, dividend = 1) => {
        const elementTop = el.getBoundingClientRect().top;

        return (
            elementTop <= (window.innerHeight || document.documentElement.clientHeight) / dividend
        );
    };

    const displayScrollElement = (element) => {
        element.classList.add('active');
    };

    const hideScrollElement = (element) => {
        element.classList.remove('active');
    };

    const handleScrollAnimation = () => {
        scrollElements.forEach((el) => {
            if (elementInView(el, 1.25)) {
                displayScrollElement(el);
            } else {
                hideScrollElement(el);
            }
        });
    };

    window.addEventListener('scroll', () => {
        handleScrollAnimation();
    });

    handleScrollAnimation();

    // Smooth scroll
    const navButtons = document.querySelectorAll('.nav-buttons button, .mobile-menu .btn');
    navButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            const targetId = e.currentTarget.getAttribute('data-scroll');
            const targetSection = document.getElementById(targetId);
            window.scrollTo({
                top: targetSection.offsetTop - 70,
                behavior: 'smooth'
            });
        });
    });

    // Burger menu
    const burgerButton = document.querySelector('.navbar-toggler');
    const mobileMenu = document.querySelector('.mobile-menu');
    burgerButton.addEventListener('click', () => {
        mobileMenu.classList.toggle('show');
    });
});
