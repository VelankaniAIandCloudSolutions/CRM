
<template>
    <div class="container">
        <div class="title">Create Quotation</div>
        <div class="box" >
        <div class="content">
            <form  @submit.prevent="submitForm">
                <div class="user-details" >
                    <div class="input-box">
                        <span class="details">Subject</span>
                        <input type="text" placeholder=" Enter subject" v-model="subject" required>
                    </div>

                    <div class="input-box">
                        <label>Client Name</label>
                        <div class="field">
                            <!-- <div class="select" style="width: 100%;"> -->
                           
                                <select size="clients.length" v-model="client_name"  >
                                    <option 
                                        v-for="client in clients"
                                        v-bind:key="client.id"
                                        v-bind:value="client.id"
                                    >
                                        {{ client.name }}
                                    </option>
                                </select>
                            <!-- </div> -->
                            
                        </div>
                    </div>

                    <div class="input-box">
                        <span class="details">Quotation Date</span>
                        <input type="date" placeholder=" Enter quotation date" v-model="quotation_date" required>
                           
                        
                            
                    </div>

                    <div class="input-box">
                        <span class="details">Expiry Date</span>
                        <input type="date" placeholder="Expiry date" v-model="expiry_date" required>
                    </div>

                    <div class="input-box">
                        <span class="details">Quotation Request Number</span>
                        <input type="text" placeholder="Quotation Number"  v-model="quotation_request_number" required>
                     
                    </div>

                    <div class="input-box">
                        <span class="details">Quotation Status</span>
                        <select v-model="quotation_status" required>
                            <option value="new">New</option>
                            <option value="accepted">Accepted</option>
                            <option value="on-going">On-Going</option>
                            <option value="completed">Completed</option>
                                
                        </select>
                        
                    </div>

                    <div class="input-box">
                        <span class="details">Quotation Owner</span>
                        <input type="text" placeholder="Enter owner" form="Quote" name="quotation_owner" required>
                       
                    </div>

                    
                </div>


                <div class="container mt-4">
                    <div class="box" style="border-radius: solid; background-color: antiquewhite;">
                        <div class="box-body">
                            <div v-for="(item, index) in form" :key="index">
                                <div class="row" >
                                    <h3>Products On Quotes  {{ index+1 }}</h3>
                                
                                   
                                    <div class="content"  >
                                        <div class="user-details">
                                            <div class="input-box">

                                        
                                                <span class="details">Service Name</span>
                                                <input type="text" class="form-control" v-model="item.service_name" >
                                            </div>
                                            

                                           <!-- <div class="input-box">
                                                <span class="details">Unit</span>
                                                <input type="text" class="form-control" v-model="item.unit" >
                                            </div> -->

                                           
                                            
                                                <div class="input-box">
                                                    <span class="details">Quantity</span>
                                                    <input type="text" class="form-control" name="qty" v-model="item.quantity"   @change="updateAmount(index)">
                                                </div>

                                                <div class="input-box">
                                                    <span class="details">Rate</span>
                                                    <input type="text" class="form-control" name="rate" v-model="item.rate"  @change="updateAmount(index)">
                                                </div>

                                                <div class="input-box">
                                                    <span class="details">Amount</span>
                                                    <input type="text" class="form-control" name="amt" v-model="item.amount" @change="updateTotal(index)">
                                                </div>
                                            
                                           
                                        

                                            <div class="input-box">
                                                <span class="details">From Date</span>
                                                <input type="date" class="form-control" v-model="item.from_date" >
                                            </div>

                                            <div class="input-box">
                                                <span class="details">To Date</span>
                                                <input type="date" class="form-control" v-model="item.to_date" >
                                            </div>

                                            <div class="input-box">
                                                <label>Inclusions</label>
                                                <div class="field">
                                                    <div class="select is-multiple" style="width: 100%;">
                                                
                                                        <select multiple size="inclusions.length" v-model="item.inclusions"  >
                                                            <option 
                                                                v-for="inclusion in inclusions"
                                                                v-bind:key="inclusion.id"
                                                                v-bind:value="inclusion.id"
                                                            >
                                                                {{ inclusion.inclusions }}
                                                            </option>
                                                        </select>
                                                    </div>
                                                    
                                                </div>
                                            </div>
                                        

                                            <div class="input-box">
                                                <label>Menu Items</label>
                                                <div class="field">
                                                    <div class="select is-multiple" style="width: 100%;">
                                                
                                                        <select multiple size="clients.length" v-model="item.menu_items"  >
                                                            <option 
                                                                v-for="menu_item in menu_items"
                                                                v-bind:key="menu_item.id"
                                                                v-bind:value="menu_item.id"
                                                            >
                                                                {{ menu_item.menu_items }}
                                                            </option>
                                                        </select>
                                                    </div>
                                                    
                                                </div>
                                                                        
                                            </div>


                                            <div class="buttons">
                                                <button type="button" class="button btn is-success " @click="addRow()">+ Add More</button>
                                                <button type="button" class="button btn is-danger" @click="removeRow(index)">X</button>
                                                
                                            </div>
                                        </div>

                                        
                                    </div>
                                </div>
                            </div>
                            
                        </div>
                    </div>
                </div>

                <div id="app">
                    <div class="container">
                        <div class="content">
                        <div class="user-details">
                            <div class="input-box">
                            <span class="details">Sub Total</span>
                            <input type="text" placeholder="Sub Total" id="subTotal" name="subTotal" v-model="sub_total" required>
                            </div>

                            <div class="input-box">
                            <span class="details">Grand Total</span>
                            <input type="text" placeholder=" Grand Total" :value="grand_total" required>
                            </div>

                            <div class="input-box">
                            <span class="details">Discount</span>
                            <input type="text" placeholder=" Enter Discount" name="discount" v-model="discount"  @change="updateTotal" >
                            </div>

                            <div class="input-box">
                            <span class="details">Discount Amount</span>
                            <input type="text" placeholder="Discount Amount" name="discountAmount" v-model="discount_amount">
                            </div>

                            <div class="input-box">
                            <span class="details"> Tax (%)</span>
                            <input type="text" placeholder=" Enter Tax " name="tax" v-model="tax" @change="updateTotal" required>
                            </div>

                            <div class="input-box">
                            <span class="details">Tax Amount</span>
                            <input type="text" placeholder="Enter Tax Amount" name="taxAmount" v-model="tax_amount">
                            </div>

                            <div class="input-box">
                            <span class="details">Description</span>
                            <textarea cols="85" rows="8" v-model="description"></textarea>
                            </div>

                            <div class="input-box">
                            <span class="details">Terms & Condition</span>
                            <textarea cols="85" rows="8" v-model="terms_and_condition"></textarea>
                            </div>

                        </div>

                        </div>
                    </div>
                    </div>
                    <br>
                    <br>
               
                    
                    <div class="field">
                        <div class="control">
                            <div class="buttons" style="margin-left: 42%;">
                                <button class="button is-success">Submit</button>

                                <button class="button is-danger" @click="$router.push('/dashboard/quotes')" >Cancel</button>
                            </div>
                        </div>
                    </div>

               
            </form>
        </div>
        </div>
    </div>

    
  
