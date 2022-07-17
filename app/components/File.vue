<script>
const { commit } = defineProps(['commit'])
const { hash, data } = useIpld('commit', commit)
</script>
<template>
<pre></pre>
</template>
