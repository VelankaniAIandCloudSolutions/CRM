<template>
    <div class="praposal-form">
      <h2>Add New Item</h2>
      <form @submit.prevent="submitForm">
        <div class="form-group">
          <label for="name">Select the Package:</label>
          <select v-model="default_package_name">
            <option v-for="default_package in defaults_package" :key="default_package.id" :value="default_package.id">
              {{ default_package.default_package_name }}
            </option>
          </select>
        </div>
        <div class="form-group">
          <label for="company">Menu Item Name :</label>
          <input type="text" v-model="item_name" required>
        </div>
        <div class="form-group">
          <label for="phone">Quantity :</label>
          <input type="number" v-model="item_quantity" required>
        </div>
  
        <div class="buttons">
          <button type="submit" class="btn-submit">Submit</button>

          <button type="submit" class="button btn is-link is-outlined"> Cancel </button>
        </div>
      </form>
    </div>
  </template>




<script>
  import axios from 'axios';
  import { reactive, onMounted } from 'vue';

  export default {
    name: 'AddItem',

    data() {
        return {
            defaults_package: [],
            item_name:'',
            item_quantity:'',
        }
    },

    mounted() {
        this.getDefaults_Package()
    },
    methods: {
        async getDefaults_Package() {
        this.$store.commit('setIsLoading', true);
        try {
          const response = await axios.get('/api/v1/get_default_packages');
          this.defaults_package = response.data;
        } catch (error) {
          console.log(error);
        }
        this.$store.commit('setIsLoading', false);
      },

  }
  }

</script>




<style>
.praposal-form {
  width: 400px;
  margin: auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: #f9f9f9;
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  font-weight: bold;
}

select,
input[type="text"],
input[type="number"] {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.btn-submit {
  padding: 10px 20px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.btn-submit:hover {
  background-color: #45a049;
}
</style>
  








