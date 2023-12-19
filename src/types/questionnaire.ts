

export interface IPosition {
  id: number | null
  shortName: string | null
  name: string | null
  rsueId: number | null
}
export interface IRate {
  id: number | null
  value: number | null
  rsueId: number | null
}

export interface IUser {
  username: string | null
  firstName: string | null
  lastName: string | null
  patronymic: string | null
}


export interface IUserPosition {
  id: number | null
  department: IDepartment | null
  position: IPosition | null
  user: IUser | null
  rate: number | null
}

export interface IDepartment {
  id: number | null
  shortName: string | null
  name: string | null
  rsueId: number | null
  faculty: number | null
}

export interface IUserPositionRegistration {
  department?: IDepartment | undefined
  position?: IPosition | undefined
  rate?: IRate | undefined
}

export interface IUserPositionRegistrationId {
  department: number | null
  position: number | null
  rate: number | null
}

export interface IDepartmentOfList {
  id: number | null
  shortName: string | null
  name: string | null
  rsueId: number | null
  faculty: number | null
  userPositions: IUserPosition[]
}

export interface ICategoryUser {
  isVerified: boolean | null | undefined,
  resultPointFixed: number | null | undefined | string,
  resultPoint?: number | undefined
  countFiles?: number
}

export interface ICategory {
  id: number
  maxWeight: number
  name: string
  description: string
  nestingLevel: number
  number: string
  periodicity: string
  rating: string
  typeCategory: number
  useInternetResourceLink: boolean
  internetResourceLinkOrDoc: boolean
  weight: number
  resultPoint: number
  resultPointFixed: number
  countFiles: number
}

export interface IFiles {
  id: number
  url: string
  quantityValue: number
  coefficient: number
  internetResourceLink: string
  prizePlace: number
  categoryQuestionnaire: number
  file: File
}

export interface IPrizePlace {
  id: number
  points: number
  name: string
  rating: number
}

export interface IDescription {
  id: number
  text: string
}
export interface IReferenceCategory {
  description: IDescription
  id: number
  name: string
}

export interface ICategoryQuestionnaireNested {
  id: number
  mainCategory?: null
  maxWeight?: null
  number: number
  parent: number
  periodicity?: null
  rating?: null
  referenceCategory?: IReferenceCategory
  typeCategory: number
  useInternetResourceLink: boolean
  internetResourceLinkOrDoc: boolean
  weight: number
}

export interface ICategoryQuestionnaire {
  categoryQuestionnaire?: ICategoryQuestionnaireNested
  id: number
  isVerified: boolean
  questionnaireUser: number
  resultPoint: number
  resultPointFixed?: null
}

export interface IEnumsTypeFile {
  id: number
  name: string
}

export interface IFileSelect {
  id: number
  name: string
}

export interface IFileCategoryQuestionnaireUser {
  categoryQuestionnaire?: ICategoryQuestionnaire
  coefficient?: null | number
  name?: null | string
  file?: File
  id?: number
  internetResourceLink?: null | string
  prizePlace?: IPrizePlace | null
  quantityValue?: null | number
  typeFile?: IEnumsTypeFile
}

export interface IFileCategoryQuestionnaireUserPatch {
  categoryQuestionnaire?: ICategoryQuestionnaire
  coefficient?: null | number
  name?: null | string
  file?: File | number
  fileId?: number
  id?: number
  internetResourceLink?: null | string
  prizePlace?: number | null
  quantityValue?: null | number
  typeFile?: number
}


export interface IListOfDepartments {
  id: number
  points: {
    resultPoint_Sum: number
  }
  shortName: string
  name: string
  rsueId: number
  faculty: string

}

export interface IListOfFaculties {
  id: number
  departments: IListOfDepartments[]
  shortName: string
  name: string
  rsueId: number
  logo: string | null
}


export interface IFile {
  dateUpload?: string
  file?: File
  fileCategoryQuestionnaireUser?: IFileCategoryQuestionnaireUser[] | number
  id?: number
  name?: string
  typeFile?: number
  user?: number
}


export interface ICategoryDialog {
  id: number
  files: IFile[] | undefined
  resultPoint: number
  resultPointFixed: number
  questionnaireUser: number
  categoryQuestionnaire: ICategoryQuestionnaireNested
}

export interface IMainCategory {
  id: number
  name: string
  number: number
  resultPoint: number
  resultPointFixed: number
  category: ICategory[]
  idReferenceCategory: number
}

export interface IQuestionnaireBase {
  id: number
  name: string
}

export interface IQuestionnaire extends IQuestionnaireBase {
  status: number
  file: string
  previewImage: string | null
}

export interface IQuestionnaireUserList {
  id: number
  userPosition: IUserPosition
  questionnaire: IQuestionnaire
  statistics: IStatisticsQuestionnaire
}

interface IStatisticsQuestionnaireObject {
  name: string
  points: number
  order: number
}

export interface IStatisticsQuestionnaire {
  [key: string]: IStatisticsQuestionnaireObject
}

export interface ICurrentChangeFileCategory {
  id: number | undefined
  typeCategory: number | undefined
  useInternetResourceLink: boolean | undefined
  internetResourceLinkOrDoc: boolean | undefined
}

export interface IQuestionnaireInfo {
  name: string | undefined
  status: number | undefined
}

export interface IQuestionnaireUser {
  id: number | undefined
  userPosition: IUserPosition
  statistics: IStatisticsQuestionnaire
  questionnaire: IQuestionnaire | null
  info: IQuestionnaireInfo
  showDialogDetailCategory: boolean
  showDialogUploadFileToCategory: boolean
  showDialogChangeFileCategory: boolean
  showDialogAttachExistingFile: boolean
  idCurrentDetailCategory: number | undefined
  currentChangeFileCategory: ICurrentChangeFileCategory
  effectiveContract: boolean | null

}

export interface IQuestionnaireStatisticsTable {
  tableName?: string
  rows: { [key: string]: string | number }[]
  columns: { [key: string]: string | number }[]
  nested?: this[]
}
