import { defineStore } from 'pinia'
import { computed, ref } from 'vue'
import type {Parameters, Topology} from "@/utils/api";
import topologyFile from '../assets/topology.yaml?url'
import {parse} from "yaml";

export const useParametersStore = defineStore('parameters', () => {
  const parameters = ref<Parameters>({
    workshop: 180,
    shuntingMovement: 8,
    movement: 5,
    coupling: 8
  })

  return { parameters }
})
