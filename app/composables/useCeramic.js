import { EthereumAuthProvider, SelfID } from '@self.id/web'

export const useCeramic = () => {
  const { ethereum } = useMetamask()

  const [head, ...tail] = await ethereum.request({ method: 'eth_requestAccounts' })

  const self = await SelfID.authenticate({
    authProvider: new EthereumAuthProvider(ethereum, head),
    connectNetwork: 'testnet-clay',
  })

  return { self }
}
