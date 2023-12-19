<template>
  <q-dialog
    v-model="showDialogChangeFileCategory"
    @show="setFileCategoryUser"
    no-backdrop-dismiss
    no-esc-dismiss
    class="dialog-change-category"
  >
    <q-card style="width: 600px; min-height: 300px; box-shadow: none">
      <q-card-section class="row items-center q-pb-none">
        <div class="text-h4">Изменить катогорию</div>
        !{{ useInternetResourceLink }} !{{ internetResourceLinkOrDoc }}
        <q-space />
        <q-btn
          @click="closeDialogUploadFileToCategory()"
          icon="close"
          flat
          round
          dense
          v-close-popup
        />
      </q-card-section>
      <q-card-section>
        <q-form v-if="file" ref="fileCategoryForm">
          <div
            class="dialog-change-category-file__coefficient"
            v-if="typeCategory === 1"
          >
            <q-input
              v-model="coefficient"
              label="Коэффициент соавторства"
              :rules="[isValidCoefficient]"
            />
          </div>
          <div
            class="dialog-change-category-file__prize-places"
            v-if="typeCategory === 2"
          >
            <q-select
              v-model="prizePlace"
              :options="referencePrizePlaces"
              class="input-textfield input-textfield--outlined"
              popup-content-class="input-textfield"
              outlined
              label="Призовое место"
              option-label="name"
              option-value="id"
              options-dense
              lazy-rules
            />
          </div>
          <div
            class="dialog-change-category-file__quantity-value"
            v-if="typeCategory === 3"
          >
            <q-input
              v-model="quantityValue"
              type="number"
              label="Введите число"
              :rules="[(val) => !!val || 'Обязательное поле']"
              lazy-rules
            />
          </div>
          <div
            v-if="useInternetResourceLink || internetResourceLinkOrDoc"
            class="dialog-change-category-file__link"
          >
            <q-input
              v-model="internetResourceLink"
              label="Ссылка на интернет-ресурс"
              lazy-rules
              :rules="[isValidInternetResourceLink]"
            />
          </div>
          <q-btn
            @click="updateFile"
            :loading="showProgressBtn"
            class="main-btn q-mt-md"
          >
            Сохранить
            <template v-slot:loading>
              <q-spinner-puff />
            </template>
          </q-btn>
        </q-form>
      </q-card-section>
      <q-inner-loading :showing="file == null">
        <q-spinner-puff class="fixed-center" size="50px" color="primary" />
      </q-inner-loading>
    </q-card>
  </q-dialog>
</template>

<script setup lang="ts">
  import { useQuestionnaire } from 'composables/useQuestionnaire'
  import { IPrizePlace } from 'src/types/questionnaire'
  import {
    IFileCategoryQuestionnaireUser,
    IFileCategoryQuestionnaireUserPatch
  } from 'src/types/questionnaire'
  import { computed, ref } from 'vue'
  import { useStore } from '../store/index'
  import { QForm } from 'quasar'
  import { useRoute } from 'vue-router'

  const route = useRoute()

  const store = useStore()
  const {
    getFileCategoryUser,
    isValidInternetResourceLink,
    isValidCoefficient,
    updateFileForCategoryUser
  } = useQuestionnaire()

  const emit = defineEmits(['updateFileCategoryUser'])

  const file = ref<IFileCategoryQuestionnaireUser | undefined>()
  const prizePlace = ref<IPrizePlace | null>()
  const quantityValue = ref<number | null | undefined>()
  const coefficient = ref<number | null | undefined>()
  const internetResourceLink = ref<string | null | undefined>()

  const setFileCategoryUser = async () => {
    file.value = undefined
    file.value = await getFileCategoryUser(
      store.state.questionnaire.currentChangeFileCategory.id
    )
    prizePlace.value = file.value?.prizePlace
    quantityValue.value = file.value?.quantityValue
    coefficient.value = file.value?.coefficient
    internetResourceLink.value = file.value?.internetResourceLink
  }

  const showProgressBtn = ref<boolean>(false)

  const fileCategoryForm = ref<QForm>()

  const typeCategory = computed<number | undefined>(
    () => store.state.questionnaire.currentChangeFileCategory.typeCategory
  )
  const showDialogChangeFileCategory = computed<boolean | undefined>(
    () => store.state.questionnaire.showDialogChangeFileCategory
  )
  const useInternetResourceLink = computed<boolean | undefined>(
    () =>
      store.state.questionnaire.currentChangeFileCategory
        .useInternetResourceLink
  )
  const internetResourceLinkOrDoc = computed<boolean | undefined>(
    () =>
      store.state.questionnaire.currentChangeFileCategory
        .internetResourceLinkOrDoc
  )
  const referencePrizePlaces = computed<IPrizePlace[] | undefined>(
    () => store.state.reference.prizePlaces
  )

  const updateFile = () => {
    void fileCategoryForm.value?.validate().then((success: boolean) => {
      if (success) {
        showProgressBtn.value = true
        const data: IFileCategoryQuestionnaireUserPatch = {
          quantityValue: quantityValue.value,
          prizePlace: prizePlace.value?.id ?? null,
          coefficient: coefficient.value,
          internetResourceLink: internetResourceLink.value
        }

        const idQuestionnaire = Number(route.params.idQuestionnaire)

        updateFileForCategoryUser(data, file.value?.id)
          .then(() => {
            void store.dispatch(
              'questionnaire/getQuestionnaireUser',
              idQuestionnaire
            )
            emit('updateFileCategoryUser')
            void closeDialogUploadFileToCategory()
          })
          .finally(() => {
            showProgressBtn.value = false
          })
      }
    })
  }

  const closeDialogUploadFileToCategory = () => {
    store.commit('questionnaire/closeDialogChangeFileCategory')
    store.commit('questionnaire/deleteCurrentChangeFileCategory')
    file.value = undefined
  }
</script>
