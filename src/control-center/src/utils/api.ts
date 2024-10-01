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

/** A quote with all the unimportant, non-editable fields removed. */
export type CoreQuote = Omit<Quote, 'id' | 'slug' | 'updatedAt' | 'createdAt' | 'owner'>

export async function getQuote(slug: string): Promise<Quote> {
  return getJson(fetchBackend, `/quotes/${slug}`)
}
export async function getQuotes(): Promise<Quote[]> {
  return getJson(fetchBackend, `/quotes`)
}
export async function createQuote(data: CoreQuote): Promise<Quote> {
  return postJson(fetchBackend, `/quotes`, data)
}
export async function updateQuote(slug: string, data: CoreQuote): Promise<Quote> {
  return putJson(fetchBackend, `/quotes/${slug}`, data)
}
export async function deleteQuote(slug: string): Promise<void> {
  return deleteJson(fetchBackend, `/quotes/${slug}`)
}
