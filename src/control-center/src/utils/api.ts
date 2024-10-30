import { deleteJson, fetchBackend, getJson, postJson, putJson } from './fetch'

export type PopupSite = {
  name: string
  id: number
  tracks: Track[]
}

export type Track = {
  id: string
  length: number
  function?: Function
}

export type Function = 'workshop' | 'toBeRetrofitted' | 'retrofitted' | 'parking' | 'stationHead'

export type Topology = {
  popupSites: PopupSite[]
}

export type Parameters = {
  workshop: number
  shuntingMovement: number
  movement: number
  coupling: number
  wagonsPerWorkshop: number
}

export type Configuration = {
  popupSite: number
  workshops: string[]
  retrofitted: string[]
  toBeRetrofitted: string[]
  stationHead: string[]
  parking: string[]
  parameters: Parameters
}

export type NewSimulationRequest = {
  configuration: Configuration
  popupSite: PopupSite
}

// Simulation Data

export type Locomotive = {
  lokomotiveId: number
  coupledWith?: Wagon[]
  position: string
}

export type Wagon = {
  wagonId: number
  length: number
  couplerType: string
}

export type WorkshopTrack = {
  [key: string]: Wagon[]
}

export type Tracks = {
  retrofitted: any[]
  toBeRetrofitted: Wagon[]
  workshopGleise: WorkshopTrack[]
}

export type SimulationState = {
  locomotive: Locomotive
  timestamp: number
  tracks: Tracks
  WorkshopGleis1IdleTime: number
  WorkshopGleis2IdleTime: number
  WorkshopGleis1CouplingTime: number
  WorkshopGleis2CouplingTime: number
  locomotiveIdleTime: number
}
