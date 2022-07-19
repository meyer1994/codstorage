<script setup>
const { params: { ipld } } = useRoute()

const { data } = await useAsyncData(`branch_${ipld}`, () => useApi(`/ipld/${ipld}`))
</script>

<template>
<div class="flex flex-col">
  <table class="table-fixed">
    <thead>
      <tr>
        <td> Hash </td>
        <td> Message </td>
        <td> Commiter </td>
        <td> Date </td>
      </tr>
    </thead>
    <tbody>
      <tr v-for="i of data" :key="i.hash">
        <td class="font-mono">
          <NuxtLink :to="`/trees/${i['tree']['/']}`">
            {{ i.hash.substring(0, 8) }}
          </NuxtLink>
        </td>
        <td class="max-w-[32em]">
          <p class="line-clamp-1"> {{ i.message }} </p>
        </td>
        <td> {{ i.author.name }} </td>
        <td> {{ i.author.date }} </td>
      </tr>
    </tbody>
  </table>
</div>
</template>
