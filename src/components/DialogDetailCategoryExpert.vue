<template>
  <div class="dialog-detail-category-expert">
    <div class="row">
      <div class="col-12 flex justify-around">
        <div class="expert-card">
          <p
            :style="
              props.resultPointFixed !== null
                ? 'color: grey;'
                : 'color: #31498B;'
            "
            class="expert-card__point"
          >
            {{ props.resultPoint.toFixed(1) }}
          </p>
          <p class="expert-card__title">Фактический балл</p>
        </div>
        <div class="expert-card">
          <input
            class="expert-form__result-point-fixed"
            type="number"
            outlined
            min="0"
            v-model="changedResultPointFixed"
            dense
          />
          <p class="expert-card__title">Отредактированный балл</p>
        </div>
        <div class="expert-card">
          <div class="expert-card__toggles">
            <q-icon
              @click="changedIsVerified = true"
              name="mdi-check-circle-outline"
              :color="changedIsVerified === true ? 'green' : 'grey'"
              size="30px"
            />
            <q-icon
              @click="changedIsVerified = false"
              name="mdi-close-circle-outline"
              :color="changedIsVerified === false ? 'red' : 'grey'"
              size="30px"
            />
          </div>
          <p class="expert-card__title">Категория проверена?</p>
        </div>
      </div>
      <div class="col-12 q-pa-md">
        <q-btn
          @click="onSubmit"
          :loading="isLoading"
          class="main-btn q-mt-md"
          label="Сохранить"
        />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
  import { ref } from 'vue'
  import { ICategoryUser } from 'src/types/questionnaire'
  import { useQuestionnaire } from 'composables/useQuestionnaire'
  import { useStore } from '../store/index'
  import { useRoute } from 'vue-router'
  import { useQuasar } from 'quasar'

  const { updateCategoryUser } = useQuestionnaire()
  const store = useStore()
  const route = useRoute()
  const $q = useQuasar()

  const emit = defineEmits(['closeDialogDetailCategory'])

  const idQuestionnaire = Number(route.params.idQuestionnaire)

  const isLoading = ref<boolean>(false)

  const props = defineProps({
    resultPoint: {
      type: Number,
      required: true
    },
    resultPointFixed: {
      type: Number,
      required: false
    },
    isVerified: {
      type: Boolean,
      required: false
    }
  })

  const changedIsVerified = ref<boolean | null | undefined>(props.isVerified)
  const changedResultPointFixed = ref<string | number | null | undefined>(
    props.resultPointFixed
  )

  const onSubmit = () => {
    isLoading.value = true
    if (changedResultPointFixed.value && changedResultPointFixed.value < 0) {
      changedResultPointFixed.value = undefined
      isLoading.value = false
      return $q.notify({
        type: 'error',
        message: 'Введите значение, которое больше либо равно нулю',
        color: 'red',
        position: 'top-right'
      })
    }
    const dataCategory: ICategoryUser = {
      isVerified: changedIsVerified.value,
      resultPointFixed:
        changedResultPointFixed.value === ''
          ? null
          : changedResultPointFixed.value
    }

    updateCategoryUser(
      store.state.questionnaire.idCurrentDetailCategory,
      dataCategory
    )
      .then(() => {
        emit('closeDialogDetailCategory')
        void store.dispatch(
          'questionnaire/getQuestionnaireUser',
          idQuestionnaire
        )
      })
      .catch((e) => {
        console.error(e)
      })
      .finally(() => (isLoading.value = false))
  }
</script>

<style lang="sass">
  input[type='number']
    -moz-appearance: textfield

  input::-webkit-outer-spin-button,
  input::-webkit-inner-spin-button
    -webkit-appearance: none
</style>
