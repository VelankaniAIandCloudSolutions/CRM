<template>
  <div class="container">
    <h1 class="title" style="text-transform: capitalize;">Proposal Details</h1>

    <nav class="breadcrumb" aria-label="breadcrumbs">
      <ul>
        <li>
          <router-link to="/dashboard" class="has-text-dark">Dashboard</router-link>
        </li>
        <li>
          <router-link to="/dashboard/proposals" class="has-text-dark">Proposals</router-link>
        </li>
      </ul>
    </nav>

    <hr>
    <div class="buttons">
      <button @click="downloadBothPDFs()" class="button is-dark is-clickable">
        <i class="fas fa-download"></i> 
      </button>
      <button @click="sendCombinedReminder()" class="button is-info is-clickable">
        <i class="far fa-envelope"></i>
      </button>
    </div>

   



    <div class="content">

      <router-link :to="`/dashboard/proposals/${this.$route.params.id}/${praposal.id}/edit-proposal`" class="button btn  is-info is-outlined"  style="margin-left:90%;">
       <i class="fas fa-edit fa-2x"></i> 
      </router-link>


      <br>
      <br>
      
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

   

    <div class="tabs" style="margin-left:33%;">
      <ul>
        <li :class="{ 'is-active': activeTab === 'service' }">
          <a @click="activeTab = 'service'">
            <i class="icon fas fa-pencil-alt"></i>

            <span class="text">+ Add Service</span>
          </a>
        </li>
        <li :class="{ 'is-active': activeTab === 'accommodation' }">
          <a @click="activeTab = 'accommodation'">
            <i class="icon fas fa-bed"></i>
            <span class="text">+ Add Accommodation</span>
          </a>
        </li>
        <li :class="{ 'is-active': activeTab === 'deposite' }">
          <a @click="activeTab = 'deposite'">
            <i class="icon fas fa-calendar"></i>
            <span class="text">+ Deposit Schedule</span>
          </a>
        </li>
        <li :class="{ 'is-active': activeTab === 'forma_invoice' }">
          <a @click="activeTab = 'forma_invoice'">
            <i class="icon fas fa-file-alt"></i>
            <span class="text">+ Pro Forma Invoice</span>
          </a>
        </li>
      </ul>
    </div>

    <div v-if="activeTab === 'service'">

      <div class="buttons">
        <button @click="getservicepdf()" class="button is-dark is-clickable">
          <i class="fas fa-download"></i> 
        </button>
        <button @click="sendServiceReminder()" class="button is-info is-clickable">
          <i class="far fa-envelope"></i>
        </button>
      </div>
      <br>
      <br>

       <!-- <button @click="showModalAccomadation = true" class="button is-link is-outlined js-modal-trigger" data-target="modal-js-example">
        + Add Accomadation
      </button>
      <div v-if="showModalAccomadation" class="modal" :class="{'is-active': showModalAccomadation}" >
        <div class="modal-background" @click="showModalAccomadation =  false"></div> -->


      <button @click="showModalService = true" class="button is-link is-outlined js-modal-trigger" data-target="modal-js-example">
        + Add Service
      </button>
      <div id="modal-js-example" class="modal" :class="{'is-active': showModalService}" >
        <div class="modal-background"  @click="showModalService =  false"></div>

        <div class="modal-content" style="width:85%;">
          <div class="box">
            <div class="content">
              <!-- <form @submit.prevent="submitServiceForm"> -->
                <div class="box-body">
                  <div v-for="(item, index) in form" :key="index">
                    <div class="title"> Add Service: </div>
                    <br>
                    <br>
                    
                      <div class="input-box">
                        <label for="date">Date:</label>
                        <div class="field">
                          <select v-model="item.date" style="width:50%;">
                            <option v-for="date in dates" :key="date" :value="date">{{ date }}</option>
                          </select>
                        </div>
                      </div>
                      <br>
                      <div class="form-row">

                      <div class="input-box">
                        <label for="events">Select Event:</label>
                        <select v-model="item.event" @change="eventField(item)">
                          <option v-for="event in events" :key="event.id" :value="event.id">
                            {{ event.events }}
                          </option>
                        </select>
                      </div>

                      <div class="input-box">
                        <label for="event_type">Select Event Type:</label>
                        <select v-model="item.event_type">
                          <option v-for="event_type in event_types" :key="event_type.id" :value="event_type.id">
                            {{ event_type.event_type }}
                          </option>
                        </select>
                      </div>

                      <div class="input-box">
                        <label for="start_time">Start Time:</label>
                        <input type="time" v-model="item.start_time" />
                      </div>

                      <div class="input-box">
                        <label for="end_time">End Time:</label>
                        <input type="time" v-model="item.end_time" />
                      </div>

                      <div class="input-box">
                        <label for="venus">Select Venue:</label>
                        <select v-model="item.venues">
                          <option v-for="venue in venues" :key="venue.id" :value="venue.id">
                            <span>{{ venue.venues }}</span>
                          </option>
                        </select>
                      </div>

                      <div class="input-box">
                        <label for="rate">Venue Rental Charges:</label>
                        <input type="number" v-model="item.venue_amount">
                      </div>

                      <div class="input-box" v-if="index === 0">
                        <label for="rate">Miscellaneous Charges:</label>
                        <input type="number" v-model="item.miscellaneous_charges">
                      </div>

                      <div class="input-box">
                        <label for="set_up">Select Set-Up:</label>
                        <select v-model="item.set_ups">
                          <option v-for="set_up in set_ups" :key="set_up.id" :value="set_up.id">
                            <span>{{ set_up.set_ups }}</span>
                          </option>
                        </select>
                      </div>

                      <div class="input-box">
                        <label for="end_time">Min_Attendance:</label>
                        <input type="number" v-model="item.min_attendance" />
                      </div>

                      <div class="input-box">
                        <label for="end_time">Max_Attendance:</label>
                        <input type="number" v-model="item.max_attendance" />
                      </div>

                      <!-- Select Package Group -->
                      
                      <div class="input-box">
                        <label for="package_group">Select Package Group:</label>
                        <select v-model="item.package_group" @change="default_packageField(item)">
                          <option v-for="packageGroup in packageGroups" :key="packageGroup.id" :value="packageGroup.id">
                            {{ packageGroup.name }}
                          </option>
                        </select>
                      </div>


                  <div class="input-box">
                    <label for="default_package_name">Package:</label>
                    <select v-model="item.default_package" @change="optionField(item)">
                      <option v-for="default_package in selectedPackageGroupDefaults(item)" :key="default_package.id" :value="default_package.id">
                        {{ default_package.default_package_name }}
                      </option>
                    </select>
                  </div>


                  <div class="input-box">
                    <label for="option">Select Package Options:</label>
                    <select v-model="item.option" @change="optionField(item)">
                      <option v-for="option in options" :key="option.id" :value="option.id">
                        {{ option.option_name }}
                      </option>
                    </select>
                  </div>
              
                  <div class="input-box">
                    <label for="rate">Rate:</label>
                    <!-- {{ item.option_rate }} -->
                    <input type="text" v-model="item.option_rate">
                  </div>
                  
                      <div class="input-box">
                        <label>Select Audio Visuals:</label>
                        <div class="field">
                          <div class="select is-multiple" style="width: 100%;">
                            <div class="dropdown-header" @click="toggleDropdown">
                              {{ selectedAudioVisualsText }}
                            </div>
                            <div class="dropdown-body" v-show="showDropdown">
                              <div
                                class="dropdown-item"
                                v-for="(audio_visual, index) in audio_visuals"
                                :key="audio_visual.id"
                                @click="toggleAudioVisual(audio_visual.id)"
                                :class="{ selected: isSelectedAudioVisual(audio_visual.id) }"
                              >
                                <div class="item-content">
                                  <b>{{index + 1}}.</b> {{ audio_visual.audio_visuals }}
                                </div>
                                <input
                                  type="checkbox"
                                  v-model="audio_visual.selected"
                                  :value="audio_visual.id"
                                />
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>



                                                
                      
                      <br>
                      <br>
                      <br>
                    </div>

                    <br>
                    <br>
                      <div class="input-box">
                      
                        <div class="toolbar" for="default_item_name" > Menu Items: 
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
                          @firstDataRendered="onFirstDataRendered"
                          @rowDataChanged="onRowDataChanged"
                          @cellValueChanged="onCellValueChanged"
                          rowSelection='multiple'
                        ></ag-grid-vue>
                      </div>
                    </div>

                    <br>
                    <!-- <div class="buttons">
                      <button type="button" class="button btn is-success is-outlined" @click="addRow()" style="width:50%;">+ Add More</button>
                      <button type="button" class="button btn is-danger is-outlined" @click="removeRow(index)" style="width:48%;">X</button>
                    </div> -->

                    <br>
                    <br>
                    <br>
                    <br>
                    <br>
                  </div>
                </div>

                <button class="button btn is-link is-outlined" style="width: 100%;"   @click="submitServiceForm" >Submit</button>
              <!-- </form> -->
            </div>
          </div>
        </div>

        <button  @click="showModalService = false" class="modal-close is-large" aria-label="close"></button>
      </div>
     

      <br>
      <br>










      <div class="title">
        <label style="text-transform: capitalize;">Service Details</label>
      </div>
      <div style="max-height: 400px; overflow: auto;">
        <table class="table is-fullwidth is-striped is-hoverable">
  <thead>
    <tr>
      <th>Date</th>
      <th>Start Time</th>
      <th>End Time</th>
      <th>Event</th>
      <th>Event Type</th>
      <th>Venue</th>
      <th>Miscellaneous Charges</th>
      <th>Set-Up</th>
      <th>Min Attendance</th>
      <th>Max Attendance</th>
      <th>Package Category</th>
      <th>Package</th>
      <th>Package Option</th>
      <th>Items</th>
      <th></th>
      <th>Rate</th>
      <th></th>
      <th></th> 
    </tr>
  </thead>
  <tbody>
    <tr v-for="service in services" :key="service.id">
      <td>{{ service.date }}</td>
      <td>{{ service.start_time }}</td>
      <td>{{ service.end_time }}</td>
      <td>
        <ul>
          <li v-for="fun in service.functions" :key="fun.id">
            {{ fun.function }}
          </li>
        </ul>
      </td>
      <td>
        <ul>
          <li v-for="function_type in service.function_types" :key="function_type.id">
            {{ function_type.function_type }}
          </li>
        </ul>
      </td>




      <td>{{ service.venues.venues }}</td>
      <td>{{ service.miscellaneous_charges }}</td>
      <td>{{ service.set_ups.set_ups }}</td>
      <td>{{ service.min_attendance }}</td>
      <td>{{ service.max_attendance }}</td>
      <td>
    <ul v-if="service.package_group">
      <li>{{ service.package_group.name }}</li>
    </ul>
  </td>
      <td>
        <ul>
          <li v-for="pkg in service.packages" :key="pkg.id">
            {{ pkg.package_name }}
          </li>
        </ul>
      </td>
      <td>
        <ul>
          <li v-for="choice in service.choices" :key="choice.id">
            {{ choice.choices }}
          </li>
        </ul>
      </td>
      <td>
        <ul>
          <li v-for="(item, index) in service.items" :key="item.id">
            <b>{{ index + 1 }}.</b> {{ item.item_name }}
            <br>
          </li>
        </ul>
      </td>
      <td></td>
      <td>{{ service.rate }}</td>
      <td>
        <a class="button is-info is-outlined" :href="`/dashboard/praposals/${this.$route.params.id}/${service.id}/edit`">
          <i class="fas fa-edit"></i>
        </a>
      </td>
      <td>
        <button class="button is-danger is-outlined" @click="deleteService(service.id)">
          <i class="fas fa-trash"></i>
        </button>
      </td>
    </tr>
  </tbody>
