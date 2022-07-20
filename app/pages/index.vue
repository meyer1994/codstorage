<script setup>
const { data, error } = await useApi(() => '/repos')
</script>

<template>
<div class="flex flex-col">
  <h1> Repos </h1>
  <table>
    <thead>
      <tr>
        <td> Ipfs </td>
        <td> Ipld </td>
        <td> Likes </td>
        <td class="invisible"> - </td>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(v, k) of data">
        <td class="font-mono">
          <NuxtLink :to="`/repos/${v.ipld}`">
            {{ v.ipfs }}
          </NuxtLink>
        </td>
        <td class="font-mono">
          <NuxtLink :to="`/repos/${v.ipld}`">
            {{ v.ipld }}
          </NuxtLink>
        </td>
        <td> {{ v.likes }} </td>
        <td>
          <button @click="share"> Share </button>
        </td>
      </tr>
    </tbody>
  </table>

  <h1> Response </h1>
  <pre> {{ data }} </pre>
</div>
</template>
