<script setup>
const { params: { ipld } } = useRoute()

const { data: repo } = await useAsyncData('repo', () => useApi(`/ipld/${ipld}`))

const branchName = ref(Object.keys(repo.value)[0])
const branchIpld = computed(() => repo.value[branchName.value]['/'])

const { data: commits } = await useAsyncData('commits', () => useApi(`/ipld/${branchIpld.value}`))
</script>

<template>
<div class="flex flex-col">
  <div class="flex">
    <h1> {{ branchName }} </h1>
    <select>
      <option v-for="(v, k) of repo" :value="v['/']"> {{ k }} </option>
    </select>
  </div>


  <table class="table-fixed">
    <thead>
      <tr>
        <td>Hash</td>
        <td>Message</td>
        <td>Commiter</td>
        <td>Date</td>
      </tr>
    </thead>
    <tbody>
      <tr v-for="i of commits" :key="i.hash">
        <td>
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
