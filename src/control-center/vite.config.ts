import { fileURLToPath, URL } from 'node:url'
import path from 'path'
import { defineConfig } from 'vite'
import vueDevTools from 'vite-plugin-vue-devtools'
import VueI18nPlugin from '@intlify/unplugin-vue-i18n/vite'
import vue from '@vitejs/plugin-vue'
import license from 'rollup-plugin-license'

// https://vitejs.dev/config/
export default defineConfig({
  server: {
    port: 8080
  },
  plugins: [
    vue(),
    vueDevTools(),
    VueI18nPlugin({
      defaultSFCLang: 'yml',
      include: [path.resolve(__dirname, './src/locales/*.yml')]
      //globalSFCScope: true,
    }),
    // docs: https://www.npmjs.com/package/rollup-plugin-license
    license({
      sourcemap: true,
      thirdParty: {
        output: {
          file: path.join(__dirname, 'dist', 'dependencies.txt')
        },
        allow: {
          // allowlist / denylist can be setup here
          // return false for violations
          test: (dependency) => {
            return (
              !!dependency.license &&
              (dependency.name === 'pop-up-sim-cc' ||
                ['MIT', 'Apache-2.0', 'ISC'].includes(dependency.license))
            )
          },
          failOnUnlicensed: true, // Fail if a dependency does not specify any licenses, default is `false`
          failOnViolation: true // Fail if a dependency specify a license that does not match given requirement, default is `false`
        }
      }
    })
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
