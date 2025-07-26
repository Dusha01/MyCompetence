document.addEventListener('DOMContentLoaded', function() {
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const navMenu = document.getElementById('navMenu');
    
    if (mobileMenuBtn && navMenu) {
        mobileMenuBtn.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            this.innerHTML = navMenu.classList.contains('active') ? 
                '<i class="fas fa-times"></i>' : '<i class="fas fa-bars"></i>';
        });
    }
    
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            e.preventDefault();
            
            if (navMenu && navMenu.classList.contains('active')) {
                navMenu.classList.remove('active');
                if (mobileMenuBtn) {
                    mobileMenuBtn.innerHTML = '<i class="fas fa-bars"></i>';
                }
            }
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                const headerHeight = document.querySelector('nav')?.offsetHeight || 70;
                const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - headerHeight;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
                
                history.pushState(null, null, targetId);
            }
        });
    });
    
    const animateOnScroll = function() {
        const elementsToAnimate = document.querySelectorAll(
            '.about-text, .about-image, ' +
            '.specialization-card, ' +
            '.university-text, .university-image, ' +
            '.competency-tile, ' +
            '.tech-layer, .tech-arrow, ' +
            '.development-text, .development-image-container img'
        );
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate');
                    // Отключаем наблюдение после анимации
                    observer.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        });
        
        elementsToAnimate.forEach(element => {
            observer.observe(element);
        });
    };
    
    animateOnScroll();
    
    const initParallax = function() {
        const parallaxElements = document.querySelectorAll('.hover-zoom');
        
        if ('requestAnimationFrame' in window) {
            const updateParallax = () => {
                const scrollValue = window.scrollY;
                
                parallaxElements.forEach((element, index) => {
                    const speed = 0.05 + (index * 0.02);
                    element.style.transform = `translateY(${scrollValue * speed}px) scale(1.05)`;
                });
                
                requestAnimationFrame(updateParallax);
            };
            
            updateParallax();
        }
    };
    
    if (window.innerWidth > 768) {
        initParallax();
    }
    
    window.addEventListener('resize', function() {
        const parallaxElements = document.querySelectorAll('.hover-zoom');
        if (window.innerWidth <= 768) {
            parallaxElements.forEach(element => {
                element.style.transform = '';
            });
        }
    });
});