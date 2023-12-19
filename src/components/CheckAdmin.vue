<template>
  <div class="row q-pb-xl">
    <div class="col-12 q-gutter-md">
      <q-btn label="Статистика" :to="{ name: 'StatisticsPage' }" />
      <q-btn
        label="Регистрация пользователя"
        :to="{ name: 'UserRegistration' }"
      />
      <q-btn label="Создание анкет" :to="{ name: 'CreatingQuestionnaires' }" />
    </div>
  </div>
</template>

<script setup lang="ts"></script>
