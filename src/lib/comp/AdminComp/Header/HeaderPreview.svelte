<script lang="ts">
  import type { HeaderConfig } from './HeaderConfig';
  import { fade, fly } from 'svelte/transition';
  import { onMount } from 'svelte';

  export let config: HeaderConfig;

  let currentTextIndex = 0;
  let displayText = '';
  let isDeleting = false;
  let typingSpeed = 150;
  
  onMount(() => {
    typeWriter();
  });
  
  function typeWriter() {
    if (config.titles.length === 0) return;
    
    const fullText = config.titles[currentTextIndex];
    
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
      currentTextIndex = (currentTextIndex + 1) % config.titles.length;
      delta = 500;
    }
    
    setTimeout(typeWriter, delta);
  }
</script>

<header class={`${config.styles.background} ${config.styles.textColor} py-16 shadow-2xl border-b border-gray-700`}>
  <div class="container mx-auto px-4">
    <div class="flex flex-col items-center text-center space-y-8">
      {#if config.imageUrl}
        <img
          src={config.imageUrl} 
          alt="Profile Photo"
          class="w-44 h-44 rounded-full object-cover border-4 ${config.styles.borderColor} shadow-xl transition-all duration-500 hover:scale-105 hover:border-indigo-500/50 hover:shadow-indigo-500/20"
          in:fly={{ y: -50, duration: 800, delay: 100 }}
          out:fade/>
      {/if}

      <h1 class="text-4xl md:text-5xl font-bold bg-clip-text text-transparent bg-gradient-to-r ${config.styles.gradientFrom} ${config.styles.gradientTo} tracking-tight"
        in:fade={{ delay: 300, duration: 800 }}
        out:fade>
        {config.name}
      </h1>

      <div class="text-xl md:text-2xl font-light max-w-2xl leading-relaxed space-y-4"
        in:fly={{ x: 50, duration: 800, delay: 500 }}
        out:fade>
        
        {#if config.titles.length > 0}
          <div class="relative inline-block min-h-[2.5rem]">
            <span class="relative z-10 text-gray-300">{displayText}</span>
            <span class="absolute bottom-0 left-0 w-full h-1 bg-gradient-to-r ${config.styles.underlineFrom} ${config.styles.underlineTo} opacity-60 rounded-full animate-pulse"></span>
            <span class="inline-block w-1 h-6 bg-blue-400 align-middle ml-1 opacity-80 animate-blink"></span>
          </div>
          
          <div class="w-full h-px bg-gradient-to-r from-transparent via-gray-600 to-transparent my-4"></div>
        {/if}
        
        <div class="relative inline-block">
          <span class="relative z-10 text-gray-300">{config.staticTitle}</span>
          <span class="absolute bottom-0 left-0 w-full h-1 bg-gradient-to-r ${config.styles.underlineFrom} ${config.styles.underlineTo} opacity-60 rounded-full animate-pulse"></span>
        </div>
      </div>
    </div>
  </div>
</header>