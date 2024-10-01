import AxeBuilder from '@axe-core/playwright'
import { expect, test } from '@playwright/test'

import { HomePage } from './HomePage'

test.describe('homepage', () => {
  // eslint-disable-next-line playwright/expect-expect
  test('visits the app root url', async ({ page }) => {
    const homePage = new HomePage(page)
    await homePage.goto()
    await expect(homePage.headline).toBeVisible()
  })

  test('should not have any automatically detectable accessibility issues', async ({ page }) => {
    const homePage = new HomePage(page)
    await homePage.goto()

    const accessibilityScanResults = await new AxeBuilder({ page }).analyze()

    expect(accessibilityScanResults.violations).toEqual([])
  })
})
