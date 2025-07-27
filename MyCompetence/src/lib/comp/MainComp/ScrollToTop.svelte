<script lang="ts">
    import { onMount } from 'svelte';
    
    let visible = false;
    const scrollThreshold = 300; 
    
    onMount(() => {
        window.addEventListener('scroll', handleScroll);
        return () => window.removeEventListener('scroll', handleScroll);
    });
    
    function handleScroll() {
        visible = window.scrollY > scrollThreshold;
    }
    
    function scrollToTop() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    }
</script>

<button
    class={`fixed bottom-8 cursor-pointer right-8 z-50 bg-gradient-to-br from-blue-500 to-purple-600 text-white p-4 rounded-full shadow-xl transition-all duration-300 transform ${visible ? 'opacity-100 hover:scale-110' : 'opacity-0 pointer-events-none'} hover:shadow-blue-500/30 border border-blue-400/20`}
    on:click={scrollToTop}
    aria-label="Вернуться наверх">
    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18" />
    </svg>
</button>

<style>
    .animate-pulse {
        animation: pulse 2.5s cubic-bezier(0.4, 0, 0.6, 1) infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 0.6; }
        50% { opacity: 0.3; }
    }
    
    .animate-blink {
        animation: blink 0.8s infinite;
    }
    
    @keyframes blink {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.3; }
    }
</style>