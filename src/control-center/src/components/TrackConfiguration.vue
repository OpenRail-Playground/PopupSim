<script setup lang="ts">
import {useTopologyStore} from "@/stores/topology";

const {popupSite} = useTopologyStore()

</script>

<template>
  <form>
    <div class="row" v-for="track of popupSite.tracks" :key="track.id">
      <div class="rea-grid" id="tracklist">
        <div class="track"><p><strong>{{ track.id }}</strong>
        </p></div>
        <div class="length"><p>{{ track.length }} Meter</p></div>
        <div>
          <select class="elm-select function" :name="track.id+'select'" :id="track.id+'select'"
                  v-model="track.function">
            <option></option>
            <option value="workshop">Werkstatt</option>
            <option value="toBeRetrofitted">umzubauende Wagen</option>
            <option value="retrofitted">umgebaute Wagen</option>
            <option value="parking">parken</option>
            <option value="stationHead">Bahnhofskopf</option>
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
