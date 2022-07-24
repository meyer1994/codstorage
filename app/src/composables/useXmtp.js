import { ethers } from 'ethers'
import { Client } from '@xmtp/xmtp-js'

import { useEthereum } from '@/composables/useEthereum'

export const useXmtp = async () => {
  const { ethereum, request } = useEthereum()

  const authenticate = async () => {
    await request()
    const provider = new ethers.providers.Web3Provider(ethereum)
    const signer = provider.getSigner()
    return await Client.create(signer)
  }

  return { authenticate }
}
