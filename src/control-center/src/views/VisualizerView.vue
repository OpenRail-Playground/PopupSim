<script setup lang="ts">
import { onMounted, type Ref, ref, watch } from 'vue'
import { useSimulationStore } from '@/stores/simulation'
import { storeToRefs } from 'pinia'

const simulationStore = useSimulationStore()
// this will contain the data. Since the call is async, it could take time, make sure to check the boolean before use
// Maybe use the sample output instead if loading is incomplete?
const { simulation, isSimulationRequested, isSimulationFinished } = storeToRefs(simulationStore)
var currentStep = 0
var lastLocomotivePosition = 'unknown' // Default initial position

// The important part: the name of the variable needs to be equal to the ref's name of the canvas element in the template
const canvasElement: Ref<HTMLCanvasElement | undefined> = ref()
const context: Ref<CanvasRenderingContext2D | undefined> = ref()
const slider: Ref<HTMLInputElement | undefined> = ref()
const timeLabel: Ref = ref()

const wagonColorToBeRetrofitted = 'vagon-blue.png'
const wagonColorRetrofitted = 'vagon-green.png'
const wagonColorInWorkshop = 'vagon-yellow.png'

var loadedJson = ''

const sliderValue = ref(0)
const isPlaying = ref(false)
let playInterval: number | undefined = undefined

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
  var baseImage = new Image()
  baseImage.src = 'rail_icons/edited.png'
  baseImage.onload = function () {
    ctx.drawImage(baseImage, 0, 0)
  }
  //setup slider
  if (!isSimulationFinished.value) {
    console.log('simulation not loaded yet')
    return
  }
  slider.value.max = (simulation.value.length - 1).toString()

  //all images are 128x128

  // Get locomotive track position
  const locomotiveTrack = simulation.value[currentStep].locomotive.position
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
  drawWagons(
    ctx,
    simulation.value[currentStep].tracks.toBeRetrofitted,
    760,
    38,
    wagonColorToBeRetrofitted
  )
  drawWagons(ctx, simulation.value[currentStep].tracks.retrofitted, 900, 740, wagonColorRetrofitted)

  // Differentiate between workshop tracks
  simulation.value[currentStep].tracks.workshopGleise.forEach((workshopGleis, workshopIndex) => {
    Object.keys(workshopGleis).forEach((key) => {
      let yPosition = workshopIndex === 0 ? 278 : 503 // Differentiate y-position for WorkshopGleis1 and WorkshopGleis2
      drawWagons(ctx, workshopGleis[key], 760, yPosition, wagonColorInWorkshop)
    })
  })

  timeLabel.value.innerText = `time: ${simulation.value[currentStep].timestamp}`
}

function drawWagons(ctx, wagons, startX, startY, defaultColor) {
  wagons.slice(0, 3).forEach((wagon, index) => {
    const color = wagon.couplerType === 'dac' ? wagonColorRetrofitted : defaultColor
    // drawColoredRect(ctx, startX + index * 128, startY, color)
    drawImage(ctx, color, startX + index * 128, startY)
  })

  if (wagons.length > 3) {
    drawText(ctx, `+${wagons.length - 3}`, startX + 3 * 128, startY + 60)
  }
}

function drawColoredRect(ctx, x, y, color) {
  ctx.fillStyle = color
  ctx.fillRect(x, y, 128, 128) // Size of the rectangle
}

function drawImage(ctx, name, x, y) {
  const image = new Image()
  image.src = `/rail_icons/${name}`
  image.onload = function () {
    ctx.drawImage(this, x, y)
  }
}

function drawText(ctx, text, x, y) {
  ctx.fillStyle = 'black'
  ctx.font = '30px Arial'
  ctx.fillText(text, x, y)
}

// Function to handle play button click
function togglePlay() {
  isPlaying.value = !isPlaying.value
  if (isPlaying.value) {
    console.log('Playing...')
    playInterval = setInterval(() => {
      if (sliderValue.value < simulation.value.length - 1) {
        sliderValue.value++
      } else {
        clearInterval(playInterval)
        isPlaying.value = false
      }
    }, 1000) // Change the interval as needed
  } else {
    console.log('Paused')
    clearInterval(playInterval)
  }
}
</script>

<template>
  <h4>
    <button @click="togglePlay">{{ isPlaying ? 'Pause' : 'Play' }}</button>
    <input type="range" min="0" v-model="sliderValue" style="width: 500px" ref="slider" />
    <label ref="timeLabel" style="margin-left: 8px">time</label>
  </h4>
  <canvas ref="canvasElement" style="width:90%; height:90%" />
</template>

<style>
button {
  margin-right: 10px;
}
</style>
