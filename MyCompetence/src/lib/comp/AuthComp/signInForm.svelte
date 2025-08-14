<script lang="ts">
    import { goto } from "$app/navigation";

    let username: string = "";
    let password: string = "";
    let error: string | null = null;
    let isLoading: boolean = false;

    const handleSubmit = async (e: Event) => {
        e.preventDefault();
        isLoading = true;
        error = null;

        try {
            const response = await fetch('http://localhost:8000/admin/token',{
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: new URLSearchParams({
                    username,
                    password,
                    grant_type: 'password'
                })
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'Authentication failed');
            }

            const { access_token } = await response.json();
            localStorage.setItem('admin_token', access_token);
            await goto('/admin/dashboard');
        } catch (err) {
            error = err instanceof Error ? err.message : 'Authentication failed';
        } finally {
            isLoading = false;
        }
    }
</script>

<form
    on:submit={handleSubmit}
    class="bg-white p-8 rounded-lg shadow-md w-full max-w-md"
>
    <h2 class="text-2xl font-bold mb-6 text-gray-800 text-center">Admin Login</h2>

    {#if error}
        <div class="mb-4 p-2 bg-red-100 text-red-700 rounded text-sm">
            {error}
        </div>
    {/if}

    <div class="mb-4">
        <label for="username" class="block text-gray-700 text-sm font-bold mb-2">Username</label>
        <input
            type="text"
            id="username"
            bind:value={username}
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            placeholder="Enter username"
            required
            autocomplete="username"
        />
    </div>

    <div class="mb-6">
        <label for="password" class="block text-gray-700 text-sm font-bold mb-2">Password</label>
        <input
            type="password"
            id="password"
            bind:value={password}
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            placeholder="Enter password"
            required
            autocomplete="current-password"
        />
    </div>

    <div class="flex items-center justify-between">
        <button
            type="submit"
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline w-full transition-colors duration-200"
            disabled={isLoading}
        >
            {#if isLoading}
                Signing in...
            {:else}
                Sign In
            {/if}
        </button>
    </div>
</form>