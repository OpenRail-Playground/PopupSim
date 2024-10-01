<script setup lang="ts">
import { toRef } from 'vue'
import { useAuthStore } from '../stores/auth'

const authStore = useAuthStore()
const isAuthenticated = toRef(authStore, 'isAuthenticated')
</script>

<template>
  <div>
    <h1 class="elm-headline">
      {{ $t('welcome') }}
    </h1>
    <RouterLink
      to="/user"
      class="elm-button"
      data-variant="brand-primary"
      :title="$t('help')"
    >
      {{ $t('user') }}
    </RouterLink>
  </div>
</template>
