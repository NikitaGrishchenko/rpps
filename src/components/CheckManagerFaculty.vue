<template>
  <div v-if="faculty" class="row">
    <div class="col-12 q-my-md">
      <h2>
        Факультет <strong>{{ toLowerCaseString(faculty?.name) }}</strong>
      </h2>
    </div>
    <div class="col-12">
      <div class="row">
        <q-list
          v-for="department of faculty.departments"
          :key="department?.id"
          bordered
          separator
          class="col-12"
        >
          <q-item clickable class="list-faculties-name">
            <q-item-section class="text-h5">
              <div class="row">
                <div
                  class="col-9 flex items-center"
                  @click="goToDepartment(department?.id)"
                >
                  {{ department?.name }}
                </div>
                <div
                  class="col-3 flex items-center justify-end list-faculties-report"
                >
                  <q-btn-dropdown
                    size="13px"
                    flat
                    fab-mini
                    icon="mdi-microsoft-excel"
                    dense
                  >
                    <q-list dense>
                      <q-item
                        v-for="questionnaire in questionnaireList"
                        :key="questionnaire.id"
                        clickable
                        v-close-popup
                        @click="
                          generateDepartmentReport(
                            department.id,
                            questionnaire.id
                          )
                        "
                      >
                        <q-item-section>
                          <q-item-label class="text-h5">{{
                            questionnaire.name
                          }}</q-item-label>
                        </q-item-section>
                      </q-item>
                    </q-list>
                  </q-btn-dropdown>
                </div>
              </div>
            </q-item-section>
          </q-item>
        </q-list>
      </div>
    </div>
  </div>
  <q-inner-loading :showing="faculty === undefined">
    <q-spinner-puff class="fixed-center" size="50px" color="primary" />
  </q-inner-loading>
</template>

<script setup lang="ts">
  import { IListOfDepartments, IQuestionnaireBase } from 'types/questionnaire'
  import { useQuestionnaire } from 'composables/useQuestionnaire'
  import { onMounted, ref } from 'vue'
  import { useStore } from '../store/index'
  import { useRouter } from 'vue-router'

  const {
    getDepartmentsOfOneFaculty,
    getQuestionnaireAllList,
    generateDepartmentReport
  } = useQuestionnaire()
  const store = useStore()
  const router = useRouter()

  const questionnaireList = ref<IQuestionnaireBase[]>()

  const goToDepartment = (idDepartment: number) => {
    void router.push({
      name: 'ListOfDepartmentsPage',
      params: { id_department: idDepartment }
    })
  }

  const toLowerCaseString = (str: string) => {
    if (str !== undefined) {
      return str.toLowerCase()
    }
  }

  const faculty = ref<IListOfDepartments[]>()

  onMounted(async () => {
    const idFaculty: number | null = store.state.auth.user.managerFacultyId
    if (idFaculty !== null) {
      faculty.value = await getDepartmentsOfOneFaculty(idFaculty)
    }
    questionnaireList.value = await getQuestionnaireAllList()
  })
</script>
