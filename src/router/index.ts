import { createRouter, createWebHistory } from 'vue-router'
// import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // {
    //   path: '/',
    //   name: 'home',
    //   component: HomeView
    // },
    // {
    //   path: '/about',
    //   name: 'about',
    //   // route level code-splitting
    //   // this generates a separate chunk (About.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import('../views/AboutView.vue')
    // },
    {
      path: '/gate',
      name: 'gate',
      component: () => import('../pages/Gate.vue')
  },
  {
      path: '/livingroom',
      name: 'livingroom',
      component: () => import('../pages/Livingroom.vue')
  },
  {
      path: '/kitchen',
      name: 'kitchen',
      component: () => import('../pages/Kitchen.vue')
  },
  {
      path: '/todolist',
      name: 'todolist',
      component: () => import('../pages/todolist.vue')
  },
  ]
})

export default router
