<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Edit note</h1>
            </div>

            <div class="column is-12">
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Name</label>
                        <div class="control">
                            <input type="text" class="input" v-model="note.name">
                        </div>
                    </div>

                    <div class="field">
                        <label>Body</label>
                        <div class="control">
                            <textarea class="textarea" v-model="note.body"></textarea>
                        </div>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Update</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    import { toast } from 'bulma-toast'

    export default {
        name: 'EditNote',
        data() {
            return {
                note: {},
                notes: {},
                
            }
        },
        mounted() {
            this.getNote()
            this.getNotes()
            
        },
        methods: {
            async getNote() {
                this.$store.commit('setIsLoading', true)

                const noteID = this.$route.params.note_id
                
              

                const clientID = this.$route.params.id

                await axios
                    .get(`/api/v1/notes/${noteID}/?client_id=${clientID}`)
                    .then(response => {
                        this.note = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })

               
               
                this.$store.commit('setIsLoading', false)
            },

            async getNotes() {

                this.$store.commit('setIsLoading', true)

                const notesID = this.$route.params.notes_id

                const leadID = this.$route.params.id

                await axios
                    .get(`/api/v1/notess/${notesID}?lead_id=${leadID}`)
                    .then(response => {
                        this.notes = response.data

                        
                        
                    })
                    .catch(error => {
                        console.log(error)
                    })
                this.$store.commit('setIsLoading',false)

            },
            async submitForm() {
                this.$store.commit('setIsLoading', true)

                const clientID = this.$route.params.id

                // const leadID = this.$route.params.id

               

                await axios
                    .patch(`/api/v1/notes/${this.note.id}/?client_id=${clientID}`, this.note)
                    .then(response => {
                        toast({
                            message: 'The note was updated',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })

                        this.$router.push({ name: 'Client', params: { id: this.$route.params.id }})
                    })
                    .catch(error => {
                        console.log(error)
                    })
                
                // await axios
                //     .patch(`/api/v1/notess/${this.notes.id}/?lead_id=${leadID}`, this.notes)
                //     .then(response => {
                //         toast({
                //             message: 'The note was updated',
                //             type: 'is-success',
                //             dismissible: true,
                //             pauseOnHover: true,
                //             duration: 2000,
                //             position: 'bottom-right',
                //         })

                //         this.$router.push({ name: 'Lead', params: { id: this.$route.params.id }})
                //     })
                //     .catch(error => {
                //         console.log(error)
                //     })

                this.$store.commit('setIsLoading', false)
            }
        }
    }
</script>
