<template>
  <div class="page-clients">
    <nav class="breadcrumb" aria-label="breadcrumbs">
      <ul>
        <li><router-link to="/dashboard">Dashboard</router-link></li>
        <li class="is-active"><router-link to="/dashboard/clients" aria-label="true">Clients</router-link></li>
      </ul>
    </nav>

    <div class="columns is-multiline">
      <div class="column is-12">
        <div class="title" style="text-transform: capitalize;">Clients</div>

        <!-- <div>
          <form @submit.prevent="getClients">
            <div class="field has-addons">
              <div class="control">
                <input type="text" class="input" v-model="query">
              </div>
              <div class="control">
                <button class="button is-success">Search</button>
              </div>
            </div>
          </form>
        </div> -->
        <br>

        <router-link to="/dashboard/clients/add" class="button btn is-primary is-rounded is-outlined" style="color: black; margin-left: 40%; height: 30%; width: 20%; text-transform: capitalize;">
          <i class="fas fa-plus"></i> Add client
        </router-link>
      </div>

      <hr>
      <br>
      <br>
      <br>
      <div class="filter-container">
        <input type="text" v-model="filterText" placeholder="Filter by Name..." class="filter-input">
      </div>

      <ag-grid-vue
        style="width: 100%; height: 500px; text-align: center;"
        class="ag-theme-alpine"
        :columnDefs="columnDefs"
        :rowData="filteredClients"
        :defaultColDef="defaultColDef"
        @firstDataRendered="onFirstDataRendered"
        :floatingFilter="true"
        :pagination="true"
        :paginationPageSize="paginationPageSize"
      ></ag-grid-vue>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { reactive, onMounted, ref } from 'vue';
import { AgGridVue } from 'ag-grid-vue3';
import 'ag-grid-community/styles/ag-grid.css';
import 'ag-grid-community/styles/ag-theme-alpine.css';
import '@fortawesome/fontawesome-free/css/all.css';
import { mapActions } from 'vuex';
import { library } from '@fortawesome/fontawesome-svg-core';
import { faL, faTrash } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

export default {
  name: 'Clients',
  components: {
    'ag-grid-vue': AgGridVue,
    FontAwesomeIcon,
  },
  data() {
    return {
      paginationPageSize: null,
      filterText: '',
      clients: [],
      query: '',
      columnDefs: [
        { headerName: 'Name', field: 'name',  filter: 'agTextColumnFilter' },
        { headerName: 'Phone', field: 'phone',  filter: 'agTextColumnFilter' },
        { headerName: 'Email', field: 'email',  filter: 'agTextColumnFilter' },
        // { headerName: 'Assigned TO', field: 'assigned_to' },
        
        {
          headerName: '',
          field: 'id',
          cellRenderer: (params) => {
            const route = {
              name: 'Client',
              params: { client_id: params.value },
            };

            const icon = document.createElement('i');
            icon.className = 'fas fa-external-link-alt';
            icon.style.cursor = 'pointer';
            icon.addEventListener('click', (e) => {
              e.stopPropagation(); // Prevent selection in ag-Grid
              this.$router.push(route);
            });

            return icon;
          },
        }

      ],
      defaultColDef: {
        sortable: true,
        resizable: true
      }
     
    };
  },
  computed: {
    filteredClients() {
      const filterText = this.filterText.toLowerCase();
      return this.clients.filter((client) =>
        client.name.toLowerCase().includes(filterText)
        
      );
    }
  },
  created() {
    this.paginationPageSize = 10;
  },
  mounted() {
    this.getClients();
  },
  methods: {
    async getClients() {
      this.$store.commit('setIsLoading', true);
      try {
        const response = await axios.get(`/api/v1/clients/?search=${this.query}`);
        this.clients = response.data.results;
      } catch (error) {
        console.log(error);
      }
      this.$store.commit('setIsLoading', false);
    },
    onFirstDataRendered(params) {
      params.api.sizeColumnsToFit();
    }
  }
};
</script>


<style>
.filter-container {
  margin-bottom: 20px;
  border-radius: 5px;
  background-color: #f9f9f9;
  padding: 15px;
  width:500px;
}

