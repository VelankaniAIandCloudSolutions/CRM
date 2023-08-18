<template>
  
  <div class="title">
    <label>Edit Service</label>
  </div>

  <div class="form-group">
  <label>Date:</label>
  <input type="date" id="date" v-model="updateservice.date.id">
</div>


  <div class="form-group">
    <label>Start Time</label>
    <input type="time" id="start_time" v-model="updateservice.start_time">
  </div>

  <div class="form-group">
    <label>End Time</label>
    <input type="time" id="end_time" v-model="updateservice.end_time">
  </div>

  <div class="form-group" v-if="updateservice.function !== null">
    <label for="events">Select Event:</label>
    <!-- {{ updateservice.function }} -->
    <select v-model="updateservice.function" @change="updateFunctionType">
      <option  v-for="event in events" :key="event.function" :value="event.function">
        {{ event.function }}
      </option>
    </select>
    <div class="buttons" style="margin-left:20px;">
      <button @click="clearEvent" class="button btn is-danger is-outlined" style="cursor: pointer;">Clear</button>
    </div>
  </div>

  <div class="form-group" v-else>
  <label for="events">Select Event:</label>
  <select v-model="updateservice.event" @change="eventField(updateservice)">
    <option v-for="event in events" :key="event.id" :value="event.id">
      {{ event.events }}
    </option>
  </select>
</div>


    <div class="form-group" v-if="updateservice.function_type !== null">
      <label for="event_type">Select Event Type:</label>
      <select v-model="updateservice.function_type">
        <option v-for="funcType in functionTypes" :key="funcType.function_type" :value="funcType.function_type">
          {{ funcType.function_type }}
        </option>
      </select>
    </div>

    <div class="form-group" v-else>
      <label for="event_types">Select Event Type</label>
      <select v-model="updateservice.event_type">
        <option v-for="event_type in event_types" :key="event_type.id" :value="event_type.id">
          {{ event_type.event_type }}
        </option>
      </select>
    </div>






  <div class="form-group">
    <label>Select Venue</label>
    <select v-model="updateservice.venues">
      <option v-for="venue in venues" :key="venue.id" :value="venue.id">
        <span>{{ venue.venues }}</span>
      </option>
    </select>
  </div>

  <div class="form-group">
    <label>Venue Amount :</label>
    <input type="number" id="venue_amount" v-model="updateservice.venue_amount">
  </div>

  <div class="form-group">
    <label>Miscellaneous Charges :</label>
    <input type="number" id="miscellaneous_charges" v-model="updateservice.miscellaneous_charges">
  </div>

  <div class="form-group">
    <label>Select Set_Up</label>
    <select v-model="updateservice.set_ups">
  <option v-for="set_up in set_ups" :key="set_up.id" :value="set_up.id">
    <span>{{ set_up.set_ups }}</span>
  </option>
