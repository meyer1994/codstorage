<script setup>
import { useRoute } from 'vue-router'

import { useApi } from '@/composables/useApi'

const { params: { ipfs } } = useRoute()
const { data } = await useApi(`files/${ipfs}`)
</script>

<template>
<div class="flex flex-col">
  <h1 class="text-3xl font-bold"> File </h1>
  <h2 class="text-xl font-medium"> {{ ipfs }} </h2>
  <pre class="mt-5 p-3 border"> {{ data }} </pre>
</div>
</template>
