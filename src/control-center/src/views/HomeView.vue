<script setup lang="ts">
import {onBeforeMount, ref, toRef} from 'vue'
import {useTopologyStore} from "@/stores/topology";
import TrackConfiguration from "@/components/TrackConfiguration.vue";
import {storeToRefs} from "pinia";

const ts = useTopologyStore()
const { topology } = storeToRefs(ts)

onBeforeMount(async () => {
  await ts.loadTopology()
})
</script>

<template>
  <div>
    <h1 class="elm-headline">
      Neue Simulation konfigurieren
    </h1>
    <TrackConfiguration v-if="topology" :tracks="topology.popupSites[0].tracks" />
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
