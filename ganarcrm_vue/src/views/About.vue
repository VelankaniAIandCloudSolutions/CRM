<template>
  <div class="about">
    <h1>This is an about page</h1>
  </div>
</template>






<template>
  <div class="container">
    <div class="title">Proposal Details</div>
    <div class="content">
      <table class="table is-fullwidth">
        <tbody>
          <tr>
            <td>Name:</td>
            <td>{{ praposal.name }}</td>
          </tr>
          <tr>
            <td>Company:</td>
            <td>{{ praposal.company }}</td>
          </tr>
          <tr>
            <td>Phone:</td>
            <td>{{ praposal.phone }}</td>
          </tr>
          <tr>
            <td>Email:</td>
            <td>{{ praposal.email }}</td>
          </tr>
          <tr>
            <td>City:</td>
            <td>{{ praposal.city }}</td>
          </tr>
          <tr>
            <td>From Date:</td>
            <td>{{ praposal.from_date }}</td>
          </tr>
          <tr>
            <td>TO Date:</td>
            <td>{{ praposal.to_date }}</td>
          </tr>
        </tbody>
      </table>
    </div>



    <div class="container">
      <div class="tabs" style="margin-right: 8%; ">
        <ul>
          <li :class="{ 'is-active': activeTab === 'service' }">
            <a @click="activeTab = 'service'"> + Add Service</a>
          </li>
          <li :class="{ 'is-active': activeTab === 'accommodation' }">
            <a @click="activeTab = 'accommodation'"> + Add Accommodation</a>
          </li>
          <li :class="{ 'is-active': avtiveTab === 'deposite' }">
            <a @click="activeTab = 'deposite'"> + Deposite Schedule</a>
          </li>
          <li :class="{ 'is-active':activeTab === 'forma_invoice' }">
            <a @click="activeTab = 'forma_invoice'"> + Pro Forma Invoice</a>
          </li>
        </ul>
      </div>

      <div v-if="activeTab === 'service'">

        <div class="box">
          <!-- <div class="form-group">
            <label for="applySameService">Apply Same Service for All Dates</label>
            <input type="checkbox" id="applySameService" v-model="applySameService">
          </div> -->

      
          <form @submit.prevent="submitServiceForm">
            <div class="box-body">
              <div v-for="(item,index) in form" :key="index">
                <div class="title">service :  {{ index+1 }}</div>
                <br>
                <br>
                <!-- <div class="form-group">
                  <label for="date">Date:</label>
                  <div class="field" style="width: 500%;">
                    <div class="select" style="width: 500%;">
                      <select size="date.length" v-model="item.date">
                        <option v-for="service in services" :key="service.id" :value="service.date">
                          {{ service.date }}
                        </option>
                      </select>
                    </div>
                  </div>
                </div> -->


                <div class="form-group">
                  <label for="date">Date:</label>
                  <div class="field" style="width:100%;">
                    <!-- <div class="select"> -->
                      <select v-model="item.date" >
                        <option  v-for="date in dates" :key="date" :value="date">{{ date }}</option>
                      </select>
                    <!-- </div> -->
                  </div>
                </div>

                <div class="form-group">
                  <label for="start_time">Start Time:</label>
                  <input type="time" id="start_time" v-model="item.start_time">
                </div>

                <div class="form-group">
                  <label for="end_time">End Time:</label>
                  <input type="time" id="end_time" v-model="item.end_time" />
                </div>

                <div class="form-group">
                  <label for="venus">Select Venue</label>
                  <!-- <div class="select" style="width:600px;"> -->
                    <select v-model="item.venues">
                      <option v-for="venue in venues" :key="venue.id" :value="venue.id">
                      <span> {{ venue.venues }}</span>
                      </option>
                    </select>
                  <!-- </div>    -->
                </div>

                <div class="form-group">
                  <label for="rate">Venue Amount :</label>
                  <input type="number" id="venue_amount" v-model="item.venue_amount">
                </div>

                <div class="form-group" v-if="index === 0">
                  <label for="rate"> Miscellaneous Charges :</label>
                  <input type="number" id="miscellaneous_charges" v-model="item.miscellaneous_charges">
                </div>

                <div class="form-group">
                  <label for="set_up">Select Set-Up :</label>
                  <!-- <div class="select"> -->
                    <select v-model="item.set_ups">
                      <option v-for="set_up in set_ups" :key="set_up.id" :value="set_up.id">
                        <span> {{ set_up.set_ups }}</span>
                      </option>
                    </select>
                  <!-- </div>  -->
                </div>

                <div class="form-group">
                  <label for="end_time">Min_Attendance :</label>
                  <input type="number" id="min_attendance" v-model="item.min_attendance" />
                </div>

                <div class="form-group">
                  <label for="end_time">Max_Attendance:</label>
                  <input type="number" id="max_attendance" v-model="item.max_attendance" />
                </div>

                <div class="form-group">
                  <label for="package_group">Select Package Group:</label>
                  <select v-model="item.package_group" @change="default_packageField(item)">
                    <option v-for="packageGroup in packageGroups" :key="packageGroup.id" :value="packageGroup.id">
                      {{ packageGroup.name }}
                    </option>
                  </select>
                </div>

                <div class="form-group">
                  <label for="default_package_name">Package:</label>
                  <select v-model="item.default_package" @change="default_itemField(item)">
                    <option v-for="default_package in selectedPackageGroupDefaults" :key="default_package.id" :value="default_package.id">
                      <span>{{ default_package.default_package_name }}</span>
                    </option>
                  </select>
                </div>


                <div class="form-group">
                  <label for="rate">Rate :</label>
                  <input type="text" id="rate" v-model="item.rate">
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
                        v-model="item.default_item"
                        style="width: 850px; height: 500px; text-align:center;"
                        class="ag-theme-alpine"
                         :rowData="defaults_item"
  :columnDefs="columnDefs"
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
                

              
                <div class="buttons">
                  <button type="button" class="button btn is-success is-outlined " @click="addRow()"  style="width:50%;">+ Add More</button>
                  <button type="button" class="button btn is-danger is-outlined"  style="width:48%;" @click="removeRow(index)">X</button>
                  
                </div>

                <br>
                <br>
                <br>
                <br>
                <br>

              
              </div>
            </div>
            <button class="button is-link is-outlined" style="width: 100%;">Submit</button>
          </form>
        </div>

      </div>
    </div>


    <div v-if="activeTab === 'accommodation'">
      <div class="box">
        <form @submit.prevent="submitAccommodationForm">

          <div class="box-body">

            <div class="form-group">
              <label for="check_in_date">Enter Check In Date :</label>
              <input type="date" id="check_in_date" placeholder="Enter Check In Date " v-model="check_in_date">
            </div>

            <div class="form-group">
              <label for="check_out_date"> Enter Check Out Date : </label>
              <input type="date" id="check_out_date" placeholder="Enter The Check Out Date" v-model="check_out_date">
            </div>

            <div class="form-group">
              <label for="room_types">Select Room Type :</label>
              <!-- <div class="select" style="width:600px;"> -->
                <select v-model="room_types" >
                  <option v-for="room_type in room_types" :key="room_type.id" :value="room_type.id">
                  <span> {{ room_type.room_types }}</span>
                  </option>
                </select>
              <!-- </div> -->
            </div>

            <div class="form-group">
              <label for="number_of_rooms">Enter Number Of Rooms :</label>
              <input type="number" id="number_of_rooms" v-model="number_of_rooms" />
            </div>

            <div class="form-group">
              <label for="occupency">Enter Occupancy :</label>
              <input type="text" id="occupancy" v-model="occupancy" />
            </div>

            <div class="form-group">
              <label>Rate :</label>
              <input type="number" id="rate" v-model="rate">
            </div>



          </div>

          <button class="button is-success is-outlined">Submit</button>

        </form>

      </div>   
    </div>


    <div v-if="activeTab === 'deposite'">

      <div class="box">
        <form @submit.prevent="submitDepositeForm">

          <div class="box-body">

            <div class="title">
              <label>DEPOSIT SCHEDULE</label>
            </div>

            <div class="form-group">
                  
              <div class="toolbar">
                <button type="button" class="factory" @click="onFactoryButton($event)" style="margin-right:200px;">
                  <i class="far fa-plus-square"></i> Add Row
                </button>

              
              </div>
            </div>
                
            <div style="width: 600px;">
              <div style="width: 600px;">
                <ag-grid-vue
                  v-model="deposite"
                  style="width: 850px; height: 500px; text-align: center;"
                  class="ag-theme-alpine"
                  :columnDefs="columnDefss"
                  :rowData="deposite"
                  :defaultColDef="defaultColDef"
                  :suppressMoveWhenRowDragging="true"
                  :rowDragManaged="true"
                  :rowClassRules="rowClassRules"
                  :frameworkComponents="frameworkComponents"
                  @gridReady="onGridReady"
                  @selectionChanged="onMenuItemsSelected($event.api.getSelectedRows())"
                  rowSelection="multiple"
                  :stopEditingWhenGridLosesFocus="true"
                  :modules="modules"
                  @firstDataRendered="onFirstDataRendered"
                >
                  <!-- Add the custom cell renderer for 'scheduled_date' column -->
                  <ag-date-picker
                    v-if="frameworkComponents.DateInputCellRenderer"
                    :value="params.value"
                    @input="onDateInput(date)"
                  ></ag-date-picker>
                </ag-grid-vue>




              </div>
            </div>
          </div>
          <br>
          <button class="button is-link is-outlined">Submit</button>
        </form>
        <br>
        <br>
      </div>
    </div>

    <div v-if="activeTab === 'forma_invoice'">

      <div class="box">




        <form @submit.prevent="submitFormaInvoiceForm">
    <table class="table is-fullwidth">
      <thead>
        <tr>
          <th>Item</th>
          <th>Date</th>
          <th>Qty</th>
          <th>Rate</th>
          <th>Amount</th>
          <th>CGST Percentage (%)</th>
          <th>CGST Amount</th>
          <th>SGST Percentage (%)</th>
          <th>SGST Amount</th>
          <th>Total</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="praposal_invoice in praposal_invoices" :key="praposal_invoice.id">
          <td>{{ praposal_invoice.item }}</td>
          <td>{{ praposal_invoice.date }}</td>
          <td>{{ praposal_invoice.qty }}</td>
          <td>{{ praposal_invoice.rate }}</td>
          <td>{{ praposal_invoice.amount }}</td>
          <td>{{ praposal_invoice.cgst_percentage }}</td>
          <td>{{ calculateCgstAmount(praposal_invoice.amount, praposal_invoice.cgst_percentage) }}</td>
          <td>{{ praposal_invoice.sgst_percentage }}</td>
          <td>{{ calculateSgstAmount(praposal_invoice.amount, praposal_invoice.sgst_percentage) }}</td>
          <td>{{ calculateTotal(praposal_invoice.amount, praposal_invoice.cgst_percentage, praposal_invoice.sgst_percentage) }}</td>
        </tr>
        <tr v-for="booking in bookings" :key="booking.id">
          <td colspan="1">Accommodation Charges</td>
          <td>{{ booking.check_in_date }} to {{ booking.check_out_date }}</td>
          <td>{{ booking.number_of_rooms }}</td>
          <td>{{ booking.rate }}</td>
          <td>{{ booking.amount }}</td>
          <td>9%</td>
          <td>{{ calculateCgstAmount(booking.amount, 9) }}</td>
          <td>9%</td>
          <td>{{ calculateSgstAmount(booking.amount, 9) }}</td>
          <td>{{ calculateTotal(booking.amount, 9, 9) }}</td>
        </tr>
        <br>
      </tbody>
      <tfoot>
      <tr>
        <td colspan="9">Grand Total:</td>
        <td>{{ calculateGrandTotal() }}</td>
      </tr>
    </tfoot>
    </table>
    <br>
    <button class="button is-link is-outlined">Submit</button>
  </form>

        
      





      </div>
    </div>
         
  </div>
