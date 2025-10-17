<script setup lang="ts">
import { ref } from 'vue';
const count = ref(0);
</script>

<template>
  <div>{{ count }}</div>

  <button @click="() => { count += 1 }"
    class="select-none px-3 py-2 bg-blue-500 text-white rounded hover:bg-red-600 transition duration-200 ease-in-out">
    button
  </button>
</template>
