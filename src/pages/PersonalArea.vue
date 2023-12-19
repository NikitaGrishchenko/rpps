<template>
  <q-page class="container">
    <div class="text-primary text-bold text-h4 q-pb-md">Личный кабинет</div>
    <q-form @submit.prevent="handleSubmit">
      <div class="row q-py-md">
        <div class="col-12 text-h4 q-py-md">Фотография пользователя</div>
        <div class="col-12 column items-center q-gutter-y-md">
          <div class="full-width row">
            <InputAvatar v-model="userInfo.userImage" />
          </div>
        </div>
      </div>
      <div
        class="row"
        v-if="reference.rates && reference.positions && reference.departments"
      >
        <div class="col-12 text-h4 q-py-md">Профиль пользователя</div>
        <UserInfoCard
          class="col-12 q-my-sm"
          v-for="userPosition in userInfo?.userPositions"
          :key="userPosition.id"
          :userPosition="userPosition"
          :rates="reference.rates"
          :positions="reference.positions"
          :departments="reference.departments"
          @update-user-position="updateUserPosition"
        />
      </div>
      <div class="row q-py-md flex justify-end">
        <q-btn :loading="inProcess" label="Обновить информацию" type="submit" />
      </div>
    </q-form>
    <q-inner-loading :showing="inProcess">
      <q-spinner-puff class="fixed-center" size="50px" color="primary" />
    </q-inner-loading>
  </q-page>
</template>

<script setup lang="ts">
  import InputAvatar from 'components/InputAvatar.vue'
  import UserInfoCard from 'components/UserInfoCard.vue'
  import { useAuth } from 'src/composables/useAuth'
  import { useReference } from 'src/composables/useReference'
  import { useStore } from 'src/store'
  import { IUserInfo, IUserPosition } from 'src/types/auth'
  import { onMounted, ref } from 'vue'

  const $store = useStore()

  const { reference } = useReference(['positions', 'rates', 'departments'])
  const { getUserInfo, updateUserInfo, inProcess } = useAuth()

  const userInfo = ref<IUserInfo>({ userImage: undefined, userPositions: [] })

  const updateUserPosition = (newUserPosition: IUserPosition) => {
    if (userInfo.value) {
      userInfo.value.userPositions = userInfo.value?.userPositions.map(
        (userPosition) => {
          return userPosition.id === newUserPosition.id
            ? newUserPosition
            : userPosition
        }
      )
    }
  }

  const handleSubmit = () => {
    userInfo.value &&
      void updateUserInfo(userInfo.value).then(() => {
        $store.commit('auth/updateUserImage', userInfo.value.userImage)
      })
  }

  onMounted(async () => {
    const data = await getUserInfo()
    if (data) userInfo.value = data
  })
</script>