</template>


<script>

    import { reactive } from 'vue'
    import axios from 'axios'



    export default {
        name: 'AddQuote',

       
        mounted(){
            this.getClients()
            this.getInclusions()
            this.getMenu_Item()
            
           

        },

        setup() {
            const form = reactive([
                {service_name : '',  rate: '', quantity: '', amount: '' , from_date: '', to_date: '', inclusions: '', menu_items: ''}
            ])

            const addRow = (index) => {
             
                form.push({  service_name : '', rate: '', quantity: '', amount: '' , from_date: '', to_date: '', inclusions: '', menu_items: ''})
            }

            const removeRow = (index) => {
                if(form.length > 1){
                    form.splice(index,1)
                }
                
            }

            

            return {
                form,
                addRow,
                
                removeRow
            }
        },






        data() {
            return {
                subject: '',
                clients:[],
                client_name: '',
                quotation_date: '',
                expiry_date: '',
                quotation_request_number: '',
                quotation_status: 'new',
                quotation_owner: 'admin-user',
                grand_total: '',
                discount: '',
                discount_amount:'',
                sub_total:'',
                tax:'',
                tax_amount:'',
                description:'',
                terms_and_condition:'',
                service_name:'',
                // unit:'',
                rate:'',
                quantity:'',
                amount:'',
                from_date:'',
                to_date:'',
                inclusions:'',
                menu_items:'',

            }
        },
        methods: {

            updateAmount(index) {
                const item = this.form[index];
                item.amount = item.quantity * item.rate;
                this.updateTotal(index);
            },
            updateTotal() {
                let sub_total = 0;
                for (let i = 0; i < this.form.length; i++) {
                    sub_total += this.form[i].amount;
                }
                this.sub_total = sub_total;

                this.discount_amount = (this.sub_total * this.discount) / 100;
                this.tax_amount = (this.sub_total - this.discount_amount) * (this.tax / 100);

                this.grand_total = this.sub_total - this.discount_amount + this.tax_amount;
            },
           

           



          
            



            async submitForm() {
                this.$store.commit('setIsLoading', true)
                
                const quote = {
                    subject:this.subject,
                    client_name:this.client_name,
                    quotataion_date:this.quotation_date,
                    expiry_date:this.expiry_date,
                    quotation_request_number:this.quotation_request_number,
                    quotation_status:this.quotation_status,
                    quotation_owner:this.quotation_owner,

                    products:this.form,

                    grand_total:this.grand_total,
                    discount:this.discount,
                    discount_amount:this.discount_amount,
                    sub_total:this.sub_total,
                    tax:this.tax,
                    tax_amount:this.tax_amount,
                    description:this.description,
                    terms_and_condition:this.terms_and_condition,



                }
                // console.log(quote)
                // // console.log(quote)

                await axios
                    .post('/api/v1/create_quotes/', quote)
                    .then(response => {
                        
                        // console.log(response.data)
                        this.$router.push('/dashboard/quotes')
                    })
                    .catch(error => {
                        console.log(error)
                    })

                

                this.$store.commit('setIsLoading', false)
                



            },

            async getClients() {
                this.$store.commit('setIsLoading', true)

                

                await axios
                    .get('/api/v1/get_clients')
                    .then(response => {
                        this.clients = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })
                this.$store.commit('setIsLoading', false)
            },

            async getInclusions() {
                this.$store.commit('setIsLoading',true)

                await axios
                    .get('/api/v1/get_inclusions')
                    .then(response => {
                        this.inclusions = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })

                this.$store.commit('setIsLoading',false)
            },

            async getMenu_Item() {
                
                this.$store.commit('setIsLoading',true)

                await axios
                    .get('/api/v1/get_menu_items')
                    .then(response => {
                        this.menu_items = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })
                this.$store.commit('setIsLoading',false)
            },


         },
     }
     
 

   
