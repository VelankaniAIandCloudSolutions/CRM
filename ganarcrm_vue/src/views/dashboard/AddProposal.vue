<template>
  <div class="praposal-form">
    <h2>Create Proposal</h2>
    <form @submit.prevent="submitForm">
      <div class="form-group">
        <label for="name">Name:</label>
        <input type="text" id="name" v-model="name" required>
      </div>
      <div class="form-group">
        <label for="company">Company:</label>
        <input type="text" id="company" v-model="company" required>
      </div>
      <div class="form-group">
        <label for="phone">Phone:</label>
        <input type="text" id="phone" v-model="phone" required>
      </div>
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="email" required>
      </div>
      <div class="form-group">
        <label for="city">City:</label>
        <input type="text" id="city" v-model="city" required>
      </div>
      <div class="form-group">
        <label for="from_date"> Event Start Date:</label>
        <input type="date" id="from_date" v-model="from_date" required>
      </div>
      <div class="form-group">
        <label for="to_date">Event End Date:</label>
        <input type="date" id="to_date" v-model="to_date">
      </div>
      <div class="form-group">
        <button type="submit" class="btn-submit">Submit</button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'AddProposal',

  data() {
    return {
      form: {
        name: '',
        company: '',
        phone: '',
        email: '',
        city: '',
        from_date: '',
        to_date: '',
      },
    };
  },

  methods: {
    async submitForm() {

      
      this.$store.commit('setIsLoading', true);

      const praposal ={
        name:this.name,
        company:this.company,
        phone:this.phone,
        email:this.email,
        city:this.city,
        from_date:this.from_date,
        to_date:this.to_date,

      }

      try {
        const response = await axios.post('/api/v1/create_praposal/', praposal)
        const praposalId = response.data.proposal.id
        this.$router.push(`/dashboard/proposals/${praposalId}`);
      } catch (error) {
        console.log(error);
      }

      this.$store.commit('setIsLoading', false);
    },


  },
};
</script>
























<style>
.praposal-form {
  background-color: #ffffff;
  padding: 30px;
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
  max-width: 500px;
  margin: 0 auto;
}

.praposal-form h2 {
  font-size: 28px;
  margin-bottom: 20px;
  color: #333333;
  text-align: center;
}

