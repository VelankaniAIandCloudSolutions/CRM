



<template>
  <div class="container">
    <h1 class="title" style="text-transform: capitalize;">Quotation Details</h1> 

    <nav class="breadcrumb" aria-label="breadcrumbs">
      <ul>
        <li><router-link to="/dashboard" style="color: black;">Dashboard</router-link></li>
        <li><router-link to="/dashboard/quotes" style="color: black;">Quotes</router-link></li>
      </ul>
    </nav>

    <hr>

    <div class="buttons" >
      <button @click="getpdf()" class="button is-dark is-outlined" style="width:18%; text-transform: capitalize;">
        <span class="icon is-small">
          <i class="fas fa-file-pdf" style="margin-right: 35px;"></i>
        </span>
        Download PDF
      </button>

      
      <button v-if="!quote.is_accepted" @click="setAsAccepted()" class="button is-success is-outlined" style="width:17%;text-transform: capitalize;">
        <span class="icon is-small">
          <i class="fas fa-check" style="margin-right: 25px;"></i>
        </span>
        Set as Accepted
      </button>

      <button v-if="!quote.is_rejected" @click="setAsRejected()" class="button is-danger is-outlined" style="width:17%;text-transform: capitalize;">
        <span class="icon is-small">
          <i class="fas fa-times" style="margin-right: 25px;"></i>
        </span>
        Set as Rejected
      </button>

      
      <button @click="sendReminder()" class="button is-info is-outlined" style="width:17%;text-transform: capitalize;">
        <span class="icon is-small">
          <i class="fas fa-envelope" style="margin-right: 38px;"></i>
        </span>
        Send E-mail
      </button>

    </div>

    <table class="table is-fullwidth is-striped">
      <thead>
        <tr>
          <th>Service Name</th>
          <th>Unit</th>
          <th>Rate</th>
          <th>Quantity</th>
          <th>Amount</th>
          <th>From Date</th>
          <th>To Date</th>
          <th>Inclusions</th>
          <th>Menu Items</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="product in products" :key="product.id">
          <td>{{ product.service_name }}</td>
          <td>{{ product.unit }}</td>
          <td>{{ product.rate }}</td>
          <td>{{ product.quantity }}</td>
          <td>{{ product.amount }}</td>
          <td>{{ product.from_date }}</td>
          <td>{{ product.to_date }}</td>
          <td>
            <ul>
              <li v-for="inclusion in product.inclusions" :key="inclusion.id">{{ inclusion.inclusions }}</li>
            </ul>
          </td>
          <td>
            <ul>
              <li v-for="menu_item in product.menu_items" :key="menu_item.id">{{ menu_item.menu_items }}</li>
            </ul>
          </td>
          <td>
            <button @click="deleteProduct(product.id)" class="button btn is-rounded is-outlined is-danger" style="text-transform: capitalize;"> <i class="fas fa-trash"> </i>Delete</button>
          </td>
        </tr>
      </tbody>
    </table>

    <table class="table is-fullwidth">
      <thead>
        <tr>
          <th>Grand Total</th>
          <th>Discount</th>
          <th>Discount Amount</th>
          <th>Sub Total</th>
          <th>Tax</th>
          <th>Tax Amount</th>
          <th>Description</th>
          <th>Terms and Condition</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="quote in quotes" :key="quote.id">
          <td>{{ quote.grand_total }}</td>
          <td>{{ quote.discount }}</td>
          <td>{{ quote.discount_amount }}</td>
          <td>{{ quote.sub_total }}</td>
          <td>{{ quote.tax }}</td>
          <td>{{ quote.tax_amount }}</td>
          <td>{{ quote.description }}</td>
          <td>{{ quote.terms_and_condition }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>



<script>
 

import axios from 'axios'
import { toast } from 'bulma-toast'
import 'vue-toastification/dist/index.css';

const fileDownload = require('js-file-download')


  export default {
      name:'Quote',
      data() {
          return {
              quote:[],
              quotes:[],
              products:[],
              inclusions:[],
              menu_items:[],
          }
      },
      mounted() {
          this.getQuotes()
          // this.getProduct()
          // this.getInclusion()
          // this.getMenu_Item()
         

      },
      methods: {
          async getQuotes() {
          this.$store.commit('setIsLoading',true)

          const quoteID = this.$route.params.id


          await axios
              .get(`/api/v1/get_quote/${quoteID}`)
              .then(response => {
                  this.quotes = response.data
                  this.products = response.data.products
                  
                  
              })
              .catch(error => {
                  console.log(error)
              })

          // await axios
          //     .get(`/api/v1/get_quotes`)
          //     .then(response => {
          //         this.quotes = response.data
          //     })
          //     .catch(error => {
          //         console.log(error)
          //     }) 

          // await axios
          //     .get(`/api/v1/quote/?quote_id=${quoteID}`)
          //     .then(response => {
          //         this.quote = response.data.results
          //     })
          //     .catch(error => {
          //         console.log(error)
          //     })
          this.$store.commit('setIsLoading',false)
      },
    
      
      async deleteProduct(product_id){

          this.$store.commit('setIsLoading', true)
          
          await axios
              .delete(`/api/v1/delete_product/${product_id}/`)
              .then(response => {
                  console.log(response.data)

                  this.$router.push('/dashboard')
              })
              .catch(error => {
                  console.log(error)
              })
          this.$store.commit('setIsLoading',false)
         
      },

      async getpdf() {
          this.$store.commit('setIsLoading', true)
          const quoteID = this.$route.params.id

          await axios
              .get(`/api/v1/quotes/${quoteID}/generate_pdf/`, {
                  responseType: 'blob',
              }).then(res => {
                  fileDownload(res.data, `quote_${quoteID}.pdf`);
              }).catch(error => {
                  console.log(error)
              })
          this.$store.commit('setIsLoading', false)
      },

      async sendReminder() {
  try {
    const quoteID = this.$route.params.id;
    const response = await axios.post(`/api/v1/quotes/${quoteID}/send_reminder/`);

    console.log("sendReminder response:", response); // log the response for debugging purposes

    if (response.data.success) {
      toast({
            message: 'Quotation sent successfully',
            type: 'is-success',
            position: 'bottom-right',
            duration: 2000,
            dismissible: true,
          });
      this.showSuccess = true;
      this.showError = false;
    } else {
      this.showSuccess = false;
      this.showError = true;
    }
  } catch (error) {
    console.error("sendReminder error:", error); // log the error for debugging purposes
    this.showSuccess = false;
    this.showError = true;
  }
},


      async setAsAccepted() {
        this.$store.commit('setIsLoading', true);

        const quoteID = this.$route.params.id;

        this.quote.is_accepted = true;


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
                })




            const updatedQuotation_status = response.data.quote;

            if (updatedQuotation_status && updatedQuotation_status.is_accepted) {
              const index = this.quotes.findIndex(q => q.id === updatedQuotation_status.id);
              if (index >= 0) {
                this.quotes.splice(index, 1, updatedQuotation_status);
              }
            }
            this.$store.commit('setIsLoading', false);


          }catch (error) {
          console.error(error);
          }
        this.$store.commit('setIsLoading', false)
      },

      async setAsRejected() {
        this.$store.commit('setIsLoading', true)

        const quoteID = this.$route.params.id

        this.quote.is_rejected = true

        try {
          const response = await axios .patch(`/api/v1/quotes/${quoteID}/reject_quotation/`)
          .then(response => {
            toast({
              message: 'The Quotaion was Rejected',
              type: 'is-success',
              dismissible: true,
              pauseOnHover: true,
              duration: 2000,
              position: 'bottom-right',
            })
            console.log('Response:',  response.data)
          })


          const updatedQuotation_status = response.data.quote

          if(updatedQuotation_status && updatedQuotation_status.is_rejected) {
            const index = this.quotes.findIndex(q => q.id === updatedQuotation_status.id)
            if(index >= 0) {
              this.quotes,splice(index, 1, updatedQuotation_status)
            }
          }
          
        }catch (error) {
          console.error(error)
        }
        this.$store.commit('setIsLoading', false)
      },


  

                    
  
  
            
     
     
     
     
  //     async sendReminder() {
  //   this.$store.commit('setIsLoading', true)

  //   const quoteID = this.$route.params.id

  //   await axios
  //     .post(`/api/v1/quotes/${quoteID}/send_reminder/`, {
  //       quote_id: quoteID
  //     })
  //     .then(response => {
  //       console.log(response.data)
  //       toast.success('Quotation sent successfully!', {
  //         timeout: 3000,
  //         position: 'top-right'
  //       });
  //     })
  //     .catch(error => {
  //       console.log(error)
  //     })

  //   this.$store.commit('setIsLoading', false)
  // }
     
     

      // async getInclusion() {
      //     this.$store.commit('setIsLoading',true)

      //     await axios
      //         .get('/api/v1/get_inclusions')
      //         .then(response => {
      //             this.inclusions = response.data
      //         })
      //         .catch(error => {
      //             console.log(error)
      //         })
      //     this.$store.commit('setIsLoading',false) 
      // },



      // async getMenu_Item() {
      //     this.$store.commit('setIsLoading',true)

      //     await axios
      //         .get('/api/v1/get_menu_items')
      //         .then(response => {
      //             this.menu_items = response.data
      //         })
      //         .catch(error => {
      //             console.log(error)
      //         })
      //     this.$store.commit('setIsLoading',false)
      // },

      
  //     async deleteInclusion(inclusions_id){
  //         this.$store.commit('setIsLoading',true)

  //         await axios
  //             .delete(`/api/v1/delete_inclusions/${inclusions_id}`)
  //             .then(response => {
  //                 console.log(response.data)

  //                 this.$router.push('/dashboard')
  //             })
  //             .catch(error => {
  //                 console.log(error)
  //             })
  //         this.$store.commit('setIsLoading',false)
  //     },

  //     async deleteMenu_Item(menu_items_id) {
  //         this.$store.commit('setIsLoading',true)

  //         await axios
  //             .delete(`/api/v1/delete_menu_items/${menu_items_id}`)
  //             .then(response => {
  //                 console.log(response.data)

  //                 this.$router.push('/dashboard/quotes/')
  //             })
  //             .catch(error => {
  //                 console.log(error)
  //             })
  //         this.$store.commit('setIsLoading',false)
  //     }
      }
  }

</script>

<style>
  td{
      color: black;
  }

  th {
background-color: #4CAF50;
color: white;
}



  

</style>