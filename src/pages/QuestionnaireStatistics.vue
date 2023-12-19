<template>
  <q-page class="container">
    <div class="text-primary text-bold text-h4 q-pb-md">
      Статистика по анкете
    </div>
    <div class="row">
      <div class="col-12 q-pb-md">
        <q-select
          v-model="selectedQuestionnaire"
          popup-content-class="input-textfield"
          filled
          color="primary"
          label="Список анкет"
          :options="questionnaireList"
          option-label="name"
          option-value="id"
          :loading="inProcess"
          @update:model-value="fetchQuestionnaireStatistics"
        />
      </div>
      <QuestionnaireStatisticsTable
        v-for="table in dataTables"
        :key="table.tableName"
        :data="table"
      />
      <q-inner-loading :showing="inProcess">
        <q-spinner-puff class="fixed-center" size="50px" color="primary" />
      </q-inner-loading>
    </div>
  </q-page>
</template>

<script setup lang="ts">
  import QuestionnaireStatisticsTable from 'components/QuestionnaireStatisticsTable.vue'
  import { useQuestionnaire } from 'composables/useQuestionnaire'
  import {
    IQuestionnaireBase,
    IQuestionnaireStatisticsTable
  } from 'src/types/questionnaire'
  import { onMounted, ref } from 'vue'

  const { getQuestionnaireStatistics, getQuestionnaireAllList, inProcess } =
    useQuestionnaire()

  const questionnaireList = ref<IQuestionnaireBase[]>()
  const selectedQuestionnaire = ref<IQuestionnaireBase>()
  const dataTables = ref<IQuestionnaireStatisticsTable[]>()

  const fetchQuestionnaireStatistics = async (value: IQuestionnaireBase) => {
    dataTables.value = await getQuestionnaireStatistics(value.id)
  }

  onMounted(async () => {
    questionnaireList.value = await getQuestionnaireAllList()
  })
</script>
