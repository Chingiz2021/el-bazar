<template>
  <div>
    <b-form style="padding-top:6rem" class="form" @submit.stop.prevent>
      <h2 class="text-center">
        Первые 1 000 клиентов получат бесплатную первую доставку!
      </h2>
      <p class="text-center other-text-form">
        Будь первым - получи свой подарок от компании за первую регистрацию!
        <br />
        Мы запускаем свой сервис 1 сентября 2021 года.
      </p>
      <div class="row justify-content-center">
        <div class="col-lg-4 col-12 p-lg-2 p-1">
          <b-form-input
            
            placeholder="Ваше имя"
            v-model="Username"
            :state="validation"
            id="feedback-user"
          ></b-form-input>
          <b-form-invalid-feedback :state="validation">
            Имя не меньше 1 символа
          </b-form-invalid-feedback>
          <b-form-valid-feedback :state="validation">
            Успешно.
          </b-form-valid-feedback>
        </div>
        <div class="col-lg-4 col-12 p-lg-2 p-1">
            <b-form-input
            
            placeholder="Ваш номер"
            v-model="phone"
            :state="validphone"
            id="feedback-phone"
          ></b-form-input>
          <b-form-invalid-feedback :state="validphone">
             Номер 11 цифр и только цифры
          </b-form-invalid-feedback>
          <b-form-valid-feedback :state="validphone">
            Успешно.
          </b-form-valid-feedback>
        </div>
        <div class="col-lg-4 col-12 p-lg-2 p-1">
          <b-form-input
            
            placeholder="E-mail"
            v-model="email"
            :state="validemail"
            id="feedback-email"
          ></b-form-input>
          <b-form-invalid-feedback :state="validemail">
            email неверно введен
          </b-form-invalid-feedback>
          <b-form-valid-feedback :state="validemail">
            Успешно.
          </b-form-valid-feedback>
        </div>
      </div>
      <div v-if="alert_true"  class="al-true alert alert-info" role="alert">
      Заявка отправлена!
      <br>
      Мы свяжемся с вами в ближайшее время.
    </div>
      <div v-if="alert_err"  class="al-true alert alert-info" role="alert">
      Заполните форму!
    </div>
      <div class="text-center mt-4">
        <button type="submit" @click="onform" class="btn-zapic">Получить подарок</button>
      </div>
      
      <p class="text-center politika ">Указывая свои данные, Вы соглашаетесь с нашей Политикой конфиденциальности</p>
    </b-form>
  </div>
</template>

<script>
export default {
  props:['oncount'],
  data() {
    return {
      Username: "",
      phone: "",
      email:"",
      alert_true:false,
      alert_err:false
    };
  },
  methods:{
    onform(){
      if (this.validemail && this.validphone && this.validation){
        let data = {
          "name_user": this.Username,
          "phone_user": this.phone,
          "email_user": this.email
        }
        let headers = {
            'Content-Type': 'application/json',
        };
         this.$axios.$post('/api/applications/',data,{
                                                        headers: headers
        }
        )
        .then(responce => {
          this.alert_true = true
          this.oncount()
          setTimeout(() => {
          this.email = ''
          this.phone = ''
          this.Username = ''
          this.alert_true = false
          }, 3000);
          
        },
         error => {
           console.log(error);
        }
      )

      
      }
      if(!this.phone && !this.email && !this.Username){
        this.alert_err = true
          setTimeout(() => {
          this.alert_err = false
        }, 2000);
      }
    }
  },
  computed: {
    validation() {
      if (this.Username) {
        return this.Username.length > 2;
      }


    },
    validphone(){
      if (this.phone) {
        let elementphone = /^(1\s|1|)?((\(\d{3}\))|\d{3})(\-|\s)?(\d{3})(\-|\s)?(\d{5})$/.test(this.phone)
        return this.phone.length > 10 && this.phone.length <= 11 && elementphone;
        
      }
    },
    validemail(){
      if (this.email) {
        const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(String(this.email).toLowerCase());
      }
    }
  },
};
</script>

<style scoped>
.form-box {
}
.other-text-form{
  font-weight: bold;
}
#feedback-user,#feedback-phone,#feedback-email
{
  border-radius: 50px;
}
.form {
  border-radius: 40px;
  background: white;
  min-height: 50vh;
  padding: 3rem;
  margin-top: 4rem;
}

@media screen {
  .form {
    border-radius: 20px;
    padding: 1rem;
    padding-top: 2rem;
    padding-bottom: 2rem;
   
  }
}
h2 {
  font-size: 1.4rem;
  font-weight: bold;
  color: #ff7c30;
}
.btn-zapic{
  background: #ff7c30;
  color: white;
  width: auto;
  height: 3rem;
  border-radius: 50px;
  border: none;
  width: 15rem;
}
.politika{
  margin-top: 4rem;
}
.al-true{
  position: absolute;
  right: 30%;
  left: 30%;
}
@media (max-width:500px) {
  .al-true{
  right: 10%;
  left: 10%;
}
}
</style>