import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      redirect: "/python",
    },
    {
      path: "/python",
      name: "python",
      component: () => import("@/views/Python.vue"),
    },
    {
      path: "/login",
      name: "login",
      component: () => import("@/views/login.vue"),
    },
    {
      path: "/echarts",
      name: "echarts",
      component: () => import("@/views/echarts.vue"),
    },
    {
      path: "/users",
      name: "users",
      component: () => import("@/views/users.vue"),
    },
    {
      path: "/settings",
      name: "settings",
      component: () => import("@/views/settings.vue"),
    },
  ],
});

export default router;
