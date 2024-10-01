import { shallowMount } from '@vue/test-utils'
import { describe, expect, test } from 'vitest'

import AppTextarea from '../AppTextarea.vue'

const commonProps = {
  modelValue: 'initial input value',
  id: 'my-input',
  title: 'My Input',
  placeholder: 'please enter some text'
}

describe('AppTextarea', () => {
  test('renders the input field', () => {
    const wrapper = shallowMount(AppTextarea, {
      props: commonProps
    })
    expect(wrapper.element).toMatchSnapshot()
  })

  test('renders an error message', () => {
    const wrapper = shallowMount(AppTextarea, {
      props: {
        ...commonProps,
        invalid: true
      },
      slots: {
        default: 'My error message'
      }
    })
    expect(wrapper.element).toMatchSnapshot()
  })

  test('renders showing a max counter', async () => {
    const wrapper = shallowMount(AppTextarea, {
      props: {
        ...commonProps,
        max: 20
      }
    })
    await wrapper.find('textarea').setValue('my input')
    expect(wrapper.element).toMatchSnapshot()
  })

  test('emits when input changes', async () => {
    const wrapper = shallowMount(AppTextarea, {
      props: commonProps
    })
    await wrapper.find('textarea').setValue('my input')
    expect(wrapper.emitted()['update:modelValue'][0]).toEqual(['my input'])
  })
})
