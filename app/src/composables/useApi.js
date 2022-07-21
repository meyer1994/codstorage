import { createFetch } from '@vueuse/core'

const client = createFetch({
  baseUrl: 'https://codstorage.herokuapp.com/',
  fetchOptions: {
    mode: 'cors',
  },
})

export const useApi = (...args) => client(...args).json()
