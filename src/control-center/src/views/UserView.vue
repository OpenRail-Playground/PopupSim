<script setup lang="ts">
import { useAuthStore } from '../stores/auth'
import { storeToRefs } from 'pinia'

const auth = useAuthStore()
const { userInfo } = storeToRefs(auth)
</script>

<template>
  <div>
    <h1 class="elm-headline">{{ userInfo?.name }}!</h1>
    <p>{{ $t('loginSuccessText') }}</p>

    <hr />

    <pre><code>{{ userInfo }}</code></pre>
  </div>
</template>
