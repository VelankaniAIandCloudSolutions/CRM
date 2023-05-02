<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">My account</h1>
            </div>

            <div class="column is-12">
                <div class="buttons">
                    <router-link :to="{ name: 'EditMember', params: { id: $store.state.user.id }}" class="button is-light">Edit</router-link>

                    <button @click="logout()" class="button is-danger">Log out</button>
                </div>
            </div>
        </div>
    </div>
    
</template>

<script>
    import axios from 'axios'

    export default {
        name: 'MyAccount',
        methods: {
            async logout() {
                await axios
                    .post('/api/v1/token/logout/')
                    .then(response => {
                        console.log('Logged out')
                    })
                    .catch(error => {
                        console.log(JSON.stringify(error))
                    })
                
                axios.defaults.headers.common['Authorization'] = ''
                localStorage.removeItem('token')
                localStorage.removeItem('username')
                localStorage.removeItem('userid')
                localStorage.removeItem('team_name')
                localStorage.removeItem('team_id')
                this.$store.commit('removeToken')

                this.$router.push('/')
            }
        }
    }
</script>








async setAsAccepted() {
    this.$store.commit('setIsLoading', true);

const quoteID = this.$route.params.id;


try {
const response = await axios.patch(`/api/v1/quotes/${quoteID}/accept_quotation/`)
.then(response => {
toast({
                  message: 'The Quotation  was Accepted',
                  type: 'is-success',
                  dismissible: true,
                  pauseOnHover: true,
                  duration: 2000,
                  position: 'bottom-right',
              })
console.log('Response:', response.data);




const updatedQuote = response.data.quote;

if (updatedQuote && updatedQuote.is_accepted) {
const index = this.quotes.findIndex(q => q.id === updatedQuote.id);
if (index >= 0) {
this.quotes.splice(index, 1, updatedQuote);


}
}




})

} catch (error) {
console.error(error);
}
this.$store.commit('setIsLoading', false);
}