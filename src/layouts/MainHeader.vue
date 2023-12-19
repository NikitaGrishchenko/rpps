<template>
  <q-toolbar class="main-header q-px-none q-py-md">
    <router-link :to="{ name: 'IndexPage' }" class="main-header__link">
      <q-toolbar-title class="flex no-wrap items-center">
        <q-avatar class="main-header__img">
          <img src="~assets/images/rsue-logo.svg" alt="РГЭУ (РИНХ)" />
        </q-avatar>
        <div class="text-h4 main-header__title section-title q-ml-sm">
          Рейтинг профессорско-<br />преподавательского состава
        </div>
      </q-toolbar-title>
    </router-link>
    <q-space />
    <template v-if="$store.state.auth.isAuth">
      <!-- <q-btn
        class="main-header__tool q-mx-sm"
        padding="sm"
        dense
        rounded
        flat
        label="Помощь"
        icon-right="mdi-help-circle-outline"
      /> -->
      <!-- <q-btn
        v-if="$store.state.auth.isAuth"
        class="main-header__tool q-mx-sm"
        dense
        rounded
        flat
        href="https://docs.google.com/forms/d/e/1FAIpQLSfcKzu0BpS7Bo0pw2gxwKWlnmJSNXsHOv54ftUA-3e5aD6wgQ/viewform?usp=sf_link"
        target="_blank"
        label="Заполнить эффективный контракт"
      /> -->
      <q-btn
        :loading="inProcess"
        class="user-card"
        flat
        :icon="
          $store.state.auth.user.userImage
            ? `img:${$store.state.auth.user.userImage}`
            : 'mdi-account-circle'
        "
        icon-right="mdi-chevron-down"
        :label="$q.screen.gt.sm ? userFullName : ''"
        color="primary"
      >
        <q-menu
          :="
            $q.screen.gt.sm
              ? { self: 'top start', offset: [0, -10] }
              : { anchor: 'bottom start', offset: [0, 0] }
          "
          class="user-card__menu"
          fit
        >
          <q-list padding>
            <!-- <q-item
              v-show="!isCheckingUser"
              :to="{ name: 'PersonalArea' }"
              class="user-card__menu-item"
              clickable
              v-close-popup
            >
              <q-item-section
                ><q-icon class="q-mr-sm" name="mdi-account-outline" />Личный
                кабинет</q-item-section
              >
            </q-item> -->
            <q-item
              v-show="!isCheckingUser"
              :to="{ name: 'FilesPage' }"
              class="user-card__menu-item"
              clickable
              v-close-popup
            >
              <q-item-section
                ><q-icon class="q-mr-sm" name="mdi-file-account-outline" />Мои
                файлы</q-item-section
              >
            </q-item>
            <q-item
              @click="eventLogoutUser"
              class="user-card__menu-item"
              clickable
              v-close-popup
            >
              <q-item-section>
                <q-icon class="q-mr-sm" name="mdi-logout" />
                Выйти из системы
              </q-item-section>
            </q-item>
          </q-list>
        </q-menu>
      </q-btn>
    </template>
    <!-- <q-btn
      v-else
      class="main-header__tool q-mx-sm"
      padding="sm"
      dense
      rounded
      flat
      label="Инструкция по работе с системой"
      icon="mdi-book-open-page-variant-outline"
    /> -->
  </q-toolbar>
</template>

<script setup lang="ts">
  import { useAuth } from 'composables/useAuth'
  import { useStore } from 'store'
  import { computed } from 'vue'

  const $store = useStore()

  const { userLogout, inProcess } = useAuth()

  // eslint-disable-next-line @typescript-eslint/no-unsafe-member-access
  const userFullName = computed((): any => $store.getters['auth/userFullName'])

  const isCheckingUser = computed(
    // eslint-disable-next-line @typescript-eslint/no-unsafe-member-access
    (): any => $store.getters['auth/isCheckingUser']
  )

  const eventLogoutUser = async () => {
    await userLogout()
  }
</script>

<!-- <style lang="sass">
  .user-card__menu-item .q-item__section
    justify-content: center !important
</style> -->
