<script setup>
import CNavbar from '@/components/CNavbar'

</script>

<template>
<div class="min-h-screen min-v-screen bg-slate-100">
  <!-- Navbar -->
  <div class="bg-white w-full drop-shadow-md mb-2">
    <div class="container mx-auto">
      <CNavbar class="p-3" />
    </div>
  </div>

  <!-- Content -->
  <Suspense>
    <div class="container mx-auto h-full bg-slate-100">
      <router-view :key="$route.fullPath" />
    </div>
  </Suspense>
</div>
</template>
