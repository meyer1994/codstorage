import { ethers } from 'ethers'
import { Client } from '@xmtp/xmtp-js'
import { shallowReactive } from 'vue'

import { useEthereum } from '@/composables/useEthereum'

const xmtp = shallowReactive({
  xmtp: null,
})

export const useXmtp = async () => {
  const { ethereum, request } = useEthereum()

  const authenticate = async () => {
    await request()
    const provider = new ethers.providers.Web3Provider(ethereum)
    const signer = provider.getSigner()
    xmtp.xmtp = await Client.create(signer)
  }

  return { ...xmtp, authenticate }
}
