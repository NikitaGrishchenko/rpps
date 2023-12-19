import { ActionTree } from 'vuex';
import { StateInterface } from '../index';
import {IPrizePlaces } from 'types/reference'
import {IReferenceState} from './state'
import { api } from 'boot/axios'

const actions: ActionTree<IReferenceState, StateInterface> = {
  getReferencePrizePlaces ( {commit}) {
    api.get<IPrizePlaces>('reference/prize-places/').then((response)=> {
      commit('setPrizePlaces', response.data)
    }).catch((error) => {
      console.error(error)
    })
  }
};

export default actions;
