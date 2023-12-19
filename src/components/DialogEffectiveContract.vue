<template>
  <q-dialog
    v-model="showDialogEffectiveContract"
    no-backdrop-dismiss
    no-esc-dismiss
    class="dialog-effective-contract"
  >
    <q-card
      style="
        width: 600px;
        max-width: 80vw;
        min-height: 220px;
        box-shadow: none;
        display: flex;
        flex-direction: column;
        justify-content: center;
      "
    >
      <q-card-section class="row items-center q-pb-none">
        <h3>
          Чтобы продолжить заполнение анкеты, подтвердите, что Вы заполнили
          эффективный контракт
        </h3>
      </q-card-section>
      <q-card-section class="row items-center q-pb-none">
        <q-btn
          class="q-mr-sm"
          color="green"
          @click="sendEffectiveContract"
          label="Подтверждаю"
        />
        <q-btn
          color="primary"
          href="https://docs.google.com/forms/d/e/1FAIpQLSfcKzu0BpS7Bo0pw2gxwKWlnmJSNXsHOv54ftUA-3e5aD6wgQ/viewform?usp=sf_link"
          target="_blank"
          label="Заполнить эффективный контракт"
        />
      </q-card-section>
    </q-card>
  </q-dialog>
</template>

<script setup lang="ts">
  import { useQuestionnaire } from 'composables/useQuestionnaire'
  // import { ICategoryDialog, IFile } from 'src/types/questionnaire'
  import { computed, ref } from 'vue'
  import { useStore } from '../store/index'

  const store = useStore()

  const { confirmEffectiveContract } = useQuestionnaire()
  const effectiveContract = computed(
    () => store.state.questionnaire?.effectiveContract
  )
  const statusQuestionnaire = computed(
    () => store.state.questionnaire?.info.status
  )
  const isCheckingUser = computed(
    // eslint-disable-next-line @typescript-eslint/no-unsafe-member-access
    (): any => store.getters['auth/isCheckingUser']
  )
  const showDialogEffectiveContract = computed(() => {
    if (
      effectiveContract.value !== true &&
      statusQuestionnaire.value === 1 &&
      !isCheckingUser.value
    ) {
      return true
    }
    return false
  })
  const sendEffectiveContract = () => {
    let idQuestionnaire = ref<number>()
    idQuestionnaire = computed(() => store.state.questionnaire?.id)
    if (idQuestionnaire.value !== undefined) {
      confirmEffectiveContract(idQuestionnaire.value)
        .then(() => {
          store.commit('questionnaire/confirmEffectiveContract')
        })
        .catch((e) => {
          console.error(e)
        })
    }
  }
</script>
