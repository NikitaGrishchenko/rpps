import { Module } from 'vuex';
import { StateInterface } from '../index';
import state from './state';
import actions from './actions';
// import getters from './getters';
import mutations from './mutations';
import { IQuestionnaireUser } from 'types/questionnaire'


const questionnaire: Module<IQuestionnaireUser, StateInterface> = {
  namespaced: true,
  actions,
  // getters,
  mutations,
  state
};

export default questionnaire;
