<template>
  <q-page class="container">
    <div class="row">
      <div class="col-12 q-mb-lg q-pl-sm">
        <h1>Регистрация пользователя</h1>
      </div>
      <div class="col-12">
        <q-form ref="registrationForm" @submit.prevent="onSubmit()">
          <div class="row">
            <div class="col-4 q-px-sm">
              <q-input
                outlined
                type="text"
                v-model="firstNameModel"
                :rules="[(val) => val?.length >= 2 || 'Минимум 2 символов']"
                label="Имя"
                lazy-rules
              />
            </div>
            <div class="col-4 q-px-sm">
              <q-input
                outlined
                type="text"
                v-model="lastNameModel"
                :rules="[(val) => val?.length >= 2 || 'Минимум 2 символа']"
                label="Фамилия"
                lazy-rules
              />
            </div>
            <div class="col-4 q-px-sm">
              <q-input
                outlined
                type="text"
                v-model="patronymicModel"
                label="Отчество"
              />
            </div>
            <div class="col-6 q-px-sm">
              <q-input
                outlined
                type="text"
                v-model="usernameModel"
                :rules="[isValidEmail]"
                label="Электронная почта"
                lazy-rules
              />
              <!-- @blur="checkIsExistUsername(usernameModel)" -->
            </div>
            <div class="col-6 q-px-sm">
              <q-input
                outlined
                :type="isPassword ? 'password' : 'text'"
                v-model="passwordModel"
                :rules="[(val) => val?.length >= 8 || 'Минимум 8 символов']"
                label="Пароль"
                lazy-rules
              >
                <template v-slot:after>
                  <q-icon
                    :name="isPassword ? 'mdi-eye-off' : 'mdi-eye'"
                    class="cursor-pointer"
                    @click="isPassword = !isPassword"
                  />
                </template>
              </q-input>
            </div>
            <div class="col-12 q-mb-md q-pl-sm">
              <h3>Должности пользователя</h3>
            </div>
            <div v-if="userPositionsModel.length === 0" class="col-12 q-px-sm">
              <p class="user-registration-positions--warning text-red">
                Добавьте должность(-и)!
              </p>
            </div>
            <div
              v-for="(item, index) in userPositionsModel"
              :key="item"
              class="col-12 q-px-sm"
            >
              <p class="user-registration-positions">
                {{ index + 1 }}.
                <strong>{{ item?.position?.name }}</strong>
                кафедры <strong>{{ item?.department?.name }}</strong> ставка
                <strong>{{ item?.rate?.value }}</strong>
              </p>
            </div>
            <div class="col-12">
              <div class="row">
                <div class="col-6 q-px-sm">
                  <q-select
                    v-model="departmentModel"
                    outlined
                    label="Кафедра"
                    popup-content-class="input-textfield"
                    :options="reference['departments']"
                    option-label="name"
                    option-value="id"
                    lazy-rules
                  />
                </div>
                <div class="col-6 q-px-sm">
                  <q-select
                    v-model="positionModel"
                    outlined
                    popup-content-class="input-textfield"
                    label="Должность"
                    :options="reference['positions']"
                    option-label="name"
                    option-value="id"
                    lazy-rules
                  />
                </div>
              </div>
              <div class="row q-pt-md">
                <div class="col-6 q-px-sm">
                  <q-select
                    v-model="rateModel"
                    outlined
                    popup-content-class="input-textfield"
                    label="Ставка"
                    :options="reference['rates']"
                    option-label="value"
                    option-value="id"
                    lazy-rules
                  />
                </div>
                <div class="col-6 q-px-sm">
                  <div
                    class="user-registration-btn"
                    @click="addUserPosition"
                    style="height: 100%"
                  >
                    Добавить
                  </div>
                </div>
              </div>
            </div>
            <div class="col-12 q-my-md q-pl-sm">
              <h3>Анкеты пользователя</h3>
            </div>
            <div class="col-6 q-pl-sm">
              <q-select
                :disable="userPositionsModel.length === 0"
                v-model="questionnairesUserModel"
                outlined
                multiple
                popup-content-class="input-textfield"
                :options="questionnaireUserOptions"
                :rules="[(val) => val?.length > 0 || 'Обязательное поле!']"
                option-label="name"
                option-value="id"
                label="Выберите анкету(-ы)"
              />
            </div>
          </div>
          <div class="col-12 q-pl-sm">
            <q-btn
              class="q-my-md"
              label="Создать"
              size="lg"
              type="submit"
              color="primary"
            >
              <q-icon name="mdi-account-multiple-plus q-ml-md" size="20px" />
            </q-btn>
          </div>
        </q-form>
      </div>
    </div>
  </q-page>
