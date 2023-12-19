<template>
  <div class="col-12">
    <div class="row">
      <div class="col-12">
        <p></p>
        <p class="questionnaire-statistic__user-department">
          Кафедра
          {{ toLowerCaseString(props?.userPosition?.department?.name) }}
          <strong>{{ props?.info?.name }}</strong>
        </p>
      </div>
      <div class="col-12">
        <p class="questionnaire-statistic__user-info section-title">
          {{ props.userPosition?.user?.lastName }}
          {{ props.userPosition?.user?.firstName }}
          {{ props.userPosition?.user?.patronymic }}
        </p>
      </div>
    </div>
  </div>
  <div class="col-12">
    <ul class="row questionnaire-statistic">
      <div class="col-3">
        <div class="questionnaire-statistic__left-block">
          <p class="questionnaire-statistic__left-block__points">
            {{ props.statistics?.fullness?.points }}
          </p>
          /
          <p class="questionnaire-statistic__left-block__percentages">
            {{ props.statistics?.fullnessPercentages?.points }}
          </p>
        </div>
      </div>
      <div class="col-6">
        <ul class="questionnaire-statistic__center-block">
          <li class="questionnaire-statistic__center-block__item">
            <p class="questionnaire-statistic__center-block__name">
              {{ props.statistics?.NIR?.name }}
            </p>
            <p class="questionnaire-statistic__center-block__points">
              {{ props.statistics?.NIR?.points }}
            </p>
          </li>
          <li class="questionnaire-statistic__center-block__item">
            <p class="questionnaire-statistic__center-block__name">
              {{ props.statistics?.UMR?.name }}
            </p>
            <p class="questionnaire-statistic__center-block__points">
              {{ props.statistics?.UMR?.points }}
            </p>
          </li>
          <li class="questionnaire-statistic__center-block__item">
            <p class="questionnaire-statistic__center-block__name">
              {{ props.statistics?.VR?.name }}
            </p>
            <p class="questionnaire-statistic__center-block__points">
              {{ props.statistics?.VR?.points }}
            </p>
          </li>
          <li class="questionnaire-statistic__center-block__item">
            <p class="questionnaire-statistic__center-block__name">
              {{ props.statistics?.LDiUM?.name }}
            </p>
            <p class="questionnaire-statistic__center-block__points">
              {{ props.statistics?.LDiUM?.points }}
            </p>
          </li>
          <li class="questionnaire-statistic__center-block__item">
            <p class="questionnaire-statistic__center-block__name">
              {{ props.statistics?.totalScore?.name }}
            </p>
            <p class="questionnaire-statistic__center-block__points">
              {{ props.statistics?.totalScore?.points }}
            </p>
          </li>
        </ul>
      </div>
      <div class="col-3">
        <a
          link
          class="questionnaire-statistic__button"
          @click="generateReport(idQuestionnaireUser)"
          target="_blank"
        >
          <q-icon name="mdi-printer-outline" size="20px" />

          <p class="questionnaire-statistic__button__p">Распечатать анкету</p>
        </a>
      </div>
    </ul>
  </div>
  <br /><br />
</template>

<script setup lang="ts">
  import {
    IQuestionnaireInfo,
    IStatisticsQuestionnaire,
    IUserPosition
  } from 'types/questionnaire'
  import { computed, PropType } from 'vue'
  import { useStore } from '../store/index'

  const store = useStore()

  const idQuestionnaireUser = computed<number | undefined>(
    () => store.state.questionnaire.id
  )

  const toLowerCaseString = (str: string | null | undefined) => {
    if (str) {
      return str.toLowerCase()
    }
  }

  const generateReport = (idQuestionnaireUser: number | undefined) => {
    if (idQuestionnaireUser !== undefined) {
      window.open(
        process.env.DEV
          ? 'http://localhost:8000/'
          : '' + `/api/v1/documents/questionnaire/${idQuestionnaireUser}/`,
        '_blank'
      )
    }
  }

  const props = defineProps({
    userPosition: Object as PropType<IUserPosition>,
    statistics: Object as PropType<IStatisticsQuestionnaire>,
    info: Object as PropType<IQuestionnaireInfo>
  })
</script>
