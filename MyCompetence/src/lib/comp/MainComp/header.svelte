<script lang="ts">
    import MyPHOTO from '../../assets/Myphotos/Main.jpg';
    import { fade, fly } from 'svelte/transition';
    import { onMount } from 'svelte';

    let loaded = false;
    
    onMount(() => {
        loaded = true;
    });
</script>

<header class="bg-gradient-to-br from-indigo-900 to-purple-800 text-white py-12 shadow-xl">
    <div class="container mx-auto px-4">
        <div class="flex flex-col items-center text-center space-y-6">
            <img 
                src={MyPHOTO} 
                alt="MainPhoto"
                class="w-40 h-40 rounded-full object-cover border-4 border-white shadow-lg transition-all duration-500 hover:scale-105 hover:shadow-xl"
                in:fly={{ y: -50, duration: 800, delay: 100 }}
                out:fade
            />

            <h1 class="text-4xl md:text-5xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-yellow-300 to-amber-500"
                in:fade={{ delay: 300, duration: 800 }}
                out:fade>Andrew Gubchenko
            </h1>

            <h2 class="text-xl md:text-2xl font-light max-w-2xl leading-relaxed"
                in:fly={{ x: 50, duration: 800, delay: 500 }}
                out:fade>
                
                <span class="relative inline-block">
                    <span class="relative z-10">Студент 2-го курса ДВГУПС</span>
                    <span class="absolute bottom-0 left-0 w-full h-2 bg-amber-400 opacity-30 rounded-full animate-pulse"></span>
                </span>
                
                <span class="mx-3">|</span>
                
                <span class="relative inline-block">
                    <span class="relative z-10">Fullstack разработчик</span>
                    <span class="absolute bottom-0 left-0 w-full h-2 bg-blue-400 opacity-30 rounded-full animate-pulse"></span>
                </span>
            </h2>

            {#if loaded}
                <div 
                    class="mt-8 w-10 h-10 rounded-full border-2 border-white border-t-transparent animate-spin"
                    transition:fly={{ y: 20, duration: 1000, delay: 1000 }}
                ></div>
            {/if}
        </div>
    </div>
</header>


<style>
    .animate-pulse {
        animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 0.3; }
        50% { opacity: 0.1; }
    }
</style>