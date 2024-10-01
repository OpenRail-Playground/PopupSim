import { defineStore } from 'pinia'
import { computed, ref } from 'vue'
import type {Topology} from "@/utils/api";
import topologyFile from '../assets/topology.yaml?url'
import {parse} from "yaml";

export const useTopologyStore = defineStore('topology', () => {
  const error = ref<Error>()
  const topology = ref<Topology[]>([])

  const getPopupSite = computed(() => (id: number) => {
    return topology.value.popupSites.find((popupSite) => popupSite.id === id)
  })

  const getDefaultPopupSite = computed(() => () => {
    return getPopupSite.value(1)
  })

  async function loadTopology() {
    const fileContent = await fetch(topologyFile)
    topology.value = parse(await fileContent.text())
  }

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

  return { getPopupSite, getDefaultPopupSite, loadTopology, topology  }
})
