import { nextTick } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'

import i18n from '../locales'
import { useAuthStore } from '../stores/auth'
import ErrorView from '../views/ErrorView.vue'
import HelpView from '../views/HelpView.vue'
import HomeView from '../views/HomeView.vue'
import VisualiserView from '../views/VisualiserView.vue'

const baseTitle = `PopUpSim-ControlCenter.js`

const { t } = i18n.global

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
      meta: { i18nKey: 'home' }
    },
    {
      path: '/visualiser',
      name: 'visualiser',
      component: VisualiserView,
      meta: { i18nKey: 'visualiser' }
    },
    {
      path: '/help',
      name: 'help',
      component: HelpView,
      meta: { i18nKey: 'help' }
    },
    {
      path: '/error',
      name: 'error',
      component: ErrorView,
      meta: { i18nKey: 'error' }
    },
    {
      path: '/user',
      name: 'user',
      // route level code-splitting
      // this generates a separate chunk (PageOne.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/UserView.vue'),
      meta: { i18nKey: 'user', requiresAuth: true }
    },
    {
      path: '/demo',
      redirect: { name: 'quotes' },
      meta: { requiresAuth: true },
      children: [
        {
          path: 'quotes',
          name: 'quotes',
          component: () => import('../views/QuotesView.vue'),
          meta: { i18nKey: 'quotes', requiresAuth: true }
        },
        {
          path: 'quotes/show/:slug',
          name: 'quote',
          component: () => import('../views/QuoteView.vue'),
          meta: { i18nKey: 'quote', requiresAuth: true }
        },
        {
          path: 'quotes/create',
          name: 'createQuote',
          component: () => import('../views/QuoteCreateView.vue'),
          meta: { i18nKey: 'createQuote', requiresAuth: true }
        },
        {
          path: 'quotes/edit/:slug',
          name: 'editQuote',
          component: () => import('../views/QuoteEditView.vue'),
          meta: { i18nKey: 'editQuote', requiresAuth: true }
        }
      ]
    }
  ]
})

const getTitle = (i18nKey: string) => `${baseTitle} - ${t(i18nKey)}`

// check authentication for marked routes by using the pinia store
router.beforeEach(async (to, from, next) => {
  if (!to.matched.some((record) => record.meta.requiresAuth)) {
    next()
    return
  }

  const authStore = useAuthStore()
  await authStore.checkAuth()

  if (authStore.isAuthenticated) {
    next()
  } else {
    next({ name: 'error' })
  }
})

// add a hook to set the page title for a better a11y
router.afterEach((to) => {
  // Use next tick to handle router history correctly
  // see: https://github.com/vuejs/vue-router/issues/914#issuecomment-384477609
  nextTick(() => {
    const i18nKey = to.meta?.i18nKey as string | undefined
    document.title = i18nKey ? getTitle(i18nKey) : baseTitle
  })
})

export default router
