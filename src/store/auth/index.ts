import { Module } from 'vuex';
import { StateInterface } from '../index';
import state, { IAuthState } from './state';
// import actions from './actions';
import getters from './getters';
import mutations from './mutations';

const auth: Module<IAuthState, StateInterface> = {
  namespaced: true,
  // actions,
  getters,
  mutations,
  state
};

export default auth;
