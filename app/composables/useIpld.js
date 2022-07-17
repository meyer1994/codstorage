import { create, CID } from 'ipfs-http-client'

export const useIpld = (key, start) => {
  const client = create({ url: 'http://localhost:5001' })

  const hash = useState(`ipld_${key}_hash`, () => (start ? start : null))
  const data = useState(`ipld_${key}_data`, () => ({ value: {}, remainderPath: '' }))

  watch(hash, async (ncid, ocid) => {
    try {
      const cid = CID.parse(ncid)
      data.value = await client.dag.get(cid)
    } catch (e) {}
  })

  if (start) {
    const cid = CID.parse(start)
    client.dag.get(cid).then(i => (data.value = i))
  }

  return { hash, data }
}
