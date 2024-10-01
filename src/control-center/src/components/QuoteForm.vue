<script setup lang="ts">
import { computed, reactive } from 'vue'
import { useVuelidate } from '@vuelidate/core'
import { required, maxLength } from '@vuelidate/validators'
import type { CoreQuote } from '@/utils/api'
import AppInput from './AppInput.vue'
import AppTextarea from './AppTextarea.vue'

const props = defineProps<{
  quote?: CoreQuote
}>()

const emit = defineEmits<{
  (e: 'submit', quote: CoreQuote): void
}>()

const maxBodyLength = 5000

const form = reactive<CoreQuote>({
  title: props.quote?.title || '',
  author: props.quote?.author || '',
  body: props.quote?.body || '',
  notes: props.quote?.notes || ''
})
const rules = computed(() => {
  return {
    title: { required, $autoDirty: true },
    author: { required, $autoDirty: true },
    body: { required, $autoDirty: true, maxLength: maxLength(maxBodyLength) }
  }
})
const v$ = useVuelidate(rules, form)

function submitForm() {
  if (!v$.value.$error) {
    emit('submit', form)
  }
}
</script>

<template>
  <form>
    <div class="row">
      <div>
        <AppInput
          :title="$t('form.title.title')"
          :placeholder="$t('form.title.placeholder')"
          id="title"
          v-model="form.title"
          :invalid="v$.title.$error"
        >
          {{ $t('form.title.error') }}
        </AppInput>
      </div>
      <div>
        <AppInput
          :title="$t('form.author.title')"
          :placeholder="$t('form.author.placeholder')"
          id="author"
          v-model="form.author"
          :invalid="v$.author.$error"
        >
          {{ $t('form.author.error') }}
        </AppInput>
      </div>
    </div>

    <AppTextarea
      :title="$t('form.body.title')"
      id="body"
      :max="maxBodyLength"
      v-model="form.body"
      :invalid="v$.body.$error"
    >
      {{ $t('form.body.error') }}
    </AppTextarea>

    <AppTextarea :title="$t('form.notes.title')" id="notes" v-model="form.notes" />

    <div class="btn-group">
      <button
        type="button"
        :disabled="v$.$invalid"
        class="elm-button"
        data-variant="primary"
        data-icon="save"
        @click="submitForm"
      >
        {{ $t('form.save') }}
      </button>
      <RouterLink
        :to="{ name: 'quotes' }"
        class="elm-button"
        data-variant="secondary"
        type="button"
        data-icon="cancel"
      >
        {{ $t('form.cancel') }}
      </RouterLink>
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
