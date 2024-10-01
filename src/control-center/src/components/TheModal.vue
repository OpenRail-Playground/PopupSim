<script setup lang="ts">
import { watch } from 'vue'

const props = withDefaults(
  defineProps<{
    title: string
    show?: boolean
    okLabel?: string
  }>(),
  {
    show: false,
    okLabel: 'OK'
  }
)

const emit = defineEmits<{
  (e: 'ok'): void
  (e: 'close'): void
}>()

watch(
  () => props.show,
  (show) => {
    const dialogEl = document.getElementById('dialog') as HTMLDialogElement
    if (show) {
      dialogEl.showModal()
    } else {
      dialogEl.close()
    }
  }
)
</script>

<template>
  <Teleport to="body">
    <dialog id="dialog" class="cmp-dialog" aria-modal="true" aria-labelledby="dialog-title">
      <header>
        <h2 class="elm-headline" id="dialog-title">{{ title }}</h2>
        <a @click="emit('close')" class="elm-link is-close" title="Close the dialog" href="#"
          >Close</a
        >
      </header>
      <main>
        <slot />
      </main>
      <footer>
        <button
          class="elm-button"
          data-variant="brand-primary"
          title="OK"
          type="button"
          @click="emit('ok')"
        >
          {{ okLabel }}
        </button>
      </footer>
    </dialog>
  </Teleport>
</template>
