// See here how to use Page object models:
// https://playwright.dev/docs/pom
import type { Locator, Page } from '@playwright/test'

export class HomePage {
  readonly page: Page
  readonly headline: Locator

  constructor(page: Page) {
    this.page = page
    this.headline = page.locator('h1', {
      hasText: 'Willkommen bei der PopUpSim-ControlCenter.js'
    })
  }

  async goto() {
    await this.page.goto('/')
  }
}
