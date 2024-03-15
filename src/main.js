import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
// import GateComponent from './components/GateComponent.vue'
import LivingroomComponent from './components/Livingroom.vue'


const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/gate',
            name: 'gate',
            component: () => import('./components/Gate.vue')
        },
        {
            path: '/livingroom',
            name: 'livingroom',
            component: LivingroomComponent
        },
        {
            path: '/kitchen',
            name: 'kitchen',
            component: () => import('./components/Kitchen.vue')
        },
        {
            path: '/terrace',
            name: 'terrace',
            component: () => import('./components/Terrace.vue')
        },
        {
            path: '/construction',
            name: 'construction',
            component: () => import('./components/Construction.vue')
        },

    ]
});
export default router


const app = createApp(App)
app.use(router)
app.mount('#app')