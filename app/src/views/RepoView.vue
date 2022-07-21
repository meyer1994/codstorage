<script setup>
import { useRoute } from 'vue-router'

import { useApi } from '@/composables/useApi'

const { params: { ipld } } = useRoute()
const { data } = await useApi(`ipld/${ipld}`)
</script>

<template>
<div class="flex flex-col">
  <h1 class="text-3xl font-bold"> Branches </h1>
  <table class="mt-5 table-auto">
    <thead>
      <tr>
        <th class="text-left text-xl font-bold"> Branch </th>
        <th class="text-left text-xl font-bold"> IPLD </th>
      </tr>
    </thead>

    <tbody>
      <tr class="border-y" v-for="(v, k) of data" :key="k">
        <!-- Branch name -->
        <td class="py-2 font-mono">
          <router-link class="hover:text-blue-800 hover:underline" :to="`/branches/${v['/']}`">
            {{ k }}
          </router-link>
        </td>

        <!-- IPLD -->
        <td class="py-2 font-mono">
          <router-link class="hover:text-blue-800 hover:underline" :to="`/branches/${v['/']}`">
            {{ v['/'] }}
          </router-link>
        </td>
      </tr>
    </tbody>
  </table>

  <h1 class="mt-5 text-3xl font-bold"> API Response </h1>
  <pre class="mt-5 p-3 border"> {{ data }} </pre>
</div>
</template>
