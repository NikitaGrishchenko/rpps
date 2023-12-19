<template>
  <div class="dialog-detail-category-file">
    <div class="row items-center w-100">
      <div class="col-1 text-center">
        <p v-if="props?.index" class="category-file__index">
          {{ props?.index }}
        </p>
      </div>
      <div class="col-6">
        <a
          :href="props?.file?.file?.file"
          target="_blank"
          class="category-file__name"
        >
          {{ props.file?.file?.name }}
        </a>
        <p class="category-file__link">
          <a :href="`${internetResourceLink}`" target="_blank">{{
            internetResourceLink
          }}</a>
        </p>
      </div>
      <div class="col-3 text-center">
        <div
          class="category-file__coefficient"
          v-if="props?.typeCategory === 1"
        >
          <p class="category-file__label">Процент соавторства:</p>
          {{ coefficient }}
        </div>
        <div
          class="category-file__prize-places"
          v-if="props?.typeCategory === 2"
        >
          <p class="category-file__label">Призовое место:</p>
          {{ prizePlace?.name }}
        </div>
        <div
          class="category-file__quantity-value"
          v-if="props?.typeCategory === 3"
        >
          <p class="category-file__label">Число:</p>
          {{ quantityValue }}
        </div>
      </div>
      <div class="col-2">
        <q-btn
          v-show="questionnaireClosed === 1 && !isCheckingUser"
          class="category-file-btn--change"
          @click="openDialogChangeFileCategory"
          outline
          color="primary"
          label="Изменить"
        />
      </div>
    </div>
    <q-icon
      v-show="questionnaireClosed === 1 && !isCheckingUser"
      class="category-file-btn--delete"
      @click="deleteFile"
      name="mdi-trash-can-outline"
      size="22px"
    />
  </div>
</template>

<script setup lang="ts">
  import {
    IFileCategoryQuestionnaireUser,
    IPrizePlace
  } from 'src/types/questionnaire'
  import { PropType, ref, computed } from 'vue'
  import { useStore } from '../store/index'
  import { useQuestionnaire } from 'composables/useQuestionnaire'
  import { useQuasar } from 'quasar'
  import { useRoute } from 'vue-router'

  const route = useRoute()
  const $q = useQuasar()
  const store = useStore()
  const { deleteFileForCategoryUser } = useQuestionnaire()

  const emit = defineEmits(['updateFileCategoryUser'])

  const props = defineProps({
    file: Object as PropType<IFileCategoryQuestionnaireUser>,
    typeCategory: Number,
    useInternetResourceLink: Boolean,
    internetResourceLinkOrDoc: Boolean,
    index: Number
  })

  const isCheckingUser = computed(
    // eslint-disable-next-line @typescript-eslint/no-unsafe-member-access
    (): any => store.getters['auth/isCheckingUser']
  )

  const idQuestionnaire = Number(route.params.idQuestionnaire)

  const quantityValue = ref<number | null | undefined>(
    props.file?.quantityValue
  )
  const prizePlace = ref<IPrizePlace | null | undefined>(props.file?.prizePlace)
  const coefficient = ref<number | null | undefined>(props.file?.coefficient)
  const internetResourceLink = ref<string | null | undefined>(
    props.file?.internetResourceLink
  )

  const questionnaireClosed = computed(
    () => store.state.questionnaire.info.status
  )

  const deleteFile = () => {
    $q.dialog({
      title: 'Подтверждение',
      message: 'Вы уверены, что хотите открепить файл от категории?',
      style: 'font-size: 1.6rem',
      ok: {
        push: true,
        label: 'Да',
        color: 'negative'
      },
      cancel: {
        push: true,
        label: 'Отменить'
      },
      persistent: true
    })
      .onOk(() => {
        deleteFileForCategoryUser(props.file?.id)
          .then(() => {
            emit('updateFileCategoryUser')
            void store.dispatch(
              'questionnaire/getQuestionnaireUser',
              idQuestionnaire
            )
          })
          .catch((e) => {
            console.error(e)
          })
      })
      .onCancel(() => {
        // console.log('>>>> Cancel')
      })
  }

  const openDialogChangeFileCategory = () => {
    store.commit('questionnaire/setCurrentChangeFileCategory', {
      id: props.file?.id,
      typeCategory: props.typeCategory,
      useInternetResourceLink: props.useInternetResourceLink,
      internetResourceLinkOrDoc: props.internetResourceLinkOrDoc
    })
    store.commit('questionnaire/openDialogChangeFileCategory')
  }
</script>
