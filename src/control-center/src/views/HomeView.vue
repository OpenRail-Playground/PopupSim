<script setup lang="ts">
import {onBeforeMount, ref, toRef} from 'vue'
import {useTopologyStore} from "@/stores/topology";
import TrackConfiguration from "@/components/TrackConfiguration.vue";
import {storeToRefs} from "pinia";
import ParameterForm from "@/components/ParameterForm.vue";
import type {PopupSite} from "@/utils/api";

const ts = useTopologyStore()
const {topology} = storeToRefs(ts)
const popupSite = ref<PopupSite>()

onBeforeMount(async () => {
  await ts.loadTopology()
  setTimeout(() => {
    popupSite.value = topology.value.popupSites[0]
  }, 1)
})
</script>

<template>
  <div>
    <h1 class="elm-headline">
      {{ $t('home') }}
    </h1>
    <TrackConfiguration v-if="popupSite" :tracks="popupSite.tracks"/>
    <ParameterForm></ParameterForm>
    <RouterLink
      to="/simulation"
      class="elm-button"
      data-variant="brand-primary"
      title="Starte Simulation"
    >
      Starte Simulation
    </RouterLink>
  </div>
</template>
