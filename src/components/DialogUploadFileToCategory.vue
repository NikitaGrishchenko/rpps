<template>
  <q-dialog
    v-model="getShowDialog"
    @show="setCurrentCategory()"
    no-backdrop-dismiss
    no-esc-dismiss
  >
    <q-card style="width: 700px; box-shadow: none">
      <q-card-section class="row items-center q-pb-none">
        <div class="text-h4">Загрузить новый файл</div>
        <q-space />
        <q-btn
          @click="closeDialog()"
          icon="close"
          flat
          round
          dense
          v-close-popup
        />
      </q-card-section>
      <q-card-section>
        <q-form @submit="onSubmit" ref="categoryUserForm">
          <q-file
            v-model="file"
            label="Файл"
            filled
            accept=".pdf, .docx, .doc, .jpg, .png,"
            :rules="[isValidFile]"
            lazy-rules
          />
          <q-input
            v-if="
              categoryUser?.categoryQuestionnaire?.useInternetResourceLink ===
                true ||
              categoryUser?.categoryQuestionnaire?.internetResourceLinkOrDoc ===
                true
            "
            v-model="internetResourceLink"
            label="Ссылка"
            ref="internetResourceLinkRef"
            :rules="[isValidInternetResourceLink]"
            lazy-rules
            filled
          />
          <q-input
            v-model="nameFile"
            label="Наименование файла"
            filled
            :rules="[
              (val) => !!val || 'Обязательное поле',
              (val) => val?.length >= 3 || 'Минимум три символа'
            ]"
            lazy-rules
          />
          <q-select
            v-model="typeFile"
            label="Тип файла"
            popup-content-class="input-textfield"
            :options="reference['enums/type-file']"
            option-label="name"
            :rules="[(val) => !!val || 'Обязательное поле']"
            lazy-rules
            filled
          />
          <q-input
            v-if="categoryUser?.categoryQuestionnaire?.typeCategory === 3"
            v-model="quantityValue"
            type="number"
            label="Введите число"
            :rules="[(val) => !!val || 'Обязательное поле']"
            lazy-rules
            filled
          />
          <q-select
            v-if="categoryUser?.categoryQuestionnaire?.typeCategory === 2"
            popup-content-class="input-textfield"
            v-model="prizePlace"
            label="Выберите призовое место"
            :options="reference['prize-places']"
            option-label="name"
            options-dense
            :rules="[(val) => !!val || 'Обязательное поле']"
            lazy-rules
            filled
          />
          <div>
            <div class="coefficient-input">
              <q-select
                v-if="
                  categoryUser?.categoryQuestionnaire?.typeCategory === 1 &&
                  showInputForCoefficient === false
                "
                popup-content-class="input-textfield"
                class="input-textfield"
                v-model="coefficient"
                :options="optionsCoefficient"
                label="Выберите количество соавторов"
                emit-value
                map-options
                :rules="[isValidCoefficient]"
                lazy-rules
                filled
              />
              <q-input
                v-if="
                  categoryUser?.categoryQuestionnaire?.typeCategory === 1 &&
                  showInputForCoefficient === true
                "
                v-model="coefficient"
                label="Введите процент соавторства (Например: 0.90)"
                :rules="[isValidCoefficient]"
                lazy-rules
                filled
              />
              <div
                class="coefficient-btn"
                v-if="categoryUser?.categoryQuestionnaire?.typeCategory === 1"
              >
                <q-icon
                  @click="showInputForCoefficient = !showInputForCoefficient"
                  size="sm"
                  name="mdi-swap-horizontal"
                />
              </div>
            </div>
          </div>
          <q-btn
            class="q-mt-md main-btn"
            type="submit"
            color="white"
            text-color="black"
            :loading="showProgressBtn"
          >
            Загрузить
            <template v-slot:loading>
              <q-spinner-puff />
            </template>
          </q-btn>
        </q-form>
      </q-card-section>
    </q-card>
  </q-dialog>
</template>

