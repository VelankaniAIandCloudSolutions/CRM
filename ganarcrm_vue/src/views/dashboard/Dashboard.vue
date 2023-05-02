<template>
    
  <br>
  <div class="container">
    <div class="row">
      <div class="col">
        <div class="box text-center text-white mb-3" id="total-leads" >
          <div class="box-header">
            <div class="title" style="color: whitesmoke;">Total New Leads</div>
            <hr style="background-color: black;">
          </div>
          <br>
          <div class="card-body">
            <h3 class="title"  style="font-size: xxx-large;  color: #0B486B;">{{ leads.length }}</h3>
          </div>
        </div>
      </div>

      <div class="col">
          
<div class="box text-center text-white mb-3" id="total-clients" >
  <div class="box-header">
    <div class="title"  style="color: whitesmoke;">Total Clients</div>
    <hr style="background-color: black;">
  </div>
  <br>
  <div class="card-body">
    <h3 class="title"  style="font-size: xxx-large;  color: #0B486B;">{{ clients.length }}</h3>
  </div>
</div>
</div>

      <div class="col">
        <div class="box text-center text-white mb-3" id="total-quotations" >
          <div class="box-header">
            <div class="title"  style="color: whitesmoke;">Total Quotations</div>
            <hr style="background-color: black;">
          </div>
          <br>
          <div class="card-body">
            <h3 class="title"  style="font-size: xxx-large;  color: #0B486B;">{{ quotes }}</h3>
          </div>
        </div>
      </div>

      <div class="col">
        <div class="box text-center text-white mb-3" id="total-accepted-quotations" >
          <div class="box-header">
            <div class="title"  style="color: whitesmoke; text: size 10%;">Accepted Quotations</div>
            <hr style="background-color: black;">
          </div>
          <br>
          <div class="card-body">
            <h3 class="title" style="font-size: xxx-large;  color: #0B486B;">{{ acceptedQuotes.length }}</h3>
          </div>
        </div>
      </div>

      <div class="col">
        <div class="box text-center text-white mb-3" id="total-rejected-quotations" >
          <div class="box-header">
            <div class="title"  style="color: whitesmoke;">Rejected Quotations</div>
            <hr style="background-color: black;">
          </div>
          <br>
          <div class="card-body">
            <h3 class="title" style="font-size: xxx-large;  color: #0B486B;">{{ rejectedQuotes.length }}</h3>
          </div>
        </div>
      </div>
    </div>
  </div>

  

  <div class="box-container">
      
  <div class="box ">
      <div class="title" style=" color: #0B486B;"> New Leads </div>
          <div class="columns is-multiline">
          
              <div class="column is-6" v-for="lead in leads" :key="lead.id">
                  <div class="card" style="background-color: #ffc371; margin-bottom: -4.5rem; height: 105%;">
                      <h3 class="is-size-4 mb-6" >{{ lead.company }}</h3>
                      <div class="buttons">
                          <router-link :to="{ name: 'Lead', params: { id: lead.id } }" class="button is-light" style="top: -50%;">Details</router-link>
                      </div>
                  </div>
              </div>
          </div>
      </div>
    
  
      <div class="column is-20" >
          <div class="box box-body">
              <div class="title">Accepted Quotations</div>
              <div class="columns is-multiline">
        
                  <table class="table">
                      <thead>
                          <tr>
                          <th>Quotation ID</th>
                          <th>Subject</th>
                          <th>Client Name</th>
                          <th>Owner</th>
                          <th>Request Number</th>
                          <th>Status</th>
                          <th>Date</th>
                          <th>Expiry Date</th>
                          <th></th>
                          <th></th>
                          </tr>
                      </thead>
          
                      <tbody>
                          <tr v-for="quote in acceptedQuotes" :key="quote.id">
                          <td>{{ quote.id }}</td>
                          <td>{{ quote.subject }}</td>
                          <td v-if="quote.client_name">{{ quote.client_name.name }}</td>
                          <td v-else>N/A</td>
                          <td>{{ quote.quotation_owner }}</td>
                          <td>{{ quote.quotation_request_number }}</td>
                          <td>{{ quote.quotation_status }}</td>
                          <td>{{ quote.quotation_date }}</td>
                          <td>{{ quote.expiry_date }}</td>
                          <td>
                              <router-link :to="{ name: 'Quote', params: { id: quote.id } }" class="button btn is-info">Details</router-link>
                          </td>
                          <td>
                              <button @click="deleteQuote(quote.id)" class="button is-danger">Delete</button>
                          </td>
                          <td>
                          </td>
                          </tr>
                      </tbody>
                  </table>
              </div>
          </div>
      </div>
  </div>
