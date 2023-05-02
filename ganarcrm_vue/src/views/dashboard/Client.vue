<!-- <template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">{{ client.name }}</h1>

                <div class="buttons">
                    <router-link :to="{ name: 'EditClient', params: { id: client.id }}" class="button is-info" style="color: black;" >Edit</router-link>
                    <button class="button is-danger" @click="deleteClient">Delete</button>
                </div>
            </div>

            <div class="column is-6">
                <div class="box" style=" background: linear-gradient(135deg, #71b7e6, #9b59b6 ); border-style: solid;">
                    <h2 class="title">Contact information</h2>

                    <p><strong>Contact person: </strong>{{ client.contact_person }}</p>
                    <p><strong>Email: </strong>{{ client.email }}</p>
                    <p><strong>Phone: </strong>{{ client.phone }}</p>
                    <p><strong>Website: </strong>{{ client.website }}</p>
                </div>
            </div>

            <div class="column is-6">
                <div class="box" style=" background: linear-gradient(135deg, #71b7e6, #9b59b6 ); border-style: solid;">
                    <h2 class="title">Details</h2>

                    <p><strong>Created at: </strong>{{ client.created_at }}</p>
                    <p><strong>Modified at: </strong>{{ client.modified_at }}</p>
                </div>
            </div>

        

            <hr>

            <div class="column is-12" style=" background: linear-gradient(135deg, #71b7e6, #9b59b6 );">
                <h2 class="subtitle" style="color: black;">Notes</h2>

                <router-link :to="{ name: 'AddNote', params: { id: client.id }}" class="button is-info mb-6" style="color: black;">Add note</router-link>
            
                <div
                    class="box" style=" background: linear-gradient(135deg, #71b7e6, #9b59b6 ); border-style: solid;"
                    v-for="note in notes"
                    v-bind:key="note.id"
                >
                    <h3 class="is-size-4">{{ note.name }}</h3>

                    <p>
                        {{ note.body }}
                    </p>

                    <router-link :to="{ name: 'EditNote', params: { id: client.id, note_id: note.id }}" class="button is-info mt-6" style="color: black;">Edit note</router-link>
                </div>
            </div>
        </div>
    </div>
</template> -->



<template>
  <div class="container">
    <h1 class="title">{{ client.name }}</h1>
    <div class="buttons">
      <router-link :to="{ name: 'EditClient', params: { id: client.id }}" class="button is-info" style="color: black;">Edit</router-link>
      <button class="button is-danger" @click="deleteClient">Delete</button>
    </div>

    <table class="table is-fullwidth is-bordered">
      <tbody>
        <tr>
          <td><strong>Contact person:</strong></td>
          <td>{{ client.contact_person }}</td>
        </tr>
        <tr>
          <td><strong>Email:</strong></td>
          <td>{{ client.email }}</td>
        </tr>
        <tr>
          <td><strong>Phone:</strong></td>
          <td>{{ client.phone }}</td>
        </tr>
        <tr>
          <td><strong>Website:</strong></td>
          <td>{{ client.website }}</td>
        </tr>
        <tr>
          <td><strong>Created at:</strong></td>
          <td>{{ client.created_at }}</td>
        </tr>
        <tr>
          <td><strong>Modified at:</strong></td>
          <td>{{ client.modified_at }}</td>
        </tr>
 
        
      </tbody>
    </table>


    <table class="table table is-fullwidth">
      <tbody>
        <tr class="subtitle" style="color: black; font-size: large;">Uploaded File</tr>
        <br>
        <tr>
          
          <td><a :href="client.pdf" target="_blank">{{ client.pdf }}</a></td>
        </tr>

      </tbody>
    </table>

    <!-- <h2 class="title" style="color: black;">Upload File</h2>
    <table class="table is-fullwidth is-bordered">
      <tbody>
   <tr v-for="client in clients" :key="client.id">
  <td style="border-style: solid; border-color: black;">
    <a :href="client.pdf" target="_blank">{{ client.pdf }}</a>
  </td>
</tr> -->
      <!-- </tbody>
    </table>
    <br>
    <br> -->

    <h2 class="subtitle" style="color: black;">Notes</h2>
    <router-link :to="{ name: 'AddNote', params: { id: client.id }}" class="button is-info mb-6" style="color: black;">Add note</router-link>
    <table class="table is-fullwidth is-bordered">
      <tbody>
        <tr v-for="note in notes" v-bind:key="note.id">
          <td style="border-style: solid; border-color: black;">
            <h3 class="is-size-4">{{ note.name }}</h3>
            <p>{{ note.body }}</p>
          </td>
          <td>
            <router-link :to="{ name: 'EditNote', params: { id: client.id, note_id: note.id }}" class="button is-info mt-6" style="color: black;">Edit note</router-link>
          </td>
        </tr>
      </tbody>
    </table>

   
  </div>
</template>





<script>
  import axios from 'axios'

  export default {
      name: 'Client',
      data() {
          return {
              client: {},
              notes: [],
              // files:[]
          }
      },
      mounted() {
          this.getClient()

      },
      // created() {
      //   this.getFiles()
      // },
      methods: {
          async deleteClient() {
              this.$store.commit('setIsLoading', true)

              const clientID = this.$route.params.id

              await axios
                  .post(`/api/v1/clients/delete_client/${clientID}/`)
                  .then(response => {
                      console.log(response.data)

                      this.$router.push('/dashboard/clients')
                  })
                  .catch(error => {
                      console.log(error)
                  })

              this.$store.commit('setIsLoading', false)
          },
          
          async getClient() {
              this.$store.commit('setIsLoading', true)

              const clientID = this.$route.params.id

              await axios
                  .get(`/api/v1/clients/${clientID}/`)
                  .then(response => {
                      this.client = response.data
                  })
                  .catch(error => {
                      console.log(error)
                  })
          
          

              await axios
                  .get(`/api/v1/notes/?client_id=${clientID}`)
                  .then(response => {
                      this.notes = response.data
                  })
                  .catch(error => {
                      console.log(error)
                  })
              this.$store.commit('setIsLoading', false)
              
          },

          //     await axios
          //         .get(`/api/v1/files/${clientID}`)
          //         .then(response => {
          //           this.files = response.data
          //           console.log(this.files);
          //         })
          //         .catch(error => {
          //           console.log(error)
          //         })

          //     this.$store.commit('setIsLoading', false)
          // },
          // getFiles(){
          //   axios .get()
          //   .then(response => {
          //     console.log(response.data)
          //     this.files = response.data
          //   })
          //   .catch(error => {
          //     console.log(error)
          //   })
          // }
      }
  }
</script>






<!-- 
async getClient() {
  this.$store.commit('setIsLoading', true)

  const clientID = this.$route.params.id

  try {
    // Retrieve the client details from the API
    const response = await axios.get(`/api/v1/clients/${clientID}/`)
    this.client = response.data

    // Retrieve the list of files for the client from the API
    const filesResponse = await axios.get(`/api/v1/clients/${clientID}/files/`)
    this.files = filesResponse.data
    // this.files = response.data
  } catch (error) {
    console.error(error)
  } finally {
    this.$store.commit('setIsLoading', false)
  } -->