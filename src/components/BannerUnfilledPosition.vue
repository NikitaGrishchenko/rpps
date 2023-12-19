<template>
  <q-banner
    v-if="
      !userPosition?.department ||
      !userPosition?.position ||
      !userPosition?.rate
    "
    inline-actions
    class="text-white bg-red q-mb-sm"
  >
    <template v-slot:avatar>
      <q-icon name="mdi-alert-circle-outline" color="white" />
    </template>
    <h5>
      Вы не указали данные для профиля. Укажите Вашу кафедру, должность и ставку
      в Личном кабинете.
    </h5>
    <template v-slot:action>
      <q-btn
        flat
        color="white"
        :to="{ name: 'PersonalArea' }"
        label="Указать"
      />
    </template>
  </q-banner>
</template>

<script setup lang="ts">
  import { computed } from 'vue'
  import { useStore } from '../store/index'
  const store = useStore()

  const userPosition = computed(() => store.state.questionnaire.userPosition)
</script>
