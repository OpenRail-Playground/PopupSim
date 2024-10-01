import { createI18n } from 'vue-i18n'

/*
 * The i18n resources in the path specified in the `@intlify/vite-plugin-vue-i18n` plugins
 * `include` option can be read as vue-i18n optimized locale messages using the import syntax
 */
import en from './en.yml'
import de from './de.yml'

export default createI18n({
  locale: 'de',
  legacy: false,
  messages: {
    en,
    de
  }
})
