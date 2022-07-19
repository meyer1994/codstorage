import { $fetch } from 'ohmyfetch'

const baseURL = 'http://localhost:8000'
const onRequest = ({ request, options }) => console.log(request, options.params)
const client = $fetch.create({ baseURL, onRequest })

export const useApi = async (path, options) => {
  return await client(path, options)
}
