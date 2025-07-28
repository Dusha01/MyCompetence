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
            description: "Модификация и улучшение open-source проекта Node-RED для создания пользовательских потоков данных с добавлением кастомных узлов и оптимизацией производительности.",
            date: "Май 2025",
            icon: "⚙️",
            tags: ["Node.js", "JavaScript", "Flow-based programming"],
        },
        {
            id: 2,
            title: "Фриланс: разработка Telegram-ботов",
            description: "Создание многофункциональных Telegram-ботов для малого бизнеса с интеграцией платежных систем, CRM и обработкой естественного языка через OpenAI API.",
            date: "Июнь - Июль 2025",
            icon: "🤖",
            tags: ["Python", "MongoDB", "REST API", "OpenAI", "Telegram API"],
        },
        {
            id: 3,
            title: "Веб-разработка полного цикла",
            description: "Полноценная разработка веб-приложений: от проектирования архитектуры и UI/UX до реализации backend и деплоя. Особый акцент на производительность и UX.",
            date: "2025 - настоящее время",
            icon: "🌐",
            tags: ["Svelte", "HTML5", "CSS3", "Tailwind CSS", "Node.js", "MongoDB", "PostgreSQL"],
        },
    ];
</script>

<section id="experience" class="py-12 px-4 sm:px-6 bg-gradient-to-br from-gray-900 to-gray-800 text-white">
    <div class="max-w-4xl mx-auto">
        <h2 
            class="text-2xl sm:text-3xl font-bold mb-8 text-left bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-purple-500"
            in:fly={{ y: 50, duration: 500 }}
            out:fade>
            Накопленный опыт за 1 год
        </h2>

        <div class="space-y-6">
            {#each experience as item (item.id)}
                <div
                    transition:fly={{ y: 100, duration: 500, delay: item.id * 100, easing: quadInOut }}
                    class="bg-gray-800/90 rounded-xl p-6 shadow-lg hover:shadow-xl transition-all duration-300 hover:-translate-y-1 border-l-4 border-indigo-500 group backdrop-blur-sm">

                    <div class="flex items-start gap-4 mb-4">
                        <span class="text-2xl mt-1 flex-shrink-0">{item.icon}</span>
                        <div class="text-left">
                            <h3 class="text-lg sm:text-xl font-semibold text-indigo-400 group-hover:text-indigo-300 transition-colors">
                                {item.title}
                            </h3>
                            {#if item.date}
                                <p class="text-sm text-gray-400 mt-1">{item.date}</p>
                            {/if}
                        </div>
                    </div>

                    <p class="text-gray-300 mb-5 text-sm sm:text-base leading-relaxed text-left">
                        {item.description}
                    </p>

                    <div class="flex flex-wrap gap-2">
                        {#each item.tags as tag}
                            <span class="px-3 py-1 bg-gray-700/50 rounded-full text-xs text-gray-300 hover:bg-gray-600 transition-colors">
                                {tag}
                            </span>
                        {/each}
                    </div>
                </div>
            {/each}
        </div>

        <div class="mt-12 text-left" in:fade={{ delay: 800 }}>
            <p class="text-gray-400 italic text-sm sm:text-base max-w-2xl leading-relaxed">
                "За год интенсивной практики освоил полный цикл разработки — от проектирования архитектуры до реализации и поддержки готовых решений."
            </p>
        </div>
    </div>
</section>