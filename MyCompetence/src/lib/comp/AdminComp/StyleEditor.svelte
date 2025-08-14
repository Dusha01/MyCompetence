<script lang="ts">
    export let siteData: {
        style: {
            primaryColor: string;
            secondaryColor: string;
            fontFamily: string;
            backgroundColor: string;
            textColor: string;
        };
    };

    const colorThemes = [
        { name: 'Синий', primary: '#3b82f6', secondary: '#8b5cf6' },
        { name: 'Зеленый', primary: '#10b981', secondary: '#06b6d4' },
        { name: 'Красный', primary: '#ef4444', secondary: '#f97316' },
        { name: 'Фиолетовый', primary: '#7c3aed', secondary: '#ec4899' }
    ];

    const applyTheme = (theme: typeof colorThemes[0]) => {
        siteData.style.primaryColor = theme.primary;
        siteData.style.secondaryColor = theme.secondary;
    };

    const updateFont = (e: Event) => {
        const target = e.target as HTMLSelectElement;
        siteData.style.fontFamily = target.value;
    };
</script>


<div class="style-editor bg-white rounded-lg shadow p-6">
  <h3 class="text-lg font-medium mb-6">Редактор стилей</h3>
  
  <div class="space-y-6">
    <div>
      <h4 class="font-medium mb-3">Цветовая схема</h4>
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-4">
        {#each colorThemes as theme}
          <button
            class="p-3 rounded-lg border hover:border-blue-500 {siteData.style.primaryColor === theme.primary ? 'ring-2 ring-blue-500' : ''}"
            on:click={() => applyTheme(theme)}
          >
            <div class="flex items-center mb-2">
              <div class="w-6 h-6 rounded-full mr-2" style={`background: ${theme.primary}`} />
              <div class="w-6 h-6 rounded-full" style={`background: ${theme.secondary}`} />
            </div>
            <span class="text-sm">{theme.name}</span>
          </button>
        {/each}
      </div>
    </div>
    
    <div>
      <h4 class="font-medium mb-3">Настроить цвета</h4>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div>
          <label class="block text-sm text-gray-500 mb-1">Основной цвет</label>
          <input
            type="color"
            class="w-full h-10"
            bind:value={siteData.style.primaryColor}
          />
          <div class="text-xs text-gray-400 mt-1">{siteData.style.primaryColor}</div>
        </div>
        <div>
          <label class="block text-sm text-gray-500 mb-1">Вторичный цвет</label>
          <input
            type="color"
            class="w-full h-10"
            bind:value={siteData.style.secondaryColor}
          />
          <div class="text-xs text-gray-400 mt-1">{siteData.style.secondaryColor}</div>
        </div>
      </div>
    </div>
    
    <div>
      <h4 class="font-medium mb-3">Шрифт</h4>
      <select
        class="w-full p-2 border rounded"
        on:change={updateFont}
        value={siteData.style.fontFamily}
      >
        <option value="'Inter', sans-serif">Inter (Современный)</option>
        <option value="'Roboto', sans-serif">Roboto (Универсальный)</option>
        <option value="'Open Sans', sans-serif">Open Sans (Читаемый)</option>
        <option value="'Montserrat', sans-serif">Montserrat (Стильный)</option>
      </select>
    </div>
    
    <div>
      <h4 class="font-medium mb-3">Предпросмотр</h4>
      <div 
        class="p-6 rounded-lg border"
        style={`background: ${siteData.style.backgroundColor}; color: ${siteData.style.textColor}; font-family: ${siteData.style.fontFamily}`}
      >
        <h5 style={`color: ${siteData.style.primaryColor}`} class="text-xl font-bold mb-2">Пример заголовка</h5>
        <p class="mb-4">Пример текста для демонстрации выбранных стилей.</p>
        <button 
          class="px-4 py-2 rounded"
          style={`background: ${siteData.style.primaryColor}; color: white`}
        >
          Пример кнопки
        </button>
      </div>
    </div>
  </div>
</div>