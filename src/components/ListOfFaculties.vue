<template>
  <div class="row">
    <div
      v-for="faculty of props.faculties"
      :key="faculty?.id"
      class="q-pa-md col-4"
    >
      <div class="text-h4 list-faculties-header">
        <img
          v-if="faculty?.logo"
          :src="faculty?.logo"
          :alt="`Логотип ${faculty?.name}`"
          class="list-faculties-header__img"
        />
        <div>{{ faculty?.name }}</div>
      </div>
      <q-list
        bordered
        v-for="department of faculty?.departments"
        :key="department?.id"
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
</template>

<script setup lang="ts">
  import { IListOfFaculties, IQuestionnaireBase } from 'types/questionnaire'
  import { PropType, onMounted, ref } from 'vue'
  import { useRouter } from 'vue-router'
  import { useQuestionnaire } from 'composables/useQuestionnaire'
  const router = useRouter()

  const { getQuestionnaireAllList, generateDepartmentReport } =
    useQuestionnaire()
  const questionnaireList = ref<IQuestionnaireBase[]>()

  const goToDepartment = (idDepartment: number) => {
    void router.push({
      name: 'ListOfDepartmentsPage',
      params: { id_department: idDepartment }
    })
  }

  const props = defineProps({
    faculties: Object as PropType<IListOfFaculties[]>
  })
  onMounted(async () => {
    questionnaireList.value = await getQuestionnaireAllList()
  })
</script>