</table>

      </div>
      


    </div>

    <div v-if="activeTab === 'accommodation'">
      <div class="buttons">
        <button @click="getbookingpdf()" class="button is-dark is-clickable">
          <i class="fas fa-download"></i> 
        </button>
        <button @click="sendBookingReminder()" class="button is-info is-clickable">
          <i class="far fa-envelope"></i>
        </button>
      </div>


      <button @click="showModalAccomadation = true" class="button is-link is-outlined js-modal-trigger" data-target="modal-js-example">
        + Add Accomadation
      </button>
      <div v-if="showModalAccomadation" class="modal" :class="{'is-active': showModalAccomadation}" >
        <div class="modal-background" @click="showModalAccomadation =  false"></div>
        <div class="modal-content" style="width:85%;">
          <div class="box">
            <div class="content">
              <!-- <form @submit.prevent="submitAccommodationForm"> -->
          <div class="box-body">

            <div class="form-row">

            <div class="input-box">
              <label for="check_in_date">Enter Check In Date And Time:</label>
              <input type="datetime-local" id="check_in_date" placeholder="Enter Check In Date" v-model="check_in_date">
            </div>
            

            <div class="input-box">
              <label for="check_out_date">Enter Check Out Date And Time :</label>
              <input type="datetime-local" id="check_out_date" placeholder="Enter The Check Out Date" v-model="check_out_date">
            </div>

            <!-- <div class="input-box">
              <label for="room_types">Select Room Type:</label>
              <select v-model="accommodation.room_type">
                <option v-for="room_type in room_types" :key="room_type.id" :value="room_type.id">
                  {{ room_type.room_types }}
                </option>
              </select>
            </div> -->

            <div class="input-box">
              <label>Select Room Types:</label>
              <div class="field">
                <div class="select is-multiple" style="width: 100%;">
                  <div class="dropdown-header" @click="toggleDropdowns">
                    {{ selectedRoomTypesText }}
                  </div>
                  <div class="dropdown-body" v-show="showDropdowns">
                    <div
                      class="dropdown-item"
                      v-for="(room_type, index) in room_types"
                      :key="room_type.id"
                      @click="toggleRoomType(room_type.id)"
                      :class="{ selected: isSelectedRoomType(room_type.id) }"
                    >
                      <b>{{ index + 1 }}.</b> {{ room_type.room_types }}
                      <input
                        type="checkbox"
                        v-model="selectedRoomTypes"
                        :value="room_type.id"
                      />
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <div class="input-box">
              <label for="number_of_rooms">Enter Number Of Rooms:</label>
              <input type="number" id="number_of_rooms" v-model="number_of_rooms" />
            </div>

            <div class="input-box">
              <label for="occupency">Enter Occupancy:</label>
              <input type="text" id="occupancy" v-model="occupancy" />
            </div>

            <!-- <div class="input-box">
              <label for="meal_plan">Select Meal Plan</label>
              <select v-model="meal_plans">
                <option v-for="meal_plan in meal_plans" :key="meal_plan.id" :value="meal_plan.id">
                  {{ meal_plan.meal_plans }}
                </option>
              </select>
            </div> -->
            <div class="input-box">
              <label>Select Meal Plan:</label>
              <div class="field">
                <div class="select is-multiple" style="width: 100%;">
                  <div class="dropdown-header" @click="toggleDropdownss">
                    {{ selecteMealPlansText }}
                  </div>
                  <div class="dropdown-body" v-show="showDropdownss">
                    <div
                      class="dropdown-item"
                      v-for="(meal_plan, index) in meal_plans"
                      :key="meal_plan.id"
                      @click="toggleMealPlan(meal_plan.id)"
                      :class="{ selected: isSelectedMealPlan(meal_plan.id) }"
                    >
                      <b>{{ index + 1 }}.</b> {{ meal_plan.meal_plans }}
                      <input
                        type="checkbox"
                        :value="meal_plan.id"
                        :checked="isSelectedMealPlan(meal_plan.id)"
                      />
                    </div>
                  </div>
                </div>
              </div>
            </div>








            <div class="input-box">
              <label>Rate:</label>
              <input type="number" id="rate" v-model="rate">
            </div>
          </div>
        </div>
        <br>

          <button class="button is-success is-outlined" @click="submitAccommodationForm" >Submit</button>
        <!-- </form> -->
            </div>
          </div>
        </div>

        <button  @click="showModalAccomadation =  false" class="modal-close is-large" aria-label="close"></button>
      </div>





      <br>
      <br>
      <div class="title">
        <label style="text-transform: capitalize;">Accommodation Details</label>
      </div>

      <table class="table is-fullwidth is-striped">
  <thead>
    <tr>
      <th>Check In Date</th>
      <th>Check Out Date</th>
      <th>Room Type</th>
      <th>Number Of Rooms</th>
      <th>Occupancy</th>
      <th>Meal Plan</th>
      <th>Rate</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="booking in bookings" :key="booking.id">
      <td>{{ booking.check_in_date }}</td>
      <td>{{ booking.check_out_date }}</td>
      <td>
        <span v-for="(roomType, index) in booking.room_types" :key="roomType.id">
          {{ roomType.room_types }}
          <span v-if="index < booking.room_types.length - 1">, </span>
        </span>
      </td>
      <td>{{ booking.number_of_rooms }}</td>
      <td>{{ booking.occupancy }}</td>
      <td>
  <span v-for="(meal_plan, index) in booking.meal_plans" :key="meal_plan.id">
    <!-- {{ meal_plan }}  -->
    {{ getMealPlanName(meal_plan.id) }} <!-- Log the result of getMealPlanName -->
    <span v-if="index < booking.meal_plans.length - 1">, </span>
  </span>
