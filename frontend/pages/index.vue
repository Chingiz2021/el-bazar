<template>
  <div class="mt-5">
    <div class="header_content">
      <div>
        <div
          class="text-center pt-5"
          style="display: flex; justify-content: center"
        >
          <p style="width: 12rem; background: #ffffff73; font-weight: bold">
            Сайт находится в стадии разработки!
            <br />
            Мы запускаем свой сервис 1 сентября 2021 года.
          </p>
        </div>

        <h1 class="text-center pt-5">
          El-Bazaar
          <br />
          - это отборные фрукты и овощи
          <br />
          по оптовым ценам у вашей двери
        </h1>
      </div>

      <div id="form-div" class="container">
        <Formzapic :oncount="oncount" />
      </div>
      <div class="mt-5">
        <p class="text-center other-header" style="background: #fdfdfdc2;">
          Уже зарегистрировались {{ count_appl }} человек
        </p>
        <p class="text-center mt-5 mb-5 other-header2">Лови момент!</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  robots: {
    UserAgent: '*',
    Disallow: ''
  },
  head: {
    title: "Отборные Фрукты И Овощи По Оптовым ценам |В Казахстане",
    meta: [
      {
        hid: "description",
        name: "description",
        content:
          "El-Bazaar- это отборные фрукты и овощи по оптовым ценам у вашей двери в Казахстане",
      },
    ],
  },
  data() {
    return {
      count: "",
    };
  },
  methods: {
    oncount() {
      this.count = this.count + 1;
    },
  },
  computed: {
    count_appl() {
      const headers = {
        "Content-Type": "application/json",
      };
      this.$axios
        .$get(`http://el-bazaar.kz/api/v1/appl/`, { 
          headers,
        })
        .then(
          (resp) => {
            this.count = String(resp);
          },
          (error) => {
            console.log(error);
          }
        );
      return this.count;
    },
  },
};
</script>

<style scoped>
.header_content {
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  background-image: url("/header.png");

  min-height: 120vh;
}
@media (max-width: 500px) {
  h1 {
    font-size: 1.3rem;
    padding: 1rem;
    font-weight: bold;
  }
}
.other-header {
  font-weight: bold;
  font-size: 1.3rem;
}
.other-header2 {
  color: #ff7c30;
  font-size: 1.5rem;
  font-weight: bold;
}
</style>
