<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'

import { useApi } from '@/composables/useApi'

const { params: { ipld } } = useRoute()

const { data } = await useApi(`ipld/${ipld}`)

const dirs = computed(() => {
  return Object.entries(data.value)
    .filter(([k, v]) => !v['/'].startsWith('Qm'))  // eslint-disable-line no-unused-vars
    .sort((a, b) => a[0].localeCompare(b[0]))
    .map(([k, v]) => [k, v['/']])
})

const files = computed(() => {
  return Object.entries(data.value)
    .filter(([k, v]) => v['/'].startsWith('Qm'))  // eslint-disable-line no-unused-vars
    .sort((a, b) => a[0].localeCompare(b[0]))
    .map(([k, v]) => [k, v['/']])
})
</script>

<template>
<div class="flex flex-col">
  <h1 class="text-3xl font-bold"> Files </h1>
  <table class="mt-5 table-auto">
    <thead>
      <tr>
        <th class="text-left text-xl font-bold"> Filename </th>
        <th class="text-left text-xl font-bold"> IPFS / IPLD </th>
      </tr>
    </thead>

    <tbody>
      <tr class="border-y" v-for="[name, link] of dirs" :key="name">
        <td class="py-1 font-mono">
          <router-link class="hover:text-blue-800 hover:underline" :to="`/trees/${link}`">
            {{ name }}
          </router-link>
        </td>
        <td class="py-1 font-mono" :title="link">
          <router-link class="hover:text-blue-800 hover:underline" :to="`/trees/${link}`">
            {{ link }}
          </router-link>
        </td>
      </tr>

      <tr class="border-y" v-for="[name, link] of files" :key="name">
        <td class="py-1 font-mono">
          <router-link class="hover:text-blue-800 hover:underline" :to="`/files/${link}`">
            {{ name }}
          </router-link>
        </td>
        <td class="py-1 font-mono" :title="link">
          <router-link class="hover:text-blue-800 hover:underline" :to="`/files/${link}`">
            {{ link }}
          </router-link>
        </td>
      </tr>
    </tbody>
  </table>

  <h1 class="mt-5 text-3xl font-bold"> API Response </h1>
  <pre class="mt-5 p-3 border"> {{ data }} </pre>
</div>
</template>
