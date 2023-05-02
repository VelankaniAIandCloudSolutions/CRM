from django.contrib import admin

from .models import Client

admin.site.register(Client)




#  <!-- <script>
# //     import axios from 'axios'

# //     import { ref, toRaw, reactive } from 'vue'

# //     import { toast } from 'bulma-toast'

# //     export default {
# //         name: 'AddClient',
# //         data() {
# //             return {
# //                 name: '',
# //                 contact_person: '',
# //                 email: '',
# //                 phone: '',
# //                 estimated_value: 0,
# //                 website: '',
# //                 pdf: '',
# //                 // api: 'http://localhost:8080/api',
# //                 // files: [],
# //                 // filename : '',
# //                 formData: new FormData(),
# //             }
# //         },
# //         mounted() {
# //             console.log('DOM mounted')
# //             this.uploadedFile()
# //         },
# //         created(){
# //             console.log('DOM created')
# //         },
# //         methods: {
# //             async submitForm() {
# //                 this.$store.commit('setIsLoading', true)

# //                 const client = {
# //                     name: this.name,
# //                     contact_person: this.contact_person,
# //                     email: this.email,
# //                     phone: this.phone,
# //                     website: this.website,
# //                     pdf : this.pdf
# //                 }
              
# //                 await axios.post('/api/v1/clients/', client)
# //                     .then(response => {
# //                       this.clientID = response.data.id
# //                         toast({
# //                             message: 'The client was added',
# //                             type: 'is-success',
# //                             dismissible: true,
# //                             pauseOnHover: true,
# //                             duration: 2000,
# //                             position: 'bottom-right',
# //                         })
# //                       })
# //                         .catch(error => {
# //                           console.log(error)
# //                         })

# //                 this.formData.append("pdf", this.$refs.file.files[0]);

# //                 await axios.post(`/api/v1/files/`, this.formData, {
# //                     headers: {
# //                         'Content-Type': 'multipart/form-data'
# //                     }
# //                 })
# //                 .then( response => {
# //                     console.log(response)
# //                 })
# //                 .catch(error => {
# //                     console.log(error)
# //                 })

# //                 this.$router.push('/dashboard/clients')
# //                 this.$store.commit('setIsLoading', false)
# //             },
# //             async uploadedFile() {
# //               this.filename = this.$refs.file.files[0]
# //               console.log(this.filename)
# //               const clientID = this.$route.params.id
              

# //               await axios
# //                 .post(`/api/v1/files/?client_id=${clientID}/`)
# //                 .then(response => {
# //                   this.files = response.data
# //                 })
# //                 .catch(error => {
# //                   console.log(error)
# //                 })
              

            
# //             }
# //         }
# //     }
# // </script>

