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
        { id: 'goals', text: 'Цели' },
        { id: 'forms', text: 'Связаться'},
        { id: 'contact', text: 'Контакты' }
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
    class="w-full z-50 transition-all duration-300 bg-white shadow-lg"
    class:fixed={sticky}
    class:top-0={sticky}
    class:left-0={sticky}
    class:relative={!sticky}
    aria-label="Основная навигация">
    <div class="container mx-auto px-4 flex justify-between items-center py-2">
        <a 
            href="#" 
            class="text-2xl font-bold bg-gradient-to-r from-indigo-600 to-purple-600 bg-clip-text text-transparent transition-all hover:scale-105"
            aria-label="Главная страница">
            Anrew <span class="font-extrabold">Gubchenko</span>
        </a>

        <button 
            class="lg:hidden p-2 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500"
            on:click={toggleMenu}
            aria-label={isMenuOpen ? "Закрыть меню" : "Открыть меню"}
            aria-expanded={isMenuOpen}
            aria-controls="mobile-menu">
            <i class={`fas ${isMenuOpen ? 'fa-times' : 'fa-bars'} text-xl text-indigo-700`} aria-hidden="true"></i>
        </button>

        <div class="hidden lg:block">
            <ul class="flex space-x-6">
                {#each menuItems as item (item.id)}
                    <li>
                        <a 
                            href={`#${item.id}`}
                            class="relative px-2 py-1 text-gray-700 hover:text-indigo-600 font-medium transition-colors after:absolute after:bottom-0 after:left-0 after:w-0 after:h-0.5 after:bg-indigo-600 after:transition-all hover:after:w-full">
                            {item.text}
                        </a>
                    </li>
                {/each}
            </ul>
        </div>
    </div>

    {#if isMenuOpen && isMobile}
        <div 
            id="mobile-menu"
            class="lg:hidden bg-white shadow-lg z-40 overflow-y-auto max-h-[calc(100vh-4rem)]"
            transition:slide={{ duration: 200 }}
            role="menu">
            <ul class="flex flex-col divide-y divide-gray-100">
                {#each menuItems as item (item.id)}
                    <li role="none">
                        <a 
                            href={`#${item.id}`}
                            class="block px-6 py-3 text-gray-700 hover:bg-indigo-50 hover:text-indigo-600 font-medium transition-colors"
                            on:click={closeMenu}
                            role="menuitem"
                        >
                            {item.text}
                        </a>
                    </li>
                {/each}
            </ul>
        </div>
    {/if}
</nav>

<style>
    .after\:transition-all::after {
        transition-duration: 300ms;
    }
</style>