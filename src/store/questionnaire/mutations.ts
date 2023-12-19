import { MutationTree } from 'vuex';
import { IQuestionnaireUser, ICurrentChangeFileCategory  } from 'types/questionnaire'


// export enum MutationType {
//   loginUser = 'LOGIN_USER',
//   logoutUser = 'LOGOUT_USER',
// }

// TODO добавить MutationType

const mutation: MutationTree<IQuestionnaireUser> = {

  updateQuestionnaireUser (state: IQuestionnaireUser, data: IQuestionnaireUser) {
      state.id = data.id
      state.questionnaire = data.questionnaire
      state.statistics = data.statistics
      state.userPosition = data.userPosition
      state.info = data.info
      state.effectiveContract = data.effectiveContract
  },
  deleteQuestionnaireUser (state: IQuestionnaireUser) {
      state.questionnaire = null
  },
  openDialogDetailCategory (state: IQuestionnaireUser ) {
    state.showDialogDetailCategory = true
  },
  closeDialogDetailCategory (state: IQuestionnaireUser) {
    state.showDialogDetailCategory = false
  },
  openDialogUploadFileToCategory (state: IQuestionnaireUser ) {
    state.showDialogUploadFileToCategory = true
  },
  closeDialogUploadFileToCategory (state: IQuestionnaireUser) {
    state.showDialogUploadFileToCategory = false
  },

  openDialogChangeFileCategory (state: IQuestionnaireUser ) {
    state.showDialogChangeFileCategory = true
  },
  closeDialogChangeFileCategory (state: IQuestionnaireUser) {
    state.showDialogChangeFileCategory = false
  },
  openDialogAttachExistingFile (state: IQuestionnaireUser ) {
    state.showDialogAttachExistingFile = true
  },
  closeDialogAttachExistingFile (state: IQuestionnaireUser) {
    state.showDialogAttachExistingFile = false
  },
  setIdCurrentDetailCategory (state: IQuestionnaireUser, idCategory: number ) {
    state.idCurrentDetailCategory = idCategory
  },
  deleteIdCurrentDetailCategory (state: IQuestionnaireUser ) {
    state.idCurrentDetailCategory = undefined
  },
  setCurrentChangeFileCategory (state: IQuestionnaireUser, file: ICurrentChangeFileCategory ) {
      state.currentChangeFileCategory.id = file.id
      state.currentChangeFileCategory.typeCategory = file.typeCategory
      state.currentChangeFileCategory.useInternetResourceLink = file.useInternetResourceLink
      state.currentChangeFileCategory.internetResourceLinkOrDoc = file.internetResourceLinkOrDoc
  },
  deleteCurrentChangeFileCategory (state: IQuestionnaireUser ) {
    state.currentChangeFileCategory.id = undefined
    state.currentChangeFileCategory.typeCategory = undefined
    state.currentChangeFileCategory.useInternetResourceLink = undefined
    state.currentChangeFileCategory.internetResourceLinkOrDoc = undefined
  },
  confirmEffectiveContract(state: IQuestionnaireUser) {
    state.effectiveContract = true
  }
};

export default mutation;
