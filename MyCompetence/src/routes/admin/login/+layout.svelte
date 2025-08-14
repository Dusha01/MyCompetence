<script lang="ts">
    import { onMount } from 'svelte';
    import { goto } from '$app/navigation';

    onMount(() => {
        const token = localStorage.getItem('admin_token');
        if (token) {
            goto('/admin/dashboard');
        }
    });
</script>

<slot />