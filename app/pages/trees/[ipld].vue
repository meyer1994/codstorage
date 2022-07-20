<script setup>
const { params: { ipld } } = useRoute()

const { data: tree } = await useApi(() => `/ipld/${ipld}`)

const dirs = computed(() => {
  return Object.entries(tree.value)
    .filter(([k, v]) => !v['/'].startsWith('Qm'))
    .sort((a, b) => a[0].localeCompare(b[0]))
    .map(([k, v]) => [k, v['/']])
})

const files = computed(() => {
  return Object.entries(tree.value)
    .filter(([k, v]) => v['/'].startsWith('Qm'))
    .sort((a, b) => a[0].localeCompare(b[0]))
    .map(([k, v]) => [k, v['/']])
})
</script>

<template>
<div class="flex flex-col">
  <table class="table-fixed">
    <thead>
      <tr>
        <td>Filename</td>
        <td>IPFS/IPLD</td>
      </tr>
    </thead>
    <tbody>
      <tr v-for="[name, link] of dirs" :key="name">
        <td>
          <NuxtLink :to="`/trees/${link}`">
            {{ name }}
          </NuxtLink>
        </td>
        <td class="font-mono" :title="link">
          <NuxtLink :to="`/trees/${link}`">
            {{ link.substring(0, 16) }}
          </NuxtLink>
        </td>
      </tr>
      <tr v-for="[name, link] of files" :key="name">
        <td> {{ name }} </td>
        <td class="font-mono" :title="link"> {{ link.substring(0, 16) }} </td>
      </tr>
    </tbody>
  </table>
</div>
</template>
