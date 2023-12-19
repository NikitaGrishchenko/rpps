<template>
  <div class="row q-col-gutter-x-sm" v-show="questionnaireUserList.length > 0">
    <div class="text-h2 section-title col-12 q-mb-md">Мои анкеты</div>
    <div
      class="col-12 col-sm-6 col-md-4 col-lg-3 q-mb-md"
      v-for="item in questionnaireUserList"
      :key="item.id"
    >
      <div
        class="questionnaire-user-list__card"
        @click="goToQuestionnaire(item.id)"
      >
        <img
          v-if="item.questionnaire.previewImage"
          :src="item.questionnaire.previewImage"
          class="questionnaire-user-list__preview--img"
        />
        <div v-else class="questionnaire-user-list__preview--text">
          {{ item.questionnaire.name }}
        </div>
        <div class="questionnaire-user-list__info">
          <div
            v-if="item.questionnaire.status === 2"
            class="questionnaire-user-list__closed"
          >
            Анкетирование окончено
          </div>
          <div class="flex column items-center text-center">
            <p class="questionnaire-user-list__department">
              {{ item.userPosition?.department?.name }}
            </p>
            <p class="questionnaire-user-list__position">
              {{ item.userPosition?.position?.name }}
            </p>
          </div>
          <div class="questionnaire-user-list__raiting-primary">
            <span class="questionnaire-user-list__raiting--major">
              {{ item.statistics?.fullness.points }}
            </span>
            <span class="questionnaire-user-list__raiting--minor"
              >/{{ item.statistics?.fullnessPercentages.points }}
            </span>
          </div>
          <div class="questionnaire-user-list__raiting-secondary">
            <div class="questionnaire-user-list__raiting-secondary-category">
              <span class="questionnaire-user-list__raiting--minor">НИР</span>
              <span class="questionnaire-user-list__raiting--major">
                {{ item.statistics?.NIR.points }}
              </span>
            </div>
            <div class="questionnaire-user-list__raiting-secondary-category">
              <span class="questionnaire-user-list__raiting--minor">УМР</span>
              <span class="questionnaire-user-list__raiting--major">
                {{ item.statistics?.UMR.points }}
              </span>
            </div>
            <div class="questionnaire-user-list__raiting-secondary-category">
              <span class="questionnaire-user-list__raiting--minor">ВР</span>
              <span class="questionnaire-user-list__raiting--major">
                {{ item.statistics?.VR.points }}
              </span>
            </div>
            <div class="questionnaire-user-list__raiting-secondary-category">
              <span class="questionnaire-user-list__raiting--minor">ЛДиУМ</span>
              <span class="questionnaire-user-list__raiting--major">
                {{ item.statistics?.LDiUM.points }}
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <q-inner-loading :showing="Object.keys(questionnaireUserList).length === 0">
    <q-spinner-puff class="fixed-center" size="50px" color="primary" />
  </q-inner-loading>
</template>

<script setup lang="ts">
  import { useQuestionnaire } from 'composables/useQuestionnaire'
  import { IQuestionnaireUserList } from 'types/questionnaire'
  import { onMounted, ref } from 'vue'
  import { useRouter } from 'vue-router'
  import _ from 'lodash'

  const { getQuestionnaireUserList } = useQuestionnaire()

  const router = useRouter()

  const goToQuestionnaire = (idQuestionnaire: number) => {
    void router.push({
      name: 'QuestionnaireUserPage',
      params: { idQuestionnaire: idQuestionnaire }
    })
  }

  const questionnaireUserList = ref<IQuestionnaireUserList[]>([])
  onMounted(async () => {
    const data = await getQuestionnaireUserList()
    if (data) {
      questionnaireUserList.value = _.reverse(
        _.orderBy(data, 'questionnaire.id')
      )
    }
  })
</script>
