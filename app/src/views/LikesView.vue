<script setup>
import { useCeramic } from '@/composables/useCeramic'

const { authenticate } = useCeramic()

const store =  await authenticate()
const { repos = [] } = await store.get('likes')
</script>

<template>
<div class="flex flex-col">
  <h1 class="text-3xl font-bold"> Liked </h1>
  <table class="mt-5 table-auto">
    <thead>
      <tr>
        <th class="text-left text-xl font-bold"> IPFS </th>
        <th class="text-left text-xl font-bold"> IPLD </th>
      </tr>
    </thead>

    <tbody>
      <tr class="border-y" v-for="(v, k) of repos" :key="k">
        <!-- IPFS -->
        <td class="py-2 font-mono">
          <router-link class="hover:text-blue-800 hover:underline" :to="`/repos/${v.ipld}`">
            {{ v.ipfs }}
          </router-link>
        </td>

        <!-- IPLD -->
        <td class="py-2 font-mono">
          <router-link class="hover:text-blue-800 hover:underline" :to="`/repos/${v.ipld}`">
            {{ v.ipld }}
          </router-link>
        </td>
      </tr>
    </tbody>
  </table>

  <h1 class="mt-5 text-3xl font-bold"> API Response </h1>
  <pre class="mt-5 p-3 border"> {{ repos }} </pre>
</div>
</template>
