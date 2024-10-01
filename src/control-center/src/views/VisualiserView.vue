<script setup lang="ts">
import { onMounted, Ref, ref } from 'vue'
import sample_simulation_output from '../../sample_simulation_output.json'

var currentStep = 0

// The important part: the name of the variable needs to be equal to the ref's name of the canvas element in the template
const canvasElement: Ref<HTMLCanvasElement | undefined> = ref()
const context: Ref<CanvasRenderingContext2D | undefined> = ref()
const slider: Ref<CanvasRenderingContext2D | undefined> = ref()

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
  ctx.canvas.width = 1920
  ctx.canvas.height = 1000

  ctx.fillStyle = '#f3f4ff'
  ctx.fillRect(0, 0, canvasElement.value!.width, canvasElement.value!.height)

  //draw background
  var base_image = new Image()
  base_image.src = 'http://localhost:8080/src/assets/rail_icons/edited.png'
  base_image.onload = function () {
    ctx.drawImage(this, 0, 0)
  }

  //setup slider

  //all images are 128x128

  //draw locomotive
  switch (sample_simulation_output.events[0].lokomotive.position) {
    case 'retrofitted':
      drawImage(ctx, 'steam-locomotive.png', 633, 60)
      break
    case 'toBeRetrofitted':
      drawImage(ctx, 'steam-locomotive.png', 515, 289)
      break
    case 'WorkshopGleis1':
      drawImage(ctx, 'steam-locomotive.png', 693, 533)
      break
    case 'WorkshopGleis2':
      drawImage(ctx, 'steam-locomotive.png', 790, 750)
      break
  }
  //draw all vagons
  drawImage(ctx, 'vagon.png', 5, 200)
  drawImage(ctx, 'vagon.png', 5, 300)
  drawImage(ctx, 'vagon.png', 5, 400)
}

function drawImage(ctx, image, x, y) {
  var base_image = new Image()
  base_image.src = 'http://localhost:8080/src/assets/rail_icons/' + image
  base_image.onload = function () {
    ctx.drawImage(this, x, y)
  }
}
</script>

<template>
  <input type="range" min="1" max="100" value="50" style="width: 500px" ref="slider" />
  <canvas ref="canvasElement" width="1920" height="1080" />
</template>
