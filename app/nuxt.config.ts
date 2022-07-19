import { defineNuxtConfig } from 'nuxt'

export default defineNuxtConfig({
  ssr: false,
  modules: [
    '@vueuse/nuxt',
    '@nuxtjs/tailwindcss',
  ],
  vite: {
    target: [
      'es2020'
    ]
  }
})
