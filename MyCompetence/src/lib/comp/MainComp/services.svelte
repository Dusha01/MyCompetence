<script lang="ts">
    import { fade, fly } from 'svelte/transition';
    
    let form = {
        name: '',
        phone: '',
        email: '',
        subject: '',
        message: ''
    };
    
    let isSubmitting = false;
    let submitSuccess = false;
    let submitError = false;
    
    async function handleSubmit() {
        isSubmitting = true;
        submitSuccess = false;
        submitError = false;
        
        try {
            // Отправка формы (server)
            await new Promise(resolve => setTimeout(resolve, 1000));
            
            form = {
                name: '',
                phone: '',
                email: '',
                subject: '',
                message: ''
            };
            
            submitSuccess = true;
        } catch (error) {
            submitError = true;
        } finally {
            isSubmitting = false;
        }
    }
</script>

<section 
    id="services" 
    class="py-20 px-4 sm:px-6 lg:px-8 bg-gradient-to-b from-gray-900 to-gray-800 text-white"
    in:fade={{ duration: 300 }}>
    
    <div class="max-w-7xl mx-auto">
        <div class="text-center mb-16" in:fly={{ y: 50, duration: 500 }}>
            <h2 class="text-4xl md:text-5xl font-bold mb-4 bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-purple-500">
                Свяжитесь со мной
            </h2>
            <p class="text-xl text-gray-300 max-w-3xl mx-auto">
                Оставьте заявку, и я свяжусь с вами для обсуждения вашего проекта
            </p>
        </div>
        
        <div class="max-w-3xl mx-auto bg-gray-800 rounded-xl border border-gray-700 p-8 md:p-10">
            {#if submitSuccess}
                <div class="mb-8 p-4 rounded-lg bg-green-900/30 border border-green-600 text-green-300" in:fade>
                    <h3 class="font-bold text-lg mb-1">Сообщение отправлено!</h3>
                    <p>Я свяжусь с вами в ближайшее время.</p>
                </div>
            {:else if submitError}
                <div class="mb-8 p-4 rounded-lg bg-red-900/30 border border-red-600 text-red-300" in:fade>
                    <h3 class="font-bold text-lg mb-1">Ошибка отправки</h3>
                    <p>Пожалуйста, попробуйте еще раз или свяжитесь другим способом.</p>
                </div>
            {/if}
            
            <form on:submit|preventDefault={handleSubmit} class="space-y-6">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div>
                        <label for="name" class="block text-sm font-medium text-gray-300 mb-2">Имя</label>
                        <input
                            type="text"
                            id="name"
                            bind:value={form.name}
                            required
                            class="w-full px-4 py-3 rounded-lg bg-gray-700 border border-gray-600 focus:border-blue-500 focus:ring-2 focus:ring-blue-500/50 text-white placeholder-gray-400 transition-all"
                            placeholder="Ваше имя"
                        />
                    </div>
                    
                    <div>
                        <label for="phone" class="block text-sm font-medium text-gray-300 mb-2">Телефон</label>
                        <input
                            type="tel"
                            id="phone"
                            bind:value={form.phone}
                            required
                            class="w-full px-4 py-3 rounded-lg bg-gray-700 border border-gray-600 focus:border-blue-500 focus:ring-2 focus:ring-blue-500/50 text-white placeholder-gray-400 transition-all"
                            placeholder="+7 (___) ___-____"
                        />
                    </div>
                </div>
                
                <div>
                    <label for="email" class="block text-sm font-medium text-gray-300 mb-2">E-mail</label>
                    <input
                        type="email"
                        id="email"
                        bind:value={form.email}
                        required
                        class="w-full px-4 py-3 rounded-lg bg-gray-700 border border-gray-600 focus:border-blue-500 focus:ring-2 focus:ring-blue-500/50 text-white placeholder-gray-400 transition-all"
                        placeholder="your@email.com"
                    />
                </div>
                
                <div>
                    <label for="subject" class="block text-sm font-medium text-gray-300 mb-2">Тема</label>
                    <input
                        type="text"
                        id="subject"
                        bind:value={form.subject}
                        required
                        class="w-full px-4 py-3 rounded-lg bg-gray-700 border border-gray-600 focus:border-blue-500 focus:ring-2 focus:ring-blue-500/50 text-white placeholder-gray-400 transition-all"
                        placeholder="О чем вы хотите поговорить?"
                    />
                </div>
                
                <div>
                    <label for="message" class="block text-sm font-medium text-gray-300 mb-2">Сообщение</label>
                    <textarea
                        id="message"
                        bind:value={form.message}
                        rows="5"
                        class="w-full px-4 py-3 rounded-lg bg-gray-700 border border-gray-600 focus:border-blue-500 focus:ring-2 focus:ring-blue-500/50 text-white placeholder-gray-400 transition-all"
                        placeholder="Опишите ваш проект или задайте вопрос..."
                    ></textarea>
                </div>
                
                <div class="pt-2">
                    <button
                        type="submit"
                        disabled={isSubmitting}
                        class="w-full px-6 py-4 rounded-lg bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-500 hover:to-purple-500 text-white font-medium shadow-lg hover:shadow-blue-500/30 transition-all disabled:opacity-70 disabled:cursor-not-allowed"
                    >
                        {#if isSubmitting}
                            <span class="inline-flex items-center justify-center">
                                <svg class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                                </svg>
                                Отправка...
                            </span>
                        {:else}
                            Отправить сообщение
                        {/if}
                    </button>
                </div>
            </form>
        </div>
    </div>
</section>