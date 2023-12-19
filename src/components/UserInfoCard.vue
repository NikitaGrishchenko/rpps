<template>
  <q-card>
    <q-card-section>
      <q-select
        v-model="selectedDepartment"
        popup-content-class="input-textfield"
        filled
        color="primary"
        label="Кафедра"
        :options="departments"
        option-label="name"
        @update:model-value="handleUpdate"
      />
      <q-select
        v-model="selectedPosition"
        popup-content-class="input-textfield"
        filled
        color="primary"
        label="Должность"
        :options="positions"
        option-label="name"
        @update:model-value="handleUpdate"
      />
      <q-select
        v-model="selectedRate"
        popup-content-class="input-textfield"
        filled
        color="primary"
        label="Ставка"
        :options="rates"
        option-label="value"
        @update:model-value="handleUpdate"
      />
    </q-card-section>
  </q-card>
</template>

<script setup lang="ts">
  import { IUserPosition } from 'src/types/auth'
  import { IDepartment, IPosition, IRate } from 'src/types/reference'
  import { onMounted, ref } from 'vue'

  const props = defineProps<{
    userPosition: IUserPosition
    rates: IRate[]
    positions: IPosition[]
    departments: IDepartment[]
  }>()
  const emit = defineEmits<{
    (e: 'updateUserPosition', userPosition: IUserPosition): void
  }>()

  const selectedDepartment = ref<IDepartment>()
  const selectedPosition = ref<IPosition>()
  const selectedRate = ref<IRate>()

  const handleUpdate = () => {
    emit('updateUserPosition', {
      id: props.userPosition.id,
      user: props.userPosition.user,
      department: selectedDepartment.value?.id || props.userPosition.department,
      position: selectedPosition.value?.id || props.userPosition.position,
      rate: selectedRate.value?.id || props.userPosition.rate
    })
  }

  onMounted(() => {
    selectedDepartment.value = props.departments.filter(
      (item) => props.userPosition.department === item.id
    )[0]
    selectedPosition.value = props.positions.filter(
      (item) => props.userPosition.position === item.id
    )[0]
    selectedRate.value = props.rates.filter(
      (item) => props.userPosition.rate === item.id
    )[0]
  })
</script>
