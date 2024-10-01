<script setup lang="ts">
import QuoteCard from '@/components/QuoteCard.vue'
import { useQuotesStore } from '@/stores/quotes'
import { onBeforeMount } from 'vue'

const qs = useQuotesStore()

onBeforeMount(() => {
  qs.getQuotes()
})
</script>

<template>
  <main class="rea-main" role="main">
    <h1 class="elm-headline">{{ $t('onlyForLoggedInUsers') }}</h1>

    <div class="rea-grid">
      <div v-for="quote of qs.quotes" :key="quote.slug">
        <QuoteCard :quote="quote" />
      </div>
    </div>

    <RouterLink
      to="/demo/quotes/create"
      class="elm-button"
      data-variant="primary"
      type="button"
      data-icon="add"
    >
      {{ $t('createQuote') }}
    </RouterLink>
  </main>
</template>
