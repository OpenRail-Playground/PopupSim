<script setup lang="ts">
import { computed, ref } from 'vue'

const props = withDefaults(
  defineProps<{
    modelValue: string
    id: string
    title: string
    placeholder?: string
    invalid?: boolean
    max?: number
  }>(),
  {
    placeholder: '',
    invalid: false
  }
)

const output = ref('')

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

function inputChange(event: Event) {
  const value = (event.target as HTMLInputElement).value
  console.log(value)
  output.value = props.max ? `${value.length}/${props.max}` : `${value.length}`
}
</script>

<template>
  <label class="elm-label" :for="id" aria-hidden="true" :id="id + '-label'">{{ title }}</label>
  <textarea
    class="elm-textarea"
    v-model="value"
    :maxlength="max"
    :placeholder="placeholder"
    :name="id"
    :id="id"
    :aria-describedby="id + '-hint'"
    :aria-invalid="invalid"
    :aria-labelledby="id + '-label'"
    @input="inputChange"
  />
  <output for="body" id="result_body">{{ output }}</output>
  <p v-if="invalid" :id="id + '-hint'" class="description">
    <slot />
  </p>
</template>

<style lang="scss" scoped>
.elm-label:has(+ textarea) {
  margin-top: 0.5rem;
  margin-bottom: 0.2rem;
  display: block;
}

textarea + output,
textarea ~ .description {
  margin-top: 0;
}
</style>
