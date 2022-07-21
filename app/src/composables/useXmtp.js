import { Client } from '@xmtp/xmtp-js'
import { ethers } from 'ethers'

import { useMetamask } from '@/composables/useMetamask'

export const useXmtp = async () => {
  const { ethereum, request } = useMetamask()
  const provider = new ethers.providers.Web3Provider(ethereum)
  request()
  const signer = provider.getSigner()
  return await Client.create(signer, {
    waitForPeersTimeoutMs: 20000  // 20 seconds
  })
}
