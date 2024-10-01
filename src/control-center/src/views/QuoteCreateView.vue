<script setup lang="ts">
import QuoteForm from '@/components/QuoteForm.vue'
import { useQuotesStore } from '@/stores/quotes'
import type { CoreQuote } from '@/utils/api'
import { useRouter } from 'vue-router'

const router = useRouter()
const { createQuote } = useQuotesStore()

async function handleQuoteCreate(quote: CoreQuote) {
  await createQuote(quote)
  router.push({ name: 'quotes' })
}
</script>

<template>
  <div class="rea-main">
    <h1 class="elm-headline">{{ $t('createQuote') }}</h1>
    <QuoteForm @submit="handleQuoteCreate" />
  </div>
</template>
