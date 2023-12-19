import { MutationTree } from 'vuex'
import { IPrizePlaces } from 'types/reference'
import { IReferenceState } from './state'

// export enum MutationType {
//   loginUser = 'LOGIN_USER',
//   logoutUser = 'LOGOUT_USER',
// }

// TODO добавить MutationType

const mutation: MutationTree<IReferenceState> = {
  setPrizePlaces(state: IReferenceState, data: IPrizePlaces) {
    state.prizePlaces = data
  },
}

export default mutation
