import { deleteJson, fetchBackend, getJson, postJson, putJson } from './fetch'


export type PopupSite = {
  name: string
  id: number
  tracks: Track[]
}

export type Track = {
  id: string,
  length: number,
  function?: Function
}

export type Function = 'workshop' | 'toBeRetrofitted' | 'retrofitted' | 'parking' | 'stationHead'

export type Topology = {
  popupSites: PopupSite[]
}

export type Parameters = {
  workshop: number,
  shuntingMovement: number,
  movement: number,
  coupling: number,
}

export type Configuration = {
  popupSite: number,
  workshops: string[],
  retrofitted: string[],
  toBeRetrofitted: string[],
  stationHead: string[],
  parking: string[],
  parameters: Parameters
}

export type NewSimulationRequest = {
  configuration: Configuration,
  popupSite: PopupSite
}
