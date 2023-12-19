import { useApi } from 'src/composables/useApi'
import {
  IQuestionnaireStatisticsTable,
  IQuestionnaireUserList,
  IQuestionnaireBase,
  ICategoryDialog,
  IFileCategoryQuestionnaireUser,
  IFileCategoryQuestionnaireUserPatch,
  IListOfDepartments,
  IDepartmentOfList,
  ICategoryUser,
  IUserPositionRegistration,
  IUserPositionRegistrationId,
} from 'types/questionnaire'
import { serialize } from 'object-to-formdata'
import { api } from 'boot/axios'
import { useQuasar } from 'quasar'

export function useQuestionnaire() {
  const { inProcess, fetch } = useApi()
  const $q = useQuasar()

  /*Получение списка всех анкет пользователя*/
  const getQuestionnaireUserList = async () => {
    const response = await api.get<IQuestionnaireUserList[]>('questionnaire/list/')
    return response.data
  }

  const getQuestionnaireStatistics = (questionnaireId: number) => {
    return fetch<IQuestionnaireStatisticsTable[]>({
      method: 'GET',
      url: `questionnaire/statistics/${questionnaireId}`
    })
  }

  const getAllUserPosition = () => {
    return fetch<IQuestionnaireBase[]>({
      method: 'GET',
      url: 'auth/user-position/'
    })
  }

  const getCategoryUser = (categoryUserId: number | undefined) => {
    if (categoryUserId !== undefined) {
      return fetch<ICategoryDialog>({
        method: 'GET',
        url: `questionnaire/category-user/${categoryUserId}`
      })
    }
  }

  const getFileCategoryUser = (fileId: number | undefined) => {
    if (fileId !== undefined) {
      return fetch<IFileCategoryQuestionnaireUser>({
        method: 'GET',
        url: `questionnaire/category-user/retrieve-file/${fileId}/`
      })
    }
  }

  const getQuestionnaireAllList = () => {
    return fetch<IQuestionnaireBase[]>({
      method: 'GET',
      url: 'questionnaire/all-list/'
    })
  }

  const uploadFileForCategoryUser = (fileData: IFileCategoryQuestionnaireUserPatch, idCategoryUser: number) => {

    const formData = serialize(fileData)

    return new Promise((resolve, reject) => {
      api
      .patch<IFileCategoryQuestionnaireUserPatch[]>(
        `questionnaire/category-user/upload-file/${idCategoryUser}/`,
        formData
      )
      .then((response) => {
        $q.notify({
          type: 'info',
          message: 'Успешно',
          color: 'primary',
          position: 'top-right'
        })
        resolve(response);
      })
      .catch((error) => {
        $q.notify({
          type: 'error',
          message: 'Ошибка сервера',
          color: 'red',
          position: 'top-right'
          })
          reject(error);
        })
      })
    }

    const attachFileForCategoryUser = (fileData: IFileCategoryQuestionnaireUserPatch, idCategoryUser: number) => {

      return new Promise((resolve, reject) => {
        api
        .patch<IFileCategoryQuestionnaireUserPatch[]>(
          `questionnaire/category-user/attach-file/${idCategoryUser}/`,
          fileData
        )
        .then((response) => {
          $q.notify({
            type: 'info',
            message: 'Файл успешно прикреплен',
            color: 'primary',
            position: 'top-right'
          })
          resolve(response);
        })
        .catch((error) => {
          $q.notify({
            type: 'error',
            message: 'Ошибка сервера',
            color: 'red',
            position: 'top-right'
            })
            reject(error);
          })
        })
      }

  const updateFileForCategoryUser = (fileData: IFileCategoryQuestionnaireUserPatch, idFileCategory: number | undefined) => {

    return new Promise((resolve, reject) => {
      if (idFileCategory !== undefined) {
        api
      .patch<IFileCategoryQuestionnaireUserPatch[]>(
        `questionnaire/category-user/update-file/${idFileCategory}/`,
        fileData
      )
      .then((response) => {
        $q.notify({
          type: 'info',
          message: 'Данные обновлены',
          color: 'primary',
          position: 'top-right'
        })
        resolve(response);
      })
      .catch((error) => {
        $q.notify({
          type: 'error',
          message: 'Ошибка сервера',
          color: 'red',
          position: 'top-right'
          })
          reject(error);
        })
      }
      })
    }

  const deleteFileForCategoryUser = (idFileCategory: number | undefined) => {
    return new Promise((resolve, reject) => {
      if (idFileCategory !== undefined) {
        api.delete(
          `questionnaire/category-user/delete-file/${idFileCategory}/`
        ).then((response)=> {
          $q.notify({
            type: 'info',
            message: 'Файл откреплён',
            color: 'primary',
            position: 'top-right'
          })
          resolve(response);
        }).catch((error)=>{
          $q.notify({
            type: 'error',
            message: 'Ошибка сервера',
            color: 'red',
            position: 'top-right'
            })
            reject(error);
        })
      }
    })
  }

  const updateCategoryUser = (idCategory: number | undefined, dataCategory: ICategoryUser) => {
    return new Promise((resolve, reject) => {
      if (idCategory !== undefined) {
        api.patch(
          `questionnaire/expert/change-category/${idCategory}/`, dataCategory
        ).then((response)=> {
          $q.notify({
            type: 'info',
            message: 'Значения обновлены успешно',
            color: 'primary',
            position: 'top-right'
          })
          resolve(response);
        }).catch((error)=>{
          $q.notify({
            type: 'error',
            message: 'Ошибка сервера',
            color: 'red',
            position: 'top-right'
            })
            reject(error);
        })
      }
    })
  }

  const getListOfFaculties = async () => {
    const response = await api.get<IListOfDepartments[]>('verification/faculty/')
    return response.data

  }

  const getDepartmentsOfOneFaculty = (idFaculty: number) => {
    return new Promise<IListOfDepartments[]>((resolve, reject) => {
        api.get<IListOfDepartments[]>(
          `verification/faculty/${idFaculty}/`
        ).then((response)=> {
          resolve(response.data);
        }).catch((error)=>{
          $q.notify({
            type: 'error',
            message: 'Ошибка сервера',
            color: 'red',
            position: 'top-right'
            })
            reject(error);
        })
    })
  }


  const getListOfDepartment = (idDepartment: number | undefined) => {
    return new Promise((resolve, reject) => {
        if (idDepartment !== undefined) {
          api.get<IDepartmentOfList>(
            `questionnaire/list-department/${idDepartment}/`
          ).then((response)=> {
            resolve(response.data);
          }).catch((error)=>{
            $q.notify({
              type: 'error',
              message: 'Ошибка сервера',
              color: 'red',
              position: 'top-right'
              })
              reject(error);
          })
        }
    })
  }

  const isValidInternetResourceLink = (val: string): boolean | string => {
    const pattern =
      /((([A-Za-z]{3,9}:(?:\/\/)?)(?:[-;:&=\+\$,\w]+@)?[A-Za-z0-9.-]+|(?:www.|[-;:&=\+\$,\w]+@)[A-Za-z0-9.-]+)((?:\/[\+~%\/.\w-_]*)?\??(?:[-\+=&;%@.\w_]*)#?(?:[\w]*))?)/

    if (val === '' || val === undefined || val === null) {
      return true
    }

    if (val !== null /**val.length > 0**/) {
      if (pattern.test(val) === false) {
        return 'Введите корректный URL-адрес'
      }
    }

    return true
    }

  const isValidCoefficient = (val: number): boolean | string => {
    if (val === undefined) {
      return 'Выберите значение'
    }
    if (val > 0 && val <= 1) {
      return true
    }
    return 'Значение введено неверно'
  }


  const isValidFile = (val: File): boolean | string => {
    const allowedFileFormats = ['pdf', 'docx', 'doc', 'jpg', 'png']
    if (val !== undefined) {
      if (Number(val.size) > 15728640) {
        return 'Размер файла превышает максимальный (15 Мб)'
      }
      const type: string | undefined = val.name.split('.').pop()
      if (type !== undefined) {
        if (allowedFileFormats.includes(type) === false) {
          return 'Выбран недопустимый формат файла (Используйте следующие типы: pdf, docx, doc, jpg, png)'
        }
      }
      return true
    }
    return true
  }

  const isValidEmail = async (username:string) => {
    const emailPattern =
      /^(?=[a-zA-Z0-9@._%+-]{6,254}$)[a-zA-Z0-9._%+-]{1,64}@(?:[a-zA-Z0-9-]{1,63}\.){1,8}[a-zA-Z]{2,63}$/
      if (emailPattern.test(username)) {
        const {data}=await api
        .post<{[key:string]:boolean}>(
          'auth/check-username/',
          { username: username }
        )
        return !data.isExist ||'Такой E-mail уже есть'

      } else {
        return 'Некорректная почта'
      }
  }

  const getPositionColor = (positionId: number) => {
    if (positionId === 12) {
      return 'text-pink'
    } else if (positionId === 9) {
      return 'text-purple'
    } else if (positionId === 8) {
      return 'text-deep-purple'
    } else if (positionId === 7) {
      return 'text-indigo'
    } else if (positionId === 6) {
      return 'text-blue'
    } else if (positionId === 11) {
      return 'text-blue'
    } else if (positionId === 13) {
      return 'text-light-blue'
    } else if (positionId === 3) {
      return 'text-cyan'
    } else if (positionId === 10) {
      return 'text-teal'
    } else if (positionId === 2) {
      return 'text-green'
    } else if (positionId === 5) {
      return 'text-cyan'
    } else if (positionId === 4) {
      return 'text-lime'
    } else if (positionId === 1) {
      return 'text-yellow'
    } else {
      return ''
    }
  }

  const userPositionsToSend = (
    userPositionsModel: IUserPositionRegistration[]
  ) => {
    const userPositions: IUserPositionRegistrationId[] = []
    userPositionsModel.forEach((element: IUserPositionRegistration) => {
      if (element.department && element.position && element.rate) {
        userPositions.push({
          department: element.department.id,
          position: element.position.id,
          rate: element.rate.id
        })
      }
    })
    return userPositions
  }

  const questionnaireToSend = (
    questionnairesUserModel: IQuestionnaireBase[]
  ) => {
    const questionnaire: number[] = []
    questionnairesUserModel.forEach((element: IQuestionnaireBase) => {
      if (element.id && element.name ) {
        questionnaire.push(element.id)
      }
    })
    return questionnaire
  }

  const confirmEffectiveContract = (idQuestionnaire: number) => {
    return new Promise((resolve, reject) => {

    api.patch(
      `questionnaire/confirm-effective-contract/${idQuestionnaire}/`, {'effectiveContract': true}
    ).then(()=> {
      resolve(
        $q.notify({
          type: 'info',
          message: 'Успешно',
          color: 'primary',
          position: 'top-right'
          })
      );
    }).catch((error)=>{
      $q.notify({
        type: 'error',
        message: 'Ошибка сервера',
        color: 'red',
        position: 'top-right'
        })
        reject(error);
    })
  })
  }

  const actualPointMainCategory = (
    resultPoint: number | undefined,
    resultPointFixed: number | undefined
  ): number | undefined => {
    if (resultPointFixed !== null) {
      return resultPointFixed
    }
    return resultPoint
  }

  const generateDepartmentReport = (
    idDepartment: number | undefined,
    idQuestionnaire: number | undefined
  ) => {
    if (idQuestionnaire && idDepartment) {
      window.open(
        process.env.DEV
          ? `http://localhost:8000/api/v1/documents/department/${idDepartment}/${idQuestionnaire}/`
          : `/api/v1/documents/department/${idDepartment}/${idQuestionnaire}/`,
        '_blank'
      )
    }
  }

  return {
    inProcess,
    getQuestionnaireUserList,
    getQuestionnaireStatistics,
    getQuestionnaireAllList,
    getCategoryUser,
    uploadFileForCategoryUser,
    updateFileForCategoryUser,
    deleteFileForCategoryUser,
    isValidInternetResourceLink,
    isValidCoefficient,
    isValidFile,
    isValidEmail,
    getFileCategoryUser,
    getListOfFaculties,
    getDepartmentsOfOneFaculty,
    getListOfDepartment,
    getPositionColor,
    updateCategoryUser,
    userPositionsToSend,
    questionnaireToSend,
    confirmEffectiveContract,
    attachFileForCategoryUser,
    actualPointMainCategory,
    generateDepartmentReport,
    getAllUserPosition,
  }
}
