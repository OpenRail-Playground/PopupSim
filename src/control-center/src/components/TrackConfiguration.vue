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
      <div class="rea-grid" id="tracklist">
        <div class="track"><p><strong>{{ track.id }}</strong>
        </p></div>
        <div class="length"><p>{{ track.length }} Meter</p></div>
        <div>
          <select class="elm-select function" :name="track.id+'select'" :id="track.id+'select'">
            <option></option>
            <option value="workshops">Workshop</option>
            <option value="toBeRetrofitted">To be retrofitted</option>
            <option value="retrofitted">retrofitted</option>
            <option value="parking">parking</option>
            <option value="stationHead">station Head</option>
          </select>
          <label class="elm-label" for="select">{{ $t('function') }}</label>

        </div>
      </div>
    </div>
  </form>
</template>

<style lang="scss" scoped>
form .row {
  display: flex;

  > div {
    flex-grow: 1;
    width: 100%;
  }
}

#tracklist {
  display: grid;
  grid-template-columns: 1fr 1fr 2fr 2fr;
  line-height: 1;
}

.function {
  min-width: 200px;
}

.track {
  min-width: 100px;
}

.length {
  white-space: nowrap;
}
</style>
