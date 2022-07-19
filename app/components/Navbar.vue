<script setup>
const { enabled, ethereum, account } = useMetamask()

const request = async () => {
  const [head, ...tail] = await ethereum.request({ method: 'eth_requestAccounts' })
  account.value = head
}
</script>

<template>
<div class="flex justify-between items-center">
  <!-- Left -->
  <div>
    <NuxtLink to="/"> Home </NuxtLink>
  </div>

  <!-- Center -->
  <div> codstorage </div>

  <!-- Right -->
  <div>
    <button :class="{ disabled: !enabled }" @click="request">
      <span v-if="!account"> Connect </span>
      <span v-else> Connected ({{ account.substring(0, 8) }})</span>
    </button>
  </div>
</div>
</template>
