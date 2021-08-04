<template>
  <div>
      <Nav />
    <div class="d-lg-none d-block">
      <!-- <Navmobile /> -->
    </div>
    <main>
      <Nuxt />
    </main>
    <footer id="contact" style="background: #f6f6f6">
      <Foot/>
    </footer>
  </div>
</template>

<script>
export default {
  head(){
    return{
      link:[{rel:"canonical",href:`http://localhost:3000${this.$route.path}`}]
    }
  },
   
}
</script>