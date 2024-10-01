import { defineStore } from 'pinia'
import { computed, ref } from 'vue'
import type {Topology} from "@/utils/api";

export const useTopologyStore = defineStore('topology', () => {
  const error = ref<Error>()
  const topology = ref<Topology[]>([])

  const getPopupSite = computed(() => (id: number) => {
    return topology.value.find((popupSite) => popupSite.id === id)
  })

  const getDefaultPopupSite = computed(() => () => {
    return getPopupSite(1);
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
