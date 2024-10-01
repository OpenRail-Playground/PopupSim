<script setup lang="ts">
import { onMounted, Ref, ref } from 'vue'
import sample_simulation_output from '../../sample_simulation_output.json'
import type { RefSymbol } from '@vue/reactivity'

var currentStep = 0

// The important part: the name of the variable needs to be equal to the ref's name of the canvas element in the template
const canvasElement: Ref<HTMLCanvasElement | undefined> = ref()
const context: Ref<CanvasRenderingContext2D | undefined> = ref()
const slider: Ref = ref()
const stepLabel: Ref = ref()

const env = import.meta.env
var loadedJson = ''

onMounted(() => {
  // Get canvas context. If 'getContext' returns 'null', set to 'undefined', so that it conforms to the Ref typing
  context.value = canvasElement.value?.getContext('2d') || undefined
  slider.value.value
  console.log('slider', slider.value.value)
  render()
})

function render() {
  if (!context.value) {
    return
  }

  console.log('render')

  console.log('currentStep', currentStep)

  slider.value.max = sample_simulation_output.events.length - 1
  currentStep = slider.value.value
  stepLabel.value.innerText = 'Step ' + sample_simulation_output.events[currentStep].timestamp

  var ctx = context.value
  ctx.canvas.width = 1920
  ctx.canvas.height = 1000

  //draw background
  var base_image = new Image()
  base_image.src = 'http://localhost:8080/src/assets/rail_icons/edited.png'
  base_image.onload = function () {
    ctx.drawImage(this, 0, 0)
  }

  //draw locomotive
  switch (sample_simulation_output.events[currentStep].lokomotive.position) {
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
  sample_simulation_output.events[currentStep].retrofitted.forEach((retrofitted, index) => {
    drawImage(ctx, 'vagon.png', 5 + index * 128 + 5, 200)
  })

  sample_simulation_output.events[currentStep].toBeRetrofitted.forEach((retrofitted, index) => {
    drawImage(ctx, 'vagon.png', 5 + index * 128 + 5, 200)
  })

  sample_simulation_output.events[currentStep].workshopGleise.forEach((element) => {
    element.wagons.forEach((wagon, index) => {
      //TODO based on
      drawImage(ctx, 'vagon.png', 5 + index * 128 + 5, 200)
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

function updateSlider() {
  render()
}
</script>

<template>
  <input
    type="range"
    min="1"
    max="100"
    value="0"
    style="width: 500px"
    ref="slider"
    @input="updateSlider"
  />
  <label ref="stepLabel">Step</label>
  <canvas ref="canvasElement" width="1920" height="1080" />
</template>
