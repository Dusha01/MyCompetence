<script lang="ts">
    import { defaultHeaderConfig, type HeaderConfig, type defaultStyles } from './HeaderConfig';
    import HeaderPreview from './HeaderPreview.svelte';
    import { loadHeaderConfig, saveHeaderConfig } from './HeaderService';
    import { onMount } from 'svelte';

    let config = $state<HeaderConfig>({ ...defaultHeaderConfig });
    let isLoading = $state(true);
    let isSaving = $state(false);
    let saveSuccess = $state(false);

    onMount(async () => {
        const savedConfig = await loadHeaderConfig();
        config = { ...savedConfig };
        isLoading = false;
    });

    function addTitle() {
        config.titles = [...config.titles, "Новый заголовок"];
    }

    function removeTitle(index: number) {
        config.titles = config.titles.filter((_, i) => i !== index);
    }

    async function handleSave() {
        isSaving = true;
        saveSuccess = await saveHeaderConfig(config);
        isSaving = false;
        
        if (saveSuccess) {
        setTimeout(() => saveSuccess = false, 3000);
        }
    }

    function resetStyles() {
        config.styles = { ...defaultStyles };
    }
</script>

<div class="grid grid-cols-1 lg:grid-cols-2 gap-8 p-6">
  <!-- Editor Column -->
  <div class="space-y-6">
    <div class="flex justify-between items-center mb-6">
      <h2 class="text-2xl font-bold">Header Editor</h2>
      <div class="flex space-x-2">
        <button 
          on:click={resetStyles}
          class="px-4 py-2 bg-gray-200 text-gray-800 rounded-md hover:bg-gray-300 transition">
          Reset Styles
        </button>
        <button 
          on:click={handleSave}
          disabled={isSaving}
          class="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 disabled:bg-blue-400 transition">
          {isSaving ? 'Saving...' : 'Save Changes'}
        </button>
      </div>
    </div>

    {#if saveSuccess}
      <div class="p-3 bg-green-100 text-green-800 rounded-md mb-4">
        Changes saved successfully!
      </div>
    {/if}

    {#if isLoading}
      <div class="flex justify-center items-center h-64">
        <div class="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500"></div>
      </div>
    {:else}
      <div class="space-y-6">
        <!-- Content Section -->
        <div class="bg-white p-4 rounded-lg shadow">
          <h3 class="text-lg font-semibold mb-4">Content</h3>
          
          <div class="space-y-4">
            <label class="block">
              <span class="text-gray-700">Profile Image URL</span>
              <input type="text" bind:value={config.imageUrl} 
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-200">
            </label>

            <label class="block">
              <span class="text-gray-700">Your Name</span>
              <input type="text" bind:value={config.name} 
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-200">
            </label>

            <div class="space-y-2">
              <span class="text-gray-700">Animated Titles</span>
              {#each config.titles as title, i}
                <div class="flex space-x-2 items-center">
                  <input type="text" bind:value={config.titles[i]} 
                    class="flex-1 rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-200">
                  <button on:click={() => removeTitle(i)} 
                    class="px-3 py-1 bg-red-500 text-white rounded-md hover:bg-red-600 transition">
                    ×
                  </button>
                </div>
              {/each}
              <button on:click={addTitle} 
                class="mt-2 px-4 py-1 bg-blue-500 text-white rounded-md hover:bg-blue-600 transition">
                Add Title
              </button>
            </div>

            <label class="block">
              <span class="text-gray-700">Static Title</span>
              <input type="text" bind:value={config.staticTitle} 
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-200">
            </label>
          </div>
        </div>

        <!-- Styles Section -->
        <div class="bg-white p-4 rounded-lg shadow">
          <h3 class="text-lg font-semibold mb-4">Styles</h3>
          
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <label class="block">
              <span class="text-gray-700">Background</span>
              <select bind:value={config.styles.background} 
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-200">
                <option value="bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900">Dark Gradient</option>
                <option value="bg-gray-800">Solid Dark</option>
                <option value="bg-white">White</option>
                <option value="bg-gradient-to-r from-blue-900 to-purple-900">Blue-Purple Gradient</option>
              </select>
            </label>

            <label class="block">
              <span class="text-gray-700">Text Color</span>
              <select bind:value={config.styles.textColor} 
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-200">
                <option value="text-white">White</option>
                <option value="text-gray-900">Dark</option>
                <option value="text-blue-600">Blue</option>
              </select>
            </label>

            <label class="block">
              <span class="text-gray-700">Border Color</span>
              <select bind:value={config.styles.borderColor} 
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-200">
                <option value="border-indigo-500/30">Indigo</option>
                <option value="border-blue-500/30">Blue</option>
                <option value="border-purple-500/30">Purple</option>
                <option value="border-white/30">White</option>
              </select>
            </label>

            <label class="block">
              <span class="text-gray-700">Name Gradient From</span>
              <select bind:value={config.styles.gradientFrom} 
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-200">
                <option value="from-blue-400">Blue 400</option>
                <option value="from-purple-400">Purple 400</option>
                <option value="from-indigo-400">Indigo 400</option>
                <option value="from-pink-400">Pink 400</option>
              </select>
            </label>

            <label class="block">
              <span class="text-gray-700">Name Gradient To</span>
              <select bind:value={config.styles.gradientTo} 
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-200">
                <option value="to-purple-500">Purple 500</option>
                <option value="to-blue-500">Blue 500</option>
                <option value="to-indigo-600">Indigo 600</option>
                <option value="to-pink-500">Pink 500</option>
              </select>
            </label>
          </div>
        </div>
      </div>
    {/if}
  </div>

  <!-- Preview Column -->
  <div class="sticky top-4 h-fit">
    <div class="bg-white p-4 rounded-lg shadow">
      <h3 class="text-lg font-semibold mb-4">Live Preview</h3>
      <div class="border rounded-lg overflow-hidden">
        <HeaderPreview {config} />
      </div>
    </div>
  </div>
</div>