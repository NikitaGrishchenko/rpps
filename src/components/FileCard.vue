<template>
  <div class="file-card__wrapper row no-wrap">
    <div class="flex items-center q-px-sm">
      <q-btn
        flat
        round
        icon="mdi-delete-outline"
        color="accent-2"
        class="file-card__button"
        @click="deleteFile"
      />
    </div>
    <q-card
      class="file-card row full-width"
      :class="{ 'file-card--no-editable items-center': !isEditable }"
    >
      <q-card-section class="file-card__section col-2">
        <q-select
          v-if="isEditable"
          class="input-textfield input-textfield--outlined"
          v-model="updatedFile.typeFile"
          outlined
          popup-content-class="input-textfield"
          :options="fileTypes"
          option-label="name"
          option-value="id"
          emit-value
          map-options
        />
        <div v-else class="text-accent-2 text-h5">
          {{ fileTypes.filter((type) => type.id === file.typeFile)[0].name }}
        </div>
      </q-card-section>
      <q-card-section class="file-card__section--main col-8">
        <q-input
          v-if="isEditable"
          v-model="updatedFile.name"
          class="input-textfield input-textfield--outlined"
          outlined
        />
        <div v-else class="row items-center">
          <div class="text-h4 col-8">{{ file.name }}</div>
          <div class="text-h5 text-right col-4">{{ file.dateUpload }}</div>
        </div>
      </q-card-section>
      <q-card-actions
        class="file-card__section flex items-center q-pa-md q-ml-auto col-1"
      >
        <q-btn
          v-if="isEditable"
          flat
          round
          icon="mdi-check"
          color="positive"
          class="file-card__button"
          @click="saveChanges"
        />
        <q-btn
          v-else
          flat
          round
          icon="mdi-pencil"
          color="accent-2"
          class="file-card__button"
          @click="isEditable = true"
        />
      </q-card-actions>
    </q-card>
    <div class="flex items-center q-px-sm">
      <q-btn
        flat
        round
        icon="mdi-download"
        color="accent-2"
        class="file-card__button"
        :href="String(file.file)"
        target="_blank"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
  import { useFile } from 'composables/useFile'
  import { ref, onMounted } from 'vue'
  import { IFile } from 'types/questionnaire'
  import { IFileType } from 'types/reference'
  import { useQuasar } from 'quasar'

  const $q = useQuasar()
  const props = defineProps<{
    file: IFile
    fileTypes: IFileType[]
  }>()
  const emit = defineEmits<{
    (e: 'fileDeleted'): void
    (e: 'fileUpdated'): void
  }>()

  // Хуки api
  const { fileById } = useFile()

  const isEditable = ref<boolean>(false)
  const updatedFile = ref<IFile>({
    name: undefined,
    typeFile: undefined
  })

  // Изменение данных файла
  const saveChanges = async () => {
    if (props.file.id) {
      await fileById(props.file.id, 'PATCH', updatedFile.value)
      emit('fileUpdated')
      isEditable.value = false
    }
  }
  const deleteFile = async () => {
    if (
      props.file.fileCategoryQuestionnaireUser &&
      Object.keys(props.file.fileCategoryQuestionnaireUser).length > 0
    ) {
      return $q.notify({
        type: 'error',
        message:
          'Вы не можете удалить этот файл, так как он прикреплен к анкете',
        color: 'red',
        position: 'top'
      })
    }
    if (props.file.id) {
      await fileById(props.file.id, 'DELETE')
      emit('fileDeleted')
    }
  }

  onMounted(() => {
    updatedFile.value.name = props.file.name
    updatedFile.value.typeFile = props.file.typeFile
  })
</script>
