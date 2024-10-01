import { describe, test, expect } from 'vitest'
import { createI18n } from 'vue-i18n'
import { mount } from '@vue/test-utils'

import TheFooter from '../TheFooter.vue'

describe('TheFooter', () => {
  test('renders properly', () => {
    const i18n = createI18n({})
    const wrapper = mount(TheFooter, {
      global: {
        plugins: [i18n]
      }
    })
    expect(wrapper.element).toMatchSnapshot()
  })
})
