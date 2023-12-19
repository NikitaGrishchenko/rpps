<template>
  <q-page class="container">
    <BannerUnfilledPosition v-if="questionnaireUser.questionnaire !== null" />
    <q-banner
      v-if="
        questionnaireUser.questionnaire !== null &&
        questionnaireUser?.info?.status === 2
      "
      inline-actions
      class="text-white bg-red q-mb-xl"
    >
      <template v-slot:avatar>
        <q-icon name="mdi-alert-circle-outline" color="white" />
      </template>
      <h3>Анкетирование окончено</h3>
    </q-banner>
    <div class="row" v-if="questionnaireUser.questionnaire !== null">
      <QuestionnaireUserHeader
        :statistics="questionnaireUser?.statistics"
        :userPosition="questionnaireUser?.userPosition"
        :info="questionnaireUser?.info"
      />
      <QuestionnaireUserTable
        :questionnaire="questionnaireUser?.questionnaire"
      />
    </div>
    <q-inner-loading :showing="questionnaireUser.questionnaire === null">
      <q-spinner-puff class="fixed-center" size="50px" color="primary" />
    </q-inner-loading>
  </q-page>
</template>

<script setup lang="ts">
  import { onMounted, computed } from 'vue'
  import { useRoute } from 'vue-router'
  import QuestionnaireUserHeader from 'components/QuestionnaireUserHeader.vue'
  import QuestionnaireUserTable from 'components/QuestionnaireUserTable.vue'
  import { useStore } from '../store/index'
  import BannerUnfilledPosition from 'components/BannerUnfilledPosition.vue'
  // import { IMainCategory } from 'src/types/questionnaire'

  const store = useStore()

  const route = useRoute()

  const idQuestionnaire = Number(route.params.idQuestionnaire)

  const questionnaireUser = computed({
    get: () => store.state.questionnaire,
    set: (val) => {
      store.commit('questionnaireModule/getQuestionnaireUser', val)
    }
  })

  onMounted(() => {
    void store.commit('questionnaire/deleteQuestionnaireUser')
    void store.dispatch('questionnaire/getQuestionnaireUser', idQuestionnaire)
    void store.dispatch('reference/getReferencePrizePlaces')
  })
</script>
