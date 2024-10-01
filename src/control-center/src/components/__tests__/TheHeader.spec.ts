import { createTestingPinia } from '@pinia/testing'
import { shallowMount } from '@vue/test-utils'
import { describe, expect, test, vi } from 'vitest'
import { createI18n } from 'vue-i18n'

import TheHeader from '../TheHeader.vue'

describe('TheHeader', () => {
  test('renders properly', () => {
    const i18n = createI18n({ legacy: false })
    const wrapper = shallowMount(TheHeader, {
      global: {
        plugins: [
          i18n,
          createTestingPinia({
            createSpy: vi.fn,
            initialState: {
              auth: { user: {} }
            }
          })
        ],
        stubs: {
          RouterLink: {}
        }
      }
    })

    expect(wrapper.text()).toContain('PopUpSim-ControlCenter.js')
  })
})
