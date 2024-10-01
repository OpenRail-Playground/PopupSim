import { createPinia, setActivePinia } from 'pinia'
import { afterEach, beforeEach, describe, expect, test, vi } from 'vitest'

import { useAuthStore } from '../auth'

describe('Counter Store', () => {
  let store: ReturnType<typeof useAuthStore>
  beforeEach(() => {
    // creates a fresh pinia and make it active, so it's automatically picked
    // up by any useStore() call without having to pass it to it:
    // `useStore(pinia)`
    setActivePinia(createPinia())
    store = useAuthStore()
  })

  describe('Getters', () => {
    describe('isAuthenticated', () => {
      test('should return false initially', () => {
        expect(store.isAuthenticated).toBe(false)
      })
      test('should return the authenticated user', () => {
        store.$patch({
          authInfo: {
            loggedIn: true,
            csrfToken: '123abc',
            user: {
              name: 'John Doe',
              email: 'John.Doe@example.org',
              sub: 'GOJd3jIu73BK9iKr1waUzjdmcjavtplah4Fd7P-SRX8s'
            }
          }
        })
        expect(store.isAuthenticated).toBe(true)
      })
    })
  })

  describe('Actions', () => {
    afterEach(() => {
      vi.restoreAllMocks()
    })

    describe('login', () => {
      test('should redirect to the BFF', () => {
        const targetUrl = 'http://foo.bar'
        global.window = Object.create(window)
        Object.defineProperty(window, 'location', {
          value: {
            href: targetUrl
          },
          writable: true
        })
        store.login()
        expect(window.location.href.endsWith('/auth/login?returnTo=http%3A%2F%2Ffoo.bar')).toBe(
          true
        )
      })
    })
    describe.todo('getUser', () => {})
    describe.todo('logout', () => {})
    describe('clearError', () => {
      test('should reset the errors', () => {
        store.$patch({ error: { message: 'my error' } })
        store.clearError()
        expect(store.error).toBeUndefined()
      })
    })
  })
})
