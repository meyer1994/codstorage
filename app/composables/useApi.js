
const options = {
  baseURL: 'https://codstorage.herokuapp.com',
  onRequest: async ({ request, options }) => console.log(request, options),
}

export const useApi = path => useFetch(path, { key: path(), ...options })
