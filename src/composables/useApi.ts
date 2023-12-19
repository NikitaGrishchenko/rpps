import { AxiosError, AxiosRequestConfig, AxiosResponse } from 'axios'
import { api } from 'boot/axios'
import { Notify } from 'quasar'
import { ref } from 'vue'

export function useApi() {
  const inProcess = ref<boolean>(false)

  const fetch = async <T>(
    options: AxiosRequestConfig,
    successCallback?: (response: AxiosResponse) => void,
    errorCallback?: (error: AxiosError) => void
  ) => {
    try {
      inProcess.value = true
      const response = await api(options)
      if (successCallback) successCallback(response)
      return <T>response.data
    } catch (error) {
      console.error(error)
      Notify.create({
        position: 'top',
        type: 'negative',
        message: 'Ошибка сервера'
      })
      if (errorCallback) errorCallback(<AxiosError>error)
    } finally {
      inProcess.value = false
    }
  }

  return {
    inProcess,
    fetch
  }
}
