<script setup>
const { params: { hash: paramHash } } = useRoute()
const { hash, data } = useIpld('root', paramHash)
</script>

<template>
<div>

</div>
</template>
