import { deleteJson, fetchBackend, getJson, postJson, putJson } from './fetch'

/**
 * A quote by an author.
 */
export type PopupSite = {
  name: string
  id: number
  tracks: Track[]
}

export type Track = {
  id: string,
  length: number
}

export type Topology = {
  popupSites: PopupSite[]
}

export type Parameters = {
  workshop: number,
  shuntingMovement: number,
  movement: number,
  coupling: number,
}
