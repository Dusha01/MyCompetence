<script lang="ts">
    import { onMount } from "svelte";
    import type { SiteData } from "$lib/comp/AdminComp/types"

    import {
        AdminHeader,
        ContentEditor,
        ComponentsManager,
        StyleEditor,
    } from '$lib';

    
    export let adminData: { username: string; email: string };

    let currentTab = 'content';
    let siteData: SiteData = {
        enabledComponents: [],
        about: {
            title: '',
            description: '',
            skills: []
        },
        experience: {},
        header: {},
        footer: {},
        style: {
            primaryColor: '#3b82f6',
            secondaryColor: '#8b5cf6',
            fontFamily: "'Inter', sans-serif",
            backgroundColor: '#ffffff',
            textColor: '#333333'
        }
    };

    let isLoading = true;
    let error: string | null = null;

    onMount(async () => {
        try {
            const token = localStorage.getItem('admin_token');
            if (!token) {
                window.location.href = '/login';
                console.log('тут')
                return;
            }

            const response = await fetch('http://localhost:8000/admin/api/site-data', {
                headers: {
                    'Authorization': `Bearer ${token}`
                }
            });
            
            if (response.status === 401) {
                window.location.href = '/login';
                return;
            }

            if (!response.ok) throw new Error('Ошибка загрузки данных');
            
            const data = await response.json();
            siteData = { ...siteData, ...data };
            isLoading = false;
        } catch (err) {
            error = err instanceof Error ? err.message : 'Неизвестная ошибка';
            console.error('Ошибка:', err);
        }
    });

    const saveChanges = async () => {
        try {
            const token = localStorage.getItem('admin_token');
            const response = await fetch('http://localhost:8000/admin/api/site-data', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`
                },
                body: JSON.stringify(siteData),
            });

            if (response.status === 401) {
                window.location.href = '/login';
                return;
            }

            if (!response.ok) throw new Error(await response.text());
            
            alert('Изменения успешно сохранены');
        } catch (err) {
            error = err instanceof Error ? err.message : 'Ошибка сохранения';
            alert(error);
        }
    };
</script>

<div class="admin-panel bg-gray-100 min-h-screen">
    <!--<AdminHeader on:save={saveChanges} username={adminData.username} />-->
    
    <div class="flex">
        <main class="flex-1 p-6">
            {#if error}
                <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
                    {error}
                </div>
            {/if}
            
            {#if isLoading}
                <div class="text-center py-20">Загрузка данных...</div>
            {:else}
                {#if currentTab === 'content'}
                    <ContentEditor bind:siteData />
                {:else if currentTab === 'components'}
                    <ComponentsManager bind:siteData />
                {:else if currentTab === 'style'}
                    <StyleEditor bind:siteData />
                {/if}
            {/if}
        </main>
    </div>
</div>

<style>
    .admin-panel {
        --sidebar-width: 250px;
    }
</style>