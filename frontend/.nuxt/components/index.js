import { wrapFunctional } from './utils'

export { default as Foot } from '../../components/Foot.vue'
export { default as Formzapic } from '../../components/Formzapic.vue'
export { default as Nav } from '../../components/Nav.vue'

export const LazyFoot = import('../../components/Foot.vue' /* webpackChunkName: "components/foot" */).then(c => wrapFunctional(c.default || c))
export const LazyFormzapic = import('../../components/Formzapic.vue' /* webpackChunkName: "components/formzapic" */).then(c => wrapFunctional(c.default || c))
export const LazyNav = import('../../components/Nav.vue' /* webpackChunkName: "components/nav" */).then(c => wrapFunctional(c.default || c))