</select>
  </div>

  <div class="form-group">
    <label>min_attendance :</label>
    <input type="number" id="min_attendance" v-model="updateservice.min_attendance">
  </div>

  <div class="form-group">
    <label>Max Attendance</label>
    <input type="number" id="max_attendance" v-model="updateservice.max_attendance">
  </div>
  
  <div class="form-group">
    <label for="currentPackage">Current Package</label>
    <input type="text" id="currentPackage" v-model="currentPackageName" readonly>
  </div>


  <div class="form-group">
      <label for="package_group">Select Package Group:</label>
      <select v-model="updateservice.package_group" @change="handlePackageGroupChange">
        <option v-for="packageGroup in packageGroups" :key="packageGroup.id" :value="packageGroup.id">
          {{ packageGroup.name }}
        </option>
      </select>
    </div>

    <!-- ... Other form inputs ... -->

    <div class="form-group">
      <label for="default_package_name">Package:</label>
      <select v-model="updateservice.default_package" @change="optionField(updateservice)">
        <option v-for="default_package in selectedPackageGroupDefaults" :key="default_package.id" :value="default_package.id">
          {{ default_package.default_package_name }}
        </option>
      </select>
    </div>


    <div class="form-group">
      <label for="option">Select Package Options:</label>
      <select v-model="updateservice.option" @change="optionField(updateservice)">
        <option v-for="option in options" :key="option.id" :value="option.id">
          {{ option.option_name }}
        </option>
      </select>
    </div>

  <div class="form-group">
    <label for="rate">Rate:</label>
    <input type="text" v-model="updateservice.option_rate">
  </div>

  <div class="form-group">
    <label for="default_item_name">Menu Items:</label>
    <div class="toolbar">
      <button type="button" class="factory factory-red" @click="onFactoryButtonClick($event)" style="margin-right:200px;">
        <i class="far fa-plus-square"></i> Add Item
      </button>

    
    </div>
  </div>
  
    <div style="width: 600px;">
      <div style="width: 600px;">
        <ag-grid-vue
          v-model="updateservice.default_item"
          style="width: 850px; height: 500px; text-align:center; margin-left:30%;"
          class="ag-theme-alpine"
          :columnDefs="columnDefs"
          :rowData="updateservice.default_item"
          :defaultColDef="defaultColDef"
          :suppressMoveWhenRowDragging="true"
          :rowDragManaged="true"
          :rowClassRules="rowClassRules"
          :frameworkComponents="frameworkComponents"
          @gridReady="onGridReady"
          @selectionChanged="onMenuItemsSelected($event.api.getSelectedRows())"
          rowSelection='multiple'
          

        ></ag-grid-vue>

      </div>
    </div>
    <br>
    <br>

    <div class="buttons" style="margin-left:38%;">

      <button class="button btn is-danger is-outlined" @click="cancelProposal"><i class="fas fa-times" style="margin-right:8px;"></i>Cancel</button>

      <button type="submit" class="button btn is-link is-outlined" @click="onSubmit" > <i class="fas fa-check " style="margin-right:8px;" ></i>Update</button>
      
    </div>
    

</template>

<script>
import { faL } from '@fortawesome/free-solid-svg-icons';
import axios from 'axios';
import { toast } from 'bulma-toast';
import { reactive, onMounted, ref, computed , watch } from 'vue';
import { AgGridVue } from 'ag-grid-vue3';
import 'ag-grid-community/styles/ag-grid.css';
import 'ag-grid-community/styles/ag-theme-alpine.css';
import '@fortawesome/fontawesome-free/css/all.css';
import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import 'vue-toastification/dist/index.css';