<script setup lang="ts">
  import { useQuestionnaire } from 'composables/useQuestionnaire'
  import { useReference } from 'src/composables/useReference'
  import {
    ICategoryDialog,
    IFileCategoryQuestionnaireUserPatch,
    IPrizePlace,
    IEnumsTypeFile
  } from 'src/types/questionnaire'
  import { computed, ref } from 'vue'
  import { QForm, useQuasar } from 'quasar'
  import { useStore } from '../store/index'
  import { useRoute } from 'vue-router'

  const $q = useQuasar()

  const route = useRoute()
  const store = useStore()
  const {
    getCategoryUser,
    uploadFileForCategoryUser,
    isValidInternetResourceLink,
    isValidCoefficient,
    isValidFile
  } = useQuestionnaire()
  const { reference } = useReference(['prize-places', 'enums/type-file'])

  const props = defineProps({
    showDialog: Boolean
  })

  const emit = defineEmits(['updateFileCategoryUser'])

  const categoryUserForm = ref<QForm>()
  const categoryUser = ref<ICategoryDialog>()

  const optionsCoefficient = [
    { label: 1, value: 1 },
    { label: 2, value: 0.5 },
    { label: 3, value: 0.33 },
    { label: 4, value: 0.25 },
    { label: 5, value: 0.2 },
    { label: 6, value: 0.17 },
    { label: 7, value: 0.14 },
    { label: 8, value: 0.13 },
    { label: 9, value: 0.11 },
    { label: 10, value: 0.1 }
  ]

  const file = ref<File | undefined>()
  const nameFile = ref<string>()
  const typeFile = ref<IEnumsTypeFile>()
  const quantityValue = ref<number>()
  const prizePlace = ref<IPrizePlace>()
  const coefficient = ref<number>()
  const internetResourceLink = ref<string>()

  const showProgressBtn = ref<boolean>(false)
  const internetResourceLinkRef = ref()
  const showInputForCoefficient = ref<boolean>(false)
  const idQuestionnaireUser = Number(route.params.idQuestionnaire)

  const setCurrentCategory = async () => {
    categoryUser.value = await getCategoryUser(
      store.state.questionnaire.idCurrentDetailCategory
    )
  }

  let getShowDialog = ref()
  getShowDialog = computed(() => {
    return props.showDialog
  })

  const clearInputValues = (): void => {
    file.value = undefined
    nameFile.value = undefined
    typeFile.value = undefined
    quantityValue.value = undefined
    prizePlace.value = undefined
    coefficient.value = undefined
    internetResourceLink.value = undefined
    categoryUserForm.value?.resetValidation()
  }

  const closeDialog = () => {
    store.commit('questionnaire/closeDialogUploadFileToCategory')
    clearInputValues()
  }

  const onSubmit = () => {
    void categoryUserForm.value?.validate().then((success: boolean) => {
      if (success && categoryUser.value?.id !== undefined) {
        showProgressBtn.value = true
        if (
          categoryUser.value?.categoryQuestionnaire
            ?.internetResourceLinkOrDoc === true
        ) {
          if (
            file.value === undefined &&
            internetResourceLink.value === undefined
          ) {
            showProgressBtn.value = false
            return $q.notify({
              type: 'error',
              message: 'Загрузите файл или введите ссыслку на интернет-ресурс',
              color: 'red',
              position: 'top',
              timeout: 7000
            })
          }
        } else {
          showProgressBtn.value = false
          if (file.value === undefined) {
            return $q.notify({
              type: 'error',
              message: 'Загрузите файл',
              color: 'red',
              position: 'top',
              timeout: 7000
            })
          }
        }

        const data: IFileCategoryQuestionnaireUserPatch = {
          file: file.value,
          name: nameFile.value,
          typeFile: typeFile.value?.id,
          quantityValue: quantityValue.value,
          prizePlace: prizePlace.value?.id,
          coefficient: coefficient.value,
          internetResourceLink: internetResourceLink.value
        }
        console.log(data)

        uploadFileForCategoryUser(data, categoryUser.value.id)
          .then(() => {
            closeDialog()
            showProgressBtn.value = false
            emit('updateFileCategoryUser')
            void store.dispatch(
              'questionnaire/getQuestionnaireUser',
              idQuestionnaireUser
            )
          })
          .catch(() => {
            showProgressBtn.value = false
          })
      }
    })
  }
</script>
