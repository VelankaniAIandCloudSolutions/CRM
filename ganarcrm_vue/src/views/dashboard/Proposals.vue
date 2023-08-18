<template>
  <div class="page-proposals">
    <nav class="breadcrumb" aria-label="breadcrumbs">
      <ul>
        <li>
          <router-link to="/dashboard">Dashboard</router-link>
        </li>
        <li class="is-active">
          <router-link to="/dashboard/proposals" aria-label="true">Proposals</router-link>
        </li>
      </ul>
    </nav>

    <div class="proposal-section">
      <h1 style="font-size:250%;">Proposals</h1>

      <div class="create-proposal">
        <router-link to="/dashboard/proposals/add" class="button is-rounded is-primary is-outlined" style="color:black; height:60px; text-transform: capitalize;">
          <i class="fas fa-plus"></i> Create New Proposal
        </router-link>

      </div>
    </div>

    <hr>

    <div class="filter-container">
      <input type="text" v-model="filterText" placeholder="Filter by Name..." class="filter-input">
    </div>


    <div class="table is-fullwidth">
      <div style="width: 600px;">
        <div style="width: 600px;">
          <ag-grid-vue
            style="width: 1380px; height: 500px; text-align:center;"
            class="ag-theme-alpine"
            :columnDefs="columnDefs"
            :rowData="filteredPraposals"
            :defaultColDef="defaultColDef"
            :suppressMoveWhenRowDragging="true"
            :rowDragManaged="true"
            :rowClassRules="rowClassRules"
            :frameworkComponents="frameworkComponents"
            @gridReady="onGridReady"
            :floatingFilter="true"
            :pagination="true"
            :paginationPageSize="paginationPageSize"
           
           
          ></ag-grid-vue>
        </div>
      </div>
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
  name: 'Proposals',
  components: {
    'ag-grid-vue': AgGridVue,
    FontAwesomeIcon,
    
  },
  data() {
  return {
    paginationPageSize: null,
    filterText: '',
    praposals: [],
    columnDefs: [
     
    {
          headerName: 'Name',
          field: 'name',
          filter: 'agTextColumnFilter',
          
        },

      { headerName: 'Phone', field: 'phone',  filter: 'agTextColumnFilter' },
      { headerName: 'Email', field: 'email' ,  filter: 'agTextColumnFilter' },
      { headerName: 'From Date', field: 'from_date' ,   filter: 'agDateColumnFilter' },
      { headerName: 'To Date', field: 'to_date' ,   filter: 'agDateColumnFilter' },
      {
        headerName: '',
        field: 'id',
        cellRenderer: (params) => {
          const route = {
            name: 'Proposal',
            params: { id: params.value },
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
      },
      {
          field: '',
          cellRenderer: (params) => {
            const deleteItem = () => {
              this.deleteItem(params.data);
            };

            const deleteIcon = document.createElement('div');
            deleteIcon.className = 'delete-icon';
            deleteIcon.innerHTML = '<a class="fas fa-trash"></a>';
            deleteIcon.addEventListener('click', deleteItem);

            return deleteIcon;
          },
        },
    ],
    defaultColDef: {
      sortable: true,
      resizable: true,
      minWidth: 250,
      // filter:true,
      
      // floatingFilter: true,
    },
  };
},
computed: {
    filteredPraposals() {
      const filterText = this.filterText.toLowerCase();
      return this.praposals.filter((praposal) =>
        praposal.name.toLowerCase().includes(filterText)
        
      );
    }
  },

  created() {
    this.getPraposals();
    this.paginationPageSize = 10;
  },
  methods: {

    

    async getPraposals() {
      this.$store.commit('setIsLoading', true);
      try {
        const response = await axios.get('/api/v1/get_proposals');
        this.praposals = response.data;
      } catch (error) {
        console.log(error);
      }
      this.$store.commit('setIsLoading', false);
    },

    async deleteItem(data) {
      try {
        await axios.delete(`/api/v1/delete_praposal/${data.id}`);
        const index = this.praposals.findIndex((item) => item.id === data.id);
        if (index !== -1) {
          this.praposals.splice(index, 1);
        }
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>



























<style scoped>
.page-proposals {
  /* max-width: 1000px; */
  margin: 0 auto;
  /* padding: 20px; */
}

.breadcrumb {
  margin-bottom: 20px;
}

.breadcrumb-link {
  color: #333;
  text-decoration: none;
}



.create-proposal {
  margin-bottom: 20px;
  text-align: center;

}


.filter-container {
  margin-bottom: 20px;
  border-radius: 5px;
  background-color: #f9f9f9;
  padding: 15px;
}

.filter-input {
  padding: 10px;
  width: 400px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.filter-input:focus {
  border-color: #007bff;
  outline: none;
}












</style>



















<!-- <div class="proposal-search">
          <form @submit.prevent="getPraposals">
            <div class="field has-addons">
              <div class="control">
                <input type="text" class="input" v-model="query" placeholder="Search">
              </div>
              <div class="control">
                <button class="button is-primary">Search</button>
              </div>
            </div>
          </form>
        </div> -->
  