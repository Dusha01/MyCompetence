<script lang="ts">
    export let siteData: {
        enabledComponents: string[];
    };

    const availableComponents = [
        { id: 'skills', name: 'Блок навыков', description: 'Отображает список ваших навыков' },
        { id: 'experience', name: 'Блок опыта', description: 'Отображает ваш профессиональный опыт' },
        { id: 'contactForm', name: 'Форма обратной связи', description: 'Позволяет посетителям связаться с вами' }
    ];

    const toggleComponent = (componentId: string) => {
        if (siteData.enabledComponents.includes(componentId)) {
            siteData.enabledComponents = siteData.enabledComponents.filter(id => id !== componentId);
        } else {
            siteData.enabledComponents = [...siteData.enabledComponents, componentId];
        }
    };
</script>

<div class="components-manager bg-white rounded-lg shadow p-6">
  <h3 class="text-lg font-medium mb-6">Управление компонентами</h3>
  
  <div class="space-y-4">
    {#each availableComponents as component}
      <div class="flex items-start p-4 border rounded-lg">
        <input
          type="checkbox"
          id={component.id}
          class="mt-1 mr-3"
          checked={siteData.enabledComponents.includes(component.id)}
          on:change={() => toggleComponent(component.id)}
        />
        <div class="flex-1">
          <label for={component.id} class="font-medium">{component.name}</label>
          <p class="text-sm text-gray-500">{component.description}</p>
        </div>
        {#if siteData.enabledComponents.includes(component.id)}
          <button 
            class="ml-4 text-sm text-blue-500"
            on:click={() => alert('Настройки компонента ' + component.name)}
          >
            Настроить
          </button>
        {/if}
      </div>
    {/each}
  </div>
</div>