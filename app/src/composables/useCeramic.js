import { DIDDataStore } from '@glazed/did-datastore'
import { EthereumAuthProvider, SelfID } from '@self.id/web'

import { useEthereum } from '@/composables/useEthereum'

const aliases = {
  definitions: {
    likes: 'kjzl6cwe1jw145oekmuo8v8tqncvla6nmgcck54qqfdwsb4h4ddxbhzkel5qygw'
  },
  schemas: {
    likes: 'ceramic://k3y52l7qbv1fry8ntb87p0yya7qj9ujfuiy6iqv3rw75xqyrddykxyfr1nlfh2l8g'
  },
  tiles: {}
}

export const useCeramic = () => {
  const { ethereum, account, request } = useEthereum()

  const authenticate = async () => {
    await request()

    const self = await SelfID.authenticate({
      authProvider: new EthereumAuthProvider(ethereum, account.value),
      ceramic: 'testnet-clay',
      connectNetwork: 'testnet-clay',
    })

    const ceramic = self.client.ceramic

    return new DIDDataStore({ ceramic, model: aliases })
  }

  return { authenticate }
}
