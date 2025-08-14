<script lang="ts">
    export let siteData: {
        about: {
            title: string;
            description: string;
            skills: Array<{
                id: number;
                title: string;
                description: string;
                icon: string;
                tags: string[];
            }>;
        };
        experience: any;
        header: any;
        footer: any;
        [key: string]: any;
    };

    let activeSection: string = 'about';
    let editingField: string | null = null;

    const sections: Record<string, string> = {
        about: 'О себе',
        experience: 'Опыт',
        header: 'Шапка',
        footer: 'Подвал'
    };

    const updateField = (section: string, field: string, value: string) => {
        siteData[section][field] = value;
        editingField = null;
    };
</script>

<div class="content-editor">
    <div class="flex mb-6 border-b border-gray-200">
        {#each Object.entries(sections) as [key, name]}
        <button
            class="px-4 py-2 font-medium {activeSection === key ? 'text-blue-600 border-b-2 border-blue-600' : 'text-gray-500 hover:text-gray-700'}"
            on:click={() => activeSection = key}
        >
            {name}
        </button>
        {/each}
    </div>

  {#if activeSection === 'about'}
    <div class="bg-white rounded-lg shadow p-6">
      <h3 class="text-lg font-medium mb-4">Секция "О себе"</h3>
      
      <div class="space-y-4">
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Заголовок</label>
          {#if editingField === 'about.title'}
            <input
              type="text"
              class="w-full p-2 border rounded"
              bind:value={siteData.about.title}
              on:blur={() => editingField = null}
            />
          {:else}
            <div 
              class="p-2 border border-transparent hover:border-gray-300 rounded cursor-text"
              on:click={() => editingField = 'about.title'}
            >
              {siteData.about.title}
            </div>
          {/if}
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Описание</label>
          {#if editingField === 'about.description'}
            <textarea
              class="w-full p-2 border rounded"
              bind:value={siteData.about.description}
              on:blur={() => editingField = null}
              rows="3"
            />
          {:else}
            <div 
              class="p-2 border border-transparent hover:border-gray-300 rounded cursor-text"
              on:click={() => editingField = 'about.description'}
            >
              {siteData.about.description}
            </div>
          {/if}
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Навыки</label>
          <div class="space-y-3">
            {#each siteData.about.skills as skill, i}
              <div class="border rounded-lg p-4">
                <div class="flex justify-between items-start">
                  <h4 class="font-medium">Навык #{i + 1}</h4>
                  <button 
                    class="text-red-500 text-sm"
                    on:click={() => siteData.about.skills.splice(i, 1)}
                  >
                    Удалить
                  </button>
                </div>
                
                <div class="mt-2 space-y-2">
                  <div class="flex items-center">
                    <span class="w-24 text-sm text-gray-500">Название:</span>
                    <input
                      type="text"
                      class="flex-1 p-1 border rounded"
                      bind:value={skill.title}
                    />
                  </div>
                  <div class="flex items-start">
                    <span class="w-24 text-sm text-gray-500">Описание:</span>
                    <textarea
                      class="flex-1 p-1 border rounded"
                      bind:value={skill.description}
                      rows="2"
                    />
                  </div>
                  <div class="flex items-center">
                    <span class="w-24 text-sm text-gray-500">Иконка:</span>
                    <input
                      type="text"
                      class="flex-1 p-1 border rounded"
                      bind:value={skill.icon}
                    />
                  </div>
                  <div class="flex items-start">
                    <span class="w-24 text-sm text-gray-500">Теги:</span>
                    <div class="flex-1">
                      {#each skill.tags as tag, j}
                        <div class="flex mb-1">
                          <input
                            type="text"
                            class="flex-1 p-1 border rounded"
                            bind:value={skill.tags[j]}
                          />
                          <button 
                            class="ml-2 text-red-500 text-sm"
                            on:click={() => skill.tags.splice(j, 1)}
                          >
                            ×
                          </button>
                        </div>
                      {/each}
                      <button 
                        class="mt-1 text-sm text-blue-500"
                        on:click={() => skill.tags.push('Новый тег')}
                      >
                        + Добавить тег
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            {/each}
            
            <button
              class="mt-2 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
              on:click={() => siteData.about.skills.push({
                id: Date.now(),
                title: 'Новый навык',
                description: 'Описание нового навыка',
                icon: '⭐',
                tags: ['Тег']
              })}
            >
              Добавить навык
            </button>
          </div>
        </div>
      </div>
    </div>
  {:else if activeSection === 'experience'}
    <!-- Аналогичный редактор для секции опыта -->
    <div class="bg-white rounded-lg shadow p-6">
      <h3 class="text-lg font-medium mb-4">Секция "Опыт работы"</h3>
      <!-- Реализация аналогична секции "О себе" -->
    </div>
  {/if}
</div>