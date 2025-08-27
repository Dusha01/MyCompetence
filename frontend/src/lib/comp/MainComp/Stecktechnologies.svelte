<script lang="ts">
    import { onMount } from 'svelte';
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
        { id: 'svelte', name: 'Svelte', category: 'web', level: 1},
        { id: 'js', name: 'JavaScript', category: 'web', level: 1},
        
        // Other
        { id: 'figma', name: 'Figma', category: 'other', level: 2 },
        { id: 'node-red', name: 'Node-RED', category: 'other', level: 1 },
        { id: 'telegram', name: 'Telegram API', category: 'other', level: 3 }
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

    let isVisible = false;
    let sectionRef: HTMLElement;

    onMount(() => {
        const observer = new IntersectionObserver(
            (entries) => {
                entries.forEach((entry) => {
                    isVisible = entry.isIntersecting;
                });
            },
            { threshold: 0.1 }
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
    id="tech" 
    class="py-12 px-4 bg-gradient-to-br from-gray-900 to-gray-800 text-white"
    bind:this={sectionRef}
>
    <div class="max-w-6xl mx-auto">
        <h2 
            class="text-2xl font-bold mb-8 text-center transition-all duration-1000 ease-out"
            class:opacity-0={!isVisible}
            class:translate-y-[-20px]={!isVisible}
            class:opacity-100={isVisible}
            class:translate-y-0={isVisible}>
            Мой стек технологий
        </h2>

        <!-- Мобильная версия (grid-cols-1) -->
        <div class="grid grid-cols-1 gap-4 md:hidden">
            <!-- Backend -->
            <div 
                class={`p-3 rounded-xl ${categoryColors.backend} transition-all duration-1000 ease-out delay-150`}
                class:opacity-0={!isVisible}
                class:translate-y-4={!isVisible}
                class:opacity-100={isVisible}
                class:translate-y-0={isVisible}>
                <h3 class="text-lg font-bold mb-3 text-center">{categoryNames.backend}</h3>
                <div class="grid grid-cols-2 gap-2">
                    {#each techStack.filter(t => t.category === 'backend') as tech, i}
                        <div 
                            class={`p-2 rounded-lg text-center text-sm ${getLevelColor(tech.level)} transition-all duration-300 ease-out`}
                            class:opacity-0={!isVisible}
                            class:translate-y-2={!isVisible}
                            class:opacity-100={isVisible}
                            class:translate-y-0={isVisible}
                            style={`transition-delay: ${150 + i * 50}ms`}>
                            {tech.name}
                        </div>
                    {/each}
                </div>
            </div>

            <!-- Web -->
            <div 
                class={`p-3 rounded-xl ${categoryColors.web} transition-all duration-1000 ease-out delay-300`}
                class:opacity-0={!isVisible}
                class:translate-y-4={!isVisible}
                class:opacity-100={isVisible}
                class:translate-y-0={isVisible}>
                <h3 class="text-lg font-bold mb-3 text-center">{categoryNames.web}</h3>
                <div class="grid grid-cols-2 gap-2">
                    {#each techStack.filter(t => t.category === 'web') as tech, i}
                        <div 
                            class={`p-2 rounded-lg text-center text-sm ${getLevelColor(tech.level)} transition-all duration-300 ease-out`}
                            class:opacity-0={!isVisible}
                            class:translate-y-2={!isVisible}
                            class:opacity-100={isVisible}
                            class:translate-y-0={isVisible}
                            style={`transition-delay: ${300 + i * 50}ms`}>
                            {tech.name}
                        </div>
                    {/each}
                </div>
            </div>

            <!-- Центральный блок -->
            <div 
                class="p-3 rounded-xl bg-gray-700 border-2 border-white transition-all duration-1000 ease-out delay-450"
                class:opacity-0={!isVisible}
                class:scale-90={!isVisible}
                class:opacity-100={isVisible}
                class:scale-100={isVisible}>
                <div class="text-center">
                    <div class="text-xl font-bold mb-1">Fullstack</div>
                    <div class="text-md">Developer</div>
                </div>
            </div>

            <!-- Databases -->
            <div 
                class={`p-3 rounded-xl ${categoryColors.db} transition-all duration-1000 ease-out delay-600`}
                class:opacity-0={!isVisible}
                class:translate-y-4={!isVisible}
                class:opacity-100={isVisible}
                class:translate-y-0={isVisible}>
                <h3 class="text-lg font-bold mb-3 text-center">{categoryNames.db}</h3>
                <div class="grid grid-cols-2 gap-2">
                    {#each techStack.filter(t => t.category === 'db') as tech, i}
                        <div 
                            class={`p-2 rounded-lg text-center text-sm ${getLevelColor(tech.level)} transition-all duration-300 ease-out`}
                            class:opacity-0={!isVisible}
                            class:translate-y-2={!isVisible}
                            class:opacity-100={isVisible}
                            class:translate-y-0={isVisible}
                            style={`transition-delay: ${600 + i * 50}ms`}>
                            {tech.name}
                        </div>
                    {/each}
                </div>
            </div>

            <!-- DevOps -->
            <div 
                class={`p-3 rounded-xl ${categoryColors.devops} transition-all duration-1000 ease-out delay-750`}
                class:opacity-0={!isVisible}
                class:translate-y-4={!isVisible}
                class:opacity-100={isVisible}
                class:translate-y-0={isVisible}>
                <h3 class="text-lg font-bold mb-3 text-center">{categoryNames.devops}</h3>
                <div class="grid grid-cols-2 gap-2">
                    {#each techStack.filter(t => t.category === 'devops') as tech, i}
                        <div 
                            class={`p-2 rounded-lg text-center text-sm ${getLevelColor(tech.level)} transition-all duration-300 ease-out`}
                            class:opacity-0={!isVisible}
                            class:translate-y-2={!isVisible}
                            class:opacity-100={isVisible}
                            class:translate-y-0={isVisible}
                            style={`transition-delay: ${750 + i * 50}ms`}>
                            {tech.name}
                        </div>
                    {/each}
                </div>
            </div>

            <!-- Other -->
            <div 
                class={`p-3 rounded-xl ${categoryColors.other} transition-all duration-1000 ease-out delay-900`}
                class:opacity-0={!isVisible}
                class:translate-y-4={!isVisible}
                class:opacity-100={isVisible}
                class:translate-y-0={isVisible}>
                <h3 class="text-lg font-bold mb-3 text-center">{categoryNames.other}</h3>
                <div class="grid grid-cols-2 gap-2">
                    {#each techStack.filter(t => t.category === 'other') as tech, i}
                        <div 
                            class={`p-2 rounded-lg text-center text-sm ${getLevelColor(tech.level)} transition-all duration-300 ease-out`}
                            class:opacity-0={!isVisible}
                            class:translate-y-2={!isVisible}
                            class:opacity-100={isVisible}
                            class:translate-y-0={isVisible}
                            style={`transition-delay: ${900 + i * 50}ms`}>
                            {tech.name}
                        </div>
                    {/each}
                </div>
            </div>
        </div>

        <!-- Десктоп версия (скрыта на мобильных) -->
        <div class="hidden md:grid md:grid-cols-5 gap-6">
            <!-- Backend -->
            <div 
                class={`p-4 rounded-xl ${categoryColors.backend} col-span-1 md:col-span-2 transition-all duration-1000 ease-out`}
                class:opacity-0={!isVisible}
                class:translate-x-[-50px]={!isVisible}
                class:opacity-100={isVisible}
                class:translate-x-0={isVisible}>
                <h3 class="text-xl font-bold mb-4 text-center">{categoryNames.backend}</h3>
                <div class="grid grid-cols-2 gap-3">
                    {#each techStack.filter(t => t.category === 'backend') as tech, i}
                        <div 
                            class={`p-3 rounded-lg text-center ${getLevelColor(tech.level)} transition-all duration-300 ease-out`}
                            class:opacity-0={!isVisible}
                            class:translate-y-4={!isVisible}
                            class:opacity-100={isVisible}
                            class:translate-y-0={isVisible}
                            style={`transition-delay: ${150 + i * 50}ms`}>
                            {tech.name}
                        </div>
                    {/each}
                </div>
            </div>

            <!-- Web -->
            <div 
                class={`p-4 rounded-xl ${categoryColors.web} col-span-1 md:col-span-3 transition-all duration-1000 ease-out delay-150`}
                class:opacity-0={!isVisible}
                class:translate-x-[50px]={!isVisible}
                class:opacity-100={isVisible}
                class:translate-x-0={isVisible}>
                <h3 class="text-xl font-bold mb-4 text-center">{categoryNames.web}</h3>
                <div class="grid grid-cols-3 gap-3">
                    {#each techStack.filter(t => t.category === 'web') as tech, i}
                        <div 
                            class={`p-3 rounded-lg text-center ${getLevelColor(tech.level)} transition-all duration-300 ease-out`}
                            class:opacity-0={!isVisible}
                            class:translate-y-4={!isVisible}
                            class:opacity-100={isVisible}
                            class:translate-y-0={isVisible}
                            style={`transition-delay: ${300 + i * 50}ms`}>
                            {tech.name}
                        </div>
                    {/each}
                </div>
            </div>

            <!-- Databases -->
            <div 
                class={`p-4 rounded-xl ${categoryColors.db} col-start-2 transition-all duration-1000 ease-out delay-300`}
                class:opacity-0={!isVisible}
                class:translate-x-[-50px]={!isVisible}
                class:opacity-100={isVisible}
                class:translate-x-0={isVisible}>
                <h3 class="text-xl font-bold mb-4 text-center">{categoryNames.db}</h3>
                <div class="grid grid-cols-1 gap-3">
                    {#each techStack.filter(t => t.category === 'db') as tech, i}
                        <div 
                            class={`p-3 rounded-lg text-center ${getLevelColor(tech.level)} transition-all duration-300 ease-out`}
                            class:opacity-0={!isVisible}
                            class:translate-y-4={!isVisible}
                            class:opacity-100={isVisible}
                            class:translate-y-0={isVisible}
                            style={`transition-delay: ${450 + i * 50}ms`}>
                            {tech.name}
                        </div>
                    {/each}
                </div>
            </div>

            <!-- Центральный блок -->
            <div 
                class="p-4 rounded-xl bg-gray-700 border-2 border-white col-span-1 flex items-center justify-center transition-all duration-1000 ease-out delay-450"
                class:opacity-0={!isVisible}
                class:scale-90={!isVisible}
                class:opacity-100={isVisible}
                class:scale-100={isVisible}>
                <div class="text-center">
                    <div class="text-2xl font-bold mb-2">Fullstack</div>
                    <div class="text-lg">Developer</div>
                </div>
            </div>

            <!-- DevOps -->
            <div 
                class={`p-4 rounded-xl ${categoryColors.devops} col-span-1 transition-all duration-1000 ease-out delay-600`}
                class:opacity-0={!isVisible}
                class:translate-x-[50px]={!isVisible}
                class:opacity-100={isVisible}
                class:translate-x-0={isVisible}>
                <h3 class="text-xl font-bold mb-4 text-center">{categoryNames.devops}</h3>
                <div class="grid grid-cols-1 gap-3">
                    {#each techStack.filter(t => t.category === 'devops') as tech, i}
                        <div 
                            class={`p-3 rounded-lg text-center ${getLevelColor(tech.level)} transition-all duration-300 ease-out`}
                            class:opacity-0={!isVisible}
                            class:translate-y-4={!isVisible}
                            class:opacity-100={isVisible}
                            class:translate-y-0={isVisible}
                            style={`transition-delay: ${600 + i * 50}ms`}>
                            {tech.name}
                        </div>
                    {/each}
                </div>
            </div>

            <!-- Other -->
            <div 
                class={`p-4 rounded-xl ${categoryColors.other} col-span-1 md:col-span-5 transition-all duration-1000 ease-out delay-750`}
                class:opacity-0={!isVisible}
                class:translate-y-[50px]={!isVisible}
                class:opacity-100={isVisible}
                class:translate-y-0={isVisible}>
                <h3 class="text-xl font-bold mb-4 text-center">{categoryNames.other}</h3>
                <div class="grid grid-cols-2 md:grid-cols-2 gap-3">
                    {#each techStack.filter(t => t.category === 'other') as tech, i}
                        <div 
                            class={`p-3 rounded-lg text-center ${getLevelColor(tech.level)} transition-all duration-300 ease-out`}
                            class:opacity-0={!isVisible}
                            class:translate-y-4={!isVisible}
                            class:opacity-100={isVisible}
                            class:translate-y-0={isVisible}
                            style={`transition-delay: ${750 + i * 50}ms`}>
                            {tech.name}
                        </div>
                    {/each}
                </div>
            </div>
        </div>

        <!-- Легенда -->
        <div 
            class="mt-8 md:mt-16 flex flex-wrap justify-center gap-3 md:gap-4 transition-all duration-1000 ease-out"
            class:opacity-0={!isVisible}
            class:translate-y-[20px]={!isVisible}
            class:opacity-100={isVisible}
            class:translate-y-0={isVisible}
            style="transition-delay: 900ms">
            {#each Object.entries(categoryNames) as [category, name]}
                <div class="flex items-center">
                    <div class={`w-3 h-3 md:w-4 md:h-4 rounded-full mr-1 md:mr-2 ${categoryColors[category as TechCategory].split(' ')[0]}`}></div>
                    <span class="text-gray-300 text-xs md:text-sm">{name}</span>
                </div>
            {/each}
        </div>
    </div>
</section>

<style>
    [class*="transition-all"] {
        transition-property: all;
        will-change: transform, opacity;
    }
</style>