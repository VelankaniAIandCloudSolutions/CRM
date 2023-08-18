<template>
    <div>
      <h1 class="title">Add a new client</h1>
  
      <form @submit.prevent="submitForm">
        <div class="field">
          <label class="label">Name</label>
          <div class="control">
            <input class="input" type="text" v-model="name" required>
          </div>
        </div>
  
        <div class="field">
          <label class="label">Contact person</label>
          <div class="control">
            <input class="input" type="text" v-model="contact_person">
          </div>
        </div>
  
        <div class="field">
          <label class="label">Email</label>
          <div class="control">
            <input class="input" type="email" v-model="email">
          </div>
        </div>
  
        <div class="field">
          <label class="label">Phone</label>
          <div class="control">
            <input class="input" type="tel" v-model="phone">
          </div>
        </div>
  
        <div class="field">
          <label class="label">Website</label>
          <div class="control">
            <input class="input" type="text" v-model="website">
          </div>
        </div>
  
        <!-- <div class="field">
          <label for="exampleFormControlFile1" class="label">PDF</label>
          <div class="control">
            <input class="form-control" type="file" @change="uploadedFile" ref="file">
          </div>
        </div> -->

  
        <div class="field is-grouped">
          <div class="control">
            <button class="button is-primary" :disabled="isSubmitting">Submit</button>
          </div>
          <div class="control">
            <button class="button is-text" @click="$router.push('/dashboard/clients')">Cancel</button>
          </div>
        </div>
      </form>
    </div>
  </template>

<script>
    
import axios from 'axios'
import { toast } from 'bulma-toast'
import { mapActions } from 'vuex'


export default {
  data() {
    return {
      name: '',
      contact_person: '',
      email: '',
      phone: '',
      website: '',
      pdf:'',
      isLoading: false
    }
  },
  methods: {
    ...mapActions(['setIsLoading']),
    async uploadedFile() {
      this.pdf = this.$refs.file.files[0]
    },
    async submitForm() {
      this.setIsLoading(true)

      const client = new FormData()
      client.append('name', this.name)
      client.append('contact_person', this.contact_person)
      client.append('email', this.email)
      client.append('phone', this.phone)
      client.append('website', this.website)
      // client.append('pdf', this.pdf )

try {
  const response = await axios.post('/api/v1/clients/', client)
  const clientID = response.data.id

  toast({
    message: 'The client was added',
    type: 'is-success',
    dismissible: true,
    pauseOnHover: true,
    duration: 2000,
    position: 'bottom-right',
  })

  this.$router.push(`/dashboard/clients/${clientID}/`)
} catch (error) {
  console.log(error)
}

this.setIsLoading(false)
}

        //         this.formData.append("pdf", this.$refs.file.files[0]);

        //         await axios.post(`/api/v1/files/`, this.formData, {
        //             headers: {
        //                 'Content-Type': 'multipart/form-data'
        //             }
        //         })
        //         .then( response => {
        //             console.log(response)
        //         })
        //         .catch(error => {
        //             console.log(error)
        //         })

        //         
        //     },
        //     async uploadedFile() {
        //       this.filename = this.$refs.file.files[0]
        //       console.log(this.filename)
        //       const clientID = this.$route.params.id
              

        //       await axios
        //         .post(`/api/v1/files/?client_id=${clientID}/`)
        //         .then(response => {
        //           this.files = response.data
        //         })
        //         .catch(error => {
        //           console.log(error)
        //         })
              

            
        //     }
        // }
    }
  }
</script>