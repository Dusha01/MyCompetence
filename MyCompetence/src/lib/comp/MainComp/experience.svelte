<script lang="ts">
    import { fade, fly } from 'svelte/transition'
    import { quadInOut } from 'svelte/easing';

    interface ExperienceItem{
        id: number,
        title: string,
        description: string,
        date?: string,
        icon: string,
        tags: string[]
    }

    const experience: ExperienceItem[] = [
        {
            id: 1,
            title: "Форк проекта Node-RED",
            description: "Модификация и улучшение open-source проекта Node-RED для создания пользовательских потоков данных.",
            date: "Май 2025",
            icon: "⚙️",
            tags: ["Node.js", "JavaScript", "Flow-based programming"],
        },
        {
            id: 2,
            title: "Фриланс: разработка Telegram-ботов",
            description: "Создание многофункциональных Telegram-ботов для малого бизнеса, включая интеграцию с платежными системами и CRM.",
            date: "Июнь - Июль 2025",
            icon: "🤖",
            tags: ["Python", "MongoDB", "REST API", "OpenAI", "Telegram API"],
        },
        {
            id: 3,
            title: "Веб-разработка полного цикла",
            description: "Разработка и запуск веб-приложений от концепции до реализации. Создание интерактивных пользовательских интерфейсов и бэкенд-систем.",
            date: "2025 - настоящее время",
            icon: "🌐",
            tags: ["Svelte", "HTML5", "CSS3", "Tailwind CSS", "Node.js", "MongoDB", "PostgreSQL"],
        },
    ];
</script>


<section id = "experience" class="py-20 px-4 md:px-8 bg-gradient-to-br from-gray-900 to-gray-800 text-white">
    <div class="max-w-6xl mx-auto">
        <h2 
            class="text-3xl md:text-4xl font-bold mb-12 text-center"
            in:fly={{ y: 50, duration: 500 }}
            out:fade>
            Накопленный опыт за 1 год
        </h2>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            {#each experience as item (item.id)}
                <div
                    transition:fly={{ y: 100, duration: 500, delay: item.id * 100, easing: quadInOut }}
                    class="bg-gray-800 rounded-xl p-6 shadow-lg hover:shadow-2xl transition-all duration-300 hover:-translate-y-2 border-l-4 border-indigo-500 group">

                    <div class="flex items-start mb-4">
                        <span class="text-3xl mr-4">{item.icon}</span>
                        <div>
                            <h3 class="text-xl font-bold text-indigo-400 group-hover:text-indigo-300 transition-colors">
                                {item.title}
                            </h3>
                            {#if item.date}
                                <p class="text-sm text-gray-400">{item.date}</p>
                            {/if}
                        </div>
                    </div>

                    <p class="text-gray-300 mb-5 leading-relaxed">
                        {item.description}
                    </p>

                    <div class="flex flex-wrap gap-2">
                        {#each item.tags as tag}
                            <span class="px-3 py-1 bg-gray-700 rounded-full text-xs text-gray-300">
                                {tag}
                            </span>
                        {/each}
                    </div>
                </div>
            {/each}
        </div>

        <div class="mt-16 text-center" in:fade={{ delay: 800 }}>
            <p class="text-gray-400 italic">
                За год интенсивной работы освоил полный цикл разработки - от идеи до реализации
            </p>
        </div>
    </div>
</section>