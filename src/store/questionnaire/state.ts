import { IQuestionnaireUser } from 'types/questionnaire'

function state(): IQuestionnaireUser {
  return {
    id: undefined,
    effectiveContract: null,
    info: {
      name: undefined,
      status: undefined,
    },
    userPosition: {
      id: null,
      department: {
        id: null,
        shortName: null,
        name: null,
        rsueId: null,
        faculty: null
      },
      position: {
        id: null,
        shortName: null,
        name: null,
        rsueId: null
      },
      user: {
        username: null,
        firstName: null,
        lastName: null,
        patronymic: null
      },
      rate: null
    },
    statistics: {},
    questionnaire: null,
    showDialogDetailCategory: false,
    showDialogUploadFileToCategory: false,
    showDialogChangeFileCategory: false,
    showDialogAttachExistingFile: false,
    idCurrentDetailCategory: undefined,
    currentChangeFileCategory: {
      id: undefined,
      typeCategory: undefined,
      useInternetResourceLink: undefined,
      internetResourceLinkOrDoc: undefined,
    }

  }
}

export default state
