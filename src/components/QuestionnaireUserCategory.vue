<template>
  <div
    @click="
      openDialogDetailCategory(
        props?.category?.typeCategory,
        props?.category?.id
      )
    "
    :class="[
      getBackgroundForCategory(props?.category),
      `questionnaire-category-line`
    ]"
  >
    <div
      class="questionnaire-category-line__cell questionnaire-category-line__cell--number"
    >
      {{ props?.category?.number }}
    </div>
    <div
      :class="[
        getIndentForCategory(),
        `questionnaire-category-line__cell--name`
      ]"
    >
      {{ props?.category?.name }}
    </div>
    <div
      class="questionnaire-category-line__cell questionnaire-category-line__cell--description"
    >
      {{ props?.category?.description }}
    </div>
    <div
      class="questionnaire-category-line__cell questionnaire-category-line__cell--periodicity"
    >
      {{ props?.category?.periodicity }}
    </div>
    <div
      class="questionnaire-category-line__cell questionnaire-category-line__cell--weight"
    >
      {{ props?.category?.weight }}
    </div>
    <div
      :class="[
        getColorForCategory(),
        `questionnaire-category-line__cell questionnaire-category-line__cell--rating`
      ]"
    >
      {{
        props?.category?.resultPointFixed !== null
          ? props?.category?.resultPointFixed
          : props?.category?.resultPoint
      }}
    </div>
    <div
      v-if="props?.category?.countFiles && props?.category?.countFiles > 0"
      class="questionnaire-category-line__cell questionnaire-category-line__cell--count-files"
    >
      +{{ props?.category?.countFiles }}
      <q-icon name="mdi-file-outline" size="20px" />
    </div>
  </div>
</template>

<script setup lang="ts">
  import { PropType } from 'vue'
  import { ICategory, ICategoryUser } from 'types/questionnaire'
  import { useStore } from '../store/index'

  const store = useStore()

  const props = defineProps({
    category: Object as PropType<ICategory>
  })

  const openDialogDetailCategory = (
    typeCategory: number | undefined,
    idCategory: number | undefined
  ) => {
    if (typeCategory !== null) {
      store.commit('questionnaire/openDialogDetailCategory')
      store.commit('questionnaire/setIdCurrentDetailCategory', idCategory)
    }
  }

  const getIndentForCategory = (): string => {
    return props.category?.nestingLevel === 3
      ? 'cell-name-nesting--third'
      : props.category?.nestingLevel === 2
      ? 'cell-name-nesting--second'
      : 'cell-name-nesting--first'
  }

  const getColorForCategory = (): string => {
    if (props.category?.resultPointFixed !== null) {
      return 'cell-point-color--yellow'
    } else if (props.category.resultPoint !== 0) {
      return 'cell-point-color--blue'
    }
    return 'cell-point-color--gray'
  }

  const getBackgroundForCategory = (
    category: ICategoryUser | undefined
  ): string => {
    if (category?.isVerified === true) {
      return 'questionnaire-category-line--verified'
    } else if (category?.isVerified === false) {
      return 'questionnaire-category-line--not-verified'
    }
    if (
      category?.isVerified === null &&
      category?.countFiles &&
      category?.countFiles > 0
    ) {
      return 'questionnaire-category-line--filled'
    }
    return 'questionnaire-category-line'
  }
</script>

<style lang="sass">
  .cell-name-nesting--first
    padding: 5px 5px 5px 5px
  .cell-name-nesting--second
    padding: 5px 5px 5px 20px
  .cell-name-nesting--third
    padding: 5px 5px 5px 40px
  .cell-point-color--blue
    color: #31498B
  .cell-point-color--gray
    color: #B1BBD7
  .cell-point-color--yellow
    color: #ffb300
</style>