</td>




      <td>{{ booking.rate }}</td>
      <td>
        <a class="button btn is-info is-outlined" :href="`/dashboard/proposals/${this.$route.params.id}/${booking.id}/edit`">
          <i class="fas fa-edit fa-2x"></i>
        </a>
      </td>
      <td>
        <button class="button btn is-danger is-outlined" @click="deleteBooking(booking.id)">
          <i class="fas fa-trash fa-2x" style="cursor: pointer;"></i>
        </button>
      </td>
    </tr>
  </tbody>
</table>



    </div>

    <div v-if="activeTab === 'deposite'">

     


      <button @click="showModalDeposit = true" class="button is-link is-outlined js-modal-trigger" data-target="modal-js-example">
        + Add Deposit
      </button>
      <div id="modal-js-example" class="modal" :class="{'is-active': showModalDeposit}" >
        <div class="modal-background"  @click="showModalDeposit =  false"></div>

        <div class="modal-content" style="width:85%;">
          <div class="box">
            <div class="content">
              <!-- <form @submit.prevent="submitDepositeForm"> -->

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
                <button class="button is-link is-outlined"  @click="submitDepositeForm" >Submit</button>
                <!-- </form> -->
            </div>
          </div>
        </div>

        <button  @click="showModalDeposit = false" class="modal-close is-large" aria-label="close"></button>
      </div>
      <br>
      <br>

      <div class="title">
        <label style="text-transform: capitalize;">Deposit Details</label>
      </div>

      <div class="buttons" style="margin-left:90%;">
        <a  class="button btn is-info  is-outlined" :href="`/dashboard/proposals/${this.$route.params.id}/edit-deposite`">
          <i class="fas fa-edit fa-2x"></i>
        </a>

      </div>
      <br>

      <table class="table is-fullwidth is-striped">
        <thead>
          <tr>
            <th>Deposite</th>
            <th>Scheduled Date</th>
            <th>Amount Due</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="deposite in deposites" :key="deposite.id">
            <td>{{ deposite.deposite }}</td>
            <td>{{ deposite.scheduled_date }}</td>
            <td>{{ deposite.amount_due }}</td>
          </tr>
        </tbody>
      </table>



    </div>

    <div v-if="activeTab === 'forma_invoice'">

      <div class="title">
        <label style="text-transform: capitalize;">Pro Forma Invoice Details</label>
      </div>
      
      <table class="table is-fullwidth is-striped is-hoverable">
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
          <td>{{ praposal_invoice.item }} - Charges</td>
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
          <td>
            {{ booking.check_in_date }}<br>
            to<br>
            {{ booking.check_out_date }}
          </td>
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



    </div>

  </div>
