from pprint import pp

from codstorage.ceramic import Ceramic

c = Ceramic()

res = c.create({})
pp(res)


# did = res['streamId']
# res = c.state(did)
# pp(res)


