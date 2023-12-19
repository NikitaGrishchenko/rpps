<template>
  <div
    class="input-avatar__wrapper"
    :class="{ 'input-avatar__wrapper--no-image': !modelValue }"
    @dragenter="handleDragEnter"
    @drop="handleDragEnd"
    @dragleave="handleDragEnd"
  >
    <img class="input-avatar__image" :src="(modelValue as string)" alt="" />
    <input @change="handleImage" class="input-avatar__field" type="file" />
    <q-menu class="input-avatar__context" context-menu>
      <q-list>
        <q-item
          class="input-avatar__context-item"
          @click="updateImage(null)"
          clickable
          v-close-popup
        >
          <q-item-section>Удалить фото</q-item-section>
        </q-item>
      </q-list>
    </q-menu>
  </div>
</template>

<script setup lang="ts">
  defineProps<{
    modelValue?: FileReader['result']
  }>()
  const emit = defineEmits<{
    (e: 'update:modelValue', modelValue: FileReader['result']): void
  }>()

  const handleImage = (e: Event) => {
    const images = (<HTMLInputElement>e.target).files
    const reader = new FileReader()

    if (images) {
      reader.onload = (e) => {
        e.target && updateImage(e.target.result)
      }
      reader.readAsDataURL(images[0])
    }
  }
  const handleDragEnter = (e: Event) => {
    ;(<HTMLElement>e.currentTarget).classList.add(
      'input-avatar__wrapper--hover'
    )
  }
  const handleDragEnd = (e: Event) => {
    ;(<HTMLElement>e.currentTarget).classList.remove(
      'input-avatar__wrapper--hover'
    )
  }

  const updateImage = (image: FileReader['result']) => {
    emit('update:modelValue', image)
  }
</script>
