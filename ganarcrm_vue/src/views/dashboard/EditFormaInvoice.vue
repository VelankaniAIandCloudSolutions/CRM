<template>
    <div class="title">
        <label>Edit Pro Forma Invoice</label>
    </div>
    <br>
    <br>

    <div class="form-group">
        <label>Total Package (Room + Banquet)</label>
        <input type="number" id="total_package" v-model="updateinvoice.total_package" @input="calculateGrandTotal">
    </div>

    <div class="form-group">
        <label>Water And Cleaning Charges</label>
        <input type="number" id="water_cleaning" v-model="updateinvoice.water_cleaning" @input="calculateGrandTotal">
    </div>

    <div class="form-group">
        <label>Security Deposite</label>
        <input type="number" id="security_deposite" v-model="updateinvoice.security_deposite" @input="calculateGrandTotal">
    </div>

    <div class="form-group">
        <label>Grand Total</label>
        <input type="number" v-model="updateinvoice.grand_total" disabled>
    </div>
    <br>
    <br>

    <div class="buttons">

        <button class="button btn is-danger is-outlined" @click="cancelInvoice"><i class="fas fa-times" style="margin-right:8px;"></i> Cancel</button>

        <button type="submit" class="button btn is-link is-outlined" @click="onSubmit"> <i class="fas fa-check " style="margin-right:8px;" ></i> Update</button>

    </div>
</template>



<script>
    import axios from 'axios';
    import { toast } from 'bulma-toast';
    import { reactive, onMounted, ref } from 'vue';

    export default {
        name: 'EditFormaInvoice',

        data() {
            return {
                updateinvoice: {
                    total_package:'',
                    water_cleaning:'',
                    security_deposite:'',
                    // grand_total:'',
                }
            }
        },

        mounted() {

            this.getForma_Invoice();
        },

        methods: {

            cancelInvoice() {
                if (confirm("Are you sure you want to cancel?")) {
                    const serviceId = this.$route.params.service_id;
                    this.$router.push(`/dashboard/proposals/${serviceId}`);
                }
            },

            calculateGrandTotal() {
            this.updateinvoice.grand_total =
                parseInt(this.updateinvoice.total_package) +
                parseInt(this.updateinvoice.water_cleaning) +
                parseInt(this.updateinvoice.security_deposite);
            },


            async getForma_Invoice() {

                this.$store.commit('setIsLoading', true)

                const formainvoiceID = this.$route.params.id

                try {

                    const response = await axios .get(`/api/v1/get_forma_invoices/${formainvoiceID}`);
                    const invoiceData = response.data;

                    this.updateinvoice = {

                        total_package:invoiceData.total_package,
                        water_cleaning:invoiceData.water_cleaning,
                        security_deposite:invoiceData.security_deposite,
                        grand_total:invoiceData.grand_total,
                    }
                } catch(error) {
                    console.log(error)
                }

                this.$store.commit('setIsLoading', false)

            },

            async onSubmit() {

                const formainvoiceID = this.$route.params.id;

                try {

                    const response = await axios .put(`/api/v1/update_forma_invoice/${formainvoiceID}/` , this.updateinvoice);

                    console.log(response.data);
                    toast({
                        message: 'Pro Forma Invoice updated successfully',
                        type: 'is-success',
                    });

                
                    const serviceId = this.$route.params.service_id;
                    this.$router.push(`/dashboard/proposals/${serviceId}`);
                    } catch (error) {
                    console.log(error);
                
                    toast({
                        message: 'Failed to update booking',
                        type: 'is-danger',
                    });
                    }

                },

               
                async get_forma_invoice() {

                    this.$store.commit('setIsLoading', true)

                    const formainvoiceID = this.$route.params.id

                    try {

                        const response = await axios .get(`/api/v1/get_forma_invoice/${formainvoiceID}`)

                        console.log(response.data)

                        this.forma_invoices = response.data

                    } catch (error) {

                        console.log(error)
                    }

                    this.$store.commit('setIsLoading', false)
                }

                




                


                
                

            

        

                

                



                

                


                



               




               



                


              


                
            }

        }
    
</script>