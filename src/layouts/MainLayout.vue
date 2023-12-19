<template>
  <q-layout view="lhr lpR fFf">
    <q-header class="bg-none q-px-xl">
      <MainHeader />
    </q-header>
    <router-view />
  </q-layout>
</template>

<script setup lang="ts">
  import MainHeader from 'layouts/MainHeader.vue'
</script>
