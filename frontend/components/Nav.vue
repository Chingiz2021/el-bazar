<template>
<div >
  <b-navbar  class="fixed-top box-nav" style="background:white"  toggleable="lg"  variant="faded" type="light" >
    <b-navbar-brand href="#"><img class="img-fluid" src="Logo.png" alt=""></b-navbar-brand>
    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav class="ml-auto ">
        <b-nav-item  href="#">О НАС</b-nav-item>
        <b-nav-item  href="#">КАК ЭТО РАБОТАЕТ</b-nav-item>
        <b-nav-item  href="#">КАТАЛОГ</b-nav-item>
        <b-nav-item  href="#">БОНУСЫ</b-nav-item>
        <b-nav-item  href="#">ДЛЯ БИЗНЕСА</b-nav-item>
        <b-nav-item  href="#">КОНТАКТЫ</b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</div>

</template>

<style  scoped>
img{
    width: 10rem;
}
.navbar-expand-lg .navbar-nav .nav-link{
    font-size: .85rem;
}
.box-nav{
  padding-left: 10rem;
  padding-right: 10rem;
}
@media (max-width:500px) {
  .box-nav{
  padding-left: 1rem;
  padding-right: 1rem;
}
}
</style>