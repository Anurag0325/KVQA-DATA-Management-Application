import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'
import Dashboard from '../views/Dashboard.vue';
import Application from '../views/Application.vue'
import ApplicationForm from '../views/ApplicationForm.vue'
import StageForm from '../views/StageForm.vue'
import Stage2Form from '../views/Stage2Form.vue'
import ApplicationDetails from '../components/Applicationdetails.vue'

const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    meta: { requiresAuth: true } // Protect this route
  },
  {
    path: '/application',
    name: 'Application',
    component: Application,
  },
  {
    path: '/applicationform',
    name: 'ApplicationForm',
    component: ApplicationForm,
  },
  {
    path: '/stageform',
    name: 'Stage Form',
    component: StageForm,
  },
  {
    path: '/stage2form',
    name: 'Stage2 Form',
    component: Stage2Form
  },
  {
    path: "/application/:organisation_name/:audit_number",
    name: "ApplicationDetails",
    component: ApplicationDetails,
    props: true
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token');
  if (to.matched.some(record => record.meta.requiresAuth) && !token) {
    next('/');
  } else {
    next();
  }
});

export default router
