<template>
  <q-page class="container relative-position">
    <div class="text-primary text-bold text-h2 q-pb-md">Мои файлы</div>
    <div class="row">
      <q-tabs
        v-model="selectedYear"
        narrow-indicator
        dense
        align="justify"
        class="text-primary"
      >
        <q-tab
          @click="selectedYear !== year ? getFilesList(year) : null"
          v-for="year in yearsList"
          :key="year"
          :name="year"
          :label="year"
        />
      </q-tabs>
    </div>
    <div
      v-if="filesList && reference['enums/type-file'] && filesList.length > 0"
      class="row q-py-md"
    >
      <div v-for="file in filesList" :key="file.id" class="col-12 q-py-sm">
        <FileCard
          @file-deleted="getFilesList(selectedYear)"
          @file-updated="getFilesList(selectedYear)"
          :file="file"
          :file-types="reference['enums/type-file']"
        />
      </div>
    </div>
    <div
      v-if="filesList && filesList.length === 0"
      class="full-width q-pa-lg row flex-center text-primary q-gutter-sm"
    >
      <div class="col-6">
        <img
          src="~assets/images/files_page.svg"
          style="min-height: 300px; width: 100%"
        />
      </div>
      <div class="col-8 text-center q-pt-md">
        <div class="text-h3">Вы не загрузили ни одного файла</div>
        <div class="text-h5">Для загрузки файлов нажмите на кнопку ниже</div>
      </div>
    </div>
    <q-inner-loading :showing="inProcess">
      <q-spinner-puff class="fixed-center" size="50px" color="primary" />
    </q-inner-loading>
    <DialogUploadFile
      v-model="fileUploadingModal"
      :file-types="reference['enums/type-file'] || []"
      @file-uploaded="getFilesList(selectedYear), (fileUploadingModal = false)"
    />
    <q-page-sticky
      v-if="selectedYear === String(new Date().getFullYear())"
      position="bottom-right"
      :offset="[18, 18]"
    >
      <q-btn @click="fileUploadingModal = true" fab icon="add" color="primary">
        <q-tooltip anchor="top start" self="center middle">
          Загрузить файл в систему
        </q-tooltip>
      </q-btn>
    </q-page-sticky>
  </q-page>
</template>

<script setup lang="ts">
  import { useFile } from 'composables/useFile'
  import { IFile } from 'types/questionnaire'
  import { onMounted, ref } from 'vue'
  import FileCard from 'components/FileCard.vue'
  import DialogUploadFile from 'components/DialogUploadFile.vue'
  import { useReference } from 'composables/useReference'

  const selectedYear = ref<string>(String(new Date().getFullYear()))
  const yearsList = ref<string[]>()
  const fileUploadingModal = ref<boolean>(false)
  const filesList = ref<IFile[]>()

  // Хуки api
  const { getFilesYearsList, getFilesByYears, inProcess } = useFile()
  const { reference } = useReference(['enums/type-file'])

  // Получение списка файлов
  const getFilesList = async (year: string) => {
    filesList.value = await getFilesByYears(year)
  }

  onMounted(async () => {
    yearsList.value = await getFilesYearsList()
    if (yearsList.value !== undefined) {
      selectedYear.value = yearsList.value[0]
      filesList.value = await getFilesByYears(selectedYear.value)
    }
  })
</script>
