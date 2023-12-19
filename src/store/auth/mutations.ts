import { MutationTree } from 'vuex'
import { IAuthState, IAuthUser } from './state'

// export enum MutationType {
//   loginUser = 'LOGIN_USER',
//   logoutUser = 'LOGOUT_USER',
// }

// TODO добавить MutationType

const mutation: MutationTree<IAuthState> = {
  loginUser(state: IAuthState, data: IAuthUser) {
    state.isAuth = true
    state.user.id = data.id
    state.user.categoryExpertId = data.categoryExpertId
    state.user.email = data.email
    state.user.first_name = data.first_name
    state.user.id = data.id
    state.user.isAdmin = data.isAdmin
    state.user.isExpert = data.isExpert
    state.user.isManagerDepartment = data.isManagerDepartment
    state.user.isManagerFaculty = data.isManagerFaculty
    state.user.isStaff = data.isStaff
    state.user.isSuperExpert = data.isSuperExpert
    state.user.last_name = data.last_name
    state.user.managerDepartmentId = data.managerDepartmentId
    state.user.managerFacultyId = data.managerFacultyId
    state.user.patronymic = data.patronymic
    state.user.username = data.username
    state.user.userImage = data.userImage
  },

  logoutUser(state: IAuthState) {
    state.isAuth = false
    state.user.categoryExpertId = null
    state.user.email = null
    state.user.first_name = null
    state.user.id = null
    state.user.isAdmin = false
    state.user.isExpert = false
    state.user.isManagerDepartment = false
    state.user.isManagerFaculty = false
    state.user.isStaff = false
    state.user.isSuperExpert = false
    state.user.last_name = null
    state.user.managerDepartmentId = null
    state.user.managerFacultyId = null
    state.user.patronymic = null
    state.user.username = null
    state.user.userImage = null
  },
  updateUserImage(state: IAuthState, image: string) {
    state.user.userImage = image
  }
}

export default mutation
