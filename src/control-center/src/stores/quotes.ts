import {
  type CoreQuote,
  type Quote,
  getQuotes as apiGetQuotes,
  createQuote as apiCreateQuote,
  updateQuote as apiUpdateQuote,
  deleteQuote as apiDeleteQuote
} from '@/utils/api'
import { defineStore } from 'pinia'
import { computed, ref } from 'vue'

export const useQuotesStore = defineStore('quotes', () => {
  const error = ref<Error>()
  const quotes = ref<Quote[]>([])

  const getQuote = computed(() => (slug: string) => {
    return quotes.value.find((q) => q.slug === slug)
  })

  async function getQuotes() {
    apiGetQuotes()
      .then((res) => {
        quotes.value = res
      })
      .catch((err) => {
        error.value = err
      })
  }
  async function createQuote(data: CoreQuote) {
    apiCreateQuote(data)
      .then((res: Quote) => {
        quotes.value = [...quotes.value, res]
      })
      .catch((err) => {
        error.value = err
      })
  }
  async function updateQuote(slug: string, data: CoreQuote) {
    apiUpdateQuote(slug, data)
      .then((res: Quote) => {
        quotes.value = [...quotes.value.filter((q) => q.slug !== slug), res]
      })
      .catch((err) => {
        error.value = err
      })
  }
  async function deleteQuote(slug: string) {
    apiDeleteQuote(slug)
      .then(() => {
        quotes.value = quotes.value.filter((q) => q.slug !== slug)
      })
      .catch((err) => {
        error.value = err
      })
  }

  return { quotes, getQuote, getQuotes, createQuote, updateQuote, deleteQuote }
})
