<template>
  <q-page class="login">
    <div class="row items-center justify-center" style="min-height: 100vh">
      <div class="login-form login-form__card">
        <div class="login-logo">
          <img src="~assets/images/rsue-logo.svg" alt="РГЭУ (РИНХ)" />
          <h1>
            Рейтинг профессорско-<br />преподавательского состава <br />
            РГЭУ (РИНХ)
          </h1>
        </div>
        <h2 class="login-form__title">Войти в систему</h2>
        <q-form
          ref="loginForm"
          @submit.prevent="onSubmit()"
          class="login-form--wrapper"
        >
          <q-input
            class="login-form__input login-form__input q-mb-sm"
            borderless
            type="text"
            v-model="usernameModel"
            :rules="[(val) => !!val]"
            label="Логин"
          />
          <q-input
            class="login-form__input login-form__input"
            borderless
            :type="isPassword ? 'password' : 'text'"
            v-model="passwordModel"
            :rules="[(val) => !!val]"
            label="Пароль"
          >
            <template v-slot:after>
              <q-icon
                :name="isPassword ? 'mdi-eye-off' : 'mdi-eye'"
                class="cursor-pointer"
                @click="isPassword = !isPassword"
              />
            </template>
          </q-input>

          <q-btn
            class="login-form__btn"
            label="Подтвердить"
            type="submit"
            color="primary"
            :loading="loadingBtn"
          >
            <q-icon name="mdi-login q-ml-xs" size="15px" />
          </q-btn>

          <q-btn
            :to="{ name: 'ApplicationSubmissionPage' }"
            no-caps
            flat
            class="login-form__subbtn"
          >
            Подать заявку на участие в анкетировании
          </q-btn>
          <q-inner-loading :showing="inProcess">
            <q-spinner-puff class="fixed-center" size="50px" color="primary" />
          </q-inner-loading>
        </q-form>

        <!-- <q-dialog
          v-model="errorModal"
          persistent
          transition-show="scale"
          transition-hide="scale"
        >
          <q-card class="q-pa-md flex justify-center" style="width: 300px">
            <q-img
              src="~assets/images/error.svg"
              style="height: 140px; max-width: 150px"
            />
            <q-card-section>
              <div class="text-h5 text-red">Ошибка</div>
            </q-card-section>
            <q-card-section>
              <div
                class="error"
                v-for="(error, index) in serverErrors"
                :key="index"
              >
                {{ error }}
              </div>
            </q-card-section>

            <q-card-actions>
              <q-btn flat @click="resetForm()" label="OK" v-close-popup />
            </q-card-actions>
          </q-card>
        </q-dialog> -->
      </div>
    </div>
  </q-page>
</template>

<script setup lang="ts">
  import { AxiosError } from 'axios'
  import { useAuth } from 'composables/useAuth'
  import { QForm, useQuasar } from 'quasar'
  import extractAxiosErrors from 'src/utils/extractAxiosErrors'
  import { ref } from 'vue'

  const $q = useQuasar()

  const serverErrors = ref<string[]>([])

  const usernameModel = ref<string>('')
  const passwordModel = ref<string>('')

  const loginForm = ref<QForm>()

  const isPassword = ref<boolean>(true)
  const loadingBtn = ref<boolean>(false)

  const { userLogin, inProcess } = useAuth()

  // const resetForm = () => {
  //   loginForm.value?.resetValidation()
  //   serverErrors.value = []
  // }

  const onSubmit = async () => {
    loadingBtn.value = true
    try {
      await userLogin(usernameModel.value.toLowerCase(), passwordModel.value)
    } catch (error) {
      serverErrors.value = extractAxiosErrors(<AxiosError>error)
      $q.notify({
        type: 'error',
        message: serverErrors.value[0],
        color: 'red',
        position: 'top',
        timeout: 7000
      })
    } finally {
      loadingBtn.value = false
    }
  }
</script>
