<script setup>
const { hash: rootHash, data: rootData } = useIpld('root')
const { hash: branchHash, data: branchData } = useIpld('branches')
const { hash: commitHash, data: commitData } = useIpld('commits')

const test = ref('bafyreihqw66adfvi7p55pg443beizhfhdhaafbfg7qo2fuhltqlshmzpsi')
</script>

<template>
<div>
  <section class="flex justify-around items-center">
    <h1 class="text-5xl font-bold"> codstorage </h1>
  </section>

  <section>
    <Repo :hash="test" />
  </section>
</div>
</template>
