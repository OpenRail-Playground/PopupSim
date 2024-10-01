import { defineStore } from 'pinia'
import { ref } from 'vue'
import type { Parameters } from '@/utils/api'

export const useParametersStore = defineStore('parameters', () => {
  const parameters = ref<Parameters>({
    workshop: 180,
    shuntingMovement: 8,
    movement: 5,
    coupling: 8,
    wagonsPerWorkshop: 3
  })

  return { parameters }
})
