<script setup lang="ts">
import { onMounted, ref } from 'vue'

const env = import.meta.env

onMounted(async () => {
  fetch(`${env.BASE_URL}sample_simulation_output.json`)
    .then((response) => response.text())
    .then((res) => {
      console.log(res) //loaded file from disk
    })
})
</script>

<template>
  hi
</template>

<style lang="scss" scoped>
</style>
