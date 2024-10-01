<script setup lang="ts">
import { onMounted, Ref, ref, watch } from 'vue'
import sample_simulation_output from '../../data.json'

var currentStep = 0

// The important part: the name of the variable needs to be equal to the ref's name of the canvas element in the template
const canvasElement: Ref<HTMLCanvasElement | undefined> = ref()
const context: Ref<CanvasRenderingContext2D | undefined> = ref()
const slider: Ref<HTMLInputElement | undefined> = ref()

const env = import.meta.env
var loadedJson = ''

const sliderValue = ref(0)

onMounted(() => {
  // Get canvas context. If 'getContext' returns 'null', set to 'undefined', so that it conforms to the Ref typing
  context.value = canvasElement.value?.getContext('2d') || undefined
  render()
})

// Watch the slider value and update the current step
watch(sliderValue, (newValue) => {
  currentStep = newValue
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
  switch (sample_simulation_output[currentStep].locomotive.position) {
    case 'kopf':
      drawImage(ctx, 'steam-locomotive.png', 68, 270)
      break
    case 'toBeRetrofitted':
      drawImage(ctx, 'steam-locomotive.png', 633, 40)
      break
    case 'WorkshopGleis1':
      drawImage(ctx, 'steam-locomotive.png', 693, 533)
      break
    case 'WorkshopGleis2':
      drawImage(ctx, 'steam-locomotive.png', 790, 750)
      break
    case 'retrofited':
      drawImage(ctx, 'steam-locomotive.png', 515, 289)
      break
  }

  //draw all wagons
  sample_simulation_output[currentStep].tracks.toBeRetrofitted.forEach((toBeRetrofitted, index) => {
    drawImage(ctx, 'vagon.png', 5 + index * 128 + 754, 38)
  })

  sample_simulation_output[currentStep].tracks.retrofitted.forEach((retrofitted, index) => {
    drawImage(ctx, 'vagon.png', 5 + index * 128 + 900, 740)
  })



 // Differentiate between workshop tracks
 sample_simulation_output[currentStep].tracks.workshopGleise.forEach((workshopGleis, workshopIndex) => {
    Object.keys(workshopGleis).forEach((key) => {
      workshopGleis[key].forEach((wagon, wagonIndex) => {
        let yPosition = workshopIndex === 0 ? 278 : 503; // Differentiate y-position for WorkshopGleis1 and WorkshopGleis2
        drawImage(ctx, 'vagon.png', 5 + wagonIndex * 128 + 540, yPosition)
      })
    })
  })
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
  <input 
    type="range" 
    min="0" 
    :max="sample_simulation_output.length - 1" 
    v-model="sliderValue" 
    style="width: 500px" 
    ref="slider" 
  />
  <canvas ref="canvasElement" width="1920" height="1080" />
</template>
