<script setup lang="ts">
import { onMounted, Ref, ref } from 'vue'
import sample_simulation_output from '../../sample_simulation_output.json'

// The important part: the name of the variable needs to be equal to the ref's name of the canvas element in the template
const canvasElement: Ref<HTMLCanvasElement | undefined> = ref()
const context: Ref<CanvasRenderingContext2D | undefined> = ref()

const env = import.meta.env
var loadedJson = ''

onMounted(() => {
  fetch(`sample_simulation_output.json`)
    .then((response) => response.text())
    .then((res) => {
      loadedJson = res
      console.log(sample_simulation_output)
    })

  // Get canvas context. If 'getContext' returns 'null', set to 'undefined', so that it conforms to the Ref typing
  context.value = canvasElement.value?.getContext('2d') || undefined
  render()
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

  ctx.roundRect(35, 10, 225, 110, 20) //or .fill() for a filled rect
}
</script>

<template>
  <canvas ref="canvasElement" width="200" height="200" />
</template>
