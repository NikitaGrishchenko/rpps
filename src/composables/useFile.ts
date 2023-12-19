import { AxiosRequestConfig } from 'axios'
import { useApi } from 'src/composables/useApi'
import { IFile, IFileSelect } from 'types/questionnaire'
import { api } from 'boot/axios'
export function useFile() {
  const { inProcess, fetch } = useApi()

  // Получение списка всех лет
  const getFilesYearsList = () => {
    return fetch<string[]>({
      method: 'GET',
      url: 'questionnaire/files/years/'
    })
  }
  // Получение файлов пользователя по году
  const getFilesByYears = (year: string) => {
    return fetch<IFile[]>({
      method: 'GET',
      url: `questionnaire/files/for-year/${year}/`
    })
  }

  const fileById = (
    id: number,
    method: AxiosRequestConfig['method'],
    data?: IFile
  ) => {
    return fetch<IFile>({
      method: method,
      url: `questionnaire/files/${id}/`,
      data: data
    })
  }
  // Добавление файла
  const addFile = (data: IFile) => {
    const formData = new FormData()
    for (const [key, value] of Object.entries(data)) formData.append(key, value)
    return fetch<IFile>({
      method: 'POST',
      url: 'questionnaire/files/',
      data: formData
    })
  }

  const getFiles = () => {
    return new Promise<IFileSelect[]>((resolve, reject) => {
      api.get<IFileSelect[]>(
        'questionnaire/files/',
      ).then((response)=> {
        resolve(response.data);
      }).catch((error)=>{
          reject(error);
      })
    })
  }

  return {
    inProcess,
    addFile,
    getFilesYearsList,
    getFilesByYears,
    fileById,
    getFiles
  }
}