</template>




<!-- //   setup() {
  //     // const form = reactive([]);
  //     const defaults_package = reactive([]);
  //     const defaults_item = reactive([]);
  //     const default_package_name = ref('');
  //     const default_item_name = [];
  //     const packageGroups = reactive([]);
  //     const selectedPackageGroupId = ref(null);
  //     const gridApi = ref(null); 
  //     const options = reactive([]);
  //     const option_name = ref('');  
      
  //     const events = ref([]); // Initialize events array
  //   const event_types = ref([]);
  
  
  //     const deleteItemRenderer = {
  //       template: `
  //         <div class="delete-icon" @click="deleteItem(params.data)">
  //           <i class="fas fa-trash"></i>
  //         </div>
  //       `,
  //       methods: {
  //         deleteItem(data) {
  //           this.$emit('delete-item', data);
  //         },
  //       },
  //     };
  
  //     const form = reactive([
  //       {
  //         date: '',
  //       start_time: '',
  //       end_time: '',
  //       venues: '',
  //       set_ups: '',
  //       package_group: '', // Change 'package' to 'package_group'
  //       default_package: '',
  //       option:'',
  //       rate: '',
  //       default_item: [],
  //       min_attendance: '',
  //       max_attendance: '',
  //       event: null, // Set the initial value for event as null
  //     event_type: null,
  //       },
  //     ]);
  
  //     const addRow = () => {
  //       const newRow = {
  //         date: '',
  //         start_time: '',
  //         end_time: '',
  //         venues: '',
  //         set_ups: '',
  //         package_group:'',
  //         default_package: '',
  //         rate: '',
  //         default_item: [],
  //         min_attendance: '',
  //         max_attendance: '',
  //       };
  
  //       form.push(newRow);
  //     };
  
  //     const removeRow = (index) => {
  //         if(form.length > 1){
  //             form.splice(index,1)
  //         }
          
  //     }
  
  //     const selectedPackageGroupDefaults = computed(() => {
  //       const packageGroupId = selectedPackageGroupId.value;
  //       return defaults_package.filter((pkg) => pkg.package_group.id === packageGroupId);
  //     });
  
  //     // const default_packageField = async (item) => {
  //     //   selectedPackageGroupId.value = item.package_group;
  //     //   const selectedDefaultPackage = defaults_package.find((default_package) => default_package.id === item.default_package);
  //     //   if (item.package_group) {
  //     //     await getDefaults_Package();
  
         
  //     //   }
  //     //   if (selectedDefaultPackage) {
  //     //     await getDefaults_Item(selectedDefaultPackage.id);
  //     //     // Update the default_item property bound to ag-grid
  //     //     item.default_item = [...defaults_item];
  //     //   } else {
  //     //     defaults_item.splice(0);
  //     //     // Clear the default_item property s
  //     //     item.default_item = [];
  //     //   }
  //     // };
  
  //     const default_packageField = async (item) => {
  //   selectedPackageGroupId.value = item.package_group;
  //   const selectedDefaultPackage = defaults_package.find((default_package) => default_package.id === item.default_package);
  
  //   if (item.package_group) {
  //     await getDefaults_Package();
  
  //     if (selectedDefaultPackage) {
  //       await getOptions(selectedDefaultPackage.id);
  //     } else {
  //       options.splice(0);
  //     }
  //   }
  // };
  
  
  
  //   const getPackageGroups = async () => {
  //   try {
  //     const response = await axios.get('/api/v1/get_package_groups/');
  //     packageGroups.splice(0, packageGroups.length, ...response.data);
  //   } catch (error) {
  //     console.log(error);
  //   }
  // };
  
  //   const getDefaults_Package = async () => {
  //     try {
  //       const packageGroupId = selectedPackageGroupId.value; // Use the stored value
  
  //       if (packageGroupId !== null) {
  //         const response = await axios.get(`/api/v1/get_defaults_package/?package_group_id=${packageGroupId}`);
  //         defaults_package.splice(0, defaults_package.length, ...response.data);
  //       } else {
  //         console.log("Selected Package Group ID is null.");
  //       }
  //     } catch (error) {
  //       console.log(error);
  //     }
  //   };
  
  //   const optionField = async (item) => {
  //   const selectedOption = options.find((option) => option.id === item.option);
  //   if (selectedOption) {
  //     await getDefaults_Item(selectedOption.id);
  //     // Update the default_item property bound to ag-grid
  //     item.default_item = [...defaults_item];
  //   } else {
  //     defaults_item.splice(0);
  //     // Clear the default_item property
  //     item.default_item = [];
  //   }
  // };
  
  
  
  //   const getOptions = async (default_packageID) => {
  //       try {
  //         const response = await axios.get(`/api/v1/get_options/?default_package_id=${default_packageID}`);
  //         options.splice(0);
  //         options.push(...response.data);
  //       } catch (error) {
  //         console.log(error);
  //       }
  //     };
  
  
  
  
    
  
  //   const default_itemField = (item) => {
  //       item.default_item = item.default_item.map((default_item) => default_item.id);
  //     };
  
  //    // Define the function to fetch default items based on default_package_id
  //    const getDefaults_Item = async (optionID) => {
  //       try {
  //         const response = await axios.get(`/api/v1/get_default_items/?option_id=${optionID}`);
  //         defaults_item.splice(0);
  //         defaults_item.push(...response.data);
  //       } catch (error) {
  //         console.log(error);
  //       }
  //     };
  
  
  //   //  code for Event Dependent Drop down  
  
  //     const eventField = async (item) => {
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
  
  //   // watch(selectedPackageGroupId, async (newVal) => {
  //   //   if (newVal !== null) {
  //   //     await getDefaults_Package();
  //   //   }
  //   // });
  
  //   watch(() => form[0].default_package, async (newVal) => {
  //     if (newVal !== '') {
  //       await getDefaults_Item(newVal);
  //     }
  //   });
  //   watch(defaults_item, (newValue) => {
  //       // Make sure gridApi is set before updating the grid
  //       if (gridApi.value) {
  //         gridApi.value.setRowData(newValue);
  //       }
  //     });
  
  
  //     onMounted(async () => {
  //   await Promise.all([getPackageGroups(), getDefaults_Package(), getEvents()]);
  // });
  
  
  
  //   return {
  //     form,
  //     defaults_package,
  //     default_itemField,
  //     default_packageField,
  //     default_package_name,
  //     defaults_item,
  //     default_item_name,
  //     addRow,
  //     removeRow,
  //     packageGroups,
  //     selectedPackageGroupDefaults,
  //     gridApi,
  //     eventField,
  //     event_typeField,
  //     events,
  //     event_types,
  //     optionField,
      
  //   };
  // }, -->



