<template>
  <div v-if="faculties" class="row">
    <div class="col-12">
      <h1>Список факультетов и кафедр</h1>
    </div>
    <div class="col-12">
      <ListOfFaculties :faculties="faculties" />
    </div>
  </div>
  <q-inner-loading :showing="faculties === undefined">
    <q-spinner-puff class="fixed-center" size="50px" color="primary" />
  </q-inner-loading>
</template>

<script setup lang="ts">
  import { IListOfDepartments } from 'types/questionnaire'
  import ListOfFaculties from 'components/ListOfFaculties.vue'
  import { useQuestionnaire } from 'composables/useQuestionnaire'
  import { onMounted, ref } from 'vue'

  const { getListOfFaculties } = useQuestionnaire()

  const faculties = ref<IListOfDepartments[]>()

  onMounted(async () => {
    faculties.value = await getListOfFaculties()
  })
</script>