.form-group {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.form-group label {
  flex: 0 0 30%;
  font-size: 16px;
  font-weight: bold;
  margin-right: 10px;
  color: #333333;
}

.form-group input[type="text"],
.form-group input[type="email"],
.form-group input[type="date"] {
  flex: 0 0 70%;
  width: 100%;
  padding: 12px;
  border: none;
  border-radius: 4px;
  background-color: #f5f5f5;
  transition: background-color 0.3s ease;
}

.form-group input[type="text"]:focus,
.form-group input[type="email"]:focus,
.form-group input[type="date"]:focus {
  background-color: #eaeaea;
}

.btn-submit {
  padding: 12px 24px;
  border: none;
  border-radius: 4px;
  background-color: #42b983;
  color: #ffffff;
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.btn-submit:hover {
  background-color: #36a677;
}
</style>










































































































































































































































































<!-- <template>
  <div class="proposal">
    <div class="proposal__header">
      <h1 class="proposal__title">Create Proposal</h1>
    </div>
    <div class="proposal__body">
      <form class="proposal__form" @submit.prevent="submitForm">
        <div class="proposal__items">
         

            <div class="proposal__item-body">
              <div class="proposal__item-row">
                <div class="proposal__item-col">
                  <div class="proposal__item-input">
                    <input type="text" placeholder="Enter Name" class="proposal__item-field" v-model="name">
                  </div>
                </div>

                <div class="proposal__item-col">
                  <div class="proposal__item-input">
                    <input type="text" placeholder="Enter Company" class="proposal__item-field" v-model="company">
                  </div>
                </div>
              </div>

              <div class="proposal__item-row">
                <div class="proposal__item-col">
                  <div class="proposal__item-input">
                    <input type="text" placeholder="Enter Phone Number" class="proposal__item-field" v-model="phone">
                  </div>
                </div>

                <div class="proposal__item-col">
                  <div class="proposal__item-input">
                    <input type="email" placeholder="Enter the Email" class="proposal__item-field" v-model="email">
                  </div>
                </div>

                <div class="proposal__item-col">
                  <div class="proposal__item-input">
                    <input type="text" placeholder="Enter City" class="proposal__item-field" v-model="city">
                  </div>
                </div>

                <div class="proposal__item-col">
                  <div class="proposal__item-input">
                    <label >Enter From-Date</label>
                    <input type="date" placeholder="Enter From-Date" class="proposal__item-field" v-model="from_date">
                  </div>
                </div>

                <div class="proposal__item-col">
                  <div class="proposal__item-input">
                    <label >Enter To-Date</label>
                    <input type="date" placeholder="Enter To-Date" class="proposal__item-field" v-model="to_date">
                  </div>
                </div>
              </div>
              <div v-for="(item, index) in form" :key="index" class="proposal__item">
                <div class="proposal__item-header">
                  <h2 class="proposal__item-title">Proposal On Service {{ index + 1 }}</h2>
                </div>

                  <div class="proposal__item-row">
                    <div class="proposal__item-col">
                      <div class="proposal__item-input">
                        <input type="date" placeholder="Enter Date" class="proposal__item-field" v-model="item.date">
                      </div>
                    </div>
                  </div>

                  <div class="proposal__item-row">
                    <div class="proposal__item-col">
                      <div class="proposal__item-input">
                        <label class="proposal__item-label">Start Time:</label>
                        <br><br>
                        <input type="time" placeholder="Enter Start-Time" class="proposal__item-field" v-model="item.start_time">
                      </div>
                    </div>

                    <div class="proposal__item-col">
                      <div class="proposal__item-input">
                        <label class="proposal__item-label">End Time:</label>
                        <br><br>
                        <input type="time" placeholder="Enter End-Time" class="proposal__item-field" v-model="item.end_time">
                      </div>
                    </div>
                  </div>

                  <div class="proposal__item-row">
                    <div class="proposal__item-col">
                      <div class="proposal__item-input">
                        <div class="select" style="width: 100%;">
                          <select size="events.length" v-model="item.event" required>
                            <option value="" disabled selected>Select Event Type</option>
                            <option
                              v-for="event in events"
                              :key="event.id"
                              :value="event.id"
                            >
                              {{ event.events }}
                            </option>
                          </select>
                        </div>
                      </div>
                    </div>

  

                    <div class="proposal__item-col">
                      <div class="proposal__item-input">
                        <input type="number" placeholder="Enter Min_Attendance" class="proposal__item-field" v-model="item.Min_Attendance">
                      </div>
                    </div>

                    <div class="proposal__item-col">
                      <div class="proposal__item-input">
                        <input type="number" placeholder="Enter Max_Attendance" class="proposal__item-field" v-model="item.Max_Attendance">
                      </div>
                    </div>


                    <div class="proposal__item-col">
                      <div class="proposal__item-input">
                        <div class="select" style="width: 100%;">
                          <select size="setups.length" v-model="item.setup" required>
                            <option value="" disabled selected>Select Set-Up</option>
                            <option
                              v-for="setup in setups"
                              :key="setup.id"
                              :value="setup.id"
                            >
                              {{ setup.setups }}
                            </option>
                          </select>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="proposal__item-row">
                    <div class="proposal__item-col">
                      <div class="proposal__item-input">
                        <div class="select" style="width: 100%;">
                          <select size="venues.length" v-model="item.venue" required>
                            <option value="" disabled selected>Select Venue</option>
                            <option
                              v-for="venue in venues"
                              :key="venue.id"
                              :value="venue.id"
                            >
                              {{ venue.venues }}
                            </option>
                          </select>
                        </div>
                      </div>
                    </div>
                    
                    <div class="proposal__item-col">
                      <div class="proposal__item-input">
                        <input type="number" placeholder="Enter Rate" class="proposal__item-field" v-model="item.rate">
                      </div>
                    </div>
                  </div>

                  <div class="proposal__item-col">
                    <div class="proposal__item-input">
                      <label>Select Package</label>
                      <div class="select" style="width: 100%;">
                        
                        <select size="packeges.length" v-model="item.packege" required>
                          <option value="" disabled >Select Package</option>
                          

                          <option
                            v-for=" packege in packeges"
                            :key="packege.id"
                            :value="packege.id"
                          >
                            {{ packege.packeges }}
                          </option>
                        </select>
                      </div>
                    </div>
                  </div>
                  
                  <div class="proposal__item-row">
                    <div class="proposal__item-col">
                      <div class="proposal__item-input">
                        <label class="proposal__item-label">Buffet:</label>
                        <select v-model="item.buffet" @change="buffetField(item)">

                          <option value="" disabled>Select Buffet</option>
                          <option v-for="buffet in buffets" :key="buffet.id" :value="buffet.id">{{ buffet.buffets }}</option>
                        </select>
                      </div>
                    </div>
                  </div>

                  <div class="proposal__item-row">
                    <div class="proposal__item-col">
                      <div class="proposal__item-input">
                        <select v-model="item.buffet_menus" style="height: 200px;" multiple>
                          <option v-for="menu_item in item.buffetMenus" :value="menu_item.id" :key="menu_item.id">
                            {{ menu_item.menu_items }}
                          </option>
                        </select>
                      

                       
                      </div>
                    </div>
                  </div>




              
            </div>

          

          </div>
        </div>
        
      
    
    
        <div class="buttons">
          <button type="button" class="button-addmore" @click="addRow()" style="color: black;">+ Add More</button>
          <button type="button" class="button-remove" @click="removeRow(index)" style="color: black;">X</button>
        </div>
        
  

        <div class="field">
          <div class="control">
            <div class="buttons" style="margin-left: 36%;">
              <button class="button is-success">Submit</button>
              <button class="button is-danger" @click="$router.push('/dashboard/proposals')">Cancel</button>
            </div>
          </div>
        </div>
  
      </form>
    </div>
  
  </div>

</template>







<script>
import { reactive, onMounted } from 'vue';
import axios from 'axios';

export default {
  name: 'AddProposal',

  mounted() {
    this.getEvents();
    this.getVenues();
    this.getSetups();
    this.getPackeges();
    this.getBuffets();
  },

  setup() {
    const form = reactive([
      // {
      //   date: '',
      //   start_time: '',
      //   end_time: '',
      //   event: '',
      //   venue: '',
      //   setup: '',
      //   attendance: '',
      //   rate: '',
      //   buffet: '',
      //   menu_item: '',
      //   buffetMenus: []
      // }
    ]);

    const buffets = reactive([]);
    const buffetMenus = reactive([]);

//     const getBuffetMenuName = (buffetmenuID) => {
//   const buffet_menu = buffetMenus.find((menu_item) => menu_item.id === buffetmenuID);
//   return buffet_menu ? buffet_menu.menu_items : '';
// };

// const getBuffetMenuQuantity = (buffetmenuID) => {
//   const buffet_menu = buffetMenus.find((menu) => menu.id === buffetmenuID);
//   return buffet_menu ? buffet_menu.quantity : 0;
// };

// const incrementBuffetMenuQuantity = (buffetmenuID) => {
//   const buffet_menu = buffetMenus.find((menu) => menu.id === buffetmenuID);
//   if (buffet_menu) {
//     if (!buffet_menu.quantity) {
//       buffet_menu.quantity = 0;
//     }
//     buffet_menu.quantity++;
//   }
// };

// const decrementBuffetMenuQuantity = (buffetmenuID) => {
//   const buffet_menu = buffetMenus.find((menu) => menu.id === buffetmenuID);
//   if (buffet_menu && buffet_menu.quantity > 0) {
//     buffet_menu.quantity--;
//   }
// };


    const buffetField = async (item) => {
  const selectedBuffet = buffets.find((buffet) => buffet.id === item.buffet);
  console.log('selectedBuffet:', selectedBuffet);
  if (selectedBuffet) {
    item.buffetMenus = await getBuffetMenus(selectedBuffet.id);
  } else {
    item.buffetMenus = [];
  }
};

    const getBuffets = async () => {
      try {
        const response = await axios.get('/api/v1/get_buffets/');
        console.log('buffets:', response.data);
        buffets.splice(0, buffets.length, ...response.data);
      } catch (error) {
        console.log(error);
      }
    };

    const getBuffetMenus = async (buffetID) => {
  console.log('buffetID:', buffetID);
  try {
    const response = await axios.get(`/api/v1/get_menu/?buffet_id=${buffetID}`);
    console.log('menu items response:', response.data);
    return response.data;
  } catch (error) {
    console.log(error);
    return [];
  }
};

    onMounted(async () => {
      await getBuffets();
    });

    return {
      name: '',
      phone: '',
      city: '',
      company: '',
      email: '',
      from_date: '',
      to_date: '',
      date: '',
      start_time: '',
      end_time: '',
      min_attendance: '',
      max_attendance: '',
      
      form,
      buffets,
      buffetMenus,
      // getBuffetMenuName,
      // getBuffetMenuQuantity,
      // incrementBuffetMenuQuantity,
      // decrementBuffetMenuQuantity,
      buffetField
    };
  },

  methods: {
    addRow() {
      const newRow = reactive({
        date: '',
        start_time: '',
        end_time: '',
        event: '',
        venue: '',
        setup: '',
        attendance: '',
        rate: '',
        buffet: '',
        // menu_item: '',
        buffetMenus: [],
      });
      this.form.push(newRow);
    },

    removeRow(index) {
      if (this.form.length > 1) {
        this.form.splice(index, 1);
      }
    },
     

    async submitForm() {
      this.$store.commit('setIsLoading', true);

      const proposal = {
        name: this.name,
        company: this.company,
        phone: this.phone,
        email: this.email,
        city: this.city,
        events: this.events,
        venues: this.venues,
        setups: this.setups,
        packages: this.packages,
        buffets: this.buffets,
        buffet_menus: this.buffet_menus,

        services: this.form
        // Additional form data
      };
      console.log(proposal.data)

      await axios
        .post('/api/v1/create_proposal/', proposal)
        .then((response) => {
          this.$router.push('/dashboard/proposals');
        })
        .catch((error) => {
          console.log(error);
        });
      this.$store.commit('setIsLoading', true);
    },

    async getEvents() {
      this.$store.commit('setIsLoading', true);

      await axios
        .get('/api/v1/get_events')
        .then((response) => {
          this.events = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
      this.$store.commit('setIsLoading', false);
    },

    async getVenues() {
      this.$store.commit('setIsLoading', true);

      await axios
        .get('/api/v1/get_venues')
        .then((response) => {
          this.venues = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
      this.$store.commit('setIsLoading', false);
    },

    async getSetups() {
      this.$store.commit('setIsLoading', true);

      await axios
        .get('/api/v1/get_setups')
        .then((response) => {
          this.setups = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
      this.$store.commit('setIsLoading', false);
    },

    async getPackeges() {
      this.$store.commit('setIsLoading', true);

      await axios
        .get('/api/v1/get_packages')
        .then((response) => {
          this.packeges = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
      this.$store.commit('setIsLoading', false);
    },

    async getBuffets() {
      this.$store.commit('setIsLoading', true);

      await axios
        .get('/api/v1/get_baffets')
        .then((response) => {
          this.buffets = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
      this.$store.commit('setIsLoading', false);
    },

    // async getBuffetMenus() {
    //   this.$store.commit('setIsLoading', true);

    //   this.buffetID = this.$route.params.id;

    //   await axios
    //     .get(`/api/v1/get_menus/?buffet_id=${buffetID}`)
    //     .then((response) => {
    //       this.menu_items = response.data.menu_items;
    //     })
    //     .catch((error) => {
    //       console.log(error);
    //     });
    //   this.$store.commit('setIsLoading', false);
    // },
  },
};
</script>















       

















                   
















 






<style>
/* Proposal Template CSS */

.proposal {
  background-color: #f5f5f5;
  padding: 20px;
}

.proposal__header {
  background-color: #42b983;
  padding: 20px;
  text-align: center;
}

.proposal__title {
  font-size: 24px;
  color: #ffffff;
  margin: 0;
}

.proposal__body {
  margin-top: 20px;
}

.proposal__form {
  padding: 20px;
}

.proposal__item {
  margin-bottom: 20px;
  padding: 20px;
  background-color: #ffffff;
  border: 1px solid #eaeaea;
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.proposal__item-header {
  text-align: center;
  margin-bottom: 10px;
}

.proposal__item-title {
  font-size: 20px;
  color: #333333;
  margin: 0;
}

.proposal__item-body {
  padding: 10px;
}

.proposal__item-row {
  margin-bottom: 20px;
}

.proposal__item-col {
  margin-bottom: 10px;
}

.proposal__item-input {
  margin-bottom: 10px;
}

.proposal__item-field {
  width: 100%;
  padding: 10px;
  border: 1px solid #eaeaea;
  border-radius: 4px;
  background-color: #f9f9f9;
  transition: border-color 0.3s ease;
}

.proposal__item-field:focus {
  border-color: #42b983;
}

.proposal__item-label {
  font-weight: bold;
  color: #333333;
}

.button-addmore,
.button-remove {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
  transition: background-color 0.3s ease, color 0.3s ease;
}

.button-addmore {
  background-color: #42b983;
  color: #ffffff;
}

.button-remove {
  background-color: #e74c3c;
  color: #ffffff;
}

.button-addmore:hover,
.button-remove:hover {
  background-color: #36a677;
}

.buttons {
  text-align: center;
  margin-top: 20px;
}

.button {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
  transition: background-color 0.3s ease, color 0.3s ease;
}

.button.is-success {
  background-color: #42b983;
  color: #ffffff;
}

.button.is-danger {
  background-color: #e74c3c;
  color: #ffffff;
}

.button.is-success:hover {
  background-color: #36a677;
}

.button.is-danger:hover {
  background-color: #c0392b;
}




























</style>
 -->
