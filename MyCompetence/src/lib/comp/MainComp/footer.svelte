<script lang="ts">
    import { fade } from 'svelte/transition';
    
    const socialLinks = [
        { name: 'GitHub', icon: 'github', url: 'https://github.com/Dusha01' },
        { name: 'Telegram', icon: 'send', url: 'https://t.me/Haunted_sss' },
        { name: 'LinkedIn', icon: 'linkedin', url: '#' },
        { name: 'Email', icon: 'mail', url: 'Ia12Kotik@yandex.ru' }
    ];
    
    const navLinks = [
        { name: 'Проекты', href: '#projects' },
        { name: 'Услуги', href: '#services' },
        { name: 'Обо мне', href: '#about' },
    ];
</script>

<footer 
    class="bg-gray-900 border-t border-gray-800 text-gray-300"
    in:fade={{ duration: 500 }}>
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-10">
            <div class="space-y-4">
                <div class="flex items-center">
                    <span class="text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-purple-500">
                        Andrew Gubchenko
                    </span>
                </div>
                <p class="text-gray-400">
                    Разработка индивидуальных решений и автоматизация процессов для вашего бизнеса.
                </p>
                <div class="flex space-x-4">
                    {#each socialLinks as link}
                        <a 
                            href={link.url} 
                            target="_blank" 
                            rel="noopener noreferrer"
                            class="text-gray-400 hover:text-blue-400 transition-colors duration-300"
                            aria-label={link.name}>
                            {#if link.icon === 'github'}
                                <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                                    <path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd" />
                                </svg>
                            {:else if link.icon === 'send'}
                                <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
                                    <path d="M2.003 2L2 22l20 1.997V2H2.003zM18 12l-7-6v5H6v2h5v5l7-6z"/>
                                </svg>
                            {:else if link.icon === 'linkedin'}
                                <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                                    <path fill-rule="evenodd" d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z" clip-rule="evenodd" />
                                </svg>
                            {:else if link.icon === 'mail'}
                                <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
                                    <path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/>
                                </svg>
                            {/if}
                        </a>
                    {/each}
                </div>
            </div>

            <div>
                <h3 class="text-lg font-semibold text-white mb-4">Навигация</h3>
                <ul class="space-y-3">
                    {#each navLinks as link}
                        <li>
                            <a 
                                href={link.href} 
                                class="text-gray-400 hover:text-blue-400 transition-colors duration-300">
                                {link.name}
                            </a>
                        </li>
                    {/each}
                </ul>
            </div>

            <div>
                <h3 class="text-lg font-semibold text-white mb-4">Контакты</h3>
                <ul class="space-y-3">
                    <li class="flex items-start">
                        <svg class="w-5 h-5 mr-3 mt-0.5" viewBox="0 0 48 48" fill="currentColor">
                            <path fill="#29b6f6" d="M24 4A20 20 0 1 0 24 44A20 20 0 1 0 24 4Z"></path>
                            <path fill="#fff" d="M33.95,15l-3.746,19.126c0,0-0.161,0.874-1.245,0.874c-0.576,0-0.873-0.274-0.873-0.274l-8.114-6.733 l-3.97-2.001l-5.095-1.355c0,0-0.907-0.262-0.907-1.012c0-0.625,0.933-0.923,0.933-0.923l21.316-8.468 c-0.001-0.001,0.651-0.235,1.126-0.234C33.667,14,34,14.125,34,14.5C34,14.75,33.95,15,33.95,15z"></path>
                            <path fill="#b0bec5" d="M23,30.505l-3.426,3.374c0,0-0.149,0.115-0.348,0.12c-0.069,0.002-0.143-0.009-0.219-0.043 l0.964-5.965L23,30.505z"></path>
                            <path fill="#cfd8dc" d="M29.897,18.196c-0.169-0.22-0.481-0.26-0.701-0.093L16,26c0,0,2.106,5.892,2.427,6.912 c0.322,1.021,0.58,1.045,0.58,1.045l0.964-5.965l9.832-9.096C30.023,18.729,30.064,18.416,29.897,18.196z"></path>
                        </svg>
                        <span>https://t.me/Haunted_sss</span>
                    </li>
                    <li class="flex items-start">
                        <svg class="w-5 h-5 mr-3 text-blue-400 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                        </svg>
                        <span>Ia12Kotik@yandex.ru</span>
                    </li>
                    <li class="flex items-start">
                        <svg class="w-5 h-5 mr-3 text-blue-400 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                        </svg>
                        <span>Хабаровск, Россия</span>
                    </li>
                </ul>
            </div>
        </div>

        <div class="mt-12 pt-8 border-t border-gray-800 text-center text-gray-500 text-sm">
            <p>© {new Date().getFullYear()} Andrew. Все права защищены.</p>
        </div>
    </div>
</footer>