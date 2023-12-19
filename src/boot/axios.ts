
import axios, { AxiosError, AxiosInstance, AxiosResponse } from 'axios';
import { boot } from 'quasar/wrappers';

declare module '@vue/runtime-core' {
  interface ComponentCustomProperties {
    $axios: AxiosInstance;
  }
}

const api = axios.create({
  baseURL: process.env.DEV
    ? 'http://localhost:8000/api/v1'
    : '/api/v1/',
  withCredentials: true,
  headers: {'Content-Type': 'application/json'}
});



export default boot(({ app, store,   }) => {

  app.config.globalProperties.$axios = axios;


  app.config.globalProperties.$api = api;


  api.interceptors.response.use((response: AxiosResponse) => {
    return response;
  }, (error: AxiosError)  => {
    if (error.response?.status === 401) {
      store.commit('auth/logoutUser')
    }
    return Promise.reject(error);
  });


});

export { api };
