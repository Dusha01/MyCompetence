<script lang="ts">
    import MyPHOTO from '../../assets/Main.jpg';
    import { fade, fly } from 'svelte/transition';
    import { onMount } from 'svelte';

    let currentTextIndex = 0;
    let displayText = '';
    let isDeleting = false;
    let typingSpeed = 150;
    
    const texts = [
        "Студент 2-го курса ДВГУПС",
        "Web-разработчик",
        "Разработчик Telegram-ботов",
        "Fullstack разработчик"
    ];
    
    onMount(() => {
        typeWriter();
    });
    
    function typeWriter() {
        const fullText = texts[currentTextIndex];
        
        if (isDeleting) {
            displayText = fullText.substring(0, displayText.length - 1);
        } else {
            displayText = fullText.substring(0, displayText.length + 1);
        }
        
        let delta = typingSpeed;
        
        if (isDeleting) {
            delta /= 2;
        }
        
        if (!isDeleting && displayText === fullText) {
            delta = 2000;
            isDeleting = true;
        } else if (isDeleting && displayText === '') {
            isDeleting = false;
            currentTextIndex = (currentTextIndex + 1) % texts.length;
            delta = 500;
        }
        
        setTimeout(typeWriter, delta);
    }
</script>

<header class="bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900 text-white py-16 shadow-2xl border-b border-gray-700">
    <div class="container mx-auto px-4">
        <div class="flex flex-col items-center text-center space-y-8">
            <img
                src={MyPHOTO} 
                alt="MainPhoto"
                class="w-44 h-44 rounded-full object-cover border-4 border-indigo-500/30 shadow-xl transition-all duration-500 hover:scale-105 hover:border-indigo-500/50 hover:shadow-indigo-500/20"
                in:fly={{ y: -50, duration: 800, delay: 100 }}
                out:fade/>

            <h1 class="text-4xl md:text-5xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-purple-500 tracking-tight"
                in:fade={{ delay: 300, duration: 800 }}
                out:fade>
                Andrew Gubchenko
            </h1>

            <div class="text-xl md:text-2xl font-light max-w-2xl leading-relaxed space-y-4"
                in:fly={{ x: 50, duration: 800, delay: 500 }}
                out:fade>
                
                <div class="relative inline-block min-h-[2.5rem]">
                    <span class="relative z-10 text-gray-300">{displayText}</span>
                    <span class="absolute bottom-0 left-0 w-full h-1 bg-gradient-to-r from-blue-500 to-purple-600 opacity-60 rounded-full animate-pulse"></span>
                    <span class="inline-block w-1 h-6 bg-blue-400 align-middle ml-1 opacity-80 animate-blink"></span>
                </div>
                
                <div class="w-full h-px bg-gradient-to-r from-transparent via-gray-600 to-transparent my-4"></div>
                
                <div class="relative inline-block">
                    <span class="relative z-10 text-gray-300">Fullstack разработчик</span>
                    <span class="absolute bottom-0 left-0 w-full h-1 bg-gradient-to-r from-blue-500 to-purple-600 opacity-60 rounded-full animate-pulse"></span>
                </div>
            </div>
        </div>
    </div>
</header>