</script>







<style>
/* General styles */

body {
  /* background-image: linear-gradient(to bottom right, #ff5f5f, #ffc371); */
  height: 100%;
  width:300%;
  background-color:white;
}

.options {
  width: 15px;
  height: auto;
}

.box {
  text-align: center;
  width: 90%;
  margin: auto;
}

.content {
  text-align: center;
}

.table {
  width: 90%;
  margin: auto;
}

.strike {
  text-decoration: line-through;
}

div.scrollmenu {
  /* background-color: #333; */
  overflow: auto;
  white-space: nowrap;
}

div.scrollmenu a:hover {
  background-color: #777;
}

/* Container and form styles */

.container {
  max-width: 700px;
  width: 100%;
  background-color: #fff;
  border-radius: 5px;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.15);
}

.container .title::before {
  content: "";
  position: absolute;
  left: 0;
  bottom: 0;
  height: 3px;
  width: 30px;
  border-radius: 5px;
  background: linear-gradient(135deg, #71b7e6, #9b59b6);
}

.content form .user-details {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  margin: 20px 0 12px 0;
}

form .user-details .input-box {
  margin-bottom: 15px;
  width: calc(100% / 2 - 20px);
}

.user-details .input-box input {
  height: 45px;
  width: 100%;
  outline: none;
  font-size: 16px;
  border-radius: 5px;
  padding-left: 15px;
  border: 1px solid #ccc;
  border-bottom-width: 2px;
  transition: all 0.3s ease;
}

select {
  height: 45px;
  width: 100%;
  outline: none;
  font-size: 16px;
  border-radius: 5px;
  padding-left: 15px;
  border: 1px solid #ccc;
  border-bottom-width: 2px;
  transition: all 0.3s ease;
}

.user-details .input-box input:focus,
.user-details .input-box input:valid {
  border-color: #9b59b6;
}

form .gender-details .gender-title {
  font-size: 20px;
  font-weight: 500;
}

form .category {
  display: flex;
  width: 80%;
  margin: 14px 0;
  justify-content: space-between;
}

form .category label {
  /* display: flex; */
  align-items: center;
  cursor: pointer;
}

form .category label .dot {
  height: 18px;
  width: 18px;
  border-radius: 50%;
  margin-right: 10px;
  background: #d9d9d9;
  border: 5px solid transparent;
  transition: all 0.3s ease;
}

#dot-1:checked ~ .category label .one,
#dot-2:checked ~ .category label .two,
#dot-3:checked ~ .category label .three {
  background: #9b59b6;
  border-color: #d9d9d9;
}

form input[type="radio"] {
  display: none;
}

/* Additional styles can be added here as needed */

</style>

