<script setup lang="ts">
import { onMounted, Ref, ref } from 'vue'

// The important part: the name of the variable needs to be equal to the ref's name of the canvas element in the template
const canvasElement: Ref<HTMLCanvasElement | undefined> = ref()
const context: Ref<CanvasRenderingContext2D | undefined> = ref()

const env = import.meta.env

onMounted(() => {
  // Get canvas context. If 'getContext' returns 'null', set to 'undefined', so that it conforms to the Ref typing
  context.value = canvasElement.value?.getContext('2d') || undefined
  render()
})

onMounted(async () => {
  fetch(`${env.BASE_URL}sample_simulation_output.json`)
    .then((response) => response.text())
    .then((res) => {
      console.log(res) //loaded file from disk
    })
})

function render() {
  if (!context.value) {
    return
  }

  var ctx = context.value
  // Define a new path
  ctx.beginPath()

  // Set a start-point
  ctx.moveTo(0, 0)

  // Set an end-point
  ctx.lineTo(200, 100)

  // Stroke it (Do the Drawing)
  ctx.stroke()
}
</script>

<template>
  <canvas ref="canvasElement" width="200" height="200" />
</template>
