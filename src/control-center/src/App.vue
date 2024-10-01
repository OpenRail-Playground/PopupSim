<script setup lang="ts">
import { RouterView } from 'vue-router'
import TheHeader from '@/components/TheHeader.vue'
import TheFooter from '@/components/TheFooter.vue'
import { onMounted } from 'vue'
import { useAuthStore } from './stores/auth'

onMounted(() => {
  const auth = useAuthStore()
  auth.checkAuth()
})
</script>

<template>
  <div class="main">
    <TheHeader />
    <main class="rea-main" role="main">
      <RouterView />
    </main>
    <TheFooter />
  </div>
</template>

<style lang="scss" scoped>
.main {
  height: 100vh;
  display: grid;
  grid-template:
    'header' auto
    'main' 1fr
    'footer' auto;
}

header {
  grid-area: header;
}

main {
  grid-area: main;
}

footer {
  grid-area: footer;
}
</style>
