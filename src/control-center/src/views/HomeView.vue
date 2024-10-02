<script setup lang="ts">
import { onBeforeMount, ref, toRef } from 'vue'
import { useTopologyStore } from '@/stores/topology'
import TrackConfiguration from '@/components/TrackConfiguration.vue'
import { storeToRefs } from 'pinia'
import ParameterForm from '@/components/ParameterForm.vue'
import type { NewSimulationRequest, Function, Track } from '@/utils/api'
import { useParametersStore } from '@/stores/parameters'
import { useSimulationStore } from '@/stores/simulation'
import router from '@/router'

const ts = useTopologyStore()
const ps = useParametersStore()
const ss = useSimulationStore()
const { popupSite } = storeToRefs(ts)
const { parameters } = storeToRefs(ps)

onBeforeMount(async () => {
  await ts.loadTopology()
})

function loadStaticData() {
  router.push({ path: '/visualizer' })
}

function simulate() {
  function findTracksOfFunction(functionAssignment: Function): string[] {
    return popupSite.value.tracks.filter((t) => t.function === functionAssignment).map((t) => t.id)
  }
  const requestBody: NewSimulationRequest = {
    configuration: {
      popupSite: popupSite.value.id,
      workshops: findTracksOfFunction('workshop'),
      retrofitted: findTracksOfFunction('retrofitted'),
      toBeRetrofitted: findTracksOfFunction('toBeRetrofitted'),
      stationHead: findTracksOfFunction('stationHead'),
      parking: findTracksOfFunction('parking'),
      parameters: parameters.value
    },
    popupSite: ts.popupSite
  }
  ss.callSimulation(requestBody)
  router.push({ path: '/visualizer' })
}
</script>

<template>
  <div>
    <h1 class="elm-headline">
      {{ $t('home') }}
    </h1>
    <h2 class="elm-headline">Popup-Site: {{ popupSite?.name || '' }}</h2>
    <div class="cmp-tab-bar" role="tablist">
      <!-- Pay attention to use a component wide, but component instance specific name to the following input[type="radio"] elements //-->
      <input type="radio" name="cmp-tab-bar-tabs-regular" id="tab_regular_0" checked />
      <label for="tab_regular_0" role="tab">Funktionszuweisung</label>
      <section id="content_regular_0" role="tabpanel">
        <TrackConfiguration />
      </section>
      <input type="radio" name="cmp-tab-bar-tabs-regular" id="tab_regular_1" />
      <label for="tab_regular_1" role="tab">Modellparameter</label>
      <section id="content_regular_1" role="tabpanel">
        <ParameterForm></ParameterForm>
      </section>
    </div>
    <button class="elm-button" data-variant="brand-primary" title="Simulieren" @click="simulate()">
      Simulieren
    </button>
    <button class="elm-button" data-variant="secondary-solid" title="Statische Daten laden" @click="loadStaticData()">
      Statische Daten laden
    </button>
  </div>
</template>

<style lang="scss" scoped>
.cmp-tab-bar {
  width: calc(100vw - 32px - 2rem);
}

.elm-button {
  margin-top: 1rem;
}
</style>
