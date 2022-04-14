import {createRouter, createWebHistory} from 'vue-router'
import Home from '@/views/Home.vue'
import Team from '@/views/Team.vue'
import Construction from '@/views/Construction.vue'
import Sponsoren from '@/views/Sponsoren.vue'

const routes = [
    {path: '/', name: 'Home', component: Home},
    {path: '/team', name: 'Team', component: Team},
    {path: '/construction', name: 'Construction', component: Construction},
    {path: '/sponsoren', name: 'Sponsoren', component: Sponsoren},

]

const router = createRouter({
    history: createWebHistory(),
    routes
})
export default router