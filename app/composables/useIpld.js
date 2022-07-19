
export const useIpld = (ipld, options) => {
  const path = () => `/ipld/${ipld()}`
  return useApi(path, options)
}