</template>
  
  
<script>
  // import { faL } from '@fortawesome/free-solid-svg-icons';
  import axios from 'axios'
  import { toast } from 'bulma-toast'
  import { reactive, onMounted, ref, computed , watch } from 'vue';
  import { AgGridVue } from 'ag-grid-vue3';
  import 'ag-grid-community/styles/ag-grid.css';
  import 'ag-grid-community/styles/ag-theme-alpine.css';
  import '@fortawesome/fontawesome-free/css/all.css';
  import { mapActions } from 'vuex';
  import { library } from '@fortawesome/fontawesome-svg-core';
  import { faL, faTrash } from '@fortawesome/free-solid-svg-icons';
  import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

  
  import 'vue-toastification/dist/index.css';
  const fileDownload = require('js-file-download')
  
  export default {
    name: 'Proposal',
    components: {
    'ag-grid-vue': AgGridVue,
    FontAwesomeIcon,

   



  },
    data() {
      return {
        services: [],
        packages: [],
        items: [],
        package_groups: [], 
        choices: [], 
        praposals:[],
        praposal:[],
        bookings:[],
        forma_invoice:[],
        form:[],
        selectedDate: null,
        dates: [],
        
        showModalService: false,
        // closeModal: false,

        showModalAccomadation:false,
        closeModalAccomadation:false,

        showModalDeposit:false,
        


        // sub_total: 0,
        // cgst_amount: 0,
        // sgst_amount: 0,
        // grand_total: 0,
        

        

        activeTab: 'service',
        
        accommodation: {
          check_in_date:'',
          check_out_date:'',
          room_types:'',
          number_of_rooms:'',
          meal_plans:'',
          occupency:'',
        },

        deposite: {
          deposite:'',
          scheduled_date:'',
          amount_due:'',
        },

        forma_invoice: {
          total_package:'',
          water_cleaning:'',
          security_deposite:'',
          grand_total:'',
        },

        
        item: {
          event: null,
          event_type: null,
        },
        events: [], 
        event_types: [],

        showDropdown: false,
        selectedAudioVisuals: [],
        audio_visuals: [],
        
        showDropdowns: false,
        selectedRoomTypes: [],

        showDropdownss: false,
        selectedRoomTypess: [],

        meal_plans:[],
        meal_plan: null,
        selectedMealPlans: [],
        selectedRoomTypes: [], // Selected room types IDs
        showDropdowns: false,
        room_types: [],

        deposite: [], 

        praposal_invoices: [],
        selectedDate: null,
        selectedroomtype: [],
        dates: [],
        bookings:[],
        form: [],
        praposal: {},
       
       
        
        venues:[],
        set_ups:[],
        default_package_name: '',
        defaults_item: [],


        check_in_date: '', 
        check_out_date: '', 
        number_of_rooms: null, 
        occupancy: '',
        meal_plans:'',
        rate: null, 
        selectedRoomTypes: [],
        selectedMelaPlans: [],
        







        praposal: {},
        services: [],
        venues:[],
        set_ups:[],
        
        default_package_name: '',
        defaults_item: [],
        columnDefs: [ 
          { headerName: 'Menu Item', field: 'default_item_name', editable: true, checkboxSelection: true, headerCheckboxSelection: true, rowDrag: true },
          { headerName: 'Rate', field: 'default_quantity', editable: true },
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
          }
        ],
        columnDefss: [
      { headerName: 'Deposite', field: 'deposite', editable: true, rowDrag: true },
      
      {
        headerName: 'Scheduled Date',
        field: 'scheduled_date',
        cellRenderer: (params) => {
          const dateIcon = document.createElement('input');
          dateIcon.type = 'date';

          function handleDateChange(event) {
            const selectedDate = event.target.value;
            console.log('Selected date:', selectedDate);

            // Get the row node from params
            const rowNode = params.node;
                
            rowNode.setDataValue('scheduled_date', selectedDate); 
            const rowData = rowNode.data;
            rowData['scheduled_date'] = selectedDate;

           
          }

          // Add the event listener to capture date changes
          dateIcon.addEventListener('change', handleDateChange);

          dateIcon.value = params.data.scheduled_date || ''; 

          return dateIcon;
        },

      },

      {
        headerName: 'Amount Due',
        field: 'amount_due',
        editable: true,
        valueGetter: (params) => {
          const amount = params.data.amount_due; 
          return amount !== undefined ? `INR ${amount}` : ''; 
        },
      },


     
      {
        field: '',
        cellRenderer: (params) => {
          const deleteItems = () => {
            this.deleteItems(params.data);
          };

          const deleteIcon = document.createElement('div');
          deleteIcon.className = 'delete-icon';
          deleteIcon.innerHTML = '<a class="fas fa-trash"></a>';
          deleteIcon.addEventListener('click', deleteItems);

          return deleteIcon;
        },
      },
    ],
        defaultColDef: {
          flex: 1,
          minWidth: 100,
          sortable: true,
          filter: true,
          resizable: true,
        },
        selectedItems: ref([]),
       
      }
    },

    setup() {
    const defaults_package = reactive([]);
    const defaults_item = reactive([]);
    const default_package_name = ref('');
    const default_item_name = [];
    const packageGroups = reactive([]);
    const selectedPackageGroupId = ref(null);
    const gridApi = ref(null);
    const options = reactive([]);
    const option_name = ref('');
    const events = ref([]); 
    const event_types = ref([]);

    

    const deleteItemRenderer = {
    template: `
      <div class="delete-icon" @click="deleteItem(params.data)">
        <i class="fas fa-trash"></i>
      </div>
    `,
    methods: {
      deleteItem(data) {
        this.$emit('delete-item', data);
      },
      
    },
  };

    const form = reactive([
    {
      date: '',
      start_time: '',
      end_time: '',
      venues: '',
      set_ups: '',
      package_group: '',
      default_package: '',
      option: '',
      option_rate: '',
      audio_visuals: '',
      default_item: [],
      min_attendance: '',
      max_attendance: '',
      event: '',
      event_type: '',
    },
  ]);

  // const addRow = () => {
  //   const newRow = {
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
  //   };

  //   form.push(newRow);
  // };

  // const removeRow = (index) => {
  //   if (form.length > 1) {
  //     form.splice(index, 1);
  //   }
  // };


  const selectedPackageGroupDefaults = (item) => {
    if (item.package_group === '') {
      return []; // Return an empty array when no package_group is selected
    }
    return defaults_package.filter((pkg) => pkg.package_group.id === item.package_group);
  };



    const default_packageField = async (item) => {
      console.log(item)
      selectedPackageGroupId.value = item.package_group;
      const selectedDefaultPackage = defaults_package.find((default_package) => default_package.id === item.default_package);

      if (item.package_group) {
        try {
          await getDefaults_Package();

        
          options.length = 0;

          if (selectedDefaultPackage) {
          
            const packageOptions = await getOptions(selectedDefaultPackage.id);
            options.push(...packageOptions);

            console.log("Options Fetched Successfully:", options); 
          }
        } catch (error) {
          console.log(error);
        }
      } else {
      
        options.length = 0;
      }
    };


    const getPackageGroups = async () => {
      try {
        const response = await axios.get('/api/v1/get_package_groups/');
        packageGroups.splice(0, packageGroups.length, ...response.data);
      } catch (error) {
        console.log(error);
      }
    };

    const getDefaults_Package = async () => {
      try {
        const packageGroupId = selectedPackageGroupId.value;

        if (packageGroupId !== null) {
          const response = await axios.get(`/api/v1/get_defaults_package/?package_group_id=${packageGroupId}`);
          defaults_package.splice(0, defaults_package.length, ...response.data);
        } else {
          console.log("Selected Package Group ID is null.");
        }
      } catch (error) {
        console.log(error);
      }
    };

    
    const optionField = async (item) => {
    const selectedDefaultPackage = defaults_package.find((pkg) => pkg.id === item.default_package);
    if (selectedDefaultPackage) {
    
      const packageOptions = await getOptions(selectedDefaultPackage.id);
      options.splice(0, options.length, ...packageOptions);

      const selectedOption = packageOptions.find((option) => option.id === item.option);
      if (selectedOption) {
      
        item.option_rate = selectedOption.option_rate;
      } else {
      
        item.option_rate = null;
      }
      await getDefaults_Item(item.option);
    } else {
      options.length = 0;
      defaults_item.length = 0;
    }

    console.log("Options after updating:", options);
  };



  watch(() => form[0].option, async (newVal, oldVal) => {
    if (newVal !== oldVal) {
      await getDefaults_Item(newVal);
    }
  });











  const getOptions = async (default_packageID) => {
    try {
      const response = await axios.get(`/api/v1/get_options/?default_package_id=${default_packageID}`);
      console.log("Options Fetched Successfully:", response.data); 
      return response.data;
    } catch (error) {
      console.log("Error Fetching Options:", error);
      return [];
    }
  };



    const default_itemField = (item) => {
      item.default_item = item.default_item.map((default_item) => default_item.id);
    };


    const getDefaults_Item = async (optionID) => {
    try {
      const response = await axios.get(`/api/v1/get_default_items/?option_id=${optionID}`);
      defaults_item.splice(0);
      defaults_item.push(...response.data);
    } catch (error) {
      console.log(error);
    }
  };

    //  code for Event Dependent Drop down  

      const eventField = async (item) => {
        const selectedEvent = events.value.find((e) => e.id === item.event);
        if (selectedEvent) {
          await getEvent_Types(selectedEvent.id);
          item.event_type = null; 
        } else {
          event_types.value.splice(0); 
          item.event_type = null; 
        }
      };





    const getEvents = async () => {
      try {
        const response = await axios.get('/api/v1/get_events/');
        events.value = response.data; // Set the data to the events array using Vue's reactivity
      } catch (error) {
        console.log(error);
      }
    };
    const event_typeField = (item) => {
        item.event_type = item.event_type.map((event_type) => event_type.id);
      };

      const getEvent_Types = async (eventId) => {
        try {
          const response = await axios.get(`/api/v1/get_event_types/${eventId}`);
          event_types.value = response.data; 
        } catch (error) {
          console.log(error);
        }
      };

    watch(() => form[0].default_package, async (newVal, oldVal) => {
      if (newVal !== oldVal) {
        await getOptions(newVal);
      }
    });

    watch(defaults_item, (newValue) => {
      if (gridApi.value) {
        gridApi.value.setRowData(newValue);
      }
    });
    watch(options, (newOptions) => {
    console.log("Options after updating:", newOptions);
  });
  watch(() => form[0].option, (newValue) => {
    console.log("Form[0].option:", newValue);
  });


    onMounted(async () => {
    await Promise.all([getPackageGroups(), getDefaults_Package(), getEvents()]);
    console.log("Form Option:", form[0].option); // Add this line
    optionField(form[0]); // Call optionField to fetch the options for the initially selected default_package
  });



    return {
      form,
      defaults_package,
      default_itemField,
      default_packageField,
      default_package_name,
      defaults_item,
      default_item_name,
      // addRow,
      // removeRow,
      packageGroups,
      selectedPackageGroupDefaults,
      gridApi,
      eventField,
      event_typeField,
      events,
      event_types,
      optionField,
      options,
    };
  },

  created() {
  this.getPraposal_invoice();
},
  
    mounted() {
      this.getServices();

      this.getPraposal();

      this.getBookings();

      this.getDeposites();

      this.getForma_Invoice();

      this.getPraposal_invoice();

      this.getAudio_visuals();

      this.getMeal_plans();

      this.getRoom_types();



      this.getVenues()
      this.getSet_Up()

     



      






      document.addEventListener('DOMContentLoaded', () => {
        // Functions to open and close a modal
        function openModal($el) {
          $el.classList.add('is-active');
        }

        function closeModal($el) {
          $el.classList.remove('is-active');
        }

        function closeAllModals() {
          (document.querySelectorAll('.modal') || []).forEach(($modal) => {
            closeModal($modal);
          });
        }

        // Add a click event on buttons to open a specific modal
        (document.querySelectorAll('.js-modal-trigger') || []).forEach(($trigger) => {
          const modal = $trigger.dataset.target;
          const $target = document.getElementById(modal);

          $trigger.addEventListener('click', () => {
            openModal($target);
          });
        });

        // Add a click event on various child elements to close the parent modal
        (document.querySelectorAll('.modal-background, .modal-close, .modal-card-head .delete, .modal-card-foot .button') || []).forEach(($close) => {
          const $target = $close.closest('.modal');

          $close.addEventListener('click', () => {
            closeModal($target);
          });
        });

        // Add a keyboard event to close all modals
        document.addEventListener('keydown', (event) => {
          const e = event || window.event;

          if (e.keyCode === 27) { // Escape key
            closeAllModals();
          }
        });
      });
    },

    computed: {
    subtotal() {
      let total = 0;
      for (const service of this.services) {
        total += this.calculateAmount(service);
      }
      return total;
    },

    selectedAudioVisualsText() {
      if (this.selectedAudioVisuals.length === 0) {
        return 'Select an option';
      }
      return this.selectedAudioVisuals.map(av => av.audio_visuals).join(', ');
    },

    selectedRoomTypesText() {
  if (this.selectedRoomTypes.length === 0) {
    return 'Select an option';
  }
  return this.selectedRoomTypes
    .filter(rt => rt !== null) 
    .map(rt => rt.room_types)
    .join(', ');
},
selecteMealPlansText() {
  if (this.selectedMelaPlans.length === 0) {
    return 'Select an option';
  }
  return this.selectedMelaPlans
    .filter(mp => mp !== null) // Filter out null values
    .map(mp => mp.meal_plans)
    .join(', ');
},
// totalRate() {

//       return this.defaults_item.reduce((sum, item) => {
//         return sum + parseFloat(item.default_quantity || 0);
//       }, parseFloat(this.item.option_rate || 0));


//     }
   
  },
  
    methods: {

    //   updateSum() {
    //   this.item.option_rate = parseFloat(this.item.option_rate || 0); 
    //   this.totalRate = this.defaults_item.reduce((sum, item) => {
    //     return sum + parseFloat(item.default_quantity || 0);
    //   }, parseFloat(this.item.option_rate || 0));
    // },


      getEventName(eventId) {
    const event = this.events.find(e => e.id === eventId);
    return event ? event.events : '';
  },
  getEventType(eventTypeId) {
    const eventType = this.event_types.find(et => et.id === eventTypeId);
    return eventType ? eventType.event_type : '';
  },

  getMealPlanName(mealPlanId) {
    const mealPlan = this.meal_plans.find(mp => mp.id === mealPlanId);
    return mealPlan ? mealPlan.meal_plans : "";
  },


      toggleDropdown() {
      this.showDropdown = !this.showDropdown;
    },
    toggleAudioVisual(audio_visualId) {
      const index = this.selectedAudioVisuals.findIndex(av => av.id === audio_visualId);
      if (index > -1) {
        this.selectedAudioVisuals.splice(index, 1);
      } else {
        const audio_visual = this.audio_visuals.find(av => av.id === audio_visualId);
        if (audio_visual) {
          this.selectedAudioVisuals.push(audio_visual);
        }
      }
    },
    isSelectedAudioVisual(audio_visualId) {
      return this.selectedAudioVisuals.some(av => av.id === audio_visualId);
    },

    toggleDropdowns() {
      this.showDropdowns = !this.showDropdowns;
    },


    toggleRoomType(room_typeID) {
  const index = this.selectedRoomTypes.findIndex(rt => rt.id === room_typeID);
  if (index > -1) {
    this.selectedRoomTypes.splice(index, 1);
  } else {
    const room_type = this.room_types.find(rt => rt.id === room_typeID);
    if (room_type) {
      this.selectedRoomTypes.push(room_type);
    }
  }
},

    isSelectedRoomType(room_typeID) {
      return this.selectedRoomTypes.some(rt => rt.id === room_typeID);
    },

    toggleDropdownss() {
      this.showDropdownss = !this.showDropdownss;
    },


    toggleMealPlan(meal_planID) {
  const index = this.selectedMealPlans.findIndex(mp => mp.id === meal_planID);
  if (index > -1) {
    this.selectedMealPlans.splice(index, 1);
  } else {
    const meal_plan = this.meal_plans.find(mp => mp.id === meal_planID);
    if (meal_plan) {
      this.selectedMealPlans.push(meal_plan);
    }
  }
},

isSelectedMealPlan(meal_planID) {
  return this.selectedMealPlans.some(mp => mp.id === meal_planID);
},


  calculateGrandTotal() {
      this.grand_total =
        parseInt(this.total_package) +
        parseInt(this.water_cleaning) +
        parseInt(this.security_deposite);
    },

      generateDates() {
        console.log(this.praposal)
        const from_date = new Date(this.praposal.from_date);
        const to_date = new Date(this.praposal.to_date);

        console.log('from_date', from_date)
        console.log('to_date', to_date)

        const dates = [];

        while (from_date <= to_date) {
          const formattedDate = from_date.toISOString().split('T')[0];
          dates.push(formattedDate);
          from_date.setDate(from_date.getDate() + 1);
        }
        console.log(dates)
        this.dates = dates;
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

 
  deleteItems(data) {
  const index = this.deposite.indexOf(data);
  if (index > -1) {
    // Create a copy of the array and modify the copy
    const updatedDeposite = [...this.deposite];
    updatedDeposite.splice(index, 1);
    this.deposite = updatedDeposite;
  }
  // Update the grid to reflect the changes
  this.gridApi.setRowData(this.deposite);
},



onGridReady(params) {
  console.log('runununun')
      this.gridApi = params.api; 
      this.columnApi = params.columnApi;
    },
    onCellValueChanged(params) {
      // This function will be called every time a cell's value is updated
      console.log('Cell value changed:', params);

      // Perform the calculation
      let total = this.defaults_item.reduce((sum, item) => {
        return sum + parseFloat(item.default_quantity || 0);
      }, parseFloat(this.item.option_rate || 0));
      console.log(total)
      // this.item.option_rate = total;

      // Assign the calculated total to the option_rate property only if totalRate is 0
      if (total !== 0) {
        console.log(this.form[0])
        this.form[0].option_rate = total;
      }

      // Call your function here to perform additional actions
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

  onFactoryButton(e) {
  const button = e.currentTarget;
  const buttonColor = button.getAttribute('');
  const side = button.getAttribute('');

  const newDepo = {
    deposite: buttonColor,
  };
  
  // Instead of directly pushing to the reactive array,
  // create a new array and assign it to the reactive property
  this.deposite = [...this.deposite, newDepo];
  
  // Update the grid to reflect the changes
  this.gridApi.setRowData(this.deposite);
},

async getPraposal() {

this.$store.commit('setIsLoading', true)

const praposalId = this.$route.params.id;

console.log('praposalId', praposalId)

await axios
  .get(`/api/v1/get_praposal/${praposalId}`)
  .then(response => {
    this.praposal = response.data.praposal;
    this.services = response.data.services;
    this.generateDates()
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

  async getAudio_visuals() {
      this.$store.commit('setIsLoading', true);

      try {
        const response = await axios.get('/api/v1/get_audio_visuals');
        this.audio_visuals = response.data; // Set the data to the audio_visuals array using Vue's reactivity
      } catch (error) {
        console.log(error);
      }

      this.$store.commit('setIsLoading', false);
    },

    async getMeal_plans() {
  this.$store.commit('setIsLoading', true);

  try {
    const response = await axios.get('/api/v1/get_meal_plans');
    this.meal_plans = response.data;
    console.log('Fetched meal plans:', this.meal_plans);
  } catch (error) {
    console.log('Error fetching meal plans:', error);
  }

  this.$store.commit('setIsLoading', false);
},


   
  




    async getServices() {
  this.$store.commit('setIsLoading', true);
  const praposalId = this.$route.params.id;

  try {
    const response = await axios.get(`/api/v1/get_services/${praposalId}`);
    console.log(response.data); 
    const data = response.data;
    this.services = data.services;
    this.packages = data.packages;
    this.items = data.items;
    this.package_groups = data.package_groups;
    this.choices = data.choices;
    this.functions = data.functions;
    this.function_types = data.function_types;
//     console.log('Services:', this.services);
//     this.services.forEach(service => {
//   console.log("Service Event Types:", service.event_types);
//   console.log("Service Events:", service.events);
// });

    
  } catch (error) {
    console.error(error);
  }

  this.$store.commit('setIsLoading', false);
},


getPackages(serviceId) {
  if (!this.packages) {
    return [];
  }
  return this.packages.filter(pkg => pkg.service.id === serviceId);
},

getFunctions(serviceId) {

  if(!this.functions) {

    return [];
  }
  return this.functions.filter(fun => fun.service.id === serviceId);
},

getFunction_Types(serviceId) {
  if(!this.function_types) {
    return [];
  }
  return this.function_types(function_type => function_type.service.id === serviceId)
},


getItems(serviceId) {
  if (!this.items) {
    return [];
  }
  return this.items.filter(item => item.choices.package.service.id === serviceId);
},


getChoices(serviceId) {
  if (!this.choices) {
    return [];
  }
  return this.choices.filter(choice => choice.package.service.id === serviceId);
},


getPackageGroups(serviceId) {
  if (!this.packages) {
    return [];
  }
  return this.packages.filter(pkg => pkg.service.id === serviceId);
},


getServiceRate(serviceId) {
  const service = this.services.find(s => s.id === serviceId);
  return service ? service.rate : null;
},


    


      

      async deleteService(serviceId) {

        this.$store.commit('setIsLoading', true)

        
        await axios
          .post(`/api/v1/delete_service/${serviceId}/`)
          .then(response => {
            // console.log(response.data)
            toast({
              message: 'The Service is Deleted',
              type: 'is-success',
              dismissible: true,
              pauseOnHover: true,
              duration: 2000,
              position: 'bottom-right',
            })

            // this.$router.push(`/dashboard/proposals/${this.$route.params.praposal_id}`);
            
          })
          .catch(error => {
            console.log(error)
          })

        this.$store.commit('setIsLoading', false)
          
      },

      async deleteBooking(bookingID) {

        this.$store.commit('setIsLoading', true)

        await axios
          .post(`/api/v1/delete_booking/${bookingID}/`)
          .then(response => {
            toast({
              message: 'The Booking is Deleted',
              type: 'is-success',
              dismissible: true,
              pauseOnHover: true,
              duration: 2000,
              position: 'bottom-right',
            })

          // this.$router.push(`/dashboard/proposals/${this.$route.params.service_id}`)
          })
          .catch(error => {
            console.log(error)
          })

        this.$store.commit('setIsLoading', false)
      },





      async getservicepdf() {
          this.$store.commit('setIsLoading', true)
          const praposalId = this.$route.params.id

          await axios
              .get(`/api/v1/praposals/${praposalId}/generate_service_pdf/`, {
                  responseType: 'blob',
              }).then(res => {
                  fileDownload(res.data, `praposal_${praposalId}.pdf`);
              }).catch(error => {
                  console.log(error)
              })
          this.$store.commit('setIsLoading', false)
      },

      

      async getbookingpdf() {
          this.$store.commit('setIsLoading', true)
          const praposalId = this.$route.params.id

          await axios
              .get(`/api/v1/praposals/${praposalId}/generate_booking_pdf/`, {
                  responseType: 'blob',
              }).then(res => {
                  fileDownload(res.data, `praposal_${praposalId}.pdf`);
              }).catch(error => {
                  console.log(error)
              })
          this.$store.commit('setIsLoading', false)
      },

      async sendServiceReminder() {
        this.$store.commit('setIsLoading', true)
            try {
              const praposalId = this.$route.params.id;
              const response = await axios.post(`/api/v1/praposals/${praposalId}/send_service_reminder/`);

              console.log("sendReminder response:", response); // log the response for debugging purposes

              if (response.data.success) {
                // Show success toast
                toast({
                  message: 'Proposal sent successfully',
                  type: 'is-success',
                  position: 'bottom-right',
                  duration: 2000,
                  dismissible: true,
                });
                this.showError = false;
              } else {
                // Show error toast
                toast({
                  message: 'Failed to send proposal reminder',
                  type: 'is-danger',
                  position: 'bottom-right',
                  duration: 2000,
                  dismissible: true,
                });
                this.showError = true;
              }
              this.showSuccess = true;
            } catch (error) {
              console.error("sendReminder error:", error); // log the error for debugging purposes
              // Show error toast
              // BulmaToast.toast({
              //   message: 'An error occurred while sending the proposal reminder',
              //   type: 'is-danger',
              //   position: 'bottom-right',
              //   duration: 4000,
              //   dismissible: true,
              // });
              this.showSuccess = false;
              this.showError = true;
            }
          this.$store.commit('setIsLoading', false)
        },

        async sendBookingReminder() {
        this.$store.commit('setIsLoading', true)
            try {
              const praposalId = this.$route.params.id;
              const response = await axios.post(`/api/v1/praposals/${praposalId}/send_booking_reminder/`);

              console.log("sendReminder response:", response); // log the response for debugging purposes

              if (response.data.success) {
                // Show success toast
                toast({
                  message: 'Booking Proposal sent successfully',
                  type: 'is-success',
                  position: 'bottom-right',
                  duration: 2000,
                  dismissible: true,
                });
                this.showError = false;
              } else {
                // Show error toast
                toast({
                  message: 'Failed to send proposal reminder',
                  type: 'is-danger',
                  position: 'bottom-right',
                  duration: 2000,
                  dismissible: true,
                });
                this.showError = true;
              }
              this.showSuccess = true;
            } catch (error) {
              console.error("sendReminder error:", error); // log the error for debugging purposes
              // Show error toast
              // BulmaToast.toast({
              //   message: 'An error occurred while sending the proposal reminder',
              //   type: 'is-danger',
              //   position: 'bottom-right',
              //   duration: 4000,
              //   dismissible: true,
              // });
              this.showSuccess = false;
              this.showError = true;
            }
          this.$store.commit('setIsLoading', false)
        },

        async sendCombinedReminder() {
          this.$store.commit('setIsLoading', true);
          try {
            const praposalId = this.$route.params.id;

            // Send service reminder
            const serviceResponse = await axios.post(`/api/v1/praposals/${praposalId}/send_service_reminder/`);
            console.log("sendServiceReminder response:", serviceResponse);

            // Send booking reminder
            const bookingResponse = await axios.post(`/api/v1/praposals/${praposalId}/send_booking_reminder/`);
            console.log("sendBookingReminder response:", bookingResponse);

            // Check the success of both reminders
            const serviceSuccess = serviceResponse.data.success;
            const bookingSuccess = bookingResponse.data.success;

            if (serviceSuccess && bookingSuccess) {
              // Show success toast
              toast({
                message: 'Service and booking reminders sent successfully',
                type: 'is-success',
                position: 'bottom-right',
                duration: 2000,
                dismissible: true,
              });
              this.showError = false;
            } else {
              // Show error toast
              toast({
                message: 'Failed to send reminders',
                type: 'is-danger',
                position: 'bottom-right',
                duration: 2000,
                dismissible: true,
              });
              this.showError = true;
            }

            this.showSuccess = true;
          } catch (error) {
            console.error("sendCombinedReminder error:", error);
            // Show error toast
            // BulmaToast.toast({
            //   message: 'An error occurred while sending reminders',
            //   type: 'is-danger',
            //   position: 'bottom-right',
            //   duration: 4000,
            //   dismissible: true,
            // });
            this.showSuccess = false;
            this.showError = true;
          }

          this.$store.commit('setIsLoading', false);
        },


        async  downloadBothPDFs() {
          this.$store.commit('setIsLoading', true);
          const praposalId = this.$route.params.id;

          try {
            const servicePDF = axios.get(`/api/v1/praposals/${praposalId}/generate_service_pdf/`, {
              responseType: 'blob',
            });

            const bookingPDF = axios.get(`/api/v1/praposals/${praposalId}/generate_booking_pdf/`, {
              responseType: 'blob',
            });

            const [serviceRes, bookingRes] = await axios.all([servicePDF, bookingPDF]);

            fileDownload(serviceRes.data, `service_praposal_${praposalId}.pdf`);
            fileDownload(bookingRes.data, `booking_praposal_${praposalId}.pdf`);

            this.$store.commit('setIsLoading', false);
          } catch (error) {
            console.log(error);
            this.$store.commit('setIsLoading', false);
          }
        },

       


        async getBookings() {

          this.$store.commit('setIsLoading', true)

          const praposalId = this.$route.params.id

          await axios
            .get(`/api/v1/get_bookings/${praposalId}`)
            .then(response => {

              this.bookings = response.data
            })
            .catch(error => {
              console.log(error)
            })

          this.$store.commit('setIsLoading', false)
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
        
        async getDeposites() {

          this.$store.commit('setIsLoading', true)

          const praposalId = this.$route.params.id
          
          await axios
            .get(`/api/v1/get_deposites/${praposalId}`)
            .then(response => {
              this.deposites = response.data
            })
            .catch(error => {
              console.log(error)
            })

          this.$store.commit('setIsLoading', false)
        },

        async getForma_Invoice() {

          this.$store.commit('setIsLoading', true)

          const praposalId = this.$route.params.id

          await axios
            .get(`/api/v1/get_forma_invoice/${praposalId}`)
            .then(response => {
              this.forma_invoices = response.data
            })
            .catch(error => {
              console.log(error)
            })

          this.$store.commit('setIsLoading', false)
        },

        async getPraposal_invoice() {
          this.$store.commit('setIsLoading', true);

          const praposalID = this.$route.params.id;

          console.log('praposalID', praposalID);

          try {
            const response = await axios.get(`/api/v1/get_praposal_invoice/${praposalID}`);
            console.log(response.data);
            this.praposal_invoices = response.data;
            
           
          } catch (error) {
            console.log(error);
          }

          this.$store.commit('setIsLoading', false);
        },




        

        calculateCgstAmount(amount, cgstPercentage) {
      if (isNaN(amount)) {
        return 0;
      }

      const cgstAmount = (amount * cgstPercentage) / 100;
      return cgstAmount.toFixed(2);
    },
    calculateSgstAmount(amount, sgstPercentage) {
      if (isNaN(amount)) {
        return 0;
      }

      const sgstAmount = (amount * sgstPercentage) / 100;
      return sgstAmount.toFixed(2);
    },
    calculateTotal(amount, cgstPercentage, sgstPercentage) {
      if (isNaN(amount)) {
        return 0;
      }

      const cgstAmount = this.calculateCgstAmount(amount, cgstPercentage);
      const sgstAmount = this.calculateSgstAmount(amount, sgstPercentage);
      const total = parseFloat(amount) + parseFloat(cgstAmount) + parseFloat(sgstAmount);

      if (isNaN(total)) {
        return 0;
      }

      return total.toFixed(2);
    },
    calculateGrandTotal() {
      let grandTotal = 0;

      // Add praposal_invoices totals
      for (const praposal_invoice of this.praposal_invoices) {
        grandTotal += parseFloat(praposal_invoice.amount) + parseFloat(this.calculateCgstAmount(praposal_invoice.amount, praposal_invoice.cgst_percentage)) + parseFloat(this.calculateSgstAmount(praposal_invoice.amount, praposal_invoice.sgst_percentage));
      }

      // Add bookings totals
      for (const booking of this.bookings) {
        grandTotal += parseFloat(booking.amount) + parseFloat(this.calculateCgstAmount(booking.amount, 9)) + parseFloat(this.calculateSgstAmount(booking.amount, 9));
      }

      return grandTotal.toFixed(2);
    },





    async submitServiceForm() {
  this.$store.commit('setIsLoading', true);

  const service = {
    services: this.form.map((item) => {
      // Convert package_group value to integer, as it seems to be passed as a string
      return {
        ...item,
        package_group: parseInt(item.package_group),
      };
    }),
  };

  console.log('Service:', service);

  const praposalId = this.$route.params.id;

  try {
    const response = await axios.post(`/api/v1/create_services/${praposalId}/`, service);
    console.log('Response:', response.data);
    toast({
      message: 'The Service Created',
      type: 'is-success',
      dismissible: true,
      pauseOnHover: true,
      duration: 2000,
      position: 'bottom-right',
    });
    
    // this.$router.push(`/dashboard/proposals/${this.$route.params.praposal_id}`);

  } catch (error) {
    console.error('Error:', error);
    toast({
      message: 'An error occurred while creating the service.',
      type: 'is-danger',
      dismissible: true,
      pauseOnHover: true,
      duration: 5000,
      position: 'bottom-right',
    });
  }

  this.$store.commit('setIsLoading', false);
},


  async submitAccommodationForm() {

    this.$store.commit('setIsLoading', true)

    const roomTypeIds = this.selectedRoomTypes.map(rt => rt.id);

    const mealPlanIds = this.selectedMealPlans.map(mp => mp.id);

  const bookingData = {
    check_in_date: this.check_in_date,
    check_out_date: this.check_out_date,
    room_types: roomTypeIds,
    meal_plans: mealPlanIds, 
    number_of_rooms: this.number_of_rooms,
    occupancy: this.occupancy,
    rate: this.rate,
   
  };
    console.log('bookingData', bookingData)

    const praposalId = this.$route.params.id

    await axios
      .post(`/api/v1/create_booking/${praposalId}/`, bookingData)
      .then(response => {
        toast({
              message: 'The Accomadation is  Created',
              type: 'is-success',
              dismissible: true,
              pauseOnHover: true,
              duration: 2000,
              position: 'bottom-right',
            })
        
        console.log('Response', response.data)

        // this.$router.push('/dashboard/proposals')
      })
      .catch(error => {
  console.log('Error:', error.response);
});

    this.$store.commit('setIsLoading', false)
  },

  async submitDepositeForm() {
  this.$store.commit('setIsLoading', true);

  const deposites = {
    deposite: this.deposite,
    scheduled_date: this.scheduled_date, // Make sure this property is set correctly
    amount_due: this.amount_due,
  };

  console.log('deposites', deposites);

  const praposalId = this.$route.params.id;

  try {
    const response = await axios.post(`/api/v1/create_deposites/${praposalId}/`, deposites);
    
    // Update the deposite data with the response data, assuming the response is an array
    this.deposite = response.data;

    toast({
      message: 'The Deposites are Created',
      type: 'is-success',
      dismissible: true,
      pauseOnHover: true,
      duration: 2000,
      position: 'bottom-right',
    });

    console.log('Response', response.data);
  } catch (error) {
    console.log(error);
  }

  this.$store.commit('setIsLoading', false);
},


      
    }
  }
</script>

  

<style scoped>
  /* Scoped CSS styles go here */

  /* CSS for the item content and checkbox */
.dropdown-item {
  display: flex;
  align-items: center;
  padding: 8px;
  border-bottom: 1px solid #ccc;
  cursor: pointer;
}

/* CSS for the selected item */
.dropdown-item.selected {
  background-color: #f9f9f9;
}

/* CSS for the checkbox */
.dropdown-item input[type="checkbox"] {
  margin-left: 8px;
}


  .tabs li a .text {
  display: none;
}

/* Show the text when hovering over the icon */
.tabs li a:hover .text {
  display: inline;
}


  .tabs {
    /* Your scoped tabs styles go here */
    display: flex;
    justify-content: center;
    margin-bottom: 20px;
  }

  .tabs ul {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .tabs li {
    display: inline-block;
    margin-right: 10px;
  }

  .tabs a {
    text-decoration: none;
    padding: 10px 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    color: #333;
  }

  .tabs a.is-active {
    background-color: #333;
    color: #fff;
  }

 


  /* Your custom styles for the Service tab form fields */


  /* CSS for the Service Form */

/* Add any global styles you may have here */

/* Styling for the container that holds the form */
.box {
  background-color: #f0f0f0;
  padding: 20px;
  border-radius: 5px;
  margin-bottom: 20px;
}

/* Styling for the service title */
.title {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 10px;
}

/* Styling for the form rows */
.form-row {
  display: flex;
  flex-wrap: wrap;
}

/* Styling for the input boxes */
.input-box {
  flex: 0 0 50%; /* Make each input box take 50% width of the form row */
  margin-bottom: 15px;
  padding: 0 10px;
}

.input-box label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.input-box input,
.input-box select {
  width: 100%;
  height: 40px;
  padding: 5px;
  border-radius: 5px;
  border: 1px solid #ccc;
}

/* Styling for the toolbar button */
.toolbar button {
  border: none;
  background-color: #007bff;
  color: #fff;
  padding: 8px 15px;
  border-radius: 5px;
  cursor: pointer;
}



@media (max-width: 768px) {
  .input-box {
    flex: 0 0 100%; /* On smaller screens, make the input boxes take 100% width */
  }

  .buttons {
    flex-direction: column; /* On smaller screens, stack the buttons vertically */
  }

  .buttons button {
    margin-bottom: 10px; /* Add some spacing between the stacked buttons */
  }
}


  /* Add other scoped styles as needed */


    /* Add custom CSS here */
    table {
    width: 100%;
  }

  /* Set a maximum width for the cells to prevent overflowing */
  td {
    max-width: 150px; /* You can adjust this value as needed */
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  /* Style the edit and delete buttons */
  .button {
    padding: 5px 10px;
    border-radius: 5px;
    cursor: pointer;
  }

  .is-info {
    background-color: #209cee; /* You can change the color as needed */
    color: #fff;
  }

  .is-danger {
    background-color: #ff3860; /* You can change the color as needed */
    color: #fff;
  }

  td {
    max-width: 300px; /* You can adjust this value as needed */
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  
</style>
  






<!-- /* Styling for the buttons at the bottom */
.buttons {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
}

.buttons button {
  flex: 0 0 48%; /* Make the buttons take 48% width of the buttons container */
}

/* Styling for the submit button */
button.is-link {
  background-color: #28a745;
  color: #fff;
  font-size: 16px;
  font-weight: bold;
  padding: 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button.is-link:hover {
  background-color: #218838;
}

/* Add any additional styles you may need for other elements */

/* Media query for responsiveness */
@media (max-width: 768px) {
  .input-box {
    flex: 0 0 100%; /* On smaller screens, make the input boxes take 100% width */
  }

  .buttons {
    flex-direction: column; /* On smaller screens, stack the buttons vertically */
  }

  .buttons button {
    margin-bottom: 10px; /* Add some spacing between the stacked buttons */
  }
} -->