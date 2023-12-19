import { AxiosError } from 'axios'

export default (
  axiosError: AxiosError<{
    [key: string]: string[] | string
  }>,
  defaultError = 'Ошибка сервера'
) => {
  const errorsList: string[] = []

  if (axiosError.response?.data !== undefined)
    Object.values(axiosError.response?.data).forEach((error) => {
      errorsList.push(Array.isArray(error) ? error.toString() : error)
    })
  else errorsList.push(defaultError)
  return errorsList
}
