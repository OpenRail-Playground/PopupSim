import { shallowMount } from '@vue/test-utils'
import { describe, expect, test } from 'vitest'

import QuoteCard from '../QuoteCard.vue'
import type { Quote } from '@/utils/api'
import { createI18n } from 'vue-i18n'

const quote: Quote = {
  id: 1,
  slug: 'quote-1',
  title: 'Quote 1',
  body: 'A great quote.',
  author: 'John Doe',
  notes: 'A short note',
  createdAt: '2023-09-27T09:19:19.042Z',
  updatedAt: '2023-10-12T18:36:03.630Z',
  owner: 'abcdef'
}

describe('QuoteCard', () => {
  test('renders the quote card', () => {
    const i18n = createI18n({ legacy: false })
    const wrapper = shallowMount(QuoteCard, {
      props: { quote },
      global: {
        plugins: [i18n],
        stubs: ['RouterLink']
      }
    })
    expect(wrapper.element).toMatchSnapshot()
  })
})
