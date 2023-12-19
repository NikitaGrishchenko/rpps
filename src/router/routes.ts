import { RouteRecordRaw } from 'vue-router'

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {
        path: '',
        name: 'IndexPage',
        component: () => import('pages/Index.vue')
      },
      {
        path: 'files/',
        name: 'FilesPage',
        component: () => import('pages/Files.vue')
      },
      {
        path: 'personal-area/',
        name: 'PersonalArea',
        component: () => import('pages/PersonalArea.vue')
      }
    ],
    meta: { middleware: ['auth'] }
  },
  {
    path: '/creating-questionnaires',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {
        path: '',
        name: 'CreatingQuestionnaires',
        component: () => import('pages/CreatingQuestionnaires.vue')
      }
    ],
    meta: { middleware: ['admin'] }
  },
  {
    path: '/statistics',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {
        path: '',
        name: 'StatisticsPage',
        component: () => import('pages/QuestionnaireStatistics.vue')
      }
    ],
    meta: { middleware: ['admin'] }
  },
  {
    path: '/registration',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {
        path: '',
        name: 'UserRegistration',
        component: () => import('pages/UserRegistration.vue')
      }
    ],
    meta: { middleware: ['admin'] }
  },
  {
    path: '/application-submission',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {
        path: '',
        name: 'ApplicationSubmissionPage',
        component: () => import('pages/ApplicationSubmission.vue')
      }
    ],
    meta: { middleware: ['open'] }
  },
  {
    path: '/login',
    component: () => import('layouts/EmptyLayout.vue'),
    children: [
      {
        path: '',
        name: 'LoginPage',
        component: () => import('pages/Login.vue')
      }
    ],
    meta: { middleware: ['login'] }
  },
  {
    path: '/ListOfDepartments',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {
        path: '/department/:id_department',
        name: 'ListOfDepartmentsPage',
        component: () => import('pages/ListOfDepartments.vue')
      }
    ],
    meta: { middleware: ['auth'] }
  },
  {
    path: '/manual',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {
        path: '',
        name: 'ManualPage',
        component: () => import('pages/Manual.vue')
      }
    ],
    meta: { middleware: ['open'] }
  },
  {
    path: '/questionnaire/:idQuestionnaire',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {
        path: '',
        name: 'QuestionnaireUserPage',
        component: () => import('pages/QuestionnaireUser.vue')
      }
    ],
    meta: { middleware: ['auth'] }
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    name: 'ErrorPage',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
