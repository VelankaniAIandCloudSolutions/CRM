<template>
    <div class="container">
      <h1 class="title">Add Lead</h1>
      <form @submit.prevent="submitForm" class="lead-form">
        <div class="form-field">
          <label for="company">Company</label>
          <input type="text" id="company" class="input" v-model="company" required>
        </div>
        <div class="form-field">
          <label for="contact_person">Contact Person</label>
          <input type="text" id="contact_person" class="input" v-model="contact_person" required>
        </div>
        <div class="form-field">
          <label for="email">Email</label>
          <input type="email" id="email" class="input" v-model="email" required>
        </div>
        <div class="form-field">
          <label for="phone">Phone</label>
          <input type="text" id="phone" class="input" v-model="phone" required>
        </div>
        <div class="form-field">
          <label for="address">Company Address</label>
          <input type="text" id="address" class="input" v-model="address" required>
        </div>
        <div class="form-field">
          <label for="designation">Designation</label>
          <input type="text" id="designation" class="input" v-model="designation" required>
        </div>
        <div class="form-field">
          <label for="website">Website</label>
          <input type="text" id="website" class="input" v-model="website" required>
        </div>
        <div class="form-field">
          <label for="status">Status</label>
          <select id="status" class="select" v-model="status" required>
            <option value="new">New</option>
            <option value="contacted">Contacted</option>
            <option value="inprogress">In Progress</option>
            <option value="lost">Lost</option>
            <option value="won">Won</option>
          </select>
        </div>
        <div class="form-field">
          <button type="submit" class="button is-success">Submit</button>
        </div>
      </form>
    </div>
  </template>

<script>
    import axios from 'axios'

    import { toast } from 'bulma-toast'

    export default {
        name: 'AddLead',
        data() {
            return {
                company: '',
                address: '',
                designation:'',
                contact_person: '',
                email: '',
                phone: '',
               
                website: '',
                status: 'new',
               
            }
        },
        methods: {
            async submitForm() {
                this.$store.commit('setIsLoading', true)

                const lead = {
                    company: this.company,
                    address: this.address,
                    designation: this.designation,
                    contact_person: this.contact_person,
                    email: this.email,
                    phone: this.phone,
                    website: this.website,
                   
                    status: this.status,
                    
                }

                await axios
                    .post('/api/v1/leads/', lead)
                    .then(response => {
                        toast({
                            message: 'The lead was added',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })

                        this.$router.push('/dashboard/leads')
                    })
                    .catch(error => {
                        console.log(error)
                    })

                this.$store.commit('setIsLoading', false)
            }
        }
    }
</script>



<style>
.container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}

.title {
  font-size: 24px;
  margin-bottom: 20px;
}

.lead-form {
  display: flex;
  flex-direction: column;
}

.form-field {
  margin-bottom: 20px;
}

label {
  display: block;
  font-weight: bold;
  margin-bottom: 5px;
}

.input,
.select {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.select {
  appearance: none;
}

.button {
  padding: 10px 20px;
  font-size: 16px;
  background-color: #28a745;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.button:hover {
  background-color: #218838;
}

.button.is-success {
  background-color: #28a745;
}

.button.is-success:hover {
  background-color: #218838;
}



</style>



