<template>
  <div>
    <!-- Редирект на страницу кафедры -->
  </div>
</template>

<script setup lang="ts">
  import { useRouter } from 'vue-router'

  import { useStore } from '../store/index'

  const store = useStore()
  const router = useRouter()

  void router.push({
    name: 'ListOfDepartmentsPage',
    params: { id_department: store.state.auth.user.managerDepartmentId }
  })
</script>
