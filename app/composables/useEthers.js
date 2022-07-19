import { ethers } from 'ethers'

export const useEthers = () => {
  const { enabled, ethereum } = useMetamask()

  if (!enabled)
    return {}

  const provider = new ethers.providers.Web3Provider(ethereum, 'any')
  const signer = provider.getSigner()

  return { provider, signer }
}
