<script setup>
useHead({
  script: [
    {
      src: 'https://auth.magic.link/pnp/callback',
      'data-magic-publishable-api-key': 'pk_live_81C08853A07C5D54',
    }
  ]
})

const magic = useMagic()
const router = useRouter()

onMounted(() => {
  window.addEventListener('@magic/ready', event => {
    magic.authenticated.value = true
    magic.token.value = event.detail.idToken
    magic.user.value = event.detail.userMetadata
    router.push({ path: '/login/success' })
  })
})
</script>

<template>
  callback
</template>
