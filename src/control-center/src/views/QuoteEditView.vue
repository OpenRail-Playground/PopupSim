<script setup lang="ts">
import QuoteForm from '@/components/QuoteForm.vue'
import { useQuotesStore } from '@/stores/quotes'
import { getQuote, type Quote, type CoreQuote } from '@/utils/api'
import { onBeforeMount, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()
const { updateQuote } = useQuotesStore()

const quote = ref<Quote>()

onBeforeMount(async () => {
  const slug = route.params?.slug
  quote.value = await getQuote(Array.isArray(slug) ? slug[0] : slug)
})

async function handleQuoteUpdate(updatedQuote: CoreQuote) {
  if (quote.value?.slug) {
    await updateQuote(quote.value?.slug, updatedQuote)
    router.push({ name: 'quotes' })
  }
}
</script>

<template>
  <div class="rea-main">
    <h1 class="elm-headline">{{ $t('updateQuote') }}</h1>
    <QuoteForm v-if="quote" :quote="quote" @submit="handleQuoteUpdate" />
  </div>
</template>
