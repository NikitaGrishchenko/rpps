export interface IBaseReference {
  id: number
  rsueId?: number
}

export interface IPosition extends IBaseReference {
  faculty?: string
  shortName: string
  name: string
}
export interface IRate extends IBaseReference {
  value: number
}

export interface IFaculty extends IBaseReference {
  shortName: string
  name: string
  logo?: string
}
export interface IDepartment extends IBaseReference {
  faculty: IFaculty
  name: string
  shortName: string
}

export interface IFileType extends IBaseReference {
  name: string
}

export interface IPrizePlaces {
  id: number
  points: number
  name: string
  rating: number
}

export interface IBanner {
  id: number
  text: string
  show: boolean
  colorText: string
  colorBg: string
  icon: string
  colorIcon: string
}


export interface IReference {
  [key: string]: IBaseReference[] | undefined
  prizePlaces?: IPrizePlaces[]
  positions?: IPosition[]
  rates?: IRate[]
  departments?: IDepartment[]
  'enums/type-file'?: IFileType[]
  banners?: IBanner[]

}



export type references = IPosition[] & IRate[] & IDepartment[] & IFileType[]
