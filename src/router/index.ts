import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
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
//   {
//       path: '/kitchen',
//       name: 'kitchen',
//       component: () => import('../pages/Kitchen.vue')
//   },
  {
      path: '/todolist',
      name: 'todolist',
      component: () => import('../pages/todolist.vue')
  },
  ]
})

export default router
