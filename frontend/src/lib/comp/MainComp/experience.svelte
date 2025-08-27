<script lang="ts">
    import { fade, fly } from 'svelte/transition';
    import { flip } from 'svelte/animate';
    import { onMount } from 'svelte';
    
    interface ExperienceItem {
      id: number;
      title: string;
      description: string;
      date?: string;
      icon: string;
      tags: string[];
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
  
    let isVisible = false;
    let sectionRef: HTMLElement;
  
    onMount(() => {
      const observer = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            isVisible = entry.isIntersecting;
          });
        },
        { threshold: 0.2 }
      );
  
      if (sectionRef) {
        observer.observe(sectionRef);
      }
      
      return () => {
        if (sectionRef) {
          observer.unobserve(sectionRef);
        }
      };
    });
  </script>
  
  <section
    id="experience"
    class="py-20 px-4 sm:px-6 lg:px-8 bg-gradient-to-b from-gray-900 to-gray-800 text-white"
    bind:this={sectionRef}>
    
    <div class="max-w-7xl mx-auto">
      <div class="text-left mb-16" 
        in:fly={{ y: 50, duration: 500, delay: 0 }}
        out:fly={{ y: 50, duration: 300 }}
        class:opacity-0={!isVisible}
        class:translate-y-[-20px]={!isVisible}
        class:opacity-100={isVisible}
        class:translate-y-0={isVisible}>
        <h2 class="text-4xl md:text-5xl font-bold mb-4 bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-purple-500">
          Накопленный опыт
        </h2>
        <p class="text-xl text-gray-300 max-w-3xl">
          За год интенсивной практики освоил полный цикл разработки — от проектирования архитектуры до реализации и поддержки готовых решений.
        </p>
      </div>
  
      <div class="grid grid-cols-1 gap-8">
        {#each experience as item (item.id)}
          <article
            role="article"
            class="relative group overflow-hidden rounded-xl bg-gray-800 border border-gray-700 hover:border-blue-400 transition-all duration-300 hover:shadow-lg hover:shadow-blue-500/20"
            animate:flip={{ duration: 500 }}
            in:fade={{ delay: 100 * item.id }}
            out:fade
            class:opacity-0={!isVisible}
            class:translate-y-4={!isVisible}
            class:opacity-100={isVisible}
            class:translate-y-0={isVisible}
            style={`transition-delay: ${item.id * 150}ms`}>
            
            <div class="absolute inset-0 bg-gradient-to-br from-blue-900/20 to-purple-900/20 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
    
            <div class="relative z-10 p-8 h-full flex flex-col">
              <div class="flex items-start mb-6">
                <div class="text-4xl mr-4 text-blue-400">{item.icon}</div>
                <div>
                  <h3 class="text-2xl font-bold text-white">{item.title}</h3>
                  {#if item.date}
                    <p class="text-gray-400 mt-1">{item.date}</p>
                  {/if}
                </div>
              </div>
    
              <p class="text-gray-300 mb-6 flex-grow">{item.description}</p>
    
              <div class="flex flex-wrap gap-2 mt-auto">
                {#each item.tags as tag}
                  <span class="px-3 py-1 rounded-full text-sm bg-gray-700 text-blue-300 group-hover:bg-blue-900/30 group-hover:text-blue-200 transition-colors">
                    {tag}
                  </span>
                {/each}
              </div>
            </div>
          </article>
        {/each}
      </div>
  
      <div class="text-center mt-16" 
        in:fly={{ y: 50, duration: 500, delay: 300 }}
        out:fly={{ y: 50, duration: 300 }}
        class:opacity-0={!isVisible}
        class:translate-y-[-20px]={!isVisible}
        class:opacity-100={isVisible}
        class:translate-y-0={isVisible}>
        <p class="text-gray-400 max-w-3xl mx-auto">
          Каждый проект — это новый вызов и возможность улучшить свои навыки. 
          Стремлюсь создавать не просто работающий код, а качественные и масштабируемые решения.
        </p>
      </div>
    </div>
  </section>
  
  <style>
    [class*="transition-all"] {
      transition-property: all;
      will-change: transform, opacity;
    }
  
    section > div > * {
      transition: opacity 0.9s ease-out, transform 0.9s ease-out;
    }
  </style>