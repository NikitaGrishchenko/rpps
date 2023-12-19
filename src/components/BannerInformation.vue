<template>
  <q-banner
    v-for="banner in reference['banners']"
    :key="banner.id"
    inline-actions
    :class="getBannerClass(banner)"
  >
    <template v-slot:avatar>
      <q-icon :name="`mdi-${banner?.icon}`" :color="banner?.colorIcon" />
    </template>
    <p class="banner-information__text">{{ banner?.text }}</p>
  </q-banner>
</template>

<script setup lang="ts">
  import { IBanner } from 'types/reference'
  import { useReference } from 'src/composables/useReference'

  const { reference } = useReference(['banners'])

  const getBannerClass = (banner: IBanner) => {
    return banner.show === true
      ? `text-${banner.colorText} bg-${banner.colorBg} q-mb-sm`
      : `text-${banner.colorText} bg-${banner.colorBg} q-mb-sm hidden`
  }
</script>
