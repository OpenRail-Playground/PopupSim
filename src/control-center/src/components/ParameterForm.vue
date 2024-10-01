<script setup lang="ts">
import { computed, reactive } from 'vue'
import AppInput from './AppInput.vue'
import type {Parameters} from "@/utils/api";
import {mapWritableState} from "pinia";
import {useParametersStore} from "@/stores/parameters";

const {parameters} = useParametersStore()

</script>

<template>
  <form>
    <div class="row">
      <div>
        <AppInput
          :title="$t('form.workshop.title')"
          :placeholder="$t('form.workshop.placeholder')"
          id="workshop"
          v-model="parameters.workshop"
        >
          {{ $t('form.workshop.error') }}
        </AppInput>
      </div>
      <div>
        <AppInput
          :title="$t('form.shuntingMovement.title')"
          :placeholder="$t('form.shuntingMovement.placeholder')"
          id="shuntingMovement"
          v-model="parameters.shuntingMovement"
        >
          {{ $t('form.shuntingMovement.error') }}
        </AppInput>
      </div>
      <div>
        <AppInput
          :title="$t('form.movement.title')"
          :placeholder="$t('form.movement.placeholder')"
          id="movement"
          v-model="parameters.movement"
        >
          {{ $t('form.movement.error') }}
        </AppInput>
      </div>
      <div>
        <AppInput
          :title="$t('form.coupling.title')"
          :placeholder="$t('form.coupling.placeholder')"
          id="coupling"
          v-model="parameters.coupling"
        >
          {{ $t('form.coupling.error') }}
        </AppInput>
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
