<script setup>
const { data, refresh } = await useAsyncData('repos', () => useApi('/repos'))
</script>

<template>
<div class="flex flex-col">
  <div> Repos </div>

  <table>
    <thead>
      <tr>
        <td>IPFS</td>
        <td>IPLD</td>
        <td>Likes</td>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(v, k) of data">
        <td>
          {{ v.ipfs }}
        </td>
        <td>
          <NuxtLink :to="`/repos/${v.ipld}`"> {{ v.ipld }} </NuxtLink>
        </td>
        <td>
          {{ v.likes }}
        </td>
      </tr>
    </tbody>
  </table>
</div>
</template>
