<template>
  <q-page class="container">
    <div v-if="department" class="row">
      <div class="col-12 q-mb-md">
        <h1>
          Кафедра
          <strong> {{ toLowerCaseString(department?.name) }}</strong>
        </h1>
        <q-btn-dropdown
          class="q-mt-sm"
          size="16px"
          flat
          icon="mdi-microsoft-excel"
          dense
          label="Отчёт"
        >
          <q-list dense>
            <q-item
              v-for="questionnaire in questionnaireList"
              :key="questionnaire.id"
              clickable
              v-close-popup
              @click="
                generateDepartmentReport(department?.id, questionnaire.id)
              "
            >
              <q-item-section padding>
                <q-item-label class="text-h5">{{
                  questionnaire.name
                }}</q-item-label>
              </q-item-section>
            </q-item>
          </q-list>
        </q-btn-dropdown>
      </div>
      <div style="font-size: 1.6rem" class="col-12">
        <div class="q-pa-md">
          <q-list bordered padding separator>
            <q-item
              v-for="(userPosition, index) in sortedUserPositions"
              :key="userPosition.id"
            >
              <q-item-section>
                <div class="flex items-center">
                  <div style="min-width: 30px" class="q-mr-md text-center">
                    <strong>{{ index + 1 }}</strong>
                  </div>
                  <div>
                    <q-item-label
                      >{{ userPosition?.user?.lastName }}
                      {{ userPosition?.user?.firstName }}
                      {{ userPosition?.user?.patronymic }}</q-item-label
                    >
                    <q-item-label
                      :class="getPositionColor(userPosition?.position?.id)"
                    >
                      {{ userPosition?.position?.name }}</q-item-label
                    >
                  </div>
                </div>
              </q-item-section>
              <q-separator spaced />
              <q-item-section
                style="flex-direction: initial; justify-content: start"
              >
                <q-chip
                  v-for="questionnaire in sortedQuestionnaireUser(
                    userPosition.questionnaireUser
                  )"
                  :key="questionnaire.id"
                  @click="goToQuestionnaire(questionnaire.id)"
                  color="primary"
                  text-color="white"
                  style="width: max-content"
                  clickable
                  >{{ questionnaire?.questionnaire?.name }}</q-chip
                >
              </q-item-section>
            </q-item>
          </q-list>
        </div>
      </div>
    </div>
    <q-inner-loading :showing="department === undefined">
      <q-spinner-puff class="fixed-center" size="50px" color="primary" />
    </q-inner-loading>
  </q-page>
</template>

<script setup lang="ts">
  import {
    IDepartmentOfList,
    IUserPosition,
    IQuestionnaireUserList,
    IQuestionnaireBase
  } from 'types/questionnaire'
  import { useQuestionnaire } from 'composables/useQuestionnaire'
  import { onMounted, ref, computed } from 'vue'
  import { useRoute } from 'vue-router'
  import _ from 'lodash'
  import { useRouter } from 'vue-router'
  const router = useRouter()

  const route = useRoute()

  const id_department = Number(route.params.id_department)

  const {
    getListOfDepartment,
    getPositionColor,
    getQuestionnaireAllList,
    generateDepartmentReport
  } = useQuestionnaire()

  const questionnaireList = ref<IQuestionnaireBase[]>()

  const department = ref<IDepartmentOfList>()
  const userPositions = ref<IUserPosition[]>()

  const sortedUserPositions = computed(() => {
    return _.orderBy(userPositions?.value, 'user.lastName')
  })

  const sortedQuestionnaireUser = (
    questionnaireUser: IQuestionnaireUserList
  ) => {
    return _.orderBy(questionnaireUser, 'id').reverse()
  }

  const toLowerCaseString = (str: string) => {
    if (str !== undefined) {
      return str.toLowerCase()
    }
  }

  const goToQuestionnaire = (idQuestionnaire: number) => {
    void router.push({
      name: 'QuestionnaireUserPage',
      params: { idQuestionnaire: idQuestionnaire }
    })
  }

  onMounted(async () => {
    department.value = await getListOfDepartment(id_department)
    questionnaireList.value = await getQuestionnaireAllList()
    userPositions.value = department.value?.userPositions
  })
</script>
