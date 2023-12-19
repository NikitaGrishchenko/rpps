<template>
  <q-dialog
    v-model="getShowDialog"
    @show="setCurrentCategory()"
    no-backdrop-dismiss
    no-esc-dismiss
  >
    <q-card style="width: 700px; box-shadow: none">
      <q-card-section class="row items-center q-pb-none">
        <div class="text-h4">Прикрепить существующий файл</div>
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
          <q-select
            popup-content-class="input-textfield"
            class="input-textfield"
            v-model="fileId"
            :options="files"
            label="Выберите файл"
            option-label="name"
            :rules="[(val) => !!val || 'Обязательное поле']"
            option-value="id"
          />
          <q-input
            v-if="categoryUser?.categoryQuestionnaire?.typeCategory === 3"
            v-model="quantityValue"
            type="number"
            label="Введите число"
            :rules="[(val) => !!val || 'Обязательное поле']"
            lazy-rules
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
          <q-input
            v-if="
              categoryUser?.categoryQuestionnaire?.useInternetResourceLink ===
              true
            "
            v-model="internetResourceLink"
            label="Ссылка"
            ref="internetResourceLinkRef"
            :rules="[isValidInternetResourceLink]"
            lazy-rules
          />
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
    IFileSelect
  } from 'src/types/questionnaire'
  import { computed, ref, onMounted } from 'vue'
  import { QForm } from 'quasar'
  import { useStore } from '../store/index'
  import { useRoute } from 'vue-router'
  import { useFile } from 'composables/useFile'
  const route = useRoute()
  const store = useStore()
  const { getFiles } = useFile()
  const {
    getCategoryUser,
    attachFileForCategoryUser,
    isValidInternetResourceLink,
    isValidCoefficient
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

  let files = ref<IFileSelect[] | undefined>()

  const quantityValue = ref<number>()
  const prizePlace = ref<IPrizePlace>()
  const coefficient = ref<number>()
  const fileId = ref<IFileSelect>()
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
    quantityValue.value = undefined
    fileId.value = undefined
    prizePlace.value = undefined
    coefficient.value = undefined
    internetResourceLink.value = undefined
    categoryUserForm.value?.resetValidation()
  }

  const closeDialog = () => {
    store.commit('questionnaire/closeDialogAttachExistingFile')
    clearInputValues()
  }

  const onSubmit = () => {
    void categoryUserForm.value?.validate().then((success: boolean) => {
      if (success && categoryUser.value?.id !== undefined) {
        showProgressBtn.value = true
        const data: IFileCategoryQuestionnaireUserPatch = {
          quantityValue: quantityValue.value ?? null,
          prizePlace: prizePlace.value?.id ?? null,
          coefficient: coefficient.value ?? null,
          internetResourceLink: internetResourceLink.value ?? null,
          fileId: fileId.value?.id
        }
        attachFileForCategoryUser(data, categoryUser.value.id)
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
  onMounted(() => {
    getFiles()
      .then((data) => {
        files.value = data
      })
      .catch((e) => {
        console.log(e)
      })
  })
</script>
