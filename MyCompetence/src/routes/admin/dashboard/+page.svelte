<script lang="ts">
    import { onMount } from 'svelte';
    import { goto } from '$app/navigation';
    import AdminPanel from '$lib/pages/AdminPanel.svelte';

    interface AdminData {
        username: string;
        email: string;
    }

    let adminData: AdminData | null = null;
    let error: string | null = null;

    onMount(async () => {
        const token = localStorage.getItem('admin_token');
        if (!token) {
            await goto('/admin/login');
            return;
        }

        try {
            const response = await fetch('http://localhost:8000/admin/me', {
                headers: {
                    'Authorization': `Bearer ${token}`
                }
            });

            if (!response.ok) {
                throw new Error(response.status === 401 ? 'Session expired' : 'Authorization error');
            }

            adminData = await response.json() as AdminData;
        } catch (err) {
            error = err instanceof Error ? err.message : 'Authorization error';
            localStorage.removeItem('admin_token');
            await goto('/admin/login');
        }
    });

    const handleLogout = () => {
        localStorage.removeItem('admin_token');
        goto('/admin/login');
    };
</script>

<div class="admin-page">
    {#if adminData}
        <AdminPanel {adminData} on:logout={handleLogout} />
    {:else if error}
        <p class="error">{error}</p>
    {:else}
        <p>Loading...</p>
    {/if}
</div>