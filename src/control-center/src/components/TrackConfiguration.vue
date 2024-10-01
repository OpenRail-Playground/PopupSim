<script setup lang="ts">
import {computed, reactive} from 'vue'
import type {CoreQuote, PopupSite} from '@/utils/api'

const props = defineProps<{
  tracks: Track[]
}>()


const form = reactive<CoreQuote>({
  title: props.quote?.title || '',
  author: props.quote?.author || '',
  body: props.quote?.body || '',
  notes: props.quote?.notes || ''
})


function submitForm() {
  emit('submit', form)
}
</script>

<template>
  <form>
    <div class="row" v-for="track of tracks" :key="track.id">
      <div class="rea-grid">
        <div><p> {{ track.id }} ({{track.length}} Meter)
        </p></div>
        <div>
          <select class="elm-select " name="select" id="select">
            <option></option>
            <option value="workshops">Workshop</option>
            <option value="toBeRetrofitted">To be retrofitted</option>
            <option value="retrofitted">retrofitted</option>
            <option value="parking">parking</option>
            <option value="stationHead">station Head</option>
          </select>
        </div>
      </div>
    </div>
  </form>
</template>

<style lang="scss" scoped>
form .row {
  margin-top: 0.5rem;
  display: flex;
  gap: 0.5rem;

  > div {
    flex-grow: 1;
    width: 100%;
  }
}
</style>
