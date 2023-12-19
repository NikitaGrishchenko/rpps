import { IPrizePlaces } from 'types/reference'

export interface IReferenceState {
  prizePlaces: IPrizePlaces | undefined
}

function state(): IReferenceState {
  return {
    prizePlaces: undefined
  }
}

export default state
