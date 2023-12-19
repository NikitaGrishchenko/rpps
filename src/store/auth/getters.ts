import { GetterTree } from 'vuex'
import { StateInterface } from '../index'
import { IAuthState } from './state'

const getters: GetterTree<IAuthState, StateInterface> = {
  userFullName(state: IAuthState): string {
    const username = [
      state.user.last_name,
      state.user.first_name,
      state.user.patronymic
    ].join(' ')
    return username !== '  ' ? username : state.user.username || ' '
  },
    isCheckingUser(state: IAuthState): boolean  {
    if (state.user.isAdmin || state.user.isExpert || state.user.isManagerDepartment || state.user.isManagerFaculty || state.user.isSuperExpert) {
      return true
    }
    return false

  },
  isSuperExpertCheckingUser(state: IAuthState): boolean {
    if (state.user.isExpert || state.user.isSuperExpert) {
      return true
    }
    return false
  }
}

export default getters