.filter-input {
  padding: 10px;
  width: 800px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.filter-input:focus {
  border-color: #007bff;
  outline: none;
}

</style>










































































<!-- 
<template>
  <div class="page-clients" >
    <nav class="breadcrumb" aria-label="breadcrumbs">
      <ul>
        <li><router-link to="/dashboard">Dashboard</router-link></li>
        <li class="is-active"><router-link to="/dashboard/clients" aria-label="true">Clients</router-link></li>
      </ul>
    </nav>

    <div class="columns is-multiline">
      <div class="column is-12">
        <div class="title" style="text-transform: capitalize;">Clients</div>

          <div>
  
              <form @submit.prevent="getClients">
                  <div class="field has-addons">
                  <div class="control">
                      <input type="text" class="input" v-model="query">
                  </div>
                  <div class="control">
                      <button class="button is-success">Search</button>
                  </div>
                  </div>
              </form>

          </div>
          <br>

          <router-link to="/dashboard/clients/add"  class="button btn is-primary is-rounded is-outlined" style="color: black; margin-left:40%; height:30%; width:20%;text-transform: capitalize;" > <i class="fas fa-plus"></i> Add client</router-link>
             

                  
                 
      </div>

      <hr>
      <br>      
  
      

      <div class="column is-3" v-for="client in clients" v-bind:key="client.id">
        <div class="card" style="background-color:whitesmoke;">
          <h3 class="is-size-4 mb-4" style="color:black;">{{ client.name }}</h3>

          <router-link :to="{ name: 'Client', params: { client_id: client.id } }" class="button is-info is-rounded is-outlined" >Details</router-link>
        </div>
      </div>
    </div>
  </div>
</template>



<script>
  import axios from 'axios'

  export default {
      name: 'Clents',
      data() {
          return {
              clients: [],
              showNextButton: false,
              showPreviousButton: false,
              currentPage: 1,
              query: '',
              num_clients: 0
          }
      },
      mounted() {
          this.getClients()
      },
      methods: {
          goToNextPage() {
              this.currentPage += 1
              this.getClients()
          },
          goToPreviousPage() {
              this.currentPage -= 1
              this.getClients()
          },
          async getClients() {
              this.$store.commit('setIsLoading', true)

              this.showNextButton = false
              this.showPreviousButton = false

              await axios
                  .get(`/api/v1/clients/`)
                  .then(response => {
                      this.num_clients = response.data.count
                  })

              await axios
                  .get(`/api/v1/clients/?page=${this.currentPage}&search=${this.query}`)
                  .then(response => {
                      this.clients = response.data.results

                      if (response.data.next) {
                          this.showNextButton = true
                      }

                      if (response.data.previous) {
                          this.showPreviousButton = true
                      }
                  })
                  .catch(error => {
                      console.log(error)
                  })

              this.$store.commit('setIsLoading', false)
          }
      }
  }
</script> -->











<style >

 .breadcrumb ul li a {
color: #333;
text-decoration: none;
}

.breadcrumb ul li.is-active a {
color: #3273dc;
}

/* Page title */
.page-clients .title {
font-size: 2rem;
font-weight: bold;
margin-bottom: 1rem;
}

/* Add client button */
.page-clients .btn.is-primary {
background-color: #3273dc;
border-color: #3273dc;
}

.page-clients .btn.is-primary:hover {
background-color: #276cdb;
border-color: #276cdb;
}

/* Search bar */
.page-clients .field.has-addons .control input {
border-radius: 4px 0 0 4px;
border: 1px solid #ccc;
padding: 0.5rem;
}

.page-clients .field.has-addons .control button {
border-radius: 0 4px 4px 0;
background-color: #3273dc;
border-color: #3273dc;
color: #fff;
padding: 0.5rem;
}

.page-clients .field.has-addons .control button:hover {
background-color: #276cdb;
border-color: #276cdb;
}

/* Client boxes */

:root {
--primary-color: #ff5f5f;
--secondary-color: #ffc371;
}

body {
background-color: #f2f2f2;
font-family: 'Montserrat', sans-serif;
display: grid;
grid-template-columns: repeat(3, 1fr);
grid-template-rows: 1fr;
gap: 1rem;
}

.card {
background-color:  #ffc371;
color: #fff;
border-radius: 10px;
padding: 2rem;
box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
transition: all 0.2s ease-in-out;
display: flex;
flex-direction: column;
justify-content: center;
align-items: center;
text-align: center;
}


@keyframes pulse {
0% {
  transform: scale(1);
}
50% {
  transform: scale(1.05);
}
100% {
  transform: scale(1);
}
}

.card:hover {
animation: pulse 1s infinite;
}
/* body {
background-image: linear-gradient(to bottom right, #ff5f5f, #ffc371);
} */



.card:hover {
transform: translateY(-5px);
box-shadow: 0 5px 20px rgba(0, 0, 0, 0.3);
}

.card h2 {
font-size: 2rem;
margin-top: 0;
margin-bottom: 1rem;
}

.card p {
font-size: 1.2rem;
margin-top: 0;
margin-bottom: 1rem;
}
/* 
.card button {
background-color: var(--primary-color);
color: #fff;
border: none;
padding: 1rem 2rem;
border-radius: 30px;
font-size: 1.2rem;
text-transform: uppercase;
font-weight: bold;
letter-spacing: 1px;
transition: all 0.2s ease-in-out;
cursor: pointer;
}

.card button:hover {
background-color: #ff3b3b;
transform: scale(5.05);
} */

.card button {
cursor: pointer;
}

.card button:hover {
cursor: url('/dashboard/clients/:id'), pointer;
}

@media (max-width: 768px) {
body {
  grid-template-columns: 1fr;
}
}


</style>


 <!-- v-if="$store.state.team.max_clients > num_clients" 
        <div class="notification is-danger" v-else>
          You have reached the top of your limitations. Please upgrade!
        </div> -->



