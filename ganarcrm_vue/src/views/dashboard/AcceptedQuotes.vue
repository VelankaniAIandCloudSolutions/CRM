<template>
  <div class="column is-12 " v-if="acceptedQuotes.length">
    <div class="box">
      <h2 class="title">Accepted Quotations</h2>

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
</template>

<script>
import axios from "axios";

export default {
  name: "AcceptedQuotes",
  data() {
    return {
      acceptedQuotes: [],
    }
  },
  async created() {
    try {
      const response = await axios.get('/api/v1/accepted_quotes');
      this.acceptedQuotes = response.data;
    } catch (error) {
      console.log(error);
    }
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
</script>
