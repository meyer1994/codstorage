<script setup>
import { computed, ref } from 'vue'

import { useApi } from '@/composables/useApi'
import { useCeramic } from '@/composables/useCeramic'

const { authenticate } = useCeramic()

const { data } = await useApi('repos')

const store =  await authenticate()
const likeds = await store.get('likes')
likeds.repos = likeds.repos ? likeds.repos : []

const liked = ref(likeds)

const repos = computed(() => {
  return data.value.map(i => ({
    ...i,
    liked: liked.value.repos.some(j => j.ipfs === i.ipfs)
  }))
})

const like = async (item) => {
  const store = await authenticate()
  const { repos = [] } = await store.get('likes')
  repos.push(item)
  await store.set('likes', { repos })
  liked.value = await store.get('likes')
}

const unlike = async (item) => {
  const store = await authenticate()
  const { repos = [] } = await store.get('likes')
  const newrepos = repos.filter(i => i.ipfs !== item.ipfs)
  await store.set('likes', { repos: newrepos })
  liked.value = await store.get('likes')
}
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

        <!-- Likes -->
        <td class="py-2">
          <button v-if="!v.liked" @click="like(v)"> Like </button>
          <button v-else @click="unlike(v)"> Unlike </button>
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
