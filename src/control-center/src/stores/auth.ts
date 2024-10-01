import { fetchBackend, getBackendUrl } from '@/utils/fetch'
import { defineStore } from 'pinia'

export type User = {
  sub: string
  email: string
  name: string
}

export type AuthResponse = {
  loggedIn: boolean
  user?: User
  csrfToken?: string
}

type State = {
  error?: Error
  authInfo?: AuthResponse
}

type Getters = {
  userInfo(): User | undefined
  isAuthenticated(): boolean
  token(): string
}

type Actions = {
  login(): void
  logout(): Promise<void>
  checkAuth(): Promise<void>
  clearError(): void
}

export const useAuthStore = defineStore<'auth', State, Getters, Actions>('auth', {
  state: () => ({
    error: undefined,
    authInfo: undefined
  }),
  getters: {
    userInfo() {
      return this.authInfo?.user
    },
    isAuthenticated() {
      return !!this.authInfo?.loggedIn
    },
    token() {
      return this.authInfo?.csrfToken || ''
    }
  },
  actions: {
    async login() {
      // Get the current URL
      const returnURL = encodeURIComponent(window.location.href)

      // Append it to the base URL
      const loginURL = `${getBackendUrl()}/auth/login?returnTo=${returnURL}`

      // Redirect the browser to the login URL
      window.location.href = loginURL
    },
    async checkAuth() {
      const res = await fetchBackend(`/auth/userinfo`)
      if (!res.ok) {
        this.error = new Error(`Unexpected status ${res.status} fetching userinfo`)
      }
      this.authInfo = (await res.json()) as AuthResponse
    },
    async logout() {
      const res = await fetchBackend(`/auth/logout`)
      if (!res.ok) {
        this.error = new Error(`Error logging out: ${res.status} ${res.statusText}`)
      }
      this.authInfo = undefined
    },
    clearError() {
      this.error = undefined
    }
  }
})
