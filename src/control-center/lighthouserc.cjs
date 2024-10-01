/* eslint-disable no-undef */
const inCI = Boolean(process.env.CI)
const baseUrl = inCI ? process.env.DK8S_APPLICATION_URL : 'http://localhost:8080'

module.exports = {
  ci: {
    assert: {
      assertions: {
        'categories:accessibility': [],
        'categories:seo': [],
        'categories:best-practices': []
      }
    },
    collect: {
      url: [`${baseUrl}/`, `${baseUrl}/imprint`, `${baseUrl}/help`],
      settings: {
        preset: 'desktop',
        chromeFlags: '--no-sandbox --ignore-certificate-errors',
        // NOTE: This is an SPA built with Vite.
        // Performance measurements are not as relevant for SPAs as they are for server-side rendered apps exposed
        // to the Internet as the SPA's JavaScript code will always be loaded upfront (which takes some time).
        // We therefore exclude performance from the Lighthouse tests.
        // Remove the 'onlyCategories' section if you want to check all Lighthouse metrics including performance.
        onlyCategories: ['accessibility', 'seo', 'best-practices']
      },
      // When running locally, we want to see results in the browser
      // but only run each test once
      ...(!inCI && {
        headful: true,
        startServerCommand: 'npm run build && npm run preview',
        numberOfRuns: 1
      })
    }
  }
}
