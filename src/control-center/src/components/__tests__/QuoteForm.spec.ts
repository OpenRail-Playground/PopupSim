import { mount, shallowMount } from '@vue/test-utils'
import { describe, expect, test } from 'vitest'

import QuoteForm from '../QuoteForm.vue'
import type { CoreQuote } from '@/utils/api'
import { createI18n } from 'vue-i18n'

const quote: CoreQuote = {
  title: 'Quote 1',
  body: 'A great quote.',
  author: 'John Doe',
  notes: 'A short note'
}

describe('QuoteForm', () => {
  function createComponent(quote?: CoreQuote, mount = shallowMount) {
    const i18n = createI18n({ legacy: false })
    return mount(QuoteForm, {
      props: { quote },
      global: {
        plugins: [i18n],
        stubs: ['RouterLink']
      }
    })
  }

  test('renders the quote form', () => {
    const wrapper = createComponent(quote)
    expect(wrapper.element).toMatchSnapshot()
  })

  test('creates an empty form with disabled submit button when no quote is passed', () => {
    const wrapper = createComponent()
    expect((wrapper.find('button[data-icon="save"]').element as HTMLInputElement).disabled).toEqual(
      true
    )
  })

  test('creates a form with pre-filled data from quote passed as prop', () => {
    const wrapper = createComponent(quote, mount)
    expect((wrapper.find('input[id="title"]').element as HTMLInputElement).value).toEqual(
      quote.title
    )
    expect((wrapper.find('input[id="author"]').element as HTMLInputElement).value).toEqual(
      quote.author
    )
    expect((wrapper.find('textarea[id="body"]').element as HTMLInputElement).value).toEqual(
      quote.body
    )
    expect((wrapper.find('textarea[id="notes"]').element as HTMLInputElement).value).toEqual(
      quote.notes
    )
  })

  test('emits the form data when submitting the form', async () => {
    const wrapper = createComponent(quote)
    await wrapper.find('button[data-icon="save"]').trigger('click')
    expect(wrapper.emitted().submit[0]).toEqual([quote])
  })
})