export default {
  name: 'EditService',
  components: {
    'ag-grid-vue': AgGridVue,
    FontAwesomeIcon,
  },
  data() {
    return {
      updateservice: {
      date: {},
      start_time: '',
      end_time: '',
      venues: '',
      venue_amount:'',
      miscellaneous_charges:'',
      set_ups: '',
      min_attendance: '',
      max_attendance: '',
      default_package: '',
      rate: '',
      package_group:'',

      default_item: [],
     
      function: null,        // Selected event ID
        function_type: null,

      
    },
    events: [],
    event_types:[], // Your events array
      functionTypes: [] ,
    currentPackageName: '',
      dates: [], 
      defaults_package: [], 
      defaults_item: [],
      packageGroups: [],
      selectedPackageGroupId: null,

      options: [],

      
        
      

      praposal: {
        from_date: '',
        to_date:'',
      },
      selectedDate: null,
      venues: [],
      set_ups: [],
      defaults_package: [],
      default_package_name: '',
      defaults_item: [],
      items: [],
      
      columnDefs: [
        { headerName: 'Menu Item', field: 'default_item_name', editable: true, checkboxSelection: true, headerCheckboxSelection: true, rowDrag: true },
        { headerName: 'Quantity', field: 'default_quantity', editable: true },
        {
          field: '',
          cellRenderer: (params) => {
            const deleteItem = () => {
              this.deleteItem(params.data);
            };

            const deleteIcon = document.createElement('div');
            deleteIcon.className = 'delete-icon';
            deleteIcon.innerHTML = '<a class="fas fa-trash"></a>';
            deleteIcon.addEventListener('click', deleteItem);

            return deleteIcon;
          },
        },
      ],
      defaultColDef: {
        flex: 1,
        minWidth: 100,
        editable: true,
        resizable: true,
      },
      rowClassRules: {
        'row-highlight': 'data.highlight',
      },
      frameworkComponents: {},
    };
  },

 
  computed: {
    selectedPackageGroupDefaults() {
      if (!this.updateservice.package_group) {
        return []; // Return an empty array when no package_group is selected
      }
      return this.defaults_package.filter(
        (pkg) => pkg.package_group.id === this.updateservice.package_group
      );
    },
  },


  mounted() {
    this.getServices();
    this.getVenues()
    this.getSet_Up()
    this.getPraposal();
    this.generateDates();
    this.getPackageGroups();
    
    this.currentPackageName = this.updateservice.default_package_name;


  },

  created() {
    this.setCurrentPackageName();
  },

  async created() {
    await this.getServices();
  },

  // 
  


  


  methods: {

    async clearEvent() {
      const confirmed = window.confirm("This will clear the data from the fields. Are you sure?");
      if (confirmed) {
        this.updateservice.function = null;
        this.updateservice.function_type = null;
        this.events = [];
        this.functionTypes = [];

        // Fetch events and event types again after clearing
        await this.getEvents();
      }
    },

    async getEvents() {
      try {
        const response = await axios.get('/api/v1/get_events/');
        this.events = response.data;
        await this.eventField(this.updateservice); 
      } catch (error) {
        console.log(error);
      }
    },

    async eventField(updateservice) {
    const selectedEvent = this.events.find((e) => e.id === updateservice.event);
    if (selectedEvent) {
      await this.getEvent_Types(selectedEvent.id);
      updateservice.event_type = null;
    } else {
      this.event_types.splice(0);
      updateservice.event_type = null;
    }
  },


  async getEvent_Types(eventId) {
    try {
      const response = await axios.get(`/api/v1/get_event_types/${eventId}`);
      this.event_types = response.data;
    } catch (error) {
      console.log(error);
    }
  },

  async getPackageGroups() {
  try {
    const response = await axios.get('/api/v1/get_package_groups/');
    console.log("Package Groups API Response:", response.data);

    this.packageGroups = response.data; // Make sure response.data is the correct data structure

    // ... rest of your code ...
  } catch (error) {
    console.log("Error fetching package groups:", error);
  }
},

async handlePackageGroupChange() {
      const selectedGroup = this.packageGroups.find(group => group.id === this.updateservice.package_group);
      if (selectedGroup) {
        const confirmation = window.confirm('Changing the package group will reset the selected package and options. Do you want to continue?');
        if (confirmation) {
          this.updateservice.default_package = null;
          // Fetch default packages and other related data based on the new package group
          await this.getDefaults_Package();
          // ... Other relevant function calls ...
        } else {
          // Revert the selected package group if user cancels
          this.updateservice.package_group = this.selectedPackageGroupId;
        }
      }
    },

    async getDefaults_Package() {
    try {
      const packageGroupId = this.updateservice.package_group;

      if (packageGroupId !== null) {
        const response = await axios.get(`/api/v1/get_defaults_package/?package_group_id=${packageGroupId}`);
        this.defaults_package.splice(0, this.defaults_package.length, ...response.data);
      } else {
        console.log("Selected Package Group ID is null.");
      }
    } catch (error) {
      console.log(error);
    }
  },
  async optionField(item) {
  const selectedDefaultPackage = this.defaults_package.find(pkg => pkg.id === item.default_package);
  if (selectedDefaultPackage) {
    const packageOptions = await this.getOptions(selectedDefaultPackage.id);
    this.options.splice(0, this.options.length, ...packageOptions);

    const selectedOption = packageOptions.find(option => option.id === item.option);
    if (selectedOption) {
      item.option_rate = selectedOption.option_rate;

      // Fetch menu items based on the selected option
      await this.getDefaults_Item(selectedOption.id);
    } else {
      item.option_rate = null;
    }
  } else {
    this.options.length = 0;
    this.defaults_item.length = 0;
  }

  console.log("Options after updating:", this.options);
},


  async getOptions(default_packageID) {
    try {
      const response = await axios.get(`/api/v1/get_options/?default_package_id=${default_packageID}`);
      console.log("Options Fetched Successfully:", response.data);
      return response.data;
    } catch (error) {
      console.log("Error Fetching Options:", error);
      return [];
    }
  },
  async getDefaults_Item(optionID) {
      try {
        const response = await axios.get(`/api/v1/get_default_items/?option_id=${optionID}`);
        this.updateservice.default_item = [...response.data]; // Update the array in a reactive way
      } catch (error) {
        console.log(error);
      }
    },


    










    cancelProposal() {
  if (confirm("Are you sure you want to cancel?")) {
    this.$router.push(`/dashboard/proposals/${this.$route.params.praposal_id}`);
  }
},






    
      checkPackageSelection() {
        if (!this.updateservice.default_package) {
          alert(" If You are Changing The Package, Then This will erase the previous package and its menu items data.");
        }
      },

    setCurrentPackageName() {
      const defaultPackageId = this.updateservice.default_package;
      if (defaultPackageId) {
        const selectedPackage = this.defaults_package.find(pkg => pkg.id === defaultPackageId);
        if (selectedPackage) {
          this.currentPackageName = selectedPackage.package_name;
        }
      }
    },


   



    onMenuItemsSelected(selectedItems) {
    if (this.item && Array.isArray(this.item.default_item)) {
      const selectedPackage = this.defaults_package.find(
        (pkg) => pkg.id === this.item.default_package
      );

      if (selectedPackage) {
        const menuItems = selectedPackage.default_item.map((itemId) =>
          this.default_item.find((item) => item.id === itemId)
        );
        this.item.default_item = menuItems;
      } else {
        this.item.default_item = [];
      }
    } else {
      this.item = {
        default_item: [] 
      };
    }
  },



  deleteItem(data) {
    console.log('Delete item:', data);
    
    const index = this.defaults_item.findIndex(item => item.default_item_name === data.default_item_name);
    console.log('Item index:', index);
    
    if (index !== -1) {
      this.defaults_item.splice(index, 1);
      console.log('Item deleted:', data.default_item_name);

      // Update the grid to reflect the changes
      this.gridApi.setRowData(this.defaults_item);
    }

    
  },

 
  


  onGridReady(params) {
    this.gridApi = params.api;
    
    this.columnApi = params.columnApi;
  },

  onFactoryButtonClick(e) {
    const button = e.currentTarget;
    const buttonColor = button.getAttribute('');
    const side = button.getAttribute('');
    const newItem = {
      default_item_name: buttonColor,
      // default_quantity: 1, 
    };

    // Add the new item to the defaults_item array
    this.defaults_item.push(newItem);

    // Update the grid to reflect the changes
    this.gridApi.setRowData(this.defaults_item);
  },



    async getPraposal() {

      await axios
        .get('/api/v1/get_proposalss')
        .then((response) => {
          this.praposal.from_date = { date: response.data.from_date };
          this.praposal.to_date = { date: response.data.to_date };

          
        })
        .catch((error) => {
          console.log(error);
        });
    },
    generateDates() {
      const from_date = new Date(this.praposal.from_date.date);
      const to_date = new Date(this.praposal.to_date.date);


        const dates = [];

        while (from_date <= to_date) {
          const formattedDate = from_date.toISOString().split('T')[0];
          dates.push({ id: formattedDate });
          from_date.setDate(from_date.getDate() + 1);
        }

        this.updateservice.dates = dates; // Assign the dates array to updateservice.dates
    },


   

    async getServices() {
  this.$store.commit('setIsLoading', true);

  const serviceId = this.$route.params.id;

  try {
    const response = await axios.get(`/api/v1/get_service/${serviceId}`);
    const serviceData = response.data;

    console.log("Service Data:", serviceData);

    this.events = serviceData.function_serializer;
    this.functionTypes = serviceData.function_type_serializer;

    this.updateservice = {
      ...this.updateservice,
      date: { id: serviceData.serializer.date },
      start_time: serviceData.serializer.start_time,
      end_time: serviceData.serializer.end_time,
      venues: serviceData.serializer.venues.id,
      venue_amount: serviceData.serializer.venue_amount,
      miscellaneous_charges: serviceData.serializer.miscellaneous_charges,
      set_ups: serviceData.serializer.set_ups.id,
      min_attendance: serviceData.serializer.min_attendance,
      max_attendance: serviceData.serializer.max_attendance,
      default_package: serviceData.serializer.default_package,
      rate: serviceData.serializer.rate,
      default_item: serviceData.serializer.default_item,
      function: serviceData.function_serializer[0].function,
      function_type: serviceData.function_type_serializer[0].function_type,
      package_group: serviceData.serializer.package_group.id // Included package_group
    };
    console.log("Update Service Data:", this.updateservice);

    if (serviceData.package_serializer.length > 0) {
      this.currentPackageName = serviceData.package_serializer[0].package_name;
    }

    this.getPraposal();
    this.generateDates();
  } catch (error) {
    console.log("Error:", error);
  }

  this.$store.commit('setIsLoading', false);
},


    // async getEvents() {
    //   try {
    //     const response = await axios.get('/api/v1/get_events/');
    //     this.events = response.data;
    //   } catch (error) {
    //     console.log(error);
    //   }
    // },
    // updateFunctionType() {
    //   if (this.selectedEventData) {
    //     this.selectedEventType = this.selectedFunctionTypeData ? this.selectedFunctionTypeData.function_type : '';
    //   } else {
    //     this.selectedEventType = '';
    //   }
    // },
  







    async getVenues() {
    
    this.$store.commit('setIsLoading', true)

    await axios
      .get('/api/v1/get_venues')
      .then(response => {
        this.venues = response.data
      })
      .catch(error => {
        console.log(error)
      })
    this.$store.commit('setIsLoading', false)
  },

  async getSet_Up() {
    
    this.$store.commit('setIsLoading', true)

    await axios
      .get('/api/v1/get_setup')
      .then(response => {
        this.set_ups = response.data
      })
      .catch(error => {
        console.log(error)
      })
    
    this.$store.commit('setIsLoading', false)
  },

  



  async onSubmit() {

    this.$store.commit('setIsLoading', true)

    const serviceId = this.$route.params.id
   
    await axios
      .post(`/api/v1/update_service/${serviceId}/`, this.updateservice)
      .then(response => {
        
        toast({
          message: 'Service updated successfully',
          type: 'is-success',
          position: 'top-right',
        });

        console.log('Data Sent to API:', this.updateservice);

        this.$router.push(`/dashboard/proposals/${this.$route.params.praposal_id}`);

      })
      .catch(error => {
        
        toast({
          message: 'Failed to update service',
          type: 'is-danger',
          position: 'top-right',
        });
        console.log(error);
      });

    this.$store.commit('setIsLoading', false)
  },

  
    
  },
};
</script>





















