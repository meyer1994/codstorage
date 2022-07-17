<script setup>
const { authenticated, user } = useMagic()
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
  <div v-if="authenticated">
    Account ({{ user.publicAddress.substring(0, 7) }})
  </div>
  <div v-else>
    <NuxtLink to="/login"> Login </NuxtLink>
  </div>
</div>
</template>
