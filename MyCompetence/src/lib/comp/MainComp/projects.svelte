<script lang="ts">
    import { fade, fly } from 'svelte/transition';
    import { flip } from 'svelte/animate';
  
    let projects = [
        {
            id: 1,
            title: "01. Telegram Bot Notepad",
            description: "Умный бот для заметок и напоминаний с категориями и тегами. Реализовано хранение данных, поиск и гибкая система напоминаний.",
            icon: "📝",
            tags: ["Python", "Aiogram", "MongoDB"],
            link: ""
        },
        {
            id: 2,
            title: "02. Новостной агрегатор",
            description: "Консольное приложение для сбора новостей из различных источников с фильтрацией по категориям и ключевым словам.",
            icon: "📰",
            tags: ["Python", "BeautifulSoup", "API"],
            link: "https://github.com/Dusha01/News-Aggregator"
        },
        {
            id: 3,
            title: "03. Server Metrics Telegram Bot",
            description: "Мониторинг серверных метрик через Prometheus. Автоматические алерты и визуализация данных в виде графиков прямо в Telegram.",
            icon: "📊",
            tags: ["Python", "Prometheus", "Grafana", "Telegram API"],
            link: "https://github.com/Dusha01/Alert_TG_BOT"
        },
        {
            id: 4,
            title: "04. AI Web Parser",
            description: "Продвинутый парсер веб-страниц с использованием AI для анализа и структурирования контента. Поддержка различных форматов вывода.",
            icon: "🤖",
            tags: ["Python", "LLM", "BeautifulSoup", "NLP"],
            link: "https://github.com/Dusha01/ai_pars_sites"
        }
    ];
  
    let hoveredProject = null;
</script>
  
<section 
    id="projects" 
    class="py-20 px-4 sm:px-6 lg:px-8 bg-gradient-to-b from-gray-900 to-gray-800 text-white"
    in:fade={{ duration: 300 }}>

    <div class="max-w-7xl mx-auto">
        <div class="text-center mb-16" in:fly={{ y: 50, duration: 500 }}>
            <h2 class="text-4xl md:text-5xl font-bold mb-4 bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-purple-500">
                Мои проекты
            </h2>
            <p class="text-xl text-gray-300 max-w-3xl mx-auto">
                Реализованные решения, демонстрирующие мой подход к разработке и навыки работы с различными технологиями
            </p>
        </div>
  
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-8">
            {#each projects as project (project.id)}
                <article
                    role="article"
                    class="relative group overflow-hidden rounded-xl bg-gray-800 border border-gray-700 hover:border-blue-400 transition-all duration-300 hover:shadow-lg hover:shadow-blue-500/20"
                    on:mouseenter={() => hoveredProject = project.id}
                    on:mouseleave={() => hoveredProject = null}
                    animate:flip={{ duration: 500 }}
                    in:fade={{ delay: 100 * project.id }}>
                    
                    <div class="absolute inset-0 bg-gradient-to-br from-blue-900/20 to-purple-900/20 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
            
                    <div class="relative z-10 p-8 h-full flex flex-col">
                        <div class="flex items-start mb-6">
                            <div class="text-4xl mr-4 text-blue-400">{project.icon}</div>
                            <h3 class="text-2xl font-bold text-white mt-1">{project.title}</h3>
                        </div>
            
                        <p class="text-gray-300 mb-6 flex-grow">{project.description}</p>
            
                        <div class="flex flex-wrap gap-2 mt-auto">
                            {#each project.tags as tag}
                                <span class="px-3 py-1 rounded-full text-sm bg-gray-700 text-blue-300 group-hover:bg-blue-900/30 group-hover:text-blue-200 transition-colors">
                                    {tag}
                                </span>
                            {/each}
                        </div>
            
                        <div class="mt-6 transform translate-y-2 opacity-0 group-hover:translate-y-0 group-hover:opacity-100 transition-all duration-300">
                            <a href={project.link} class="inline-flex items-center text-blue-400 hover:text-blue-300 font-medium">
                                Подробнее
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 ml-2" viewBox="0 0 20 20" fill="currentColor">
                                    <path fill-rule="evenodd" d="M10.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L12.586 11H5a1 1 0 110-2h7.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
                                </svg>
                            </a>
                        </div>
                    </div>
                </article>
            {/each}
        </div>
  
        <div class="text-center mt-16" in:fly={{ y: 50, duration: 500, delay: 300 }}>
            <a href="https://github.com/Dusha01" class="inline-block px-8 py-3 rounded-full bg-gradient-to-r from-blue-500 to-purple-600 text-white font-medium hover:shadow-lg hover:shadow-blue-500/30 transition-all transform hover:-translate-y-1">
                Посмотреть все проекты
            </a>
        </div>
    </div>
</section>