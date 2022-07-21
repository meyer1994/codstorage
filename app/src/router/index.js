import { createRouter, createWebHashHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'repos',
    component: () => import(/* webpackChunkName: "group-landing" */ '@/views/ReposView'),
  },
  {
    path: '/repos/:ipld',
    name: 'repo',
    component: () => import(/* webpackChunkName: "group-landing" */ '@/views/RepoView'),
  },
  {
    path: '/branches/:ipld',
    name: 'branch',
    component: () => import(/* webpackChunkName: "group-landing" */ '@/views/BranchView'),
  },
  {
    path: '/trees/:ipld',
    name: 'tree',
    component: () => import(/* webpackChunkName: "group-landing" */ '@/views/TreeView'),
  },
  {
    path: '/files/:ipfs',
    name: 'file',
    component: () => import(/* webpackChunkName: "group-landing" */ '@/views/FileView'),
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
