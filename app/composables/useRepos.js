
export const useRepos = async () => {
  console.log('nice')
  return await useFetch('http://localhost:8000/repos', {
    default: () => []
  })
}
