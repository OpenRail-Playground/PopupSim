<script setup lang="ts">
import { onMounted, Ref, ref } from 'vue'
import sample_simulation_output from '../../sample_simulation_output.json'

// The important part: the name of the variable needs to be equal to the ref's name of the canvas element in the template
const canvasElement: Ref<HTMLCanvasElement | undefined> = ref()
const context: Ref<CanvasRenderingContext2D | undefined> = ref()

const env = import.meta.env
var loadedJson = ''

onMounted(() => {
  // Get canvas context. If 'getContext' returns 'null', set to 'undefined', so that it conforms to the Ref typing
  context.value = canvasElement.value?.getContext('2d') || undefined
  render()
})

function render() {
  if (!context.value) {
    return
  }
  console.log('render')

  var ctx = context.value
  ctx.canvas.width = window.innerWidth
  ctx.canvas.height = window.innerHeight

  ctx.fillStyle = '#f3f4ff'
  ctx.fillRect(0, 0, canvasElement.value!.width, canvasElement.value!.height)

  var base_image = new Image()
  base_image.src = 'http://localhost:8080/src/assets/rail_icons/edited.svg'
  base_image.onload = function () {
    ctx.drawImage(base_image, 0, 0)
  }
}
</script>

<template>
  <canvas ref="canvasElement" width="1920" height="1080" />
</template>
