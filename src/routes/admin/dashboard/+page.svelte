<script lang="ts">
    import { onMount } from 'svelte';
    import { goto } from '$app/navigation';
    import { authStore } from '$lib/comp/AuthComp/auth';
    import AdminPanel from '$lib/pages/AdminPanel.svelte';
    import { browser } from '$app/environment';

    onMount(async () => {
        if (!browser) return;

        if (!$authStore.isAuthenticated) {
            await goto('/admin/login');
            return;
        }

        try {
            const response = await fetch('http://localhost:8000/admin/me', {
                headers: {
                    'Authorization': `Bearer ${$authStore.token}`
                }
            });

            if (!response.ok) {
                throw new Error(response.status === 401 ? 'Session expired' : 'Authorization error');
            }

            const data = await response.json();
            authStore.update(state => ({
                ...state,
                adminData: data,
                error: null
            }));
        } catch (err) {
            const errorMessage = err instanceof Error ? err.message : 'Authorization error';
            authStore.update(state => ({
                ...state,
                error: errorMessage,
                isAuthenticated: false,
                token: null
            }));
            if (browser) {
                sessionStorage.removeItem('admin_token');
                await goto('/admin/login');
            }
        }
    });

    const handleLogout = () => {
        if (browser) {
            authStore.update(state => ({
                ...state,
                isAuthenticated: false,
                token: null,
                adminData: null,
                error: null
            }));
            sessionStorage.removeItem('admin_token');
            goto('/admin/login');
        }
    };
</script>

<div class="admin-page">
    <AdminPanel/>
</div>