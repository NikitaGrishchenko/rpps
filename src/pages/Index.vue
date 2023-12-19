<template>
  <q-page class="container">
    <BannerInformation />
    <CheckAdmin v-if="userAuth.isAdmin" />
    <CheckExpert v-if="userAuth.isSuperExpert || userAuth.isExpert" />
    <CheckManagerDepartment v-if="userAuth.isManagerDepartment" />
    <CheckManagerFaculty v-if="userAuth.isManagerFaculty" />
    <QuestionnaireUserList
      v-if="
        !userAuth.isManagerFaculty &&
        !userAuth.isManagerDepartment &&
        !userAuth.isSuperExpert &&
        !userAuth.isExpert &&
        !userAuth.isAdmin
      "
    />
  </q-page>
</template>

<script setup lang="ts">
  import QuestionnaireUserList from 'components/QuestionnaireUserList.vue'
  import CheckExpert from 'components/CheckExpert.vue'
  import CheckAdmin from 'components/CheckAdmin.vue'
  import CheckManagerDepartment from 'components/CheckManagerDepartment.vue'
  import CheckManagerFaculty from 'components/CheckManagerFaculty.vue'
  import BannerInformation from 'components/BannerInformation.vue'
  import { useStore } from '../store/index'
  import { computed } from 'vue'

  const store = useStore()

  const userAuth = computed(() => store.state.auth.user)
</script>
