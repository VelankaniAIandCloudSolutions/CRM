
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
        <div class="title">Clients</div>

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

          <router-link to="/dashboard/clients/add"  class="button btn is-primary" style="color: black;" >Add client</router-link>
             

                  
                  <!-- v-if="$store.state.team.max_clients > num_clients" 
        <div class="notification is-danger" v-else>
          You have reached the top of your limitations. Please upgrade!
        </div> -->
      </div>

      <hr>
      
  
      

      <div class="column is-3" v-for="client in clients" v-bind:key="client.id">
        <div class="card" style="background-color:  #ffc371;">
          <h3 class="is-size-4 mb-4">{{ client.name }}</h3>

          <router-link :to="{ name: 'Client', params: { id:client.id } }" class="button is-light">Details</router-link>
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
</script>


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




