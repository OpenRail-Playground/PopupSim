<script setup lang="ts">
import { onMounted, Ref, ref, watch } from 'vue'
import sample_simulation_output from '../../data.json'

var currentStep = 0
var lastLocomotivePosition = 'unknown'  // Default initial position

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

  // Get locomotive track position
  const locomotiveTrack = sample_simulation_output[currentStep].locomotive.position
  let locomotiveX = 340
  let locomotiveY = 270

  switch (locomotiveTrack) {
    case 'kopf':
      locomotiveX = 68
      locomotiveY = 270
      break
    case 'toBeRetrofitted':
      locomotiveX = 633
      locomotiveY = 37
      break
    case 'WorkshopGleis1':
      locomotiveX = 633
      locomotiveY = 270
      break
    case 'WorkshopGleis2':
      locomotiveX = 633
      locomotiveY = 750
      break
    case 'retrofited':
      locomotiveX = 633
      locomotiveY = 289
      break
  }


  // Draw locomotive at the specified position
  drawImage(ctx, 'steam-locomotive.png', locomotiveX, locomotiveY)

  //draw all wagons with appropriate colors
  drawWagons(ctx, sample_simulation_output[currentStep].tracks.toBeRetrofitted, 760, 38, 'blue')
  drawWagons(ctx, sample_simulation_output[currentStep].tracks.retrofitted, 900, 740, 'green')

  // Differentiate between workshop tracks
  sample_simulation_output[currentStep].tracks.workshopGleise.forEach((workshopGleis, workshopIndex) => {
    Object.keys(workshopGleis).forEach((key) => {
      let yPosition = workshopIndex === 0 ? 278 : 503; // Differentiate y-position for WorkshopGleis1 and WorkshopGleis2
      drawWagons(ctx, workshopGleis[key], 760, yPosition, 'yellow')
    })
  })
}

function drawWagons(ctx, wagons, startX, startY, defaultColor) {
  wagons.slice(0, 3).forEach((wagon, index) => {
    const color = wagon.couplerType === 'dac' ? 'green' : defaultColor
    drawColoredRect(ctx, startX + index * 128, startY, color)
    drawImage(ctx, 'vagon.png', startX + index * 128, startY)
  })

  if (wagons.length > 3) {
    drawText(ctx, `+${wagons.length - 3}`, startX + 3 * 128, startY + 60)
  }
}

function drawColoredRect(ctx, x, y, color) {
  ctx.fillStyle = color
  ctx.fillRect(x, y, 128, 128) // Size of the rectangle
}

function drawImage(ctx, image, x, y) {
  var base_image = new Image()
  base_image.src = 'http://localhost:8080/src/assets/rail_icons/' + image
  base_image.onload = function () {
    ctx.drawImage(this, x, y)
  }
}

function drawText(ctx, text, x, y) {
  ctx.fillStyle = 'black'
  ctx.font = '30px Arial'
  ctx.fillText(text, x, y)
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
