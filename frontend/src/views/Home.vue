<script setup lang="ts">
import { ref } from 'vue';
const count = ref(0);
</script>

<template>
  <div class="h-screen bg-[#f6f7f9]">
    <div class="flex justify-center p-10 select-none">
      <div class="text-center rounded-md bg-[#ff00ff] text-white w-[2rem]">
        {{ count }}
      </div>
    </div>
    <div class="flex gap-1 justify-center">
      <div v-for="_ in Array(10)" @click="count += 1"
        class="px-2 py-2 bg-blue-500 text-center text-white hover:bg-blue-600 select-none rounded-md transition duration-300 ease-in-out w-15 h-10 ">
        {{ count }} </div>
    </div>
  </div>
</template>

