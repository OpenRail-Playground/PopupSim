import { defineStore } from 'pinia'
import { computed, ref } from 'vue'
import type { PopupSite, Topology } from '@/utils/api'
import { parse } from 'yaml'

export const useTopologyStore = defineStore('topology', () => {
  const topology = ref<Topology>()
  const popupSite = ref<PopupSite>()

  const getPopupSite = computed(() => (id: number) => {
    return topology.value.popupSites.find((popupSite) => popupSite.id === id)
  })

  const getDefaultPopupSite = computed(() => () => {
    return getPopupSite.value(1)
  })

  async function loadTopology() {
    if (!topology.value) {
      const fileContent = await fetch(`${import.meta.env.BASE_URL}topology.yaml`)
      topology.value = parse(await fileContent.text())
      popupSite.value = topology.value.popupSites[0]
    }
  }

  return { popupSite, getPopupSite, getDefaultPopupSite, loadTopology, topology }
})