</template>

<script setup lang="ts">
  import { QForm, Notify } from 'quasar'
  import { ref, onMounted } from 'vue'
  import { useReference } from 'src/composables/useReference'
  import { useQuestionnaire } from 'composables/useQuestionnaire'
  import { useAuth } from 'composables/useAuth'
  import { IQuestionnaireBase } from 'types/questionnaire'
  import {
    IDepartment,
    IPosition,
    IRate,
    IUserPositionRegistration
  } from 'types/questionnaire'
  // import { api } from 'boot/axios'

  const { reference } = useReference(['rates', 'positions', 'departments'])
  const questionnaireUserOptions = ref<IQuestionnaireBase[] | undefined>()
  const {
    getQuestionnaireAllList,
    userPositionsToSend,
    questionnaireToSend,
    isValidEmail
  } = useQuestionnaire()
  const { createUserquestionnaire } = useAuth()

  const registrationForm = ref<QForm>()
  const isPassword = ref<boolean>(true)

  const firstNameModel = ref<string>()
  const lastNameModel = ref<string>()
  const patronymicModel = ref<string>()
  const usernameModel = ref<string>()
  const passwordModel = ref<string>()
  const questionnairesUserModel = ref<IQuestionnaireBase[]>([])
  const userPositionsModel = ref<IUserPositionRegistration[]>([])

  const departmentModel = ref<IDepartment | undefined>()
  const positionModel = ref<IPosition | undefined>()
  const rateModel = ref<IRate | undefined>()

  const onSubmit = () => {
    void registrationForm.value?.validate().then((success: boolean) => {
      if (userPositionsModel.value.length === 0) {
        return Notify.create({
          position: 'top',
          type: 'negative',
          message: 'Добавьте должности пользователя'
        })
      }
      if (success) {
        const resultData = {
          userPositions: userPositionsToSend(userPositionsModel.value),
          questionnaire: questionnaireToSend(questionnairesUserModel.value),
          password: passwordModel.value,
          username: usernameModel.value,
          firstName: firstNameModel.value,
          lastName: lastNameModel.value,
          patronymic: patronymicModel.value ?? null,
          userImage: null
        }
        createUserquestionnaire(resultData)
          .then(() => {
            firstNameModel.value = undefined
            lastNameModel.value = undefined
            patronymicModel.value = undefined
            usernameModel.value = undefined
            passwordModel.value = undefined
            questionnairesUserModel.value = []
            userPositionsModel.value = []
            registrationForm.value?.resetValidation()
          })
          .catch((e) => {
            console.error(e)
          })
      }
    })
  }

  const addUserPosition = () => {
    if (departmentModel.value && positionModel.value && rateModel.value) {
      for (let x = 0; x < userPositionsModel.value.length; x++) {
        if (
          userPositionsModel.value[x].department === departmentModel.value &&
          userPositionsModel.value[x].position === positionModel.value &&
          userPositionsModel.value[x].rate === rateModel.value
        ) {
          return Notify.create({
            position: 'top',
            type: 'negative',
            message: 'Такая должность уже добавлена'
          })
        }
      }
      userPositionsModel.value &&
        userPositionsModel.value.push({
          department: departmentModel.value,
          position: positionModel.value,
          rate: rateModel.value
        })

      departmentModel.value = undefined
      positionModel.value = undefined
      rateModel.value = undefined
    }
  }

  onMounted(async () => {
    questionnaireUserOptions.value = await getQuestionnaireAllList()
  })
</script>

<style lang="sass">
  .q-field__bottom
    padding: 3px 0 0 0 !important
</style>
