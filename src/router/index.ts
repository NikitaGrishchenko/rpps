import { route} from 'quasar/wrappers';
import {
  createMemoryHistory,
  createRouter,
  createWebHashHistory,
  createWebHistory,
} from 'vue-router';
import { StateInterface } from '../store';
import routes from './routes';
import { api } from 'boot/axios';
import _ from 'lodash'


export default route<StateInterface>(function ( { store }) {
  const createHistory = process.env.SERVER
    ? createMemoryHistory
    : (process.env.VUE_ROUTER_MODE === 'history' ? createWebHistory : createWebHashHistory);



  const Router = createRouter({
    scrollBehavior: () => ({ left: 0, top: 0 }),
    routes,

    history: createHistory(
      process.env.MODE === 'ssr' ? void 0 : process.env.VUE_ROUTER_BASE
    ),
  });

  Router.beforeEach(async (to)  => {
    // при обновлении или открытии страницы загрузка данных в store
    if (store.state.auth.isAuth === false) {
        await api.get('/auth/user/data/').then((response) => {
          store.commit('auth/loginUser', response.data)
          }).catch(() => {
            store.commit('auth/logoutUser')
          });
    }
    // если страница открыта
    if (_.includes(to.meta.middleware as [], 'open')) {
      return
    // доступ для админа
    } else if (_.includes(to.meta.middleware as [], 'admin')) {
      if (store.state.auth.isAuth === true && store.state.auth.user.isAdmin) {
        return
      } else {
        return Router.push('/')
    }
    // обработка страницы логин
  } else if (_.includes(to.meta.middleware as [], 'login')) {
    if (store.state.auth.isAuth === true) {
      return Router.push('/')
    } else if (store.state.auth.isAuth === false){
      return
    }
    // доступ для обычного пользователя
    } else if (_.includes(to.meta.middleware as [], 'auth')) {
      if (store.state.auth.isAuth === true) {
      } else {
        return Router.push('/login')
      }
    }
  })

  return Router;
});
