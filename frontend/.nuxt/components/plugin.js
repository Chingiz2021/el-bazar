import Vue from 'vue'
import { wrapFunctional } from './utils'

const components = {
  Foot: () => import('../../components/Foot.vue' /* webpackChunkName: "components/foot" */).then(c => wrapFunctional(c.default || c)),
  Formzapic: () => import('../../components/Formzapic.vue' /* webpackChunkName: "components/formzapic" */).then(c => wrapFunctional(c.default || c)),
  Nav: () => import('../../components/Nav.vue' /* webpackChunkName: "components/nav" */).then(c => wrapFunctional(c.default || c))
}

for (const name in components) {
  Vue.component(name, components[name])
  Vue.component('Lazy' + name, components[name])
}
