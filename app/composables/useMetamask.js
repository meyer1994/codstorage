
export const useMetamask = () => {
  const ethereum = useState('metamask_ethereum', () => null)
  const enabled = computed(() => !!ethereum.value)

  const account = useState('metamask_account', () => null)
  const connected = computed(() => !!account.value)

  onMounted(() => (ethereum.value = window.ethereum))

  const request = opts => ethereum.value.request(opts)

  return { account, ethereum, enabled, connected, request }
}
