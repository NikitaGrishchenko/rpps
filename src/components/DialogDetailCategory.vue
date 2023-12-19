<template>
  <q-dialog
    v-model="showDialogDetailCategory"
    @show="setCurrentCategory()"
    no-backdrop-dismiss
    no-esc-dismiss
    class="dialog-detail-category"
  >
    <q-card
      style="width: 800px; max-width: 80vw; min-height: 450px; box-shadow: none"
    >
      <q-card-section
        v-if="categoryUser !== undefined"
        class="row items-center q-pb-none"
      >
        <div class="col-10 text-h5">
          Категория анкеты "{{
            categoryUser?.categoryQuestionnaire?.referenceCategory?.name
          }}"
        </div>
        <q-space />
        <q-btn
          @click="closeDialogDetailCategory()"
          icon="close"
          flat
          round
          dense
          v-close-popup
        />
      </q-card-section>
      <q-card-section
        v-show="categoryUser !== undefined"
        class="row items-center q-pb-none"
      >
        <q-btn
          v-if="questionnaireClosed === 1 && !isCheckingUser"
          @click="openDialogUploadFileToCategory()"
          class="main-btn"
          icon="mdi-cloud-upload-outline"
          label="Загузить новый файл"
        />
        <!-- <q-btn
          v-if="questionnaireClosed === 1 && !isCheckingUser"
          @click="openDialogAttachExistingFile()"
          class="main-btn q-ml-sm"
          icon="mdi-paperclip"
          label="Прикрепить существующий файл"
        /> -->
        <DialogDetailCategoryExpert
          v-if="categoryUser !== undefined && isCheckingUser"
          :result-point="categoryUser?.resultPoint"
          :result-point-fixed="categoryUser?.resultPointFixed"
          :is-verified="categoryUser?.isVerified"
          @close-dialog-detail-category="closeDialogDetailCategory"
        />
      </q-card-section>
      <q-card-section
        v-if="!!categoryUser?.files && categoryUser?.files?.length > 0"
        class="q-mt-md"
      >
        <h3>Прикрепленные файлы</h3>
        <div v-for="(file, index) in files" :key="file.id">
          <DialogDetailCategoryItem
            @update-file-category-user="setCurrentCategory"
            :index="index + 1"
            :file="file"
            :type-category="categoryUser?.categoryQuestionnaire?.typeCategory"
            :use-internet-resource-link="
              categoryUser?.categoryQuestionnaire?.useInternetResourceLink
            "
            :internet-resource-link-or-doc="
              categoryUser?.categoryQuestionnaire?.internetResourceLinkOrDoc
            "
          />
        </div>
      </q-card-section>
      <q-card-section
        v-if="!!categoryUser?.files && categoryUser?.files?.length === 0"
      >
        <div class="row">
          <div class="col-12 text-center items-center q-pt-md">
            <img src="~assets/images/files_page.svg" style="height: 250px" />
            <h3 class="q-my-md">Нет добавленных файлов</h3>
          </div>
        </div>
      </q-card-section>
      <q-inner-loading :showing="categoryUser == null">
        <q-spinner-puff class="fixed-center" size="50px" color="primary" />
      </q-inner-loading>
    </q-card>
    <DialogUploadFileToCategory
      :show-dialog="showDialogUploadFileToCategory"
      @update-file-category-user="setCurrentCategory"
    />
    <DialogChangeFileCategory
      @update-file-category-user="setCurrentCategory"
      :show-dialog="showDialogChangeFileCategory"
    />
    <DialogAttachExistingFile
      @update-file-category-user="setCurrentCategory"
      :show-dialog="showDialogAttachExistingFile"
    />
  </q-dialog>
</template>

<script setup lang="ts">
  import { useQuestionnaire } from 'composables/useQuestionnaire'
  import DialogDetailCategoryItem from 'src/components/DialogDetailCategoryItem.vue'
  import { ICategoryDialog, IFile } from 'src/types/questionnaire'
  import { computed, ref } from 'vue'
  import { useStore } from '../store/index'
  import DialogUploadFileToCategory from 'src/components/DialogUploadFileToCategory.vue'
  import DialogChangeFileCategory from 'src/components/DialogChangeFileCategory.vue'
  import DialogDetailCategoryExpert from 'components/DialogDetailCategoryExpert.vue'
  import DialogAttachExistingFile from 'components/DialogAttachExistingFile.vue'

  const store = useStore()

  const { getCategoryUser } = useQuestionnaire()

  const props = defineProps({
    showDialog: Boolean
  })

  const categoryUser = ref<ICategoryDialog>()
  const files = ref<IFile[]>()

  const isCheckingUser = computed(
    // eslint-disable-next-line @typescript-eslint/no-unsafe-member-access
    (): any => store.getters['auth/isSuperExpertCheckingUser']
  )

  const setCurrentCategory = async () => {
    categoryUser.value = undefined
    categoryUser.value = await getCategoryUser(
      store.state.questionnaire.idCurrentDetailCategory
    )
    files.value = categoryUser.value?.files
  }

  let showDialogDetailCategory = ref()
  showDialogDetailCategory = computed(() => {
    return props.showDialog
  })

  const questionnaireClosed = computed(
    () => store.state.questionnaire.info.status
  )

  const closeDialogDetailCategory = () => {
    store.commit('questionnaire/closeDialogDetailCategory')
    store.commit('questionnaire/deleteIdCurrentDetailCategory')
    categoryUser.value = undefined
  }

  let showDialogUploadFileToCategory = ref()
  const openDialogUploadFileToCategory = () => {
    store.commit('questionnaire/openDialogUploadFileToCategory')
  }
  showDialogUploadFileToCategory = computed(
    () => store.state.questionnaire.showDialogUploadFileToCategory
  )

  let showDialogChangeFileCategory = ref()
  showDialogChangeFileCategory = computed(
    () => store.state.questionnaire.showDialogChangeFileCategory
  )

  let showDialogAttachExistingFile = ref()
  showDialogAttachExistingFile = computed(
    () => store.state.questionnaire.showDialogAttachExistingFile
  )
  // const openDialogAttachExistingFile = () => {
  //   store.commit('questionnaire/openDialogAttachExistingFile')
  // }
</script>
