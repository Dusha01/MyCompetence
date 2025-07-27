<script lang="ts">
    import { onMount } from 'svelte';
    import { slide } from 'svelte/transition';
    
    let sticky = false;
    let menuHeight = 0;
    let isMenuOpen = false;
    let isMobile = true;

    const menuItems = [
        { id: 'about', text: 'Обо мне' },
        { id: 'projects', text: 'Проекты'},
        { id: 'experience', text: 'Опыт'},
        { id: 'tech', text: 'Технологии' },
        { id: 'career', text: 'Карьера' },
        { id: 'services', text: 'Услуги'},
    ];

    const checkMobile = () => {
        isMobile = window.innerWidth < 1024;
        if (!isMobile) {
            isMenuOpen = false;
        }
    };

    const toggleMenu = () => {
        isMenuOpen = !isMenuOpen;
    };

    const closeMenu = () => {
        isMenuOpen = false;
    };

    onMount(() => {
        checkMobile();
        
        const menu = document.querySelector('nav') as HTMLElement;
        if (menu) {
            menuHeight = menu.offsetHeight;
        }

        window.addEventListener('scroll', handleScroll);
        window.addEventListener('resize', handleResize);

        return () => {
            window.removeEventListener('scroll', handleScroll);
            window.removeEventListener('resize', handleResize);
        };
    });

    function handleResize() {
        checkMobile();
        const menu = document.querySelector('nav') as HTMLElement;
        if (menu) {
            menuHeight = menu.offsetHeight;
        }
    }

    function handleScroll() {
        const pageTop = document.querySelector('#page-top') as HTMLElement;
        if (!pageTop) {
            sticky = window.scrollY > 100; 
            return;
        }
        
        const pageTopRect = pageTop.getBoundingClientRect();
        const pageTopBottom = pageTopRect.bottom + window.scrollY;
        
        sticky = window.scrollY > pageTopBottom - menuHeight;
    }
</script>

<!-- svelte-ignore element_invalid_self_closing_tag -->
<div id="page-top" class="w-full h-0" />

<nav 
    class="w-full z-50 transition-all duration-300 bg-gray-900 border-b border-gray-700 shadow-xl"
    class:fixed={sticky}
    class:top-0={sticky}
    class:left-0={sticky}
    class:relative={!sticky}
    aria-label="Основная навигация">
    <div class="container mx-auto px-4 flex justify-between items-center py-4">
        <a 
            href="#" 
            class="text-2xl font-bold bg-gradient-to-r from-blue-400 to-purple-500 bg-clip-text text-transparent transition-all hover:scale-105"
            aria-label="Главная страница">
            Andrew <span class="font-extrabold">Gubchenko</span>
        </a>

        <button 
            class="lg:hidden p-3 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500 transition-all"
            on:click={toggleMenu}
            aria-label={isMenuOpen ? "Закрыть меню" : "Открыть меню"}
            aria-expanded={isMenuOpen}
            aria-controls="mobile-menu">
            <svg class={`w-6 h-6 ${isMenuOpen ? 'text-purple-400' : 'text-gray-300'}`} fill="none" stroke="currentColor" viewBox="0 0 24 24">
                {#if isMenuOpen}
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                {:else}
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
                {/if}
            </svg>
        </button>

        <div class="hidden lg:block">
            <ul class="flex space-x-8">
                {#each menuItems as item (item.id)}
                    <li class="relative">
                        <a 
                            href={`#${item.id}`}
                            class="block px-4 py-3 text-gray-300 hover:text-white font-medium transition-colors text-lg"
                            on:mouseenter={e => {
                                const underline = e.currentTarget.querySelector('.underline');
                                if (underline) underline.classList.add('w-full');
                            }}
                            on:mouseleave={e => {
                                const underline = e.currentTarget.querySelector('.underline');
                                if (underline) underline.classList.remove('w-full');
                            }}>
                            <span class="relative z-10">
                                {item.text}
                            </span>
                            <span class="absolute bottom-2 left-0 h-0.5 bg-gradient-to-r from-blue-400 to-purple-500 transition-all duration-300 w-0 underline"></span>
                        </a>
                    </li>
                {/each}
            </ul>
        </div>
    </div>

    {#if isMenuOpen && isMobile}
        <div 
            id="mobile-menu"
            class="lg:hidden bg-gray-800 shadow-xl z-40 overflow-y-auto max-h-[calc(100vh-5rem)]"
            transition:slide={{ duration: 200 }}
            role="menu">
            <ul class="flex flex-col divide-y divide-gray-700">
                {#each menuItems as item (item.id)}
                    <li role="none" class="relative">
                        <a 
                            href={`#${item.id}`}
                            class="block px-8 py-4 text-gray-300 hover:text-white font-medium transition-colors text-lg
                                   hover:bg-gradient-to-r hover:from-blue-900/20 hover:to-purple-900/20"
                            on:click={closeMenu}
                            role="menuitem">
                            <span>{item.text}</span>
                            <span class="absolute bottom-3 left-8 right-8 h-0.5 bg-gradient-to-r from-blue-400 to-purple-500 opacity-0 hover:opacity-100 transition-opacity"></span>
                        </a>
                    </li>
                {/each}
            </ul>
        </div>
    {/if}
</nav>

<style>
    .underline {
        transition-property: width;
        transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
        transition-duration: 300ms;
    }
    
    .w-full {
        width: 100%;
    }
</style>