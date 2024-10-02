<script setup lang="ts">
import { onMounted, ref } from 'vue'
let licensesTxt = ref<string>()

onMounted(async () => {
  fetch(`${import.meta.env.BASE_URL}/dependencies.txt`)
    .then((response) => response.text())
    .then((res) => {
      licensesTxt.value = res
    })
})
</script>

<template>
  <div>
    <h1 class="elm-headline">
      {{ $t('imprint') }}
    </h1>

    <address>Firmenname AG Straße PLZ, Stadt</address>

    <p>
      {{ $t('contact') }}:<br />
      some@deutschebahn.com
    </p>

    <p>
      Sitz der Gesellschaft: Frankfurt am Main<br />
      Registergericht: Frankfurt am Main, HRB ????<br />
      USt-IdNr.: DE ???????<br />
      Vorstand: Name, Name, Name
      <br />
      Vorsitzender des Aufsichtsrates: Name
    </p>

    <p>Stand [15.05.2019]</p>

    <hr />

    <h2>{{ $t('technicalInformation') }}</h2>
    <p>{{ $t('version') }} 1.1.0</p>

    <!-- <ul>
      <li v-for="(value, key) in env" :key="key">{{ key }}: {{ value }}</li>
    </ul> -->

    <hr />

    <h2>{{ $t('3rdParty') }}</h2>
    <div class="ws-pre">
      {{ licensesTxt }}
    </div>
  </div>
</template>

<style lang="scss" scoped>
.ws-pre {
  white-space: pre;
}
</style>
