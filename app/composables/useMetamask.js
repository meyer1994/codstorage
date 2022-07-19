
export const useMetamask = () => {
  const account = useState('metamask_account', () => null)
  const connected = computed(() => !!account.value)
  const ethereum = window.ethereum
  const enabled = typeof ethereum !== 'undefined'
  return { account, ethereum, enabled, connected }
}
