import { Module } from 'vuex';
import { StateInterface } from '../index';
import { IReferenceState } from './state'
import actions from './actions';
// import getters from './getters';
import mutations from './mutations';
import state from './state';


const reference: Module<IReferenceState, StateInterface> = {
  namespaced: true,
  actions,
  // getters,
  mutations,
  state
};

export default reference;
