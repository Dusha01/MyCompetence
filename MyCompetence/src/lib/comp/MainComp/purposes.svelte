<script lang="ts">
    import { fade, fly, scale } from 'svelte/transition';

    const careerPath = [
        {
            id: 1,
            title: "Junior Developer",
            description: "Освоение фундаментальных навыков",
            skills: [
                "Основы алгоритмов и структур данных",
                "Базовый синтаксис Python/JavaScript",
                "Работа с Git и GitHub",
                "Простые SQL-запросы",
                "Основы HTTP и REST API"
            ],
            duration: "6-12 месяцев",
            icon: "👶",
            position: "left",
            zIndex: 2
        },
        {
            id: 2,
            title: "Middle Backend Developer",
            description: "Специализация в серверной разработке",
            skills: [
                "Продвинутый Python (FastAPI/Django)",
                "Асинхронное программирование",
                "Оптимизация SQL-запросов",
                "Кэширование (Redis)",
                "Docker и базовый DevOps",
                "Тестирование (pytest, unittest)"
            ],
            duration: "1.5-2 года",
            icon: "💻",
            position: "right",
            zIndex: 2
        },
        {
            id: 3,
            title: "Senior Backend Engineer",
            description: "Архитектура сложных систем",
            skills: [
                "Проектирование микросервисов",
                "Message brokers (Kafka/RabbitMQ)",
                "Мониторинг (Prometheus/Grafana)",
                "Kubernetes и облачные решения",
                "Безопасность и оптимизация",
                "Mentoring & Code Review"
            ],
            duration: "2+ года",
            icon: "🧠",
            position: "left",
            zIndex: 2
        },
        {
            id: 4,
            title: "Tech Lead / Architect",
            description: "Полный контроль над продуктом",
            skills: [
                "Системное проектирование",
                "Управление техническим долгом",
                "Принятие архитектурных решений",
                "Координация команд",
                "Бюджетирование технических решений",
                "Интеграция CI/CD процессов"
            ],
            duration: "3+ года",
            icon: "👑",
            position: "center",
            highlight: true,
            zIndex: 3
        }
    ];

</script>

<section
    id="career"
    class="py-28 px-4 sm:px-6 lg:px-8 bg-gradient-to-b from-gray-900 to-gray-800 text-white relative overflow-hidden"
    in:fade={{ duration: 300 }}>

    <div class="max-w-7xl mx-auto relative z-10">
        <div class="text-center mb-20" in:fly={{ y: 50, duration: 500 }}>
            <h2 class="text-4xl md:text-5xl font-bold pb-3 mb-4 bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-purple-500">
                Карьерный путь Backend-разработчика
            </h2>
            <p class="text-xl pb-5 text-gray-300 max-w-3xl mx-auto">
                От джуниора до технического лидера: системный подход к профессиональному росту
            </p>
        </div>

        <div class="relative h-[700px] md:h-[800px] mt-10">
            <div class="absolute left-1/2 top-10 bottom-32 w-1 bg-gradient-to-b from-blue-500 to-purple-600 transform -translate-x-1/2" style="z-index: 1;"></div>

            {#each careerPath as step (step.id)}
                <div
                    class={`absolute transition-all duration-500 ${step.position === 'left' ? 'left-[25%]' : step.position === 'right' ? 'left-[75%]' : 'left-1/2'} ${
                        step.id === 1 ? 'top-10' :
                        step.id === 2 ? 'top-1/3' :
                        step.id === 3 ? 'top-2/3' : 'top-[85%]'
                    } transform -translate-x-1/2 -translate-y-1/2`}
                    style={`z-index: ${step.zIndex};`}
                    in:fly={{ y: 100, duration: 500, delay: step.id * 100 }}>

                    <div
                        class={`relative w-72 md:w-80 p-6 rounded-xl bg-gray-800 border ${step.highlight ? 'border-blue-400 shadow-lg shadow-blue-500/30' : 'border-gray-700'} transition-all duration-300 hover:scale-105 hover:shadow-lg ${step.highlight ? 'hover:shadow-blue-500/30' : 'hover:shadow-purple-500/20'}`}
                        in:scale={{ duration: 500, delay: step.id * 100 + 300 }}>

                        {#if step.highlight}
                            <div class="absolute -top-3 -right-3 bg-blue-500 text-white text-xs font-bold px-2 py-1 rounded-full animate-pulse">
                                Target Position
                            </div>
                        {/if}

                        <div class="flex items-start mb-3">
                            <div class={`text-3xl mr-4 ${step.highlight ? 'text-blue-400' : 'text-purple-400'}`}>
                                {step.icon}
                            </div>
                            <div>
                                <h3 class="text-xl font-bold text-white mb-1">
                                    {step.title}
                                </h3>
                                <p class="text-gray-400 text-sm">
                                    {step.description} • {step.duration}
                                </p>
                            </div>
                        </div>
                        <div class="border-t border-gray-700 pt-3">
                            <h4 class="text-xs font-semibold text-blue-400 mb-2 uppercase tracking-wider">Ключевые навыки:</h4>
                            <ul class="text-xs text-gray-400 space-y-1.5">
                                {#each step.skills as skill}
                                    <li class="flex items-start">
                                        <svg class="w-3 h-3 mt-0.5 mr-2 text-blue-400 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                                        </svg>
                                        {skill}
                                    </li>
                                {/each}
                            </ul>
                        </div>
                    </div>
                </div>
            {/each}
        </div>

        <div class="mt-32 grid md:grid-cols-3 gap-8" in:fly={{ y: 50, duration: 500, delay: 800 }}>
            <div class="bg-gray-800/50 p-6 rounded-xl border border-gray-700 hover:border-blue-400 transition-colors">
                <div class="text-blue-400 text-2xl mb-3">📚</div>
                <h3 class="text-xl font-bold mb-2">Глубокие знания</h3>
                <p class="text-gray-300">Освоение computer science fundamentals: алгоритмы, структуры данных, паттерны проектирования, системы хранения данных</p>
            </div>
            <div class="bg-gray-800/50 p-6 rounded-xl border border-gray-700 hover:border-blue-400 transition-colors">
                <div class="text-blue-400 text-2xl mb-3">🛠️</div>
                <h3 class="text-xl font-bold mb-2">Практический опыт</h3>
                <p class="text-gray-300">Участие в сложных проектах с полным циклом разработки от проектирования до production-развертывания</p>
            </div>
            <div class="bg-gray-800/50 p-6 rounded-xl border border-gray-700 hover:border-blue-400 transition-colors">
                <div class="text-blue-400 text-2xl mb-3">🧩</div>
                <h3 class="text-xl font-bold mb-2">Системное мышление</h3>
                <p class="text-gray-300">Умение проектировать масштабируемые и отказоустойчивые системы с учетом бизнес-требований</p>
            </div>
        </div>
    </div>
</section>