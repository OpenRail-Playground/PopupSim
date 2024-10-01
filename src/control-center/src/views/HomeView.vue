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
    <h2 class="elm-headline">
      Popup-Site: {{popupSite.name}}
    </h2>
    <div class="cmp-tab-bar" role="tablist">

      <!-- Pay attention to use a component wide, but component instance specific name to the following input[type="radio"] elements //-->
      <input type="radio" name="cmp-tab-bar-tabs-regular" id="tab_regular_0" checked>
      <label for="tab_regular_0" role="tab">Funktionszuweisung</label>
      <section id="content_regular_0" role="tabpanel">
        <TrackConfiguration :tracks="popupSite.tracks"/>
      </section>
      <input type="radio" name="cmp-tab-bar-tabs-regular" id="tab_regular_1">
      <label for="tab_regular_1" role="tab">Modellparameter</label>
      <section id="content_regular_1" role="tabpanel">
        <ParameterForm></ParameterForm>
      </section>
    </div>
    <RouterLink
      to="/visualizer"
      class="elm-button"
      data-variant="brand-primary"
      title="Simulieren"
    >
      Simulieren
    </RouterLink>
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
