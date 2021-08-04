<template>
  <div class="container">
    <h2 class="text-center mt-5">Вход в панель администратора</h2>
     <form class="form justify-content-center" v-on:submit="postLogin($event)">
       <label for="email">Email адресс</label>
            <input
              type="email"
              id="email"
              class="form-control"
              v-model="email"
              placeholder="email"
            />
            <label class="mt-4" for="password">Введите пароль</label>
            <input
              type="password"
              id="password"
              class=" form-control "
              v-model="password"
              placeholder="Пароль"
            />
            <div class="text-center mt-5">
              <button class="btn btn-info" type="submit">войти</button>
             
            </div>
          </form>
  </div>
</template>

<script>
const Cookie = process.client ? require("js-cookie") : undefined;
export default {
    layout: 'admin',
    data() {
      return {
        password: '',
        email:''
      };
    },
    methods:{
      postLogin(event) {
      event.preventDefault();
      let data = {
        username: this.email,
        password: this.password
      };
      var formData = new FormData();
      Object.keys(data).forEach((key) => {
      formData.append(key, data[key])
    })
    
      const headers = {
        "Content-Type": "application/json"
      };
      let response = this.$axios
        .$post("https://el-bazaar.kz/api/v1/auth/jwt/login", formData, {
          headers
        })
        .then(
          token => {
            const auth = {
              access_token: `Bearer ${token.access_token}`,
              user: token.user
            };
            this.$store.commit("setAuth", auth);
            Cookie.set("auth", auth);
            this.$router.push('/admin/'+'data')
          },
          error => {
            console.log(error);
          }
        );
    }
    }

    

}
</script>