<!-- setup() {
  //   const defaults_package = reactive([]);
  //   const defaults_item = reactive([]);
  //   const default_package_name = ref('');
  //   const default_item_name = [];

  //   const form = reactive([
  //   {
  //     date: '',
  //     start_time: '',
  //     end_time: '',
  //     venues: '',
  //     set_ups: '',
  //     package_group: '',
  //     default_package: '',
  //     option: '',
  //     rate: '',
  //     audio_visuals: '',
  //     default_item: [],
  //     min_attendance: '',
  //     max_attendance: '',
  //     event: '',
  //     event_type: '',
  //   },
  // ]);

  //   const default_packageField = async (item) => {
  //     if (item.default_package) {
       
  //       alert("Selecting a new package will erase the previous package and its menu items data.");
  //     }

  //     const selectedDefaultPackage = defaults_package.find((default_package) => default_package.id === item.default_package);
  //     if (selectedDefaultPackage) {
  //       await getDefaults_Item(selectedDefaultPackage.id);
  //       item.default_item = [...defaults_item];
  //     } else {
  //       defaults_item.splice(0);
  //       item.default_item = [];
  //     }
  //   };



  //   const default_itemField = (item) => {
  //     item.default_item = item.default_item.map((default_item) => default_item.id);
  //   };

  //   const getDefaults_Package = async () => {
  //     try {
  //       const response = await axios.get('/api/v1/get_defaults_package/');
  //       defaults_package.splice(0, defaults_package.length, ...response.data);
  //     } catch (error) {
  //       console.log(error);
  //     }
  //   };

  //   const getDefaults_Item = async (default_packageID) => {
  //     try {
  //       const response = await axios.get(`/api/v1/get_default_items/?default_package_id=${default_packageID}`);
  //       defaults_item.splice(0);
  //       defaults_item.push(...response.data);
  //     } catch (error) {
  //       console.log(error);
  //     }
  //   };

  //    //  code for Event Dependent Drop down  

  //    const eventField = async (item) => {
  //       const selectedEvent = events.value.find((e) => e.id === item.event);
  //       if (selectedEvent) {
  //         await getEvent_Types(selectedEvent.id);
  //         item.event_type = null; 
  //       } else {
  //         event_types.value.splice(0); 
  //         item.event_type = null; 
  //       }
  //     };





  //   const getEvents = async () => {
  //     try {
  //       const response = await axios.get('/api/v1/get_events/');
  //       events.value = response.data; // Set the data to the events array using Vue's reactivity
  //     } catch (error) {
  //       console.log(error);
  //     }
  //   };
  //   const event_typeField = (item) => {
  //       item.event_type = item.event_type.map((event_type) => event_type.id);
  //     };

  //     const getEvent_Types = async (eventId) => {
  //       try {
  //         const response = await axios.get(`/api/v1/get_event_types/${eventId}`);
  //         event_types.value = response.data; 
  //       } catch (error) {
  //         console.log(error);
  //       }
  //     };

  //   watch(() => form[0].default_package, async (newVal, oldVal) => {
  //     if (newVal !== oldVal) {
  //       await getOptions(newVal);
  //     }
  //   });

  //   watch(defaults_item, (newValue) => {
  //     if (gridApi.value) {
  //       gridApi.value.setRowData(newValue);
  //     }
  //   });
  // //   watch(options, (newOptions) => {
  // //   console.log("Options after updating:", newOptions);
  // // });
  // // watch(() => form[0].option, (newValue) => {
  // //   console.log("Form[0].option:", newValue);
  // // });


  //   onMounted(async () => {
  //   await Promise.all([getPackageGroups(), getDefaults_Package(), getEvents()]);
  //   console.log("Form Option:", form[0].option); // Add this line
  //   // optionField(form[0]); // Call optionField to fetch the options for the initially selected default_package
  // });

    

    

  //   return {
  //     defaults_package,
  //     default_itemField,
  //     default_packageField,
  //     default_package_name,
  //     defaults_item,
  //     default_item_name,
  //   };
  // }, -->
