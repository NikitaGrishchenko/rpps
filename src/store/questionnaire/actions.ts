import { api } from 'boot/axios'
import { IQuestionnaireUser } from 'types/questionnaire'
import { ActionTree } from 'vuex'
import { StateInterface } from '../index'



const actions: ActionTree<IQuestionnaireUser, StateInterface> = {
  getQuestionnaireUser({ commit, rootState }, idQuestionnaire: number) {

    const userAuth = rootState.auth.user

    if (userAuth.isAdmin || userAuth.isExpert || userAuth.isManagerDepartment || userAuth.isManagerFaculty || userAuth.isSuperExpert) {
      api
        .get<IQuestionnaireUser>(
          '/questionnaire/expert/detail/' + String(idQuestionnaire) + '/'
        )
        .then((response) => {
          commit('updateQuestionnaireUser', response.data)
        })
        .catch((error) => {
          console.error(error)
        })
    } else {
      api
        .get<IQuestionnaireUser>(
          'questionnaire/detail/' + String(idQuestionnaire) + '/'
        )
        .then((response) => {
          commit('updateQuestionnaireUser', response.data)
        })
        .catch((error) => {
          console.error(error)
        })
    }

  }
}

export default actions
