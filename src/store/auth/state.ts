export interface IAuthUser {
  categoryExpertId: null | number
  email: string | null
  first_name: string | null
  id: number | null
  isAdmin: boolean
  isExpert: boolean
  isManagerDepartment: boolean
  isManagerFaculty: boolean
  isStaff: boolean
  isSuperExpert: boolean
  last_name: string | null
  managerDepartmentId: null | number
  managerFacultyId: null | number
  patronymic: string | null
  username: string | null
  userImage: string | null
}

export interface IAuthState {
  isAuth: boolean
  user: IAuthUser
}

function state(): IAuthState {
  return {
    isAuth: false,
    user: {
      categoryExpertId: null,
      email: null,
      first_name: null,
      id: null,
      isAdmin: false,
      isExpert: false,
      isManagerDepartment: false,
      isManagerFaculty: false,
      isStaff: false,
      isSuperExpert: false,
      last_name: null,
      managerDepartmentId: null,
      managerFacultyId: null,
      patronymic: null,
      username: null,
      userImage: null
    }
  }
}

export default state
