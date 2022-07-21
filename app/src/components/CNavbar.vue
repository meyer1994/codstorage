<script setup>
import { useMetamask } from '@/composables/useMetamask'

const { enabled, request, account } = useMetamask()

const login = async () => {
  const accounts = await request({ method: 'eth_requestAccounts' })
  account.value = accounts[0]
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
    <button :class="{ disabled: !enabled }" @click="login">
      <span v-if="!account"> Connect </span>
      <span v-else> Connected ({{ account.substring(0, 8) }})</span>
    </button>
  </div>
</div>
</template>
