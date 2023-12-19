export interface IUsernamePasswordAuth {
  username: string
  password: string
}

export interface IUserPosition {
  id: number
  department: number
  position: number
  rate: number
  user: number
}
export interface IUserInfo {
  userImage?: string
  userPositions: IUserPosition[]
}
