<script setup lang="ts">
import { computed, reactive } from 'vue'
import AppInput from './AppInput.vue'
import type { Parameters } from '@/utils/api'
import { mapWritableState } from 'pinia'
import { useParametersStore } from '@/stores/parameters'

const { parameters } = useParametersStore()
</script>

<template>
  <form>
    <div>
      <AppInput :title="$t('form.workshop.title')" id="workshop" v-model="parameters.workshop">
        {{ $t('form.workshop.error') }}
      </AppInput>
    </div>
    <div>
      <AppInput
        :title="$t('form.shuntingMovement.title')"
        id="shuntingMovement"
        v-model="parameters.shuntingMovement"
      >
        {{ $t('form.shuntingMovement.error') }}
      </AppInput>
    </div>
    <div>
      <AppInput :title="$t('form.movement.title')" id="movement" v-model="parameters.movement">
        {{ $t('form.movement.error') }}
      </AppInput>
    </div>
    <div>
      <AppInput :title="$t('form.coupling.title')" id="coupling" v-model="parameters.coupling">
        {{ $t('form.coupling.error') }}
      </AppInput>
    </div>
    <div>
      <AppInput
        :title="$t('form.wagonsPerWorkshop.title')"
        id="wagonsPerWorkshop"
        v-model="parameters.wagonsPerWorkshop"
      >
        {{ $t('form.wagonsPerWorkshop.error') }}
      </AppInput>
    </div>
  </form>
</template>

<style lang="scss" scoped>
form {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-column-gap: 1rem;
  grid-row-gap: 1rem;
  > div {
  }
}
</style>
