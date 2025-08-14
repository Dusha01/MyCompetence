<script lang="ts">
    import { onMount } from 'svelte';
    import { goto } from '$app/navigation';
    import { authStore, initializeAuth } from '$lib/comp/AuthComp/auth';

    import { browser } from '$app/environment';

    initializeAuth();

    if (browser) {
        initializeAuth();
    }

    onMount(() => {
        const unsubscribe = authStore.subscribe((store) => {
            if (!store.isAuthenticated && browser) {
                goto('/admin/login');
            }
        });

        return () => unsubscribe();
    });
</script>

<slot />