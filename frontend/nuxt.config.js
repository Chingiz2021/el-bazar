export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'Отборные Фрукты И Овощи По Оптовым ценам |В Казахстане',
    htmlAttrs: {
      lang: 'en'
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: 'El-Bazaar- это отборные фрукты и овощи по оптовым ценам у вашей двери в Казахстане' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },
 

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
    '@/theme/index.css'
  ],
  
  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    '@/plugins/telinput.js'
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/bootstrap
    'bootstrap-vue/nuxt',
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    '@nuxtjs/robots',
    '@nuxtjs/sitemap'
  ],

  sitemap: {
    generate: true,
    hostname: 'http://localhost:3000',
    exclude: [
      '/admin',
      '/admin/data',
    ]
  },

//port
  server: {
    port: 80 // default: 3000
  },
  robots: {
    /* module options */
  },
  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {},
  auth: {
    // Options
  },
  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
  }
}
