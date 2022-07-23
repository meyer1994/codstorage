<script setup>
import { useEthereum } from '@/composables/useEthereum'

const { account, request } = useEthereum()

const connect = async () => {
  await request()
}
</script>

<template>
<div class="flex justify-between items-center">
  <!-- Left -->
  <div>
    <router-link to="/"> Home </router-link>
  </div>

  <!-- Center -->
  <div> codstorage </div>

  <!-- Right -->
  <div>
    <button @click="connect">
      Metamask
      <span v-if="account" :title="account">
        ({{ account.substring(0, 8) }})
      </span>
    </button>
  </div>
</div>
</template>
