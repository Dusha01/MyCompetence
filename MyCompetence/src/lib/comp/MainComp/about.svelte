<script lang="ts">
  import { fade, fly } from 'svelte/transition';
  import { flip } from 'svelte/animate';
  
  let skills = [
    {
      id: 1,
      title: "Frontend разработка",
      description: "Создаю современные, быстрые и адаптивные интерфейсы с использованием Svelte, TypeScript и Tailwind CSS. Фокусируюсь на производительности, доступности и удобстве пользователя.",
      icon: "💻",
      tags: ["Svelte", "TypeScript", "Tailwind CSS"]
    },
    {
      id: 2,
      title: "Backend API",
      description: "Разрабатываю надежные и масштабируемые серверные решения на Python (Rest API). Специализируюсь на создании RESTful API для интеграции с фронтендом и сторонними сервисами.",
      icon: "🔌",
      tags: ["Python", "FastAPI", "REST"]
    },
    {
      id: 3,
      title: "Fullstack решения",
      description: "Полный цикл разработки: от проектирования архитектуры до развертывания. Включает интеграцию фронтенда и бэкенда, автоматизированное тестирование, CI/CD и контейнеризацию (Docker).",
      icon: "🔄",
      tags: ["Docker", "CI/CD", "Testing"]
    },
    {
      id: 4,
      title: "Telegram API",
      description: "Создание интеллектуальных Telegram-ботов для автоматизации бизнес-процессов, чат-сервисов и интеграции с другими платформами. От простых уведомлений до сложных интерактивных систем.",
      icon: "🤖",
      tags: ["Python", "Aiogram", "Telegram API"]
    }
  ];

  let hoveredSkill = null;
</script>

<section id="about" class="py-20 px-4 sm:px-6 lg:px-8 bg-gradient-to-b from-gray-900 to-gray-800 text-white" in:fade={{ duration: 300 }}>
  <div class="max-w-7xl mx-auto">
      <div class="text-center mb-16" in:fly={{ y: 50, duration: 500 }}>
          <h2 class="text-4xl md:text-5xl font-bold mb-4 bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-purple-500">
              О себе
          </h2>
          <p class="text-xl text-gray-300 max-w-3xl mx-auto">
              Я студент 2-го курса ДВГУПС по специальности "Программная инженерия". Как начинающий разработчик, я увлечен созданием качественных digital-решений и постоянно совершенствую свои навыки в веб-разработке.
          </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
          {#each skills as skill (skill.id)}
              <article
                  role="article"
                  class="relative group overflow-hidden rounded-xl bg-gray-800 border border-gray-700 hover:border-blue-400 transition-all duration-300 hover:shadow-lg hover:shadow-blue-500/20"
                  on:mouseenter={() => hoveredSkill = skill.id}
                  on:mouseleave={() => hoveredSkill = null}
                  animate:flip={{ duration: 500 }}
                  in:fade={{ delay: 100 * skill.id }}>
                  
                  <div class="absolute inset-0 bg-gradient-to-br from-blue-900/20 to-purple-900/20 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
          
                  <div class="relative z-10 p-8 h-full flex flex-col">
                      <div class="flex items-start mb-6">
                          <div class="text-4xl mr-4 text-blue-400">{skill.icon}</div>
                          <h3 class="text-2xl font-bold text-white mt-1">{skill.title}</h3>
                      </div>
          
                      <p class="text-gray-300 mb-6 flex-grow">{skill.description}</p>
          
                      <div class="flex flex-wrap gap-2 mt-auto">
                          {#each skill.tags as tag}
                              <span class="px-3 py-1 rounded-full text-sm bg-gray-700 text-blue-300 group-hover:bg-blue-900/30 group-hover:text-blue-200 transition-colors">
                                  {tag}
                              </span>
                          {/each}
                      </div>
                  </div>
              </article>
          {/each}
      </div>

      <div class="text-center mt-16" in:fly={{ y: 50, duration: 500, delay: 300 }}>
          <p class="text-gray-400 max-w-3xl mx-auto">
              В своих проектах я уделяю внимание чистоте кода, модульности архитектуры и современным практикам разработки. 
              Всегда открыт для новых вызовов и возможностей профессионального роста.
          </p>
      </div>
  </div>
</section>