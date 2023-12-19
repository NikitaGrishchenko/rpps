import { useApi } from 'src/composables/useApi'
import { useStore } from 'src/store'
import { IUserInfo } from 'src/types/auth'
import { useRouter } from 'vue-router'
import { api } from 'boot/axios'
import { Notify } from 'quasar'
import {AxiosError} from 'axios';


export function useAuth() {
  const router = useRouter()
  const store = useStore()

  const { inProcess, fetch } = useApi()

  const userLogin = async (username: string, password: string) => {
    await api.post(
      'auth/token/login/',
      {
        username,
        password
      }
    )
    void router.push({
      name: 'IndexPage'
    })


  }

  const userLogout = async () => {
    await api.post('auth/token/logout/')
    store.commit('auth/logoutUser')
    void router.push({
      name: 'LoginPage'
    })
  }

  // const userLogout = () => {
  //   return fetch(
  //     {
  //       method: 'POST',
  //       url: 'auth/token/logout/'
  //     },
  //     () => {
  //       store.commit('auth/logoutUser')
  //       void router.push({
  //         name: 'LoginPage'
  //       })
  //     }
  //   )
  // }

  const getUserInfo = () => {
    return fetch<IUserInfo>({
      method: 'GET',
      url: 'auth/user-info/'
    })
  }

  const updateUserInfo = (userInfo: IUserInfo) => {
    return fetch<IUserInfo>({
      method: 'PATCH',
      url: 'auth/user-info/',
      data: userInfo
    })
  }

  const createUserquestionnaire = (resultData: any) => {

    return new Promise((resolve, reject) => {
      api
      .post(
        'auth/create-user/',
        resultData
      )
      .then((response) => {
        Notify.create({
          type: 'info',
          message: 'Пользователь создан',
          color: 'primary',
          position: 'top'
        })
        resolve(response);
      })
      .catch((error:AxiosError) => {
        Notify.create({
          type: 'error',
          message: 'Ошибка сервера',
          color: 'red',
          position: 'top'
          })
          reject(error);
        })
      })
    }

  const createApplicationSubmission = (resultData: any) => {

    return new Promise((resolve, reject) => {
      api
      .post(
        'auth/application-submission/',
        resultData
      )
      .then((response) => {
        Notify.create({
          type: 'info',
          message: 'Вы успешно подали заявку на участие в анкетировании. В течение одного рабочего дня на Ваш E-mail придет сообщение с данными для входа',
          color: 'primary',
          position: 'top',
          timeout: 30000
        })
        resolve(response);
      })
      .catch((error) => {
        Notify.create({
          type: 'error',
          message: 'Ошибка сервера',
          color: 'red',
          position: 'top'
          })
          reject(error);
        })
      })
    }

  return {
    userLogin,
    userLogout,
    getUserInfo,
    updateUserInfo,
    createUserquestionnaire,
    createApplicationSubmission,
    inProcess,
  }
}
