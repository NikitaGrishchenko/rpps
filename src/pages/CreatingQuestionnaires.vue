<template>
  <q-page class="container">
    <div class="text-primary text-bold text-h4 q-pb-md">Создание анкет</div>
    <div class="row">
      <div class="col-9">
        <q-select
          v-model="selectedQuestionnaires"
          :options="questionnaireAllList"
          label="Выберите анкету"
          option-value="id"
          option-label="name"
          emit-value
          map-options
          multiple
        />
        {{ selectedUserPositions }}
        {{ selectedQuestionnaires }}
      </div>
      <div class="col-3">
        <q-btn
          class="q-mt-md main-btn"
          type="submit"
          color="white"
          text-color="black"
          @click="submit"
        >
          Создать анкету для выбранных пользователей
          <template v-slot:loading>
            <q-spinner-puff />
          </template>
        </q-btn>
      </div>
      <div class="col-12 q-mt-md">
        <table style="font-size: 16px">
          <thead>
            <tr>
              <th class="text-left">
                <q-btn @click="allSelected" small color="primary"
                  >Выбрать всех</q-btn
                >
              </th>
              <th class="text-left">Логин</th>
              <th class="text-left">ФИО</th>
              <th class="text-left">Кафедра</th>
              <th class="text-left">Должность</th>
              <th class="text-left">Ставка</th>
              <th class="text-left">
                Анкеты, в которых участвует пользователь
              </th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="item in userPositions"
              :key="item.id"
              style="border-top: 1px solid #aeaeae"
            >
              <td>
                <q-checkbox
                  v-model="selectedUserPositions"
                  :val="item.id"
                ></q-checkbox>
              </td>
              <td>{{ item.user.username }}</td>
              <td>
                {{ item.user.lastName }}
                {{ item.user.firstName }}
                {{ item.user.patronymic }}
              </td>
              <td v-if="item.department == null"></td>
              <td v-else>{{ item.department.name }}</td>
              <td v-if="item.position == null"></td>
              <td v-else>{{ item.position.name }}</td>
              <td v-if="item.rate == null"></td>
              <td v-else>{{ item.rate.value }}</td>
              <td>
                <q-chip
                  v-for="questionnaireUser in item.questionnaireUser"
                  :key="questionnaireUser.id"
                >
                  {{ questionnaireUser.questionnaire.name }}
                </q-chip>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <q-inner-loading :showing="inProcess">
        <q-spinner-puff class="fixed-center" size="50px" color="primary" />
      </q-inner-loading>
    </div>
  </q-page>
</template>

<script setup lang="ts">
  import { useQuestionnaire } from 'composables/useQuestionnaire'
  import { onMounted, ref } from 'vue'
  import { api } from 'boot/axios'
  const { getQuestionnaireAllList, getAllUserPosition, inProcess } =
    useQuestionnaire()

  const selectedQuestionnaires = ref<any[]>([])
  const selectedUserPositions = ref<any[]>([])

  const userPositions = ref<any>()
  const questionnaireAllList = ref<any>()

  const allSelected = () => {
    selectedUserPositions.value = userPositions.value.map((u) => u.id)
    console.log(selectedUserPositions.value.length)
  }

  const submit = () => {
    const resultData = {
      userPositions: selectedUserPositions.value,
      questionnairesUsers: selectedQuestionnaires.value
    }
    console.log(resultData)

    api
      .post('questionnaire/creation-for-all/', resultData)
      .then(() => {
        selectedQuestionnaires.value = []
        selectedUserPositions.value = []
      })
      .catch((e) => {
        console.log(e)
      })
  }

  onMounted(async () => {
    userPositions.value = await getAllUserPosition()
    questionnaireAllList.value = await getQuestionnaireAllList()
  })
</script>
