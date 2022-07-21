import { computed, onMounted, ref } from 'vue'

export const useMetamask = () => {
  const ethereum = ref(null)
  const enabled = computed(() => !!ethereum.value)

  const account = ref(null)
  const connected = computed(() => !!account.value)

  onMounted(() => (ethereum.value = window.ethereum))

  const request = opts => ethereum.value.request(opts)

  return { account, ethereum, enabled, connected, request }
}
