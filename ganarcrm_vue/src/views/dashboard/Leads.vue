<template>
    <div class="page-leads">
      <nav class="breadcrumb" aria-label="breadcrumbs">
        <ul>
          <li><router-link to="/dashboard">Dashboard</router-link></li>
          <li class="is-active"><router-link to="/dashboard/leads" aria-label="true">Leads</router-link></li>
        </ul>
      </nav>
  
      <div class="columns is-multiline">
        <div class="column is-12">
          <div class="title" style="text-transform: capitalize;">Leads</div>
  
          <!-- <div>
            <form @submit.prevent="getLeads">
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
          <br> -->
  
          <router-link to="/dashboard/leads/add" class="button btn is-primary is-rounded is-outlined" style="color: black; margin-left:40%; height:40%; width:20%;text-transform: capitalize;"> <i class="fas fa-plus"></i>Add lead</router-link>
        </div>

        <div class="filter-container">
        <input type="text" v-model="filterText" placeholder="Filter by Name..." class="filter-input">
      </div>
  
      <ag-grid-vue
        style="width: 100%; height: 500px; text-align: center;"
        class="ag-theme-alpine"
        :columnDefs="columnDefs"
        :rowData="filteredLeads"
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
    name: 'Leads',
    components: {
      'ag-grid-vue': AgGridVue,
      FontAwesomeIcon,
    },
    data() {
      return {
        paginationPageSize: null,
        filterText: '',
        leads: [],
        query: '',
        columnDefs: [
          { headerName: 'Compant', field: 'company',  filter: 'agTextColumnFilter' },
          { headerName: 'Phone', field: 'phone',  filter: 'agTextColumnFilter' },
          { headerName: 'Contact Person', field: 'contact_person',  filter: 'agTextColumnFilter' },
          // { headerName: 'Assigned TO', field: 'assigned_to' },
          
          {
            headerName: '',
            field: 'id',
            cellRenderer: (params) => {
              const route = {
                name: 'Lead',
                params: { lead_id: params.value },
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
        filteredLeads() {
        const filterText = this.filterText.toLowerCase();
        return this.leads.filter((lead) =>
          lead.company.toLowerCase().includes(filterText)
          
        );
      }
    },
    created() {
      this.paginationPageSize = 10;
    },
    mounted() {
      this.getLeads();
    },
    methods: {
      async getLeads() {
        this.$store.commit('setIsLoading', true);
        try {
    const response = await axios.get(`/api/v1/leads/?search=${this.query}`);
    this.leads = response.data.results;
    console.log(this.leads); // Check the response data
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
  
  
  
  


































































<!-- 
<template>
    <div class="page-leads">
      <nav class="breadcrumb" aria-label="breadcrumbs">
        <ul>
          <li><router-link to="/dashboard">Dashboard</router-link></li>
          <li class="is-active"><router-link to="/dashboard/leads" aria-label="true">Leads</router-link></li>
        </ul>
      </nav>
  
      <div class="columns is-multiline">
        <div class="column is-12">
          <div class="title" style="text-transform: capitalize;">Leads</div>
  
          <div>
            <form @submit.prevent="getLeads">
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
  
          <router-link to="/dashboard/leads/add" class="button btn is-primary is-rounded is-outlined" style="color: black; margin-left:40%; height:30%; width:20%;text-transform: capitalize;"> <i class="fas fa-plus"></i>Add lead</router-link>
         
        </div>
  
        <hr>
  
        <div class="column is-3" v-for="lead in leads" v-bind:key="lead.id" value="lead.id">
          <div class="card" style="background-color: whitesmoke">
            <h3 class="is-size-4 mb-4" style="color:black">{{ lead.company }}</h3>
            <h3 class="is-size-4 mb-4" style="color:black">{{ lead.phone }}</h3>
            <hr>
            <div class="buttons">
               

                <router-link :to="{ name: 'Lead', params: { lead_id: lead.id } }" class="button is-info is-rounded is-outlined">Details</router-link>

            </div>
          </div>
        </div>

    </div>

      <div class="buttons">
        <button class="button is-info is-rounded is-outlined" style="width:11%; color:black" @click="goToPreviousPage()" v-if="showPreviousButton">
            <span class="icon">
                <i class="fas fa-chevron-left" style="margin-right:80%;"></i>
            </span>
            Previous
        </button>

        <button class="button is-info is-rounded is-outlined" style="color: black; width:11%;" @click="goToNextPage()" v-if="showNextButton">
            <span class="icon">
                <i class="fas fa-chevron-right" style="margin-right:120%"></i>
            </span>
            Next</button>
      </div>
    </div>
  </template>

<script>
    import axios from 'axios'

    export default {
        name: 'Leads',
        data() {
            return {
                leads: [],
                showNextButton: false,
                showPreviousButton: false,
                currentPage: 1,
                query: '',
                num_leads: 0
            }
        },
        mounted() {
            this.getLeads()
        },
        methods: {
            goToNextPage() {
                this.currentPage += 1
                this.getLeads()
            },
            goToPreviousPage() {
                this.currentPage -= 1
                this.getLeads()
            },
            async getLeads() {
                this.$store.commit('setIsLoading', true)

                this.showNextButton = false
                this.showPreviousButton = false

                await axios
                    .get(`/api/v1/leads/`)
                    .then(response => {
                        console.log(response.data)
                        this.num_leads = response.data.count
                    })

                await axios
                    .get(`/api/v1/leads/?page=${this.currentPage}&search=${this.query}`)
                    .then(response => {
                        this.leads = response.data.results

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























































<!-- <template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Leads</h1>

                <router-link 
                    to="/dashboard/leads/add"
                    v-if="$store.state.team.max_leads > num_leads" class="button btn is-primary" style="color: black;"
                >Add lead</router-link>

                <div 
                    class="notification is-danger"
                    v-else
                >
                    You have reached the top of your limitations. Please upgrade!
                </div>

                <hr>

                <form @submit.prevent="getLeads">
                    <div class="field has-addons">
                        <div class="control">
                            <input type="text" class="input" v-model="query">
                        </div>
                        <div class="control">
                            <button class="button is-success" style="color: black;">Search</button>
                        </div>
                    </div>
                </form>
            </div>

            <div class="column is-12">
                <table class="table is-fullwidth" style=" background: linear-gradient(135deg, #71b7e6, #9b59b6 ); border-style: solid;">
                    <thead>
                        <tr>
                            <th style="color: black;">Company</th>
                            <th style="color: black;">Contact person</th>
                            <th style="color: black;">Assigned to</th>
                            <th style="color: black;">Status</th>
                            <th></th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr style="color: black;"
                            v-for="lead in leads"
                            v-bind:key="lead.id">
                                <td>{{ lead.company }}</td>
                                <td>{{ lead.contact_person }}</td>
                                <td>
                                    <template v-if="lead.assigned_to">{{ lead.assigned_to.first_name }} {{ lead.assigned_to.last_name }}</template>
                                </td>
                                <td>{{ lead.status }}</td>
                                <td>
                                    <router-link :to="{ name: 'Lead', params: { id: lead.id }}" class="button btn is-info" style="color: black;" >Details</router-link>
                                </td>
                        </tr>
                    </tbody>
                </table>

                <div class="buttons">
                    <button class="button is-primary" style="color: black;" @click="goToPreviousPage()" v-if="showPreviousButton">Previous</button>
                    <button class="button is-primary" style="color: black;" @click="goToNextPage()" v-if="showNextButton">Next</button>
                </div>
            </div>
        </div>
    </div>
   
</template> -->