</template>


<script>
import axios from 'axios';

export default {
  name: 'Dashboard',
  data() {
          return {
              leads: [],
              quotes:[],
              clients:[],
              
             
              
          }
  },
  mounted() {
          this.getLeads()
          this.acceptedQuotes()
          this.rejectedQuotes()
          this.getQuotes()
          this.getClients()
      },
  
  methods : {
    async getLeads() {
this.$store.commit('setIsLoading', true)

try {
  const response = await axios.get('/api/v1/leads_new/')
  console.log(response.data)
  this.num_leads = response.data.length
  this.leads = response.data
} catch (error) {
  console.error(error)
  // handle error
}

this.$store.commit('setIsLoading', false)
},
   
      async acceptedQuotes() {
        this.$store.commit('setIsLoading', true)
          
          try {
              
              const response = await axios.get('/api/v1/accepted_quotes');
              this.acceptedQuotes = response.data
             
          } catch (error) {
              console.log(error);
          }
        this.$store.commit('setIsLoading', false)
          
      },
      async rejectedQuotes() {

        try{
          const response  = await axios .get('/api/v1/rejected_quotes');
          this.rejectedQuotes = response.data
        } catch(error) {
          console.log(error)
        }
      },
      async getQuotes() {
          try {
              

              const response = await axios.get('/api/v1/get_quotes');
              this.quotes = response.data.length;

              
          } catch (error) {
              console.log(error.message || 'Failed to fetch quotes');
              
          }
      },
      async getClients() {
          this.$store.commit('setIsLoading', true)

          await axios
              .get(`/api/v1/clients/`)
              .then(response => {
                  console.log(response.data)
                  this.num_clients = response.data.count
                  this.clients = response.data.results
              })
          this.$store.commit('setIsLoading', false)
          },

      
      }
}
</script>


<style scoped>

 .box-container {
  display: grid;
  grid-template-columns: repeat(2, 5fr);
  grid-gap: 2rem;
  margin-top: 2rem;
}
.col {
width: 33.33%;
display: inline-block;
vertical-align: top;
height: fit-content;
}
.col {
width: 20%;
display: inline-block;
vertical-align: top;
padding: 0 10px;
margin-bottom: 20px;
}

.box {
height: 200px;
}

.box {
width: 100%;
}

@media (min-width: 768px) {
.col {
  flex: 1;
}
} 



/* Style for the container */
/* Style for the boxes */
.box {
border-radius: 5px;
box-shadow: 0 0 10px rgba(0,0,0,0.3);
padding: 25px;
}



.box:hover {
transform: scale(1.1);
}

.box-header {
display:flex;
justify-content:center;
align-items:first baseline;
width: 100%;
height: 50px;
background: linear-gradient(45deg, #0B486B, #0022FF);
color: #fff;
border-radius: 20px 20px 0px 0px;
}

.box-header .title {
font-size: 20px;
font-weight: 600;
}

/* .box-body {
display: flex;
justify-content: center;
align-items: center;
height: 100%;
padding: 20px;
} */

.box-body .title {
font-size: 48px;
font-weight: 600;
color: #0B486B;
}



.card-body {
background-color: #F5F5F5;
padding: 20px;
border-radius: 5px;
text-align: center;
}

.card-body h3.title {
font-size: 36px;
font-weight: 600;
color: #0B486B;
margin: 0;
padding: 0;
}












</style>








