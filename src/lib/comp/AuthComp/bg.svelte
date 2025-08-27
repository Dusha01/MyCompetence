<script lang="ts">
    //Скрипт заднего фона
</script>

<div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-50 to-indigo-100 p-4">
    <slot />
</div>

<style>
    div {
        background-size: cover;
        background-position: center;
    }
</style>