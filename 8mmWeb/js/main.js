// Mobil menü işlevselliği
const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');

    burger.addEventListener('click', () => {
        // Menüyü aç/kapa
        nav.classList.toggle('nav-active');

        // Link animasyonları
        navLinks.forEach((link, index) => {
            if (link.style.animation) {
                link.style.animation = '';
            } else {
                link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.3}s`;
            }
        });

        // Burger animasyonu
        burger.classList.toggle('toggle');
    });
}

// Sayfa kaydırma animasyonu
const smoothScroll = () => {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
}

// Neon glow ve blur efekti
const createNeonGlowEffect = () => {
    const glow = document.createElement('div');
    glow.className = 'neon-glow';
    document.body.appendChild(glow);

    document.addEventListener('mousemove', (e) => {
        glow.style.left = `${e.pageX}px`;
        glow.style.top = `${e.pageY}px`;
    });
};

// Sayfa yüklendiğinde çalıştır
document.addEventListener('DOMContentLoaded', () => {
    navSlide();
    smoothScroll();
    createNeonGlowEffect();
});

// Scroll olayını dinle
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 100) {
        navbar.style.background = 'var(--primary-color)';
    } else {
        navbar.style.background = 'linear-gradient(to right, var(--primary-color), var(--secondary-color))';
    }
}); 