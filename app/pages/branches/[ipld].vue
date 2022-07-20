<script setup>
const { params: { ipld } } = useRoute()
const { data } = await useApi(() => `/ipld/${ipld}`)
</script>

<template>
<div class="flex flex-col">
  <h1 class="text-3xl font-bold"> Commits </h1>
  <table class="mt-5 table-auto">
    <thead>
      <tr>
        <th class="text-left text-xl font-bold"> Hash </th>
        <th class="text-left text-xl font-bold"> Message </th>
        <th class="text-left text-xl font-bold"> Commiter </th>
        <th class="text-left text-xl font-bold"> Date </th>
      </tr>
    </thead>

    <tbody>
      <tr class="border-y" v-for="i of data" :key="i.hash">
        <!-- Hash -->
        <td class="py-1 font-mono">
          <NuxtLink
            class="hover:text-blue-800 hover:underline"
            :title="i.hash"
            :to="`/trees/${i['tree']['/']}`"
          >
            {{ i.hash.substring(0, 8) }}
          </NuxtLink>
        </td>

        <!-- Message -->
        <td class="py-1 font-mono max-w-[32em]">
          <p class="line-clamp-1"> {{ i.message }} </p>
        </td>

        <!-- Author -->
        <td class="py-1 font-mono">
          {{ i.author.name }}
        </td>

        <!-- Date -->
        <td class="py-1 font-mono">
          {{ i.author.date }}
        </td>
      </tr>
    </tbody>
  </table>

  <h1 class="mt-5 text-3xl font-bold"> API Response </h1>
  <pre class="mt-5 p-3 border"> {{ data }} </pre>
</div>
</template>
