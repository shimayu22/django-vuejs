import Vue from 'vue'
import VueRouter from 'vue-router'

import Auth from '../components/pages/Auth'
import HedgeHogs from '../components/pages/HedgeHogs'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'HedgeHogs',
    component: HedgeHogs
  },
  {
    path: '/auth',
    name: 'Auth',
    component: Auth
    // component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
