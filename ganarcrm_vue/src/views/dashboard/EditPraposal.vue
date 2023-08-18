<template>
    <div class="title">
        <label>Edit Proposal</label>
    </div>
    <br>
    <br>

    <div class="form-group">
        <label>Name :</label>
        <input type="text" id="name" v-model="praposal.name">
    </div>

    <div class="form-group">
        <label>Company :</label>
        <input type="text" id="company" v-model="praposal.company">
    </div>

    <div class="form-group">
        <label>Phone :</label>
        <input type="number" id="phone" v-model="praposal.phone">
    </div>

    <div class="form-group">
        <label>Email :</label>
        <input type="email" id="email" v-model="praposal.email">
    </div>

    <div class="form-group">
        <label>City :</label>
        <input type="text" id="city" v-model="praposal.city">
    </div>

    <div class="form-group">
        <label>From Date :</label>
        <input type="date" id="from_date" v-model="praposal.from_date">
    </div>

    <div class="form-group">
        <label>To Date :</label>
        <input type="date" id="to_date" v-model="praposal.to_date">
    </div>

    <br>
    <br>
    <div class="buttons">
      <button class="button btn is-danger is-outlined" @click="cancelPraposal"><i class="fas fa-times" style="margin-right:8px;"></i> Cancel</button>
      <button type="submit" class="button btn is-link is-outlined" @click="onSubmit"> <i class="fas fa-check " style="margin-right:8px;" ></i> Update</button>
    </div>
</template>

<script>
    import axios from 'axios';
    import { toast } from 'bulma-toast';
    import { reactive, onMounted, ref } from 'vue';

    export default {

        name: 'EditPraposal',

        data() {

            return {

                praposal: {
                    name:'',
                    company:'',
                    phone:'',
                    emial:'',
                    city:'',
                    from_date:'',
                    to_date:'',
                }
            }
        },

        mounted() {
            this.getPraposal()
        },

        methods: {

            cancelPraposal() {
                if (confirm("Are you sure you want to cancel?")) {
                this.$router.push(`/dashboard/proposals/${this.$route.params.praposal_id}`);
                }
            },

            async getPraposal() {
                
                this.$store.commit('setIsLoading', true)

                const praposalId = this.$route.params.id

                try {

                    const response = await axios .get(`/api/v1/get_praposal_edit/${praposalId}`);
                    const praposalData = response.data

                    this.praposal = {

                        name:praposalData.name,
                        company:praposalData.company,
                        phone:praposalData.phone,
                        email:praposalData.email,
                        city: praposalData.city,
                        from_date : praposalData.from_date,
                        to_date:praposalData.to_date,

                    }
                } catch (error) {
                    console.log(error)
                }

                this.$store.commit('setIsLoading', false)
            },

            async onSubmit() {

                const praposalId = this.$route.params.id

                try {

                    const response = await axios .put(`/api/v1/update_praposal/${praposalId}/` , this.praposal);

                    console.log(response.data);

                    toast({
                        message: 'The Proposal Updated Successfully',
                        type: 'is-success',
                    });
                    this.$router.push(`/dashboard/proposals/${this.$route.params.praposal_id}`);

                } catch(error) {
                    console.log(error);

                    toast({
                        message:'There was an error updating the proposal.',
                        type: 'is-danger',
                    })
                }
            },
        }
    }
</script>