<!-- 
// {
  //   headerName: 'Scheduled Date',
  //   field: 'scheduled_date',
  //   editable: true,
  //   cellRendererFramework: 'DateInputCellRenderer',
  // },
  // {
  //   headerName: 'Scheduled Date',
  //   field: 'scheduled_date',
  //   cellRenderer: (params) => {

  //     const dateIcon = document.createElement('input');
  //     dateIcon.type = 'date';
  //     console.log('render')
  //     function handleDateChange(event) {
  //     const selectedDate = event.target.value;
  //       console.log('Selected date:', selectedDate);
  //       var rowNode  = params.node.value
  //       console.log(rowNode)
  //       // rowNode.setDataValue('scheduled_date', selectedDate)
  //       console.log(params.node.data)
  //       // params.api.redrawRows({rowNodes : [rowNode]})
  //       dateIcon.value = selectedDate
  //       console.log(dateIcon.value)
  //       // You can perform any further processing with the selectedDate value here
  //     }

  //     // Add the event listener to capture date changes
  //     dateIcon.addEventListener('change', handleDateChange);
  //     // deleteIcon.innerHTML = '<a class="fas fa-trash"></a>';

  //     return dateIcon;
  //   },
  // }, -->





<!-- 
<table>
  <thead>
    <tr>
      <th>Item</th>
      <th>Units</th>
      <th>Days / Nights</th>
      <th>Total</th>
    </tr>
  </thead>
  <tbody>
      {% for booking in bookings%}
      
    <tr>
      
      <td>Guest Rooms</td>
      <td>{{ booking.number_of_rooms }}</td>
      <td>{{ days_nights }}</td>
      <td>{{ booking.total }}</td>     
    </tr>
    
    {% endfor %}
    <tr>
      <td>Banquet Venue from  {{praposal.from_date}} to {{praposal.to_date}}</td>
      <td></td>
      <td></td>
      <td></td>
      
                     
    </tr>

    {% for forma_invoice in forma_invoices %}
    
    <tr>
      <td>Total Package (Room + Banquet)</td>
      <td></td>
      <td></td>
      <td>{{ forma_invoice.total_package }}</td>
    </tr>
    <tr>
      <td>Water and Cleaning Charges</td>
      <td></td>
      <td></td>
      <td>{{forma_invoice.water_cleaning}}</td>
    </tr>
    <tr>
      <td>Security Deposit - Refundable Deposit</td>
      <td></td>
      <td></td>
      <td>{{forma_invoice.security_deposite}}</td>
    </tr>
    <tr>
      <td>Extras if anything will be charged on actual basis</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Grand Total (Approx.)</td>

                    
      <td colspan="4"> INR {{ forma_invoice.grand_total }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table> -->























<!-- <div id="modal-js-example" class="modal">
  <div class="modal-background"></div>

  <div class="modal-content">
    <div class="box">
      <p>Select Package</p>
       Your content -->
      <!-- <form @submit.prevent="submitPage">
        <div class="form-group">
          <label >Package:</label>
          <div class="field" style="width: 500%;">
            <div class="select">
              <select size="packages.length" v-model="selectedPackage">
                <option
                  v-for="pkg in packages"
                  :key="pkg.id"
                  :value="pkg.id"
                >
                  {{ pkg.package_name }}
                </option>
              </select>
            </div>
          </div>
        </div>
        <button class="button is-link is-outlined">Add Package</button>            
      </form>
    </div>
  </div>

  <button class="modal-close is-large" aria-label="close"></button>
</div>  -->























































<!-- 

# from django.db import models

# class Proposal(models.Model):
    
#     WEDDING_PACKAGE = 'wedding_package'
#     BIRTHDAY_PACKAGE = 'Birthday_package'
#     ANNIVERSARY_PACKAGE = 'anniversary_package'
#     CORPORATE_PACKAGE = 'corporate_package'
    
#     CHOICE_PACKAGE = (
#         (WEDDING_PACKAGE, 'Wedding_Package'),
#         (BIRTHDAY_PACKAGE, 'Birthday_Package'),
#         (ANNIVERSARY_PACKAGE, 'Anniversary_Package'),
#         (CORPORATE_PACKAGE, 'Corporate_Package'),
#     )
    
    
    
    
    
    
#     name = models.CharField(max_length=255, blank=True, null=True)
#     date = models.DateField(auto_now_add=False, auto_now=False)
#     start_time = models.TimeField(auto_now=False, auto_now_add=False)
#     end_time = models.TimeField(auto_now_add=False, auto_now=False)
#     event = models.CharField(max_length=255, blank=True, null=True)
#     venue = models.CharField(max_length=255, blank=True, null=True)
#     setup = models.CharField(max_length=255, blank=True, null=True)
#     attendance = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#     rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     company = models.CharField(max_length=255, blank=True, null=True)
#     city = models.CharField(max_length=255, blank=True, null=True)
#     phone = models.CharField(max_length=255, blank=True, null=True)
#     package = models.CharField(max_length=255, choices=CHOICE_PACKAGE, blank=True)

#     def __str__(self):
#         return self.name


# class Buffet(models.Model):
    
#     BREAK_FAST_BUFFET = 'Break_Fast_Buffet'
#     LUNCH_BUFFET = 'Lunch_Buffet'
#     DINNER_BUFFET = 'Dinner_Buffet'
     
    
#     CHOICE_BUFFET = (
#         (BREAK_FAST_BUFFET, 'Break_Fast_Buffet'),
#         (LUNCH_BUFFET, 'Lunch_Buffet'),
#         (DINNER_BUFFET, 'Dinner_Buffet'),
        
#     )
    
    
#     proposal=models.ForeignKey(Proposal, related_name='buffets', on_delete=models.CASCADE, null=True, default=None)
#     name = models.CharField(max_length=255, choices=CHOICE_BUFFET, blank=True, null=True)

#     def __str__(self):
#         return self.name

# class Addition(models.Model):
#     buffet = models.ForeignKey(Buffet, related_name='additions', on_delete=models.CASCADE, null=True, default=None)
#     name = models.CharField(max_length=500, blank=True, null=True)

#     def __str__(self):
#         return self.name

# class Menu(models.Model): 
#     buffet = models.ForeignKey(Buffet, related_name='menus', on_delete=models.CASCADE, null=True, default=None)
#     name = models.CharField(max_length=500, blank=True, null=True)

#     def __str__(self):
#         return self.name

    
    
    
    
    
    



# # class Soup(models.Model):
# #     proposal = models.ForeignKey(Proposal, related_name='soups', on_delete=models.CASCADE, null=True, default=None)
# #     name = models.CharField(max_length=500)

# #     def __str__(self):
# #         return self.name
     -->





















<!-- 




     <script>
import { reactive, onMounted } from 'vue';
import axios from 'axios';

export default {
  name: 'AddProposal',

  mounted() {
    this.getEvents()
    this.getVenues()
    this.getsetups()
    this.getPackeges()
    this.getBuffets()
    this.getBuffet_Menus()
  },

  components: {
    // CustomDropdown component
  },

  setup() {
    const form = reactive([
      // Form data
    ]);

    const buffets = reactive([])
    const buffet_menu = reactive([])

    const getBuffet_MenuName = (buffet_menuID) => {
      let buffet_menu = buffet_menus.find((buffet_menu) => buffet_menu.id == buffet_menuID)
      return buffet_menu ? buffet_menu.buffet_menus:'';

    };

    const getBuffet_MenuQuantity = (buffet_menuID) => {
      const buffet_menu = buffet_menus.find((buffet_menu) => buffet_menu.id === buffet_menuID);
      return buffet_menu ? buffet_menu.quantity : 0;
    };

    const increamentBuffet_MenuQuantity = (buffet_menuID) => {
      const buffet_menu = buffet_menus.find((buffet_menu) => buffet_menu.id ===buffet_menuID);
      if(buffet_menu){
        if(!buffet_menu.quantity) {
          buffet_menu.quantity = 0;
        }
        buffet_menu.quantity++;
      }
    };

    const decrementBuffet_MenuQuantity = (buffet_menuID) => {
      const buffet_menu = buffet_menus.find((buffet_menu) => buffet_menu.id ===buffet_menuID);
      if(buffet_menu && buffet_menu.quantity > 0){
        buffet_menu.quantity--;
      }
    };


    const buffetField = async () => {
      const selectedBaffet = buffets.find((baffet) => baffet.id === item.baffet);
      if (selectedBaffet) {
        await getBuffet_Menus(selectedBaffet.id)
        } else {
          buffet_menus.splice(0);
        }
        form[0].buffet_menus = [];
    };
    
    const buffet_menuField = () => {
      const selectedBuffet_Menus = buffet_menu.filter((buffet_menu) => form[0].buffet_menu.includes(buffet_menu.id));
      form[0].buffet_menu = selectedBuffet_Menus.map((buffet_menu) => buffet_menu.id);
    };


    const getBaffets = async () => {
      try {
        const response = await axios .get('/api/v1/get_buffets/');
        buffets.splice(0, buffets.length, ...response.data)
      } catch (error) {
        console.log(error)
      }
    };

    const getBuffets_Menus = async (baffetID) => {
      try {
        const response = await axios .get(`/api/v1/get_menu/?baffet_id=${baffetID}`);
        buffet_menus.splice(0, buffet_menus.length, ...response.data)
      } catch (error) {
        console.log(error)
      }
    }  










    // const buffets = reactive([]);
    // const additions = reactive([]);
    // const menu_items = reactive([]);

    // const incrementAdditionQuantity = (additionId) => {
    //   const addition = additions.find((addition) => addition.id === additionId);
    //   if (addition) {
    //     if (!addition.quantity) {
    //       // If quantity is not defined, initialize it to 0
    //       addition.quantity = 0;
    //     }
    //     addition.quantity++;
    //   }
    // };

    // const decrementAdditionQuantity = (additionId) => {
    //   const addition = additions.find((addition) => addition.id === additionId);
    //   if (addition && addition.quantity > 0) {
    //     addition.quantity--;
    //   }
    // };

    // const getAdditionName = (additionId) => {
    //   const addition = additions.find((addition) => addition.id === additionId);
    //   return addition ? addition.name : '';
    // };

    // const getAdditionQuantity = (additionId) => {
    //   const addition = additions.find((addition) => addition.id === additionId);
    //   return addition ? addition.quantity : 0;
    // };

    // const getMenuName = (menuId) => {
    //   const menu_item = menu_items.find((menu_item) => menu_item.id === menuId);
    //   return menu_item ? menu_item.name : '';
    // };

    // const getMenuQuantity = (menuId) => {
    //   const menu_item = menu_items.find((menu_item) => menu_item.id === menuId);
    //   return menu_item ? menu_item.quantity : 0;
    // };

    // const buffetField = async () => {
    //   const selectedBuffet = buffets.find((baffet) => baffet.id === item.baffet);
    //   if (selectedBuffet) {
    //     // await getAdditions(selectedBuffet.id);
    //     await getMenus(selectedBuffet.id);
    //   } else {
    //     // additions.splice(0);
    //     menu_items.splice(0);
    //   }
    //   // form[0].addition = [];
    //   form[0].menu_items = [];
    // };

    // const additionField = async () => {
    //   const selectedAdditions = additions.filter((addition) => form[0].addition.includes(addition.id));
    //   form[0].addition = selectedAdditions.map((addition) => addition.id);
    //   form[0].menu = [];
    // };

    // const menuField = () => {
    //   const selectedMenus = menu_items.filter((menu_item) => form[0].menu_item.includes(menu_item.id));
    //   form[0].menu_item = selectedMenus.map((menu_item) => menu_item.id);
    // };

    // const incrementMenuQuantity = (menuId) => {
    //   const menu_item = menu_items.find((menu_item) => menu_item.id === menuId);
    //   if (menu_item) {
    //     if (!menu_item.quantity) {
    //       // If quantity is not defined, initialize it to 0
    //       menu_item.quantity = 0;
    //     }
    //     menu_item.quantity++;
    //   }
    // };

    // const decrementMenuQuantity = (menuId) => {
    //   const menu_item = menu_items.find((menu_item) => menu_item.id === menuId);
    //   if (menu_item && menu_item.quantity > 0) {
    //     menu_item.quantity--;
    //   }
    // };

    // const getBuffets = async () => {
    //   try {
    //     const response = await axios.get('/api/v1/get_buffets/');
    //     buffets.splice(0, buffets.length, ...response.data);
    //   } catch (error) {
    //     console.log(error);
    //   }
    // };

    // const getAdditions = async (buffetId) => {
    //   try {
    //     const response = await axios.get(`/api/v1/get_additions/?buffet_id=${buffetId}`);
    //     additions.splice(0, additions.length, ...response.data);
    //   } catch (error) {
    //     console.log(error);
    //   }
    // };

    // const getMenus = async (buffetId) => {
    //   try {
    //     const response = await axios.get(`/api/v1/get_menus/?buffet_id=${buffetId}`);
    //     menus.splice(0, menus.length, ...response.data);
    //   } catch (error) {
    //     console.log(error);
    //   }
    // };

    onMounted(async () => {
      await getBaffets();
    });

    return {
      name:'',
      phone:'',
      city:'',
      company:'',
      email:'',
      from_date:'',
      to_date:'',
      date:'',
      start_time:'',
      end_time:'',
      min_attendance:'',
      max_attendance:'',

      form,
      buffets,
      // additions,
      // buffet_menus,
      // incrementAdditionQuantity,
      // decrementAdditionQuantity,
      // getAdditionName,
      // getAdditionQuantity,
      getBuffet_MenuName,
      getBuffet_MenuQuantity,
      buffetField,
      // additionField,
      buffet_menuField,
      increamentBuffet_MenuQuantity,
      decrementBuffet_MenuQuantity,
      events:[],
      venues:[],
      setups:[],
      packeges:[],
      buffets:[],
      buffet_menus:[],
      menu_items:[],
    };
  },

  methods: {
    addRow() {
      this.form.push({
        // name: '',
        date: '',
        start_time: '',
        end_time: '',
        event: '',
        venue: '',
        setup: '',
        attendance: '',
        rate: '',
        // company: '',
        // city: '',
        // phone: '',
        additions: [],
        menus: [],
      });
    },
    removeRow(index) {
      if (this.form.length > 1) {
        this.form.splice(index, 1);
      }
    },

    async submitForm() {
      this.$store.commit('setIsLoading', true)

      const proposal = {
        name:this.name,
        company:this.company,
        phone:this.phone,
        emial:this.email,
        city:this.city,
        from_date:this.from_date,
        to_date:this.to_date,

        services:this.form



      }
      await axios
        .post('/api/v1/create_proposal/',proposal)
        .then(response => {
          this.$router.push('/dashboard/propsoals')
        })
        .catch(error => {
          console.log(error)
        })
      
      this.$store.commit('setIsLoading', false)
    },

    async getEvents() {
      this.$store.commit('setIsLoading', true)

      await axios
        .get('/api/v1/get_events')
        .then(response => {
          this.events = response.data
        })
        .catch(error => {
          console.log(error)
        })
      this.$store.commit('setIsLoading', false)
    },

    async getVenues() {
      this.$store.commit('setIsLoading', false)

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

    async getsetups() {
      this.$store.commit('setIsLoading', true)

      await axios
        .get('/api/v1/get_setups')
        .then(response => {
          this.setups = response.data
        })
        .catch(error => {
          console.log(error)
        })
      this.$store.commit('setIsLoading', false)
    },

    async getPackeges() {
      this.$store.commit('setIsLoading', true)

      await axios
        .get('/api/v1/get_packages')
        .then(response => {
          this.packeges = response.data
        })
        .catch(error => {
          console.log(error)
        })
      this.$store.commit('setIsLoading', false)

    },

    async getBuffets() {
      this.$store.commit('setIsLoading', true)
      await axios
        .get('/api/v1/get_baffets')
        .then(response => {
          this.buffets = response.data
        })
        .catch(error => {
          console.log(error)
        })
      this.$store.commit('setIsLoading', false)
    },

   

    async getBuffet_Menus() {
      this.$store.commit('setIsLoading', true)

      this.buffet_menuID = this.$route.params.id

      await axios
        .get(`/api/v1/get_menus/${buffet_menuID}`)
        .then(response => {
          this.buffet_menus = response.data.buffet_menus
        })
        .catch(error => {
          console.log(error)
        })
      this.$store.commit('setIsLoading', false)
    },
    // async submitForm() {
    //   // Submit the form data to the server or perform any other necessary actions
    //   try {
    //     const proposal = {
    //       proposals: this.form,
    //     };
    //     await axios.post('/api/v1/create_proposal/', proposal);
    //     this.$router.push('/dashboard/proposals');
    //   } catch (error) {
    //     console.log(error);
    //   } finally {
    //     this.$store.commit('setIsLoading', false);
    //   }
    // },

    // async getAdditions(){
    //   this.$store.commit('setIsLoading', true)

    //   this.additionID = this.$route.params.id

    //   await axios
    //     .get(`/api/v1/get_addition/${additionID}`)
    //     .then(response => {
    //       this.additions = response.data.getAdditions
    //     })
    //     .catch(error => {
    //       console.log(error)
    //     })
    //   this.$store.commit('setIsLoading', false)
    // },
    async getMenus()  {
      this.$store.commit('setIsLoading', true)

      this.menuId = this.$route.params.id

      await axios 
        .get(`/api/v1/get_menu/${menuId}`)
        .then(response => {
          this.menus = response.data.menus
        })
        .catch(error => {
          console.log(error)
        })
      this.$store.commit('setIsLoading', false)
    }
  },

























  




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
    this.getBuffetMenuName()
    // this.getBuffetMenus();
    // this.Menu_Items()
  },

  setup() {
    const form = reactive([
      // Form data
    ]);

    const buffets = reactive([]);
    const buffet_menus = reactive([]);

    // const getBuffetMenuName = (buffetmenuID) => {
    //   const buffet_menu = buffet_menus.find((buffet_menu) => buffet_menu.id === buffetmenuID);
    //   return buffet_menu ? buffet_menu.menu_items : '';
    // };

    const getBuffetMenuQuantity = (buffetmenuID) => {
      const buffet_menu = buffet_menus.find((buffet_menu) => buffet_menu.id === buffetmenuID);
      return buffet_menu ? buffet_menu.quantity : 0;
    };

    const incrementBuffetMenuQuantity = (buffetmenuID) => {
      const buffet_menu = buffet_menus.find((buffet_menu) => buffet_menu.id === buffetmenuID);
      if (buffetmenuID) {
        if (!buffet_menu.quantity) {
          buffet_menu.quantity = 0;
        }
        buffet_menu.quantity++;
      }
    };

    const decrementBuffetMenuQuantity = (buffetmenuID) => {
      const buffet_menu = buffet_menus.find((buffet_menu) => buffet_menu.id === buffetmenuID);
      if (buffet_menu && buffet_menu.quantity > 0) {
        buffet_menu.quantity--;
      }
    };

    const buffetField = async (item) => {
      const selectedBaffet = this.buffets.find((baffet) => baffet.id === item.baffet);
      if (selectedBaffet) {
        
        await getBuffet_menus(selectedBaffet.id);
        item.buffet_menus = buffet_menus.map((buffet_menu) => buffet_menu.id);
      } 
      else {
        buffet_menus.splice(0);
        item.buffet_menus = [];
      }
    };

    async getBuffetMenuName(buffetMenuId) {
       
      const selectedBuffet_Menus = buffet_menus.filter((buffet_menu) => form[0].buffet_menu.includes(buffet_menu.id));
      form[0].buffet_menu = selectedBuffet_Menus.map((buffet_menu) => buffet_menu.id);
    };

    const getBuffets = async () => {
      try {
        const response = await axios.get('/api/v1/get_buffets/');
        buffets.splice(0, buffets.length, ...response.data);
      } catch (error) {
        console.log(error);
      }
    };

    const getBuffetMenus = async () => {
      try {
        const baffetID = this.$route.params.id;
        const response = await axios.get(`/api/v1/get_menu/${buffetID}`);
        buffetMenus.splice(0, buffetMenus.length, ...response.data);
      } catch (error) {
        console.log(error);
      }
    };

    onMounted(async () => {
      await getBuffets();
    });

    return {
      name:'',
      phone:'',
      city:'',
      company:'',
      email:'',
      from_date:'',
      to_date:'',
      date:'',
      start_time:'',
      end_time:'',
      min_attendance:'',
      max_attendance:'',


      form,
      buffets,
      // buffet_menus,
      // getBuffetMenuName,
      getBuffetMenuQuantity,
      // buffetField,
      // buffetMenuField,
      buffet_menus:[],
    };
  },

  methods: {
    addRow() {
      this.form.push({
        // name: '',
        date: '',
        start_time: '',
        end_time: '',
        event: '',
        venue: '',
        setup: '',
        attendance: '',
        rate: '',
        // company: '',
        // city: '',
        // phone: '',
        additions: [],
        menus: [],
      });
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

      await axios
        .post('/api/v1/create_proposal/', proposal)
        .then(response => {
          this.$router.push('/dashboard/proposals')
        })
        .catch(error => {
          console.log(error)
        })
      this.$store.commit('setIsLoading', true)
    },
    
    async getEvents() {
      
      this.$store.commit('setIsLoading', true)

      await axios
        .get('/api/v1/get_events')
        .then(response => {
          this.events = response.data
        })
        .catch(error => {
          console.log(error)
        })
      this.$store.commit('setIsLoading', false)
    },

    async getVenues() {
      
      this.$store.commit('setIsLoading', true)

      await axios
        .get('/api/v1/get_venues')
        .then(response => {
          this.venues = response.data
        })
      this.$store.commit('setIsLoading', false)
    },

    async getSetups() {

      this.$store.commit('setIsLoading', true)

      await axios
        .get('/api/v1/get_setups')
        .then(response => {
          this.setups = response.data
        })
        .catch(error => {
          console.log(error)
        })
      this.$store.commit('setIsLoading', false)
    },

    async getPackeges() {
      this.$store.commit('setIsLoading', true)

      await axios
        .get('/api/v1/get_packages')
        .then(response => {
          this.packeges = response.data
        })
        .catch(error => {
          console.log(error)
        })
      this.$store.commit('setIsLoading', false)

    },

    async getBuffets() {

      this.$store.commit('setIsLoading', true)

      await axios
        .get('/api/v1/get_baffets')
        .then(response => {
          this.buffets = response.data
        })
        .catch(error => {
          console.log(error)
        })
      this.$store.commit('setIsLoading', false)
    },

//     async getBuffetMenus() {
//   this.$store.commit('setIsLoading', true)

//   const baffetID = this.$route.params.id

//   await axios
//     .get(`/api/v1/get_menus/${baffetID}`)
//     .then(response => {
//       this.menu_items = response.data;
//     })
//     .catch(error => {
//       console.log(error);  
//     })

//   this.$store.commit('setIsLoading', false);
// },


    // async Menu_Items() {

    //   this.$store.commit('setIsLoading', true)

    //   // this.menuId = this.$route.params.id

    //   await axios
    //     .get(`/api/v1/get_items/`)
    //     .then(response => {
    //       this.menu_items = response.data
    //     })
    //     .catch(error => {
    //       console.log(error)
    //     })
    //   this.$store.commit('setIsLoading', false)
    // },






  },
};
</script> -->







 <!-- <div v-for="menu in item.buffet_menus" :key="menu">
                          <div class="buttons">
                            <label>
                              <input type="checkbox" v-model="item.selectedMenus" :value="menu" />
                              {{ getBuffetMenuName(menu) }}
                              <button type="button" class="button btn is-primary" @click="incrementBuffetMenuQuantity(menu)">+</button>
                              Quantity: {{ getBuffetMenuQuantity(menu) }}
                              <button type="button" class="button btn is-danger" @click="decrementBuffetMenuQuantity(menu)">-</button>
                            </label>
                          </div>
                        </div> -->













<!-- 






                        # <script>
                        # import axios from 'axios';
                        # import { reactive, onMounted, ref } from 'vue';
                        # import { AgGridVue } from 'ag-grid-vue3';
                        # import 'ag-grid-community/styles/ag-grid.css';
                        # import 'ag-grid-community/styles/ag-theme-alpine.css';
                        # import '@fortawesome/fontawesome-free/css/all.css';
                        # import { mapActions } from 'vuex';
                        # import { library } from '@fortawesome/fontawesome-svg-core';
                        # import { faTrash } from '@fortawesome/free-solid-svg-icons';
                        # import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
                        
                        # library.add(faTrash);
                        
                        
                        
                        
                        
                        # export default {
                        #   name: 'Praposal',
                        #   components: {
                        #     'ag-grid-vue': AgGridVue,
                        #     FontAwesomeIcon,
                        
                        
                        
                        #   },
                          
                        #   data() {
                        #     return {
                        #       form: [],
                        #       praposal: {},
                        #       services: [],
                        #       venues:[],
                        #       set_ups:[],
                        #       default_package_name: '',
                        #       defaults_item: [],
                        #       default_item:[],
                        #       columnDefs: [
                        #       // {
                        #       //     headerName: '',
                        #       //     field: 'selected',
                        #       //     headerCheckboxSelection: true,
                        #       //     checkboxSelection: true,
                        #       //     rowClassRules: {
                        #       //     'selected-row': 'data.selected',
                        #       //     },
                                  
                        #       //   },  
                        #         { headerName: 'Menu Item', field: 'default_item_name',  editable: true, checkboxSelection: true, headerCheckboxSelection: true,rowDrag: true},
                        #         { headerName: 'Quantity', field: 'default_quantity', editable: true },
                        #         {
                        #             field: '',
                        #             cellRenderer: function(params) {
                        #               const deleteItem = () => {
                        #                 this.deleteItem(params.data);
                        #               };
                        
                        #               const deleteIcon = document.createElement('div');
                        #               deleteIcon.className = 'delete-icon';
                        #               deleteIcon.innerHTML = '<a class="fas fa-trash"></a>';
                        #               deleteIcon.addEventListener('click', deleteItem);
                        
                        #               return deleteIcon;
                        #             }.bind(this),
                        #         },
                        #       ],
                        #       defaultColDef: {
                        #         flex: 1,
                        #         minWidth: 100,
                        #         sortable: true,
                        #         filter: true,
                        #         resizable: true,
                        #       },
                        #       // frameworkComponents: {
                        #       //   deleteItemRenderer: deleteItemRenderer,
                        #       // },
                        #     };
                        #   },
                        #   setup() {
                        #     // const form = reactive([]);
                        #     const defaults_package = reactive([]);
                        #     const defaults_item = reactive([]);
                        #     const default_package_name = ref('');
                        #     const default_item_name = [];
                        
                        
                        #     const deleteItemRenderer = {
                        #       template: `
                        #         <div class="delete-icon" @click="onClick(params.data)">
                        #           <i class="fas fa-trash"></i>
                        #         </div>
                        #       `,
                        #       methods: {
                        #         onClick(data) {
                        #           this.$emit('delete-item', data);
                        #         },
                        #       },
                        #     };
                        
                        
                        
                        #     const form = reactive([
                        #       {
                        #         date: '',
                        #         start_time: '',
                        #         end_time: '',
                        #         venues: '',
                        #         set_ups: '',
                        #         package: '',
                        #         menu_items: [], 
                        #       },
                        #     ]);
                        
                        #     const addRow = () => {
                        #   const newRow = {
                        #     date: '',
                        #     start_time: '',
                        #     end_time: '',
                        #     venues: '',
                        #     set_ups: '',
                        #     default_package: '',
                        #     rate: '',
                        #     default_item: [],
                        #     min_attendance: '',
                        #     max_attendance: '',
                        #   };
                        
                        #   form.push(newRow);
                        # };
                        
                        
                        
                        
                        
                        
                        
                        #     const removeRow = (index) => {
                        #         if(form.length > 1){
                        #             form.splice(index,1)
                        #         }
                                
                        #     }
                        
                        
                        
                        
                        
                        
                        #     const default_packageField = async (item) => {
                        #   const selectedDefaultPackage = defaults_package.find((default_package) => default_package.id === item.default_package);
                        #   if (selectedDefaultPackage) {
                        #     await getDefaults_Item(selectedDefaultPackage.id);
                        #     // Update the default_item property bound to ag-grid
                        #     item.default_item = [...defaults_item];
                        #   } else {
                        #     defaults_item.splice(0);
                        #     // Clear the default_item property
                        #     item.default_item = [];
                        #   }
                        # };
                        
                        
                        # const default_itemField = () => {
                        #   item.default_item = item.default_item.map((default_item) => default_item.id);
                        # };
                        
                        
                        # const getDefaults_Package = async () => {
                        #   try {
                        #     const response = await axios.get('/api/v1/get_defaults_package/');
                        #     defaults_package.splice(0, defaults_package.length, ...response.data);
                        #   } catch (error) {
                        #     console.log(error);
                        #   }
                        # };
                        
                        # const getDefaults_Item = async (default_packageID) => {
                        #   try {
                        #     const response = await axios.get(`/api/v1/get_default_items/?default_package_id=${default_packageID}`);
                        #     defaults_item.splice(0);
                        #     defaults_item.push(...response.data);
                        #   } catch (error) {
                        #     console.log(error);
                        #   }
                        # };
                        
                        
                        
                        
                        
                        
                        
                        
                        #     onMounted(async () => {
                        #       await getDefaults_Package();
                        #     });
                        
                        #     return {
                        #       form,
                        
                        #       // getBuffetMenuName,
                        #       // getBuffetMenuQuantity,
                        #       // incrementBuffetMenuQuantity,
                        #       // decrementBuffetMenuQuantity,
                        
                        #       defaults_package,
                        #       default_itemField,
                        #       default_packageField,
                        #       default_package_name,
                        #       defaults_item,
                        #       default_item_name,
                        #       deleteItemRenderer,
                        #       addRow,
                        #       removeRow,
                              
                        #       // deleteMenuItem,
                        #       // deleteButtonRenderer
                        #     };
                        #   },
                        #   mounted() {
                        #     this.getPraposal();
                        #     this.getVenues();
                        #     this.getSet_Up();
                        
                        #      // Define the deleteButtonRenderer component here
                            
                        #   },
                        #   methods: {
                        
                        #     onMenuItemsSelected(selectedItems) {
                        #     const selectedPackage = this.defaults_package.find(
                        #       (pkg) => pkg.id === this.item.default_package
                        #     );
                        
                        #     if (selectedPackage) {
                        #       const menuItems = selectedPackage.menu_items.map((itemId) =>
                        #         this.defaults_item.find((item) => item.id === itemId)
                        #       );
                        #       this.item.menu_items = menuItems;
                        #     } else {
                        #       this.item.menu_items = [];
                        #     }
                        #   },
                        
                        #     deleteItem(data) {
                        #     const index = this.defaults_item.findIndex(item => item.default_item_name === data.default_item_name);
                        #     if (index !== -1) {
                        #       this.defaults_item.splice(index, 1);
                        #     }
                        #   },
                        #     onGridReady(params) {
                        #       this.gridApi = params.api;
                        #       this.columnApi = params.columnApi;
                        #     },
                        
                        #   onFactoryButtonClick(e) {
                        #     const button = e.currentTarget;
                        #     const buttonColor = button.getAttribute('');
                        #     const side = button.getAttribute('');
                        #     const newItem = {
                        #       default_item_name: buttonColor,
                        #       // default_quantity: 1, 
                        #     };
                        
                        #     // Add the new item to the defaults_item array
                        #     this.defaults_item.push(newItem);
                        
                        #     // Update the grid to reflect the changes
                        #     this.gridApi.setRowData(this.defaults_item);
                        #   },
                        
                        
                        
                        #     async getPraposal() {
                        
                        #       this.$store.commit('setIsLoading', true)
                        
                        #       const praposalId = this.$route.params.id;
                              
                        #       console.log('praposalId', praposalId)
                        
                        #       await axios
                        #         .get(`/api/v1/get_praposal/${praposalId}`)
                        #         .then(response => {
                        #           this.praposal = response.data.praposal;
                        #           this.services = response.data.services;
                        #         })
                        #         .catch(error => {
                        #           console.log(error)
                        #         })
                        #       this.$store.commit('setIsLoading', false)
                        
                        #     },
                        
                        #     async getVenues() {
                              
                        #       this.$store.commit('setIsLoading', true)
                        
                        #       await axios
                        #         .get('/api/v1/get_venues')
                        #         .then(response => {
                        #           this.venues = response.data
                        #         })
                        #         .catch(error => {
                        #           console.log(error)
                        #         })
                        #       this.$store.commit('setIsLoading', false)
                        #     },
                        
                        #     async getSet_Up() {
                        
                        #       this.$store.commit('setIsLoading', true)
                        
                        #       await axios
                        #         .get('/api/v1/get_setup')
                        #         .then(response => {
                        #           this.set_ups = response.data
                        #         })
                        #         .catch(error =>{
                        #           console.log(error)
                        #         })
                        #       this.$store.commit('setIsLoading', false)
                        #     },
                        #   }
                        # };
                        
                        # </script> -->