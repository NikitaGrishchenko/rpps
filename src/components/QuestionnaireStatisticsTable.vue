<template>
  <template v-if="data.nested">
    <div class="col-12 q-pa-sm">
      <h4 class="text-h4 q-pb-md">{{ data.tableName }}</h4>
      <q-table
        class="q-mb-md"
        v-for="(table, index) in data.nested"
        :key="index"
        :="tableProps"
        :rows="getRows(table.rows)"
        :columns="getColumns(table.columns)"
      />
    </div>
  </template>

  <template v-else>
    <div class="col-6 q-pa-sm">
      <h4 class="text-h4 q-pb-md">{{ data.tableName }}</h4>
      <q-table
        :="tableProps"
        :rows="getRows(data.rows)"
        :columns="getColumns(data.columns)"
      />
    </div>
  </template>
</template>

<script setup lang="ts">
  import { IQuestionnaireStatisticsTable } from 'src/types/questionnaire'

  defineProps<{
    data: IQuestionnaireStatisticsTable
  }>()

  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const tableProps = {
    'row-key': 'name',
    bordered: true,
    flat: true,
    pagination: { rowsPerPage: 10 },
    'rows-per-page-label': 'Записей на странице:',
    'wrap-cells': true
  }

  const getColumns = (columns: IQuestionnaireStatisticsTable['columns']) => {
    return columns.map((col) => {
      return {
        align: 'left',
        field: col.name,
        ...col
      }
    })
  }

  const getRows = (rows: IQuestionnaireStatisticsTable['rows']) => {
    return rows.map((row) => row)
  }
</script>
