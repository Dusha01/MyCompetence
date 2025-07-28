<script lang="ts">
    import { fade, fly } from 'svelte/transition';

    type TechCategory = 'backend' | 'db' | 'devops' | 'web' | 'other';

    interface TechItem {
        id: string;
        name: string;
        category: TechCategory;
        level: number;
    }

    const techStack: TechItem[] = [
        // Backend
        { id: 'python', name: 'Python', category: 'backend', level: 3 },
        { id: 'golang', name: 'Golang', category: 'backend', level: 2 },
        { id: 'cpp', name: 'C++', category: 'backend', level: 1 },
        { id: 'js', name: 'JavaScript', category: 'backend', level: 2 },
        
        // Databases
        { id: 'mongo', name: 'MongoDB', category: 'db', level: 3 },
        { id: 'redis', name: 'Redis', category: 'db', level: 2 },
        { id: 'sql', name: 'SQL', category: 'db', level: 2 },
        
        // DevOps
        { id: 'docker', name: 'Docker', category: 'devops', level: 3 },
        { id: 'prometheus', name: 'Prometheus', category: 'devops', level: 1 },
        { id: 'grafana', name: 'Grafana', category: 'devops', level: 1 },
        
        // Web
        { id: 'html', name: 'HTML/CSS', category: 'web', level: 3 },
        { id: 'rest', name: 'REST API', category: 'web', level: 3 },
        { id: 'telegram', name: 'Telegram API', category: 'web', level: 2 },
        { id: 'svelte', name: 'Svelte', category: 'web', level: 1},
        
        // Other
        { id: 'figma', name: 'Figma', category: 'other', level: 2 },
        { id: 'node-red', name: 'Node-RED', category: 'other', level: 1 }
    ];

    const categoryColors: Record<TechCategory, string> = {
        backend: 'bg-indigo-500 border-indigo-700',
        db: 'bg-emerald-500 border-emerald-700',
        devops: 'bg-amber-500 border-amber-700',
        web: 'bg-rose-500 border-rose-700',
        other: 'bg-purple-500 border-purple-700'
    };

    const categoryNames: Record<TechCategory, string> = {
        backend: 'Backend',
        db: 'Базы данных',
        devops: 'DevOps',
        web: 'Веб-технологии',
        other: 'Другое'
    };

    const getLevelColor = (level: number) => {
        switch(level) {
            case 3: return 'border-4 border-white shadow-lg';
            case 2: return 'border-2 border-white shadow-md';
            default: return 'border border-white shadow-sm';
        }
    };
</script>

