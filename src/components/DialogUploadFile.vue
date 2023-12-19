<template>
  <q-dialog
    :model-value="modelValue"
    @update:modelValue="$emit('update:modelValue', $event)"
  >
    <q-card class="q-pa-md" style="min-width: 500px">
      <q-card-actions align="between">
        <div class="text-h4">Загрузить файл</div>
        <q-btn flat round icon="mdi-close" v-close-popup />
      </q-card-actions>
      <q-form @submit.prevent="handleNewFile">
        <q-card-section class="q-gutter-y-xs">
          <q-input
            v-model="newFile.name"
            class="input-textfield input-textfield--outlined"
            label="Наименование файла"
            :rules="[(val) => !!val || 'Название не может быть пустым!']"
            outlined
          />
          <q-select
            class="input-textfield input-textfield--outlined"
            v-model="newFile.typeFile"
            label="Тип файла"
            outlined
            popup-content-class="input-textfield"
            :options="fileTypes"
            :rules="[(val) => val !== undefined || 'Выберите тип файла!']"
            option-label="name"
            option-value="id"
            emit-value
            map-options
          />
          <q-file
            class="input-textfield input-textfield--outlined"
            v-model="newFile.file"
            label="Выбрать файл"
            clearable
            outlined
            counter
            accept=".png, .jpg, .jpeg, .docx, .doc, .pdf"
            :max-file-size="15 * 1024 ** 2"
            :rules="[
                (val: File)=>!!val||'Файл не может быть пустым!',
                (val:File) =>
                  val.name.length < 90  ||
                  'Длинна имени загружаемого файла не дожна превышать 90 символов!'
              ]"
            @rejected="handleFileErrors"
          />
          <div class="text-h6 text-accent-2">
            Типы файлов для загрузки:
            <span class="text-bold">DOC, DOCX, JPEG ,JPG, PDF</span>
          </div>
        </q-card-section>
        <q-card-actions align="right">
          <q-btn type="submit" color="positive" label="Загрузить файл" />
        </q-card-actions>
      </q-form>
      <q-inner-loading :showing="inProcess">
        <q-spinner-puff class="fixed-center" size="50px" color="primary" />
      </q-inner-loading>
    </q-card>
  </q-dialog>
</template>

<script setup lang="ts">
  import { useFile } from 'composables/useFile'
  import { IFile } from 'types/questionnaire'
  import { IFileType } from 'types/reference'
  import { ref } from 'vue'
  import { useQuasar } from 'quasar'

  defineProps<{
    modelValue: boolean
    fileTypes: IFileType[]
  }>()
  const emit = defineEmits<{
    (e: 'update:modelValue', value: boolean): void
    (e: 'fileUploaded'): void
  }>()
  const $q = useQuasar()

  const { addFile, inProcess } = useFile()

  const newFile = ref<IFile>({
    typeFile: undefined,
    name: '',
    file: undefined
  })

  const handleFileErrors = (errors: any[]) => {
    $q.notify({
      type: 'negative',
      message: `${errors.length} файл(ов) не прошли проверку.`
    })
  }
  const handleNewFile = () => {
    void addFile(newFile.value).then(() => {
      emit('fileUploaded')
      newFile.value = {
        typeFile: undefined,
        name: '',
        file: new File([], '')
      }
    })
  }
</script>
