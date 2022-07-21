import { computed, ref } from 'vue'

export const useMetamask = () => {
  const accounts = ref([])
  const account = computed(() => accounts.value[0])
  const ethereum = window.ethereum
  const enabled = computed(() => !!window.ethereum)
  const connected = computed(() => !!account.value)

  const request = async () => {
    accounts.value = await ethereum.request({ method: 'eth_requestAccounts' })
  }

  return { account, ethereum, enabled, connected, request }
}