<section id="tech" class="py-12 px-4 bg-gradient-to-br from-gray-900 to-gray-800 text-white">
    <div class="max-w-6xl mx-auto">
        <h2 
            class="text-2xl font-bold mb-8 text-center"
            in:fly={{ y: 50, duration: 500 }}
            out:fade>
            Мой стек технологий
        </h2>

        <!-- Мобильная версия (grid-cols-1) -->
        <div class="grid grid-cols-1 gap-4 md:hidden">
            <!-- Backend -->
            <div class={`p-3 rounded-xl ${categoryColors.backend}`}>
                <h3 class="text-lg font-bold mb-3 text-center">{categoryNames.backend}</h3>
                <div class="grid grid-cols-2 gap-2">
                    {#each techStack.filter(t => t.category === 'backend') as tech, i}
                        <div 
                            class={`p-2 rounded-lg text-center text-sm ${getLevelColor(tech.level)}`}
                            in:fly={{ y: 20, duration: 300, delay: 100 * i }}
                        >
                            {tech.name}
                        </div>
                    {/each}
                </div>
            </div>

            <!-- Web -->
            <div class={`p-3 rounded-xl ${categoryColors.web}`}>
                <h3 class="text-lg font-bold mb-3 text-center">{categoryNames.web}</h3>
                <div class="grid grid-cols-2 gap-2">
                    {#each techStack.filter(t => t.category === 'web') as tech, i}
                        <div 
                            class={`p-2 rounded-lg text-center text-sm ${getLevelColor(tech.level)}`}
                            in:fly={{ y: 20, duration: 300, delay: 100 * i }}
                        >
                            {tech.name}
                        </div>
                    {/each}
                </div>
            </div>

            <!-- Центральный блок -->
            <div class="p-3 rounded-xl bg-gray-700 border-2 border-white">
                <div class="text-center">
                    <div class="text-xl font-bold mb-1">Fullstack</div>
                    <div class="text-md">Developer</div>
                </div>
            </div>

            <!-- Databases -->
            <div class={`p-3 rounded-xl ${categoryColors.db}`}>
                <h3 class="text-lg font-bold mb-3 text-center">{categoryNames.db}</h3>
                <div class="grid grid-cols-2 gap-2">
                    {#each techStack.filter(t => t.category === 'db') as tech, i}
                        <div 
                            class={`p-2 rounded-lg text-center text-sm ${getLevelColor(tech.level)}`}
                            in:fly={{ y: 20, duration: 300, delay: 100 * i }}
                        >
                            {tech.name}
                        </div>
                    {/each}
                </div>
            </div>

            <!-- DevOps -->
            <div class={`p-3 rounded-xl ${categoryColors.devops}`}>
                <h3 class="text-lg font-bold mb-3 text-center">{categoryNames.devops}</h3>
                <div class="grid grid-cols-2 gap-2">
                    {#each techStack.filter(t => t.category === 'devops') as tech, i}
                        <div 
                            class={`p-2 rounded-lg text-center text-sm ${getLevelColor(tech.level)}`}
                            in:fly={{ y: 20, duration: 300, delay: 100 * i }}
                        >
                            {tech.name}
                        </div>
                    {/each}
                </div>
            </div>

            <!-- Other -->
            <div class={`p-3 rounded-xl ${categoryColors.other}`}>
                <h3 class="text-lg font-bold mb-3 text-center">{categoryNames.other}</h3>
                <div class="grid grid-cols-2 gap-2">
                    {#each techStack.filter(t => t.category === 'other') as tech, i}
                        <div 
                            class={`p-2 rounded-lg text-center text-sm ${getLevelColor(tech.level)}`}
                            in:fly={{ y: 20, duration: 300, delay: 100 * i }}
                        >
                            {tech.name}
                        </div>
                    {/each}
                </div>
            </div>
        </div>

        <!-- Десктоп версия (скрыта на мобильных) -->
        <div class="hidden md:grid md:grid-cols-5 gap-6">
            <!-- Оригинальная разметка для десктопа -->
            <!-- Backend -->
            <div 
                class={`p-4 rounded-xl ${categoryColors.backend} col-span-1 md:col-span-2`}
                in:fly={{ x: -50, duration: 400 }}>
                <h3 class="text-xl font-bold mb-4 text-center">{categoryNames.backend}</h3>
                <div class="grid grid-cols-2 gap-3">
                    {#each techStack.filter(t => t.category === 'backend') as tech, i}
                        <div 
                            class={`p-3 rounded-lg text-center ${getLevelColor(tech.level)}`}
                            in:fly={{ y: 20, duration: 300, delay: 100 * i }}
                        >
                            {tech.name}
                        </div>
                    {/each}
                </div>
            </div>

            <!-- Web -->
            <div 
                class={`p-4 rounded-xl ${categoryColors.web} col-span-1 md:col-span-3`}
                in:fly={{ x: 50, duration: 400, delay: 100 }}>
                <h3 class="text-xl font-bold mb-4 text-center">{categoryNames.web}</h3>
                <div class="grid grid-cols-3 gap-3">
                    {#each techStack.filter(t => t.category === 'web') as tech, i}
                        <div 
                            class={`p-3 rounded-lg text-center ${getLevelColor(tech.level)}`}
                            in:fly={{ y: 20, duration: 300, delay: 100 * i }}
                        >
                            {tech.name}
                        </div>
                    {/each}
                </div>
            </div>

            <!-- Databases -->
            <div 
                class={`p-4 rounded-xl ${categoryColors.db} col-start-2`}
                in:fly={{ x: -50, duration: 400, delay: 200 }}>
                <h3 class="text-xl font-bold mb-4 text-center">{categoryNames.db}</h3>
                <div class="grid grid-cols-1 gap-3">
                    {#each techStack.filter(t => t.category === 'db') as tech, i}
                        <div 
                            class={`p-3 rounded-lg text-center ${getLevelColor(tech.level)}`}
                            in:fly={{ y: 20, duration: 300, delay: 100 * i }}>
                            {tech.name}
                        </div>
                    {/each}
                </div>
            </div>

            <!-- Центральный блок -->
            <div 
                class="p-4 rounded-xl bg-gray-700 border-2 border-white col-span-1 flex items-center justify-center"
                in:fade={{ duration: 500, delay: 300 }}>
                <div class="text-center">
                    <div class="text-2xl font-bold mb-2">Fullstack</div>
                    <div class="text-lg">Developer</div>
                </div>
            </div>

            <!-- DevOps -->
            <div 
                class={`p-4 rounded-xl ${categoryColors.devops} col-span-1`}
                in:fly={{ x: 50, duration: 400, delay: 200 }}>
                <h3 class="text-xl font-bold mb-4 text-center">{categoryNames.devops}</h3>
                <div class="grid grid-cols-1 gap-3">
                    {#each techStack.filter(t => t.category === 'devops') as tech, i}
                        <div 
                            class={`p-3 rounded-lg text-center ${getLevelColor(tech.level)}`}
                            in:fly={{ y: 20, duration: 300, delay: 100 * i }}
                        >
                            {tech.name}
                        </div>
                    {/each}
                </div>
            </div>

            <!-- Other -->
            <div 
                class={`p-4 rounded-xl ${categoryColors.other} col-span-1 md:col-span-5`}
                in:fly={{ y: 50, duration: 400, delay: 400 }}>
                <h3 class="text-xl font-bold mb-4 text-center">{categoryNames.other}</h3>
                <div class="grid grid-cols-2 md:grid-cols-2 gap-3">
                    {#each techStack.filter(t => t.category === 'other') as tech, i}
                        <div 
                            class={`p-3 rounded-lg text-center ${getLevelColor(tech.level)}`}
                            in:fly={{ y: 20, duration: 300, delay: 100 * i }}>
                            {tech.name}
                        </div>
                    {/each}
                </div>
            </div>
        </div>

        <!-- Легенда -->
        <div class="mt-8 md:mt-16 flex flex-wrap justify-center gap-3 md:gap-4" in:fade={{ delay: 800 }}>
            {#each Object.entries(categoryNames) as [category, name]}
                <div class="flex items-center">
                    <div class={`w-3 h-3 md:w-4 md:h-4 rounded-full mr-1 md:mr-2 ${categoryColors[category as TechCategory].split(' ')[0]}`}></div>
                    <span class="text-gray-300 text-xs md:text-sm">{name}</span>
                </div>
            {/each}
        </div>
    </div>
</section>