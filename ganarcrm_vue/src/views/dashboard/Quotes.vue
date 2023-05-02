<template>
  <div class="page-quotes"  >
    
    <nav class="breadcrumb" aria-label="breadcrumbs">
      <ul>
        <li><router-link to="/dashboard">Dashboard</router-link></li>
        <li class="is-active"><router-link to="/dashboard/quotes" aria-label="true">Quotes</router-link></li>
      </ul>
    </nav>

    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Quotes</h1>

        <router-link to="/dashboard/quotes/add" class="button btn is-primary">Add Quote</router-link>
      </div>

      <div class="column is-12">
        <div class="table-wrapper">
          <table class="table is-fullwidth">
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
                <th></th>
              </tr>
            </thead>

            <tbody>
              <tr v-for="quote in quotes" :key="quote.id">
                <td>{{ quote.id }}</td>
                <td>{{ quote.subject }}</td>
                <td>{{ quote.client_name ? quote.client_name.name : '' }}</td>
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
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>








<script>

import axios from 'axios'

export default {
  name:'Quotes',
  data() {
      return {
          quotes:[],
         
      }
  },
  mounted() {
      this.getQuotes()
      
  },
  methods: {
      async getQuotes() {
          this.$store.commit('setIsLoading',true)

                     
          await axios
              .get(`/api/v1/get_quotes`)
              .then(response => {
                  this.quotes = response.data
              })
              .catch(error => {
                  console.log(Error)
              })

          this.$store.commit('setIsLoading', false)
      },

      async deleteQuote(quote_id) {

        this.$store.commit('setIsLoadng', true)
          
          await axios
              .delete(`/api/v1/delete_quote/${quote_id}/`)
              .then(response => {
                  console.log(response.data)

                  this.$router.push('/dashboard/quotes')
              })
              .catch(error => {
                  console.log(error)
              })
        this.$store.commit('setIsLoading',false)
         
      },
  }
}

</script>


<!-- // async updateQuote() {
  //                 this.$store.commit('setIsLoading',true)
  
  //                 const quoteID = this.$route.params.id
  
  //                 axios
  //                     .patch(`/api/v1/${quoteID}/`,this.quote)
  //                     .then(response => {
  //                         this.$router.push(`/dashboard/quotes/${quoteID}`)
  //                     })
  //                     .catch(error => {
  //                         console.log(error)
  //                     })
  //                 this.$store.commit('setIsLoading',false)
} -->
           



<!-- style="background: linear-gradient(135deg, #71b7e6, #9b59b6); border-style:solid;" -->































<style>
.page-quotes {
padding: 3rem;
}

.title {
font-size: 2rem;
margin-bottom: 2.5rem;
}

.buttons {
display: flex;
flex-wrap: wrap;
justify-content: space-between;
}

.button {
display: inline-flex;
align-items: center;
justify-content: center;
padding: 0.5rem 1rem;
border-radius: 5rem;
border: none;
cursor: pointer;
font-size: 1rem;
font-weight: 600;
text-align: center;
text-decoration: none;
transition: all 0.3s ease-in-out;
}

/* Dark Button */
.button.is-dark {
background-color: #4a4a4a;
color: #fff;
}

/* Success Button */
.button.is-success {
background-color: #48c774;
color: #fff;
}
.buttons button {
border-radius: 100px;
padding: 0.5rem 1rem;
margin-right: 1rem;
}


.buttons button:last-child {
margin-right: 0;
}

/* Danger Button */
.button.is-danger {
background-color: #f14668;
color: #fff;
}

/* Info Button */
.button.is-info {
background-color: #209cee;
color: #fff;
}

/* Hover State */
.button:hover {
opacity: 0.8;
}
/* 
.table-wrapper {
overflow-x: auto;
}

.table {
border-collapse: collapse;
}

.table {
background-color: #fff;
border-collapse: collapse;
border-radius: 5px;
box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

.scrollmenu {
overflow-x: auto;
}

table {
width: 100%;
text-align: left;
} */

thead {
background-color: #f5f5f5;
}

th {
padding: 1rem;
font-weight: bold;
}

td {
padding: 0.5rem 1rem;
}

tr:nth-child(even) {
background-color: #f5f5f5;
}



</style>