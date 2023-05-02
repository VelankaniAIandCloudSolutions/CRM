<!-- <template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Leads</h1>

                <router-link 
                    to="/dashboard/leads/add"
                    v-if="$store.state.team.max_leads > num_leads" class="button btn is-primary" style="color: black;"
                >Add lead</router-link>

                <div 
                    class="notification is-danger"
                    v-else
                >
                    You have reached the top of your limitations. Please upgrade!
                </div>

                <hr>

                <form @submit.prevent="getLeads">
                    <div class="field has-addons">
                        <div class="control">
                            <input type="text" class="input" v-model="query">
                        </div>
                        <div class="control">
                            <button class="button is-success" style="color: black;">Search</button>
                        </div>
                    </div>
                </form>
            </div>

            <div class="column is-12">
                <table class="table is-fullwidth" style=" background: linear-gradient(135deg, #71b7e6, #9b59b6 ); border-style: solid;">
                    <thead>
                        <tr>
                            <th style="color: black;">Company</th>
                            <th style="color: black;">Contact person</th>
                            <th style="color: black;">Assigned to</th>
                            <th style="color: black;">Status</th>
                            <th></th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr style="color: black;"
                            v-for="lead in leads"
                            v-bind:key="lead.id">
                                <td>{{ lead.company }}</td>
                                <td>{{ lead.contact_person }}</td>
                                <td>
                                    <template v-if="lead.assigned_to">{{ lead.assigned_to.first_name }} {{ lead.assigned_to.last_name }}</template>
                                </td>
                                <td>{{ lead.status }}</td>
                                <td>
                                    <router-link :to="{ name: 'Lead', params: { id: lead.id }}" class="button btn is-info" style="color: black;" >Details</router-link>
                                </td>
                        </tr>
                    </tbody>
                </table>

                <div class="buttons">
                    <button class="button is-primary" style="color: black;" @click="goToPreviousPage()" v-if="showPreviousButton">Previous</button>
                    <button class="button is-primary" style="color: black;" @click="goToNextPage()" v-if="showNextButton">Next</button>
                </div>
            </div>
        </div>
    </div>
   
</template> -->







<template>
    <div class="page-leads">
      <nav class="breadcrumb" aria-label="breadcrumbs">
        <ul>
          <li><router-link to="/dashboard">Dashboard</router-link></li>
          <li class="is-active"><router-link to="/dashboard/leads" aria-label="true">Leads</router-link></li>
        </ul>
      </nav>
  
      <div class="columns is-multiline">
        <div class="column is-12">
          <div class="title">Leads</div>
  
          <div>
            <form @submit.prevent="getLeads">
              <div class="field has-addons">
                <div class="control">
                  <input type="text" class="input" v-model="query">
                </div>
                <div class="control">
                  <button class="button is-success">Search</button>
                </div>
              </div>
            </form>
          </div>
          <br>
  
          <router-link to="/dashboard/leads/add" class="button btn is-primary" style="color: black;">Add lead</router-link>
          <!-- v-if="$store.state.team.max_leads > num_leads" 
          
  
          <div class="notification is-danger" v-else>
            You have reached the top of your limitations. Please upgrade!
          </div> -->
        </div>
  
        <hr>
  
        <div class="column is-3" v-for="lead in leads" v-bind:key="lead.id">
          <div class="card" style="background-color:  #ffc371;">
            <h3 class="is-size-4 mb-4">{{ lead.company }}</h3>
            <div class="buttons">
                <router-link :to="{ name: 'Lead', params: { id: lead.id } }" class="button is-light">Details</router-link>
            </div>
          </div>
        </div>
      </div>
  
      <div class="buttons">
        <button class="button is-primary" style="color: black;" @click="goToPreviousPage()" v-if="showPreviousButton">Previous</button>
        <button class="button is-primary" style="color: black;" @click="goToNextPage()" v-if="showNextButton">Next</button>
      </div>
    </div>
  </template>

<script>
    import axios from 'axios'

    export default {
        name: 'Leads',
        data() {
            return {
                leads: [],
                showNextButton: false,
                showPreviousButton: false,
                currentPage: 1,
                query: '',
                num_leads: 0
            }
        },
        mounted() {
            this.getLeads()
        },
        methods: {
            goToNextPage() {
                this.currentPage += 1
                this.getLeads()
            },
            goToPreviousPage() {
                this.currentPage -= 1
                this.getLeads()
            },
            async getLeads() {
                this.$store.commit('setIsLoading', true)

                this.showNextButton = false
                this.showPreviousButton = false

                await axios
                    .get(`/api/v1/leads/`)
                    .then(response => {
                        console.log(response.data)
                        this.num_leads = response.data.count
                    })

                await axios
                    .get(`/api/v1/leads/?page=${this.currentPage}&search=${this.query}`)
                    .then(response => {
                        this.leads = response.data.results

                        if (response.data.next) {
                            this.showNextButton = true
                        }

                        if (response.data.previous) {
                            this.showPreviousButton = true
                        }
                    })
                    .catch(error => {
                        console.log(error)
                    })

                this.$store.commit('setIsLoading', false)
            }
        }
    }
</script>




