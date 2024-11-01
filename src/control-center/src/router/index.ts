import { nextTick } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'

import i18n from '../locales'
import ErrorView from '../views/ErrorView.vue'
import HelpView from '../views/HelpView.vue'
import HomeView from '../views/HomeView.vue'
import VisualizerView from '../views/VisualizerView.vue'

const baseTitle = `PopUpSim - Control Center`

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
      path: '/visualizer',
      name: 'visualizer',
      component: VisualizerView,
      meta: { i18nKey: 'visualizer' }
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
    }
  ]
})

const getTitle = (i18nKey: string) => `${baseTitle} - ${t(i18nKey)}`

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
