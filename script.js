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
            
            if (navMenu?.classList.contains('active')) {
                navMenu.classList.remove('active');
                mobileMenuBtn.innerHTML = '<i class="fas fa-bars"></i>';
            }
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                const headerHeight = document.querySelector('nav')?.offsetHeight || 70;
                const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - headerHeight;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
                
                if (history.pushState) {
                    history.pushState(null, null, targetId);
                } else {
                    window.location.hash = targetId;
                }
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
            '.development-text, .development-image-container'
        );
        
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };
        
        const observerCallback = (entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate');
                    observer.unobserve(entry.target);
                }
            });
        };
        
        const observer = new IntersectionObserver(observerCallback, observerOptions);
        
        elementsToAnimate.forEach(element => {
            observer.observe(element);
        });
    };
    
    animateOnScroll();
    
    const initParallax = function() {
        const parallaxElements = document.querySelectorAll('.hover-zoom');
        
        if (!('requestAnimationFrame' in window)) return;
        
        let lastScrollPosition = window.scrollY;
        let ticking = false;
        
        const updateParallax = () => {
            const scrollValue = window.scrollY;
            
            parallaxElements.forEach((element, index) => {
                const speed = 0.05 + (index * 0.02);
                const translateY = scrollValue * speed;
                
                const rect = element.getBoundingClientRect();
                if (rect.top < window.innerHeight && rect.bottom > 0) {
                    element.style.transform = `translateY(${translateY}px)`;
                }
            });
            
            ticking = false;
        };
        
        const onScroll = () => {
            lastScrollPosition = window.scrollY;
            
            if (!ticking) {
                window.requestAnimationFrame(updateParallax);
                ticking = true;
            }
        };
        
        window.addEventListener('scroll', onScroll, { passive: true });
        
        updateParallax();
        
        return () => {
            window.removeEventListener('scroll', onScroll);
            parallaxElements.forEach(el => el.style.transform = '');
        };
    };
    
    let cleanupParallax = null;
    if (window.innerWidth > 768) {
        cleanupParallax = initParallax();
    }
    
    const handleResize = () => {
        if (window.innerWidth <= 768 && cleanupParallax) {
            cleanupParallax();
            cleanupParallax = null;
        } else if (window.innerWidth > 768 && !cleanupParallax) {
            cleanupParallax = initParallax();
        }
    };
    
    window.addEventListener('resize', handleResize);
    
    window.addEventListener('beforeunload', () => {
        if (cleanupParallax) cleanupParallax();
        window.removeEventListener('resize', handleResize);
    });
});