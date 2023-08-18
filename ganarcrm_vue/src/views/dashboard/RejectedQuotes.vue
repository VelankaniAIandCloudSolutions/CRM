<template>
    <div class="column is-12" v-if="rejectedQuotes.length">
        <div class="box">
            <h2 class="title">Rejected Quotations</h2>

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
                    <tr v-for="quote in rejectedQuotes" :key="quote.id">
                        <td>{{ quote.id }}</td>
                        <td>{{ quote.subject }}</td>
                        <td>{{ quote.client_name.name }}</td>
                        <td>{{ quote.quotation_owner }}</td>
                        <td>{{ quote.quotation_request_number }}</td>
                        <td>{{ quote.quotation_status }}</td>
                        <td>{{ quote.quotation_date }}</td>
                        <td>{{ quote.expiry_date }}</td>
                        <td>
                        <router-link :to="{ name: 'Quote', params: { id: quote.id } }" class="button btn is-info is-rounded is-outlined"><i class="fas fa-info-circle"></i> Details</router-link>
                        </td>
                        <td>
                        <button @click="deleteQuote(quote.id)" class="button is-danger is-rounded is-outlined"><i class="fas fa-trash"> </i> Delete</button>
                        </td>
                        
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    name: 'RejectedQuotes',
    data() {
        return {
            rejectedQuotes: [],
        }
    },

    async created() {
        try {
            const response = await axios.get('/api/v1/rejected_quotes')
            this.rejectedQuotes = response.data
        } catch(error) {
            console.log(error)
        }
    },

}
</script>