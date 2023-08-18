

<template>
    <div class="container">
        <h1 class="title">{{ lead.company }}</h1>

        <div class="buttons">
            <router-link :to="{ name: 'EditLead', params: { id: $route.params.lead_id }}" class="button is-link is-rounded is-outlined" style="color: black;">Edit</router-link>
            <button @click="convertToClient" class="button is-link is-rounded is-outlined" style="color: black;">Convert to client</button>
            <button @click="deleteLead" class="button is-danger is-rounded is-outlined" style="color: black;">Delete</button>
        </div>

        <table class="table is-fullwidth">
            <tbody>
                <tr>
                    <td>Status:</td>
                    <td>{{ lead.status }}</td>
                </tr>
                <!-- <tr>
                    <td>Priority:</td>
                    <td>{{ lead.priority }}</td>
                </tr> -->
                <!-- <tr>
                    <td>Confidence:</td>
                    <td>{{ lead.confidence }}</td>
                </tr> -->
                <!-- <tr>
                    <td>Estimated value:</td>
                    <td>{{ lead.estimated_value }}</td>
                </tr> -->
                <tr>
                    <td>Assigned to:</td>
                    <td>{{ lead.assigned_to ? lead.assigned_to.first_name + ' ' + lead.assigned_to.last_name : '' }}</td>
                </tr>
                <tr>
                    <td>Created at:</td>
                    <td>{{ lead.created_at }}</td>
                </tr>
                <tr>
                    <td>Modified at:</td>
                    <td>{{ lead.modified_at }}</td>
                </tr>
                <tr>
                    <td>Contact person:</td>
                    <td>{{ lead.contact_person }}</td>
                </tr>
                <tr>
                    <td>Email:</td>
                    <td>{{ lead.email }}</td>
                </tr>
                <tr>
                    <td>Phone:</td>
                    <td>{{ lead.phone }}</td>
                </tr>
                <tr>
                    <td>Company Address</td>
                    <td>{{ lead.address }}</td>
                </tr>
                <tr>
                    <td>Designation Of Contact Person</td>
                    <td>{{ lead.designation }}</td>
                </tr>
                <tr>
                    <td>Website:</td>
                    <td>{{ lead.website }}</td>
                </tr>
            </tbody>
        </table>

        <h2 class="subtitle" style="color: black;">Notes</h2>
        <router-link :to="{ name: 'AddNote' , params: { id: $route.params.lead_id  } }" class="button is-primary mb-6 is-rounded is-outlined"  style="color: black;"> + Add Notes</router-link>
        <table class="table is-fullwidth is-bordered">
            <tbody>
                <tr v-for="notes in notess" v-bind:key="notes.id">
                    <td style="border-style: solid; border-color: black;">
                        <h3 class="is-size-4">{{ notes.name }}</h3>
                        <p>{{ notes.body }}</p>
                    </td>

                    <td>
                        <router-link :to="{ name: 'EditNotes', params: { id: $route.params.lead_id , notes_id: notes.id } }" class="button is-link is-rounded is-outlined mt-6" style="color: black;">Edit Note</router-link>
                    </td>
                </tr>
            </tbody>
        </table> 
    </div>
</template>






<script>
    import axios from 'axios'
    import router from '../../router'

    export default {
    name: "Lead",
    data() {
        return {
            lead: {},
            notess:[]
        };
    },
    mounted() {
        console.log('test')
        const leadID = this.$route.params.lead_id;
        console.log(this.$route.params)
        this.getLead();
    },
    methods: {
        async deleteLead() {
            this.$store.commit("setIsLoading", true);
            const leadID = this.$route.params.lead_id;
            console.log(this.$route.params)
            await axios
                .post(`/api/v1/leads/delete_lead/${leadID}/`)
                .then(response => {
                console.log(response.data);
                this.$router.push("/dashboard/leads");
            })
                .catch(error => {
                console.log(error);
            });
            this.$store.commit("setIsLoading", false);
        },
        async getLead() {
            this.$store.commit("setIsLoading", true);
            const leadID = this.$route.params.lead_id;
            console.log(leadID)

            await axios
                .get(`/api/v1/leads/${leadID}/`)
                .then(response => {
                this.lead = response.data;
                console.log(response.data)
                })
                .catch(error => {
                    console.log(error)
                })
            await axios
                .get(`/api/v1/notess/?lead_id=${leadID}`)
                .then(response => {
                    this.notess = response.data
                })
                .catch(error => {
                console.log(error);
                });

            
            this.$store.commit("setIsLoading", false);
        },
        async convertToClient() {
            this.$store.commit("setIsLoading", true);
            const leadID = this.$route.params.lead_id;
            const data = {
                lead_id: leadID
            };
            await axios
                .post(`/api/v1/convert_lead_to_client/`, data)
                .then(response => {
                console.log("converted to client");
                this.$router.push("/dashboard/clients");
            })
                .catch(error => {
                console.log(error);
            });
            this.$store.commit("setIsLoading", false);
        }
    },
    components: { router }
}
</script>


























































<!-- <template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">{{ lead.company }}</h1>

                <div class="buttons">
                    <router-link :to="{ name: 'EditLead', params: { id: lead.id }}" class="button is-info" style="color: black;">Edit</router-link>
                    <button @click="convertToClient" class="button is-info" style="color: black;">Convert to client</button>
                    <button @click="deleteLead" class="button is-danger" style="color: black;">Delete</button>
                </div>
            </div>

            <div class="column is-6">
                <div class="box" style=" background: linear-gradient(135deg, #71b7e6, #9b59b6 ); border-style:solid;">
                    <h2 class="title">Details</h2>

                    <template v-if="lead.assigned_to">
                        <p><strong>Assigned to: </strong>{{ lead.assigned_to.first_name }} {{ lead.assigned_to.last_name }}</p>
                    </template>
                    <p><strong>Status: </strong>{{ lead.Status }}</p>
                    <p><strong>Priority: </strong>{{ lead.priority }}</p>
                    <p><strong>Confidence: </strong>{{ lead.confidence }}</p>
                    <p><strong>Estimated value: </strong>{{ lead.estimated_value }}</p>
                    <p><strong>Created at: </strong>{{ lead.created_at }}</p>
                    <p><strong>Modified at: </strong>{{ lead.modified_at }}</p>
                </div>
            </div>

            <div class="column is-6">
                <div class="box"  style=" background: linear-gradient(135deg, #71b7e6, #9b59b6 ); border-style:solid ;">
                    <h2 class="title">Contact information</h2>

                    <p><strong>Contact person: </strong>{{ lead.contact_person }}</p>
                    <p><strong>Email: </strong>{{ lead.email }}</p>
                    <p><strong>Phone: </strong>{{ lead.phone }}</p>
                    <p><strong>Website: </strong>{{ lead.website }}</p>
                    
                </div>
            </div>
        </div>
    </div>
    
</template> -->