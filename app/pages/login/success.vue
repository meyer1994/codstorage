<script setup>
const { token } = useMagic()

const command = computed(() => {
  return `git config http.extraHeader 'Authorization: Bearer ${token.value}'`
})

const { copy } = useClipboard({ source: command })
</script>

<template>
<div class="flex justify-center items-center h-full w-full">
  <div class="
    flex flex-col justify-center items-center gap-6
    h-1/2 w-1/2
    bg-white
    rounded-lg
    drop-shadow-lg
  ">
    <h1 class="text-3xl font-bold">
      Congratulations!
    </h1>
    <h2 class="text-xl text-center max-w-[80%]">
      You have successfully logged in. Now you can push your code to
      <span class="underline underline-offset-2"> codstorage </span>
      by including the header in your git commands
    </h2>
    <pre class="
      p-5 max-w-[80%]
      font-medium text-ellipsis overflow-hidden
      rounded-lg
      bg-indigo-200"
    >{{ command }}</pre>
    <button
      @click="copy()"
      class="px-5 py-2 rounded-full bg-slate-200 hover:bg-slate-3002"
    >
      Click to copy
    </button>
  </div>
</div>
</template>
