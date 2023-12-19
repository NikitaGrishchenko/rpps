<template>
  <router-view v-if="$q.screen.gt.xs" />
  <div v-else class="flex justify-center items-center">
    <span class="section-title text-h5">Пожалуйста зайдите с компьютера!</span>
  </div>
</template>

<script setup lang="ts">
  import { useQuasar } from 'quasar'

  const $q = useQuasar()
  $q.iconSet.type.warning = 'mdi-alert-circle'
</script>
