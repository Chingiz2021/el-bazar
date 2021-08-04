<template>
  <div class="container mt-5">
    <div style="width: 100%; overflow-x: scroll">
      <b-form-group label="Фильтр" v-slot="{ ariaDescribedby }">
        <b-form-radio
          v-model="selected"
          :aria-describedby="ariaDescribedby"
          name="some-radios"
          value="Все"
          >Все</b-form-radio
        >
        <b-form-radio
          v-model="selected"
          :aria-describedby="ariaDescribedby"
          name="some-radios"
          value="Обработанные"
          >Обработанные</b-form-radio
        >
        <b-form-radio
          v-model="selected"
          :aria-describedby="ariaDescribedby"
          name="some-radios"
          value="Не обработанные"
          >Не обработанные</b-form-radio
        >
      </b-form-group>
    </div>
    <table class="table table-hover">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Имя</th>
          <th scope="col">Email</th>
          <th scope="col">Телефон</th>
          <th scope="col">Дата заявки</th>
          <th scope="col">Обработана ли</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(zapic, index) of onlistappll" :key="index" scope="row">
          <td>{{ index + 1 }}</td>
          <td>{{ zapic.name_user }}</td>
          <td>{{ zapic.email_user }}</td>
          <td>{{ zapic.phone_user }}</td>
          <td>{{ zapic.create_at.slice(0, 10) }}</td>
          <td>
            <b-form-checkbox
              @change="check(zapic.id, zapic.cheked_apll)"
              v-model="zapic.cheked_apll"
              name="check-button"
              switch
            >
            </b-form-checkbox>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  layout: "admin",
  middleware: "authenticated",
  asyncData({ $axios, store, error }) {
    const headers = {
      "Content-Type": "application/json",
      Authorization: `${store.state.auth.access_token}`,
    };
    return $axios
      .$get(`/api/applications/`, {
        headers: headers,
      })
      .then((listdata) => {
        return { listdata };
      });
  },
  computed: {
    onlistappll() {
      if (this.selected === "Все") {
        return this.listdata;
      }
      if (this.selected === "Обработанные") {
        return this.listdata.filter((elem) => {
          return elem.cheked_apll === true
        });
      }
      if (this.selected === "Не обработанные") {
        return this.listdata.filter((elem) => {
          return elem.cheked_apll === false
        });
      }
    },
  },
  methods: {
    check(appl_id, cheked_apll) {
      const headers = {
        "Content-Type": "application/json",
      };
      let data = {
        cheked_apll: cheked_apll,
      };
      let response = this.$axios
        .$put(`/api/applications/${appl_id}`, data, {
          headers,
        })
        .then(
          (resp) => {
            console.log("ok");
          },
          (error) => {
            console.log(error);
          }
        );
    },
  },
  data() {
    return {
      checked: [],
      selected: "Все",
    };
  },
};
</script>