import { defineStore } from 'pinia'
import { computed, ref } from 'vue'
import type { NewSimulationRequest, SimulationState } from '@/utils/api'
import { fetchBackend, postJson } from '@/utils/fetch'

export const useSimulationStore = defineStore('simulation', () => {
  const simulation = ref<SimulationState[]>([])
  const simulationCallOngoing = ref<Boolean>(false)
  async function callSimulation(request: NewSimulationRequest) {
    simulationCallOngoing.value = true
    simulation.value = await postJson(fetchBackend, '/process', request)
  }
  const isSimulationRequested = computed(
    () => simulationCallOngoing.value || simulation.value?.length > 0
  )

  const isSimulationFinished = computed(() => simulation.value?.length > 0)
  return { simulation, callSimulation, isSimulationRequested, isSimulationFinished }
})
