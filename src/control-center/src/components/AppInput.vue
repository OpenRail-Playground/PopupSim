<script setup lang="ts">
import { computed } from 'vue'

const props = withDefaults(
  defineProps<{
    modelValue: string
    id: string
    title: string
    placeholder?: string
    invalid?: boolean
  }>(),
  {
    placeholder: '',
    invalid: false
  }
)

const emit = defineEmits<{
  (e: 'update:modelValue', value: string): void
}>()

const value = computed({
  get() {
    return props.modelValue
  },
  set(value: string) {
    emit('update:modelValue', value)
  }
})
</script>

<template>
  <input
    type="text"
    class="elm-input"
    v-model="value"
    :placeholder="placeholder"
    :name="id"
    :id="id"
    :aria-describedby="id + '-hint'"
    :aria-invalid="invalid"
    :aria-labelledby="id + '-label'"
  />
  <label class="elm-label" :for="id" aria-hidden="true" :id="id + '-label'">{{ title }}</label>
  <p v-if="invalid" :id="id + '-hint'" class="description">
    <slot />
  </p>
</template>
