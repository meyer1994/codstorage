<script setup>
import { Wallet } from 'ethers'
import { Client } from '@xmtp/xmtp-js'
console.log(Wallet, Client)
import { useApi } from '@/composables/useApi'
const { data } = useApi('repos')
</script>

<template>
<div class="flex flex-col">
  <h1 class="text-3xl font-bold"> Repos </h1>
  <table class="mt-5 table-auto">
    <thead>
      <tr>
        <th class="text-left text-xl font-bold"> IPFS </th>
        <th class="text-left text-xl font-bold"> IPLD </th>
        <th class="text-left text-xl font-bold"> Likes </th>
        <th class="text-left text-xl font-bold invisible"> - </th>
      </tr>
    </thead>

    <tbody>
      <tr class="border-y" v-for="(v, k) of data" :key="k">
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

        <!-- Likes -->
        <td class="py-2">
          {{ v.likes }}
        </td>

        <!-- Share -->
        <td class="py-2">
          <button @click="share"> Share </button>
        </td>
      </tr>
    </tbody>
  </table>

  <h1 class="mt-5 text-3xl font-bold"> API Response </h1>
  <pre class="mt-5 p-3 border"> {{ data }} </pre>
</div>
</template>
