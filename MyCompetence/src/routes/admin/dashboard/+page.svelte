<script lang="ts">
    import { onMount } from 'svelte';
    import { goto } from '$app/navigation';

    let adminData: { username: string; email: string } | null = null;
    let error: string | null = null;

    onMount(async () => {
        const token = localStorage.getItem('admin_token');
        if (!token) {
            goto('/admin/login');
            return;
        }

        try {
            const response = await fetch('/admin/me', {
                headers: {
                    'Authorization': `Bearer ${token}`
                }
            });

            if (!response.ok) {
                throw new Error(response.status === 401 ? 'Session expired' : 'Authorization error');
            }

            adminData = await response.json();
        } catch (err) {
            error = err instanceof Error ? err.message : 'Authorization error';
            localStorage.removeItem('admin_token');
            goto('/admin/login');
        }
    });

    const handleLogout = () => {
        localStorage.removeItem('admin_token');
        goto('/admin/login');
    };
</script>

<div class="min-h-screen bg-gray-50 p-4">
    {#if error}
        <div class="p-4 bg-red-100 text-red-700 rounded mb-4">
            {error}
        </div>
    {/if}

    {#if adminData}
        <div class="max-w-4xl mx-auto bg-white rounded-lg shadow-md p-8">
            <div class="flex justify-between items-center mb-6">
                <h1 class="text-2xl font-bold">Admin Dashboard</h1>
                <button
                    on:click={handleLogout}
                    class="bg-red-500 hover:bg-red-600 text-white font-medium py-2 px-4 rounded transition-colors duration-200"
                >
                    Logout
                </button>
            </div>

            <div class="space-y-4">
                <div class="p-4 bg-gray-50 rounded">
                    <h2 class="text-xl font-semibold mb-2">Admin Information</h2>
                    <p><span class="font-medium">Username:</span> {adminData.username}</p>
                    <p><span class="font-medium">Email:</span> {adminData.email}</p>
                </div>
            </div>
        </div>
    {:else}
        <div class="text-center py-8">
            <p>Loading admin data...</p>
        </div>
    {/if}
</div>