import { ref, computed } from 'vue'

const account = ref(null)
const enabled = computed(() => !!window.ethereum)
const ethereum = window.ethereum

export const useEthereum = () => {
  const request = async () => {
    const accounts = await ethereum.request({ method: 'eth_requestAccounts' })
    account.value = accounts[0]
  }
  return { request, account, ethereum, enabled }
}
