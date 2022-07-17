<script setup>
const { hash } = defineProps(['hash'])

const { hash: rootHash, data: rootData } = useIpld('root', hash)
const { hash: branchHash, data: branchData } = useIpld('branches')
const { hash: commitHash, data: commitData } = useIpld('commits')
</script>

<template>
<div>
  <p>Branch: {{ branchHash }} </p>

  <select v-model="branchHash">
    <option v-for="(v, k) of rootData.value" :key="k" :value="v.toString()">
      {{ k }}
    </option>
  </select>

  <table class="table-auto">
    <thead>
      <tr>
        <td> Commit </td>
        <td> Message </td>
        <td> Author </td>
        <td> Date </td>
      </tr>
    </thead>

    <tbody>
      <tr v-for="(v, k) of branchData.value" :key="k">
        <td> {{ k.substring(0, 6) }} </td>
        <td> {{ v.message }} </td>
        <td> {{ v.author.name }} </td>
        <td> {{ v.committer.date }} </td>
      </tr>
    </tbody>
  </table>
</div>
</template>
