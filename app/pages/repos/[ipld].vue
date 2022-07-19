<script setup>
const { params: { ipld } } = useRoute()
const { data } = await useAsyncData(`repo_${ipld}`, () => useApi(`/ipld/${ipld}`))
</script>

<template>
<div class="flex flex-col">
  <pre> {{ repo }} </pre>
  <table class="table-fixed">
    <thead>
      <tr>
        <td> Branch </td>
        <td> IPLD </td>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(v, k) of data" :key="k">
        <td><NuxtLink :to="`/branches/${v['/']}`"> {{ k }} </NuxtLink></td>
        <td><NuxtLink :to="`/branches/${v['/']}`"> {{ v['/'] }} </NuxtLink></td>
      </tr>
    </tbody>
  </table>
</div>
</template>
