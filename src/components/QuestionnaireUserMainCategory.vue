<template>
  <div class="questionnaire">
    <div class="questionnaire-main-category">
      <p class="questionnaire-main-category__text">
        {{ props?.mainCategory?.name }}
      </p>
      <div class="questionnaire-main-category__point">
        {{
          actualPointMainCategory(
            props?.mainCategory?.resultPoint,
            props?.mainCategory?.resultPointFixed
          )
        }}
      </div>
    </div>
    <div class="questionnaire-category">
      <div class="questionnaire-category-header">
        <div
          class="questionnaire-category-header__cell questionnaire-category-header__cell--number"
        >
          №
        </div>
        <div
          class="questionnaire-category-header__cell questionnaire-category-header__cell--name"
        >
          Наименование
        </div>
        <div
          class="questionnaire-category-header__cell questionnaire-category-header__cell--description"
        >
          Описание
        </div>
        <div
          class="questionnaire-category-header__cell questionnaire-category-header__cell--periodicity"
        >
          Период
        </div>
        <div
          class="questionnaire-category-header__cell questionnaire-category-header__cell--weight"
        >
          Вес
        </div>
        <div
          class="questionnaire-category-header__cell questionnaire-category-header__cell--rating"
        >
          Показатели
        </div>
        <div
          class="questionnaire-category-header__cell questionnaire-category-header__cell--count-files"
          style="width: 5%"
        ></div>
      </div>

      <QuestionnaireUserCategory
        v-for="category in props?.mainCategory?.category"
        :key="category?.id"
        :category="category"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
  import { PropType } from 'vue'
  import { IMainCategory } from 'types/questionnaire'
  import QuestionnaireUserCategory from 'components/QuestionnaireUserCategory.vue'
  import { useQuestionnaire } from 'composables/useQuestionnaire'

  const { actualPointMainCategory } = useQuestionnaire()

  const props = defineProps({
    mainCategory: Object as PropType<IMainCategory>
  })
</script>
