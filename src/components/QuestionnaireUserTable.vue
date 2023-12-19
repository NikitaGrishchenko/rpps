<template>
  <div class="col-12 questionnaire-user-table">
    <div v-for="mainCategory in props?.questionnaire" :key="mainCategory?.id">
      <QuestionnaireUserMainCategory
        :mainCategory="mainCategory"
        v-if="hideMainCategoryForExpert(mainCategory?.idReferenceCategory)"
      />
    </div>
    <DialogDetailCategory :showDialog="showDialogDetailCategory" />
    <!-- <DialogEffectiveContract /> -->
  </div>
</template>

<script setup lang="ts">
  import DialogDetailCategory from 'src/components/DialogDetailCategory.vue'
  // import DialogEffectiveContract from 'src/components/DialogEffectiveContract.vue'
  import QuestionnaireUserMainCategory from 'components/QuestionnaireUserMainCategory.vue'
  import { IMainCategory } from 'types/questionnaire'
  import { computed, PropType } from 'vue'
  import { useStore } from '../store/index'

  const store = useStore()

  const props = defineProps({
    questionnaire: Object as PropType<IMainCategory[]>
  })

  const showDialogDetailCategory = computed(
    () => store.state.questionnaire.showDialogDetailCategory
  )

  /** Если пользователь эсперт определенной категории, функция скроет остальное главные категории **/
  const hideMainCategoryForExpert = (idReferenceCategory: number) => {
    if (store.state.auth.user.isExpert) {
      const categoryExpertId = store.state.auth.user.categoryExpertId
      if (idReferenceCategory != categoryExpertId) {
        return false
      }
    }
    return true
  }
</script>
