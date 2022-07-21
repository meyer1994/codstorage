import { Client } from '@xmtp/xmtp-js'
import { Web3Provider } from 'ethers'

import { useMetamask } from '@/composables/useMetamask'

export const useXmtp = async () => {
  const { ethereum } = useMetamask()
  const provider = new Web3Provider(ethereum)
  const signer = provider.getSigner()
  return await Client.create(signer)
}
