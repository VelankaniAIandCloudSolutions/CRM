<template>
    <div class="container">
      <h1 class="title">Edit Accommodation</h1>
      <br>
      <br>
  
      <div class="form-group">
        <label for="check_in_date">Check In date:</label>
        <input type="date" id="check_in_date" v-model="updatebooking.check_in_date">
      </div>
  
      <div class="form-group">
        <label for="check_out_date">Check Out Date:</label>
        <input type="date" id="check_out_date" v-model="updatebooking.check_out_date">
      </div>
  
      <div class="form-group">
        <label for="room_types">Select Room Type:</label>
        <select id="room_types" v-model="updatebooking.room_types">
          <option v-for="room_type in room_types" :key="room_type.id" :value="room_type">
            {{ room_type.room_types }}
          </option>
        </select>
      </div>
  
      <div class="form-group">
        <label for="number_of_rooms">Enter Number Of Rooms:</label>
        <input type="number" id="number_of_rooms" v-model="updatebooking.number_of_rooms">
      </div>
  
      <div class="form-group">
        <label for="occupancy">Occupancy:</label>
        <input type="text" id="occupancy" v-model="updatebooking.occupancy">
      </div>
      <br>
      <br>
  
      <div class="buttons">
        <button class="button is-danger is-outlined" style="width:10%;" @click="cancelBooking">
          <span class="icon">
            <i class="fas fa-times" style="margin-right:30px;"></i>
          </span>
          Cancel
        </button>
  
        <button type="submit" class="button is-link is-outlined" style="width:10%;" @click="onSubmit">
          <span class="icon">
            <i class="fas fa-check " style="margin-right:30px;" ></i>
          </span>
          Update
        </button>
      </div>
    </div>
  </template>
  


<script>
   import axios from 'axios';
    import { toast } from 'bulma-toast';
    import { reactive, onMounted, ref } from 'vue';

    export default {
        name: 'EditAccomadation',

        data() {
            return {
                updatebooking: {
                    check_in_date: '',
                    check_out_date: '',
                    room_types: '',
                    number_of_rooms: '',
                    occupancy: '',
                },
                room_types: [], 
            };
        },

        mounted() {
            this.getBookings();
            // this.getServices();
            this.getRoom_types();

        },

        methods: {

            cancelBooking() {
                if (confirm("Are you sure you want to cancel?")) {
                    const serviceId = this.$route.params.service_id;
                    this.$router.push(`/dashboard/proposals/${serviceId}`);
                }
            },



            async getBookings() {
            this.$store.commit('setIsLoading', true);
            const bookingID = this.$route.params.id;

            try {
                const response = await axios.get(`/api/v1/get_booking/${bookingID}`);
                const bookingData = response.data;

                this.updatebooking = {
                check_in_date: bookingData.check_in_date,
                check_out_date: bookingData.check_out_date,
                room_types: bookingData.room_types,
                number_of_rooms: bookingData.number_of_rooms,
                occupancy: bookingData.occupancy,
                };

                this.getRoom_types();
            } catch (error) {
                console.log(error);
            }

            this.$store.commit('setIsLoading', false);
            },


            async getRoom_types() {

                this.$store.commit('setIsLoading', true)

                await axios
                .get('/api/v1/get_room_types')
                .then(response => {
                    this.room_types = response.data
                })
                .catch(error => {
                    console.log(error)
                })

                this.$store.commit('setIsLoading', false)
            },


            async onSubmit() {
               
                const bookingID = this.$route.params.id;

                try {
                
                const response = await axios.put(`/api/v1/update_booking/${bookingID}/`, this.updatebooking);

               
                console.log(response.data);
                toast({
                    message: 'Booking updated successfully',
                    type: 'is-success',
                });

               
                this.$router.push(`/dashboard/proposals/${this.$route.params.service_id}`);
                } catch (error) {
                console.log(error);
               
                toast({
                    message: 'Failed to update booking',
                    type: 'is-danger',
                });
                }
            },







           
            
        }
    }
</script>