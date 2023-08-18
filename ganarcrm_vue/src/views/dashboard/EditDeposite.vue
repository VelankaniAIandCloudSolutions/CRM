<template>
    <div>
      <div class="title">
        <label style="text-transform: capitalize;">Edit Deposit</label>
      </div>
  
      <div class="form-group">
        <div class="toolbar">
          <button type="button" class="factory" @click="onFactoryButtonClick($event)" style="margin-right:200px;">
            <i class="far fa-plus-square"></i> Add Row
          </button>
        </div>
      </div>
  
      <div style="width: 850px; height: 500px; text-align: center;">
        <ag-grid-vue
          style="width: 100%; height: 100%;"
          class="ag-theme-alpine"
          :columnDefs="columnDefs"
          :rowData="updatedeposite"
          :defaultColDef="defaultColDef"
          :suppressMoveWhenRowDragging="true"
          :rowDragManaged="true"
          :rowClassRules="rowClassRules"
          :frameworkComponents="frameworkComponents"
          @gridReady="onGridReady"
          @selectionChanged="onMenuItemsSelected($event.api.getSelectedRows())"
          rowSelection="multiple"
        ></ag-grid-vue>
      </div>
    </div>
    <br>

    <div>
    <div style="border: 1px solid #ccc; width: 400px; height: 200px; margin-bottom: 10px;">
      <canvas ref="canvas" style="cursor: crosshair;"></canvas>
    </div>
    <div class="buttons">
      <button @click="clearSignature">Clear</button>
      <button @click="saveSignature">Save Signature</button>
    </div>
    <div v-if="previewSignature">
      <h3>Signature Preview</h3>
      <img :src="previewSignature" alt="Signature Preview">
    </div>
  </div>

  <br>



  
    <div class="buttons">
      <button class="button btn is-danger is-outlined" @click="cancelDeposite"> <i class="fas fa-times" style="margin-right:8px;"></i> Cancel</button>
      <button type="submit" class="button btn is-link is-outlined" @click="onSubmit"> <i class="fas fa-check " style="margin-right:8px;" ></i> Update</button>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import { ref, onMounted } from 'vue';
  import { toast } from 'bulma-toast';
  import { AgGridVue } from 'ag-grid-vue3';
  import 'ag-grid-community/styles/ag-grid.css';
  import 'ag-grid-community/styles/ag-theme-alpine.css';

  import SignaturePad from 'signature_pad';


  axios.defaults.headers.common['X-CSRFToken'] = 'your-csrf-token';
  
  export default {
    name: 'EditDeposite',
  
    components: {
      AgGridVue,
    },
  
    data() {
      return {

        signaturePad: null,
      signatureData: '',
      previewSignature: '',

        updatedeposite: [],
        columnDefs: [
          { headerName: 'Deposite', field: 'deposite', editable: true },
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

                // Check if rowNode and setDataValue are available before proceeding
                if (rowNode && typeof rowNode.setDataValue === 'function') {
                // Update the 'scheduled_date' property in the row node
                rowNode.setDataValue('scheduled_date', selectedDate);

                // Update the 'scheduled_date' property in the rowData as well
                const rowData = rowNode.data;
                rowData['scheduled_date'] = selectedDate;
                } else {
                console.error('Cannot update scheduled_date. RowNode or setDataValue is not available.');
                }
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
            return `INR ${amount}`;
            },
         },
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
          sortable: true,
          filter: true,
          resizable: true,
        },
        frameworkComponents: {},
        gridApi: null,
        columnApi: null,
      };
    },

    setup() {

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

        return {
            deleteItemRenderer
        }

    },
  
    mounted() {
      this.getDeposites();

      const canvas = this.$refs.canvas;
    this.signaturePad = new SignaturePad(canvas);
    },
  
    methods: {
      async getDeposites() {
        this.$store.commit('setIsLoading', true);
  
        const praposalId = this.$route.params.praposal_id;
  
        try {
          const response = await axios.get(`/api/v1/get_deposite/${praposalId}`);
          this.updatedeposite = response.data;
        } catch (error) {
          console.log(error);
        }
  
        this.$store.commit('setIsLoading', false);
      },
  
      cancelDeposite() {
        if (confirm("Are you sure you want to cancel?")) {
          this.$router.push(`/dashboard/proposals/${this.$route.params.praposal_id}`);
        }
      },
  
      async onSubmit() {
           const praposalId = this.$route.params.praposal_id;
      const updatedDeposits = this.updatedeposite.map((deposit) => {
        return {
          id: deposit.id,
          deposite: deposit.deposite,
          scheduled_date: deposit.scheduled_date,
          amount_due: deposit.amount_due,
        };
      });
  
      try {
        await axios.put(`/api/v1/update_deposits/${praposalId}/`, updatedDeposits);
        toast({
          message: 'Deposits updated successfully',
          type: 'is-success',
          position: 'top-right',
        });
        this.$router.push(`/dashboard/proposals/${this.$route.params.praposal_id}`);
      } catch (error) {
        console.error('Error updating deposits:', error);
      }
    },
  
    onFactoryButtonClick(e) {
  const button = e.currentTarget;
  const buttonColor = button.getAttribute(''); // Specify the attribute name containing the color
  const quantity = 1; // Specify the desired quantity

  for (let i = 0; i < quantity; i++) {
    const newItem = {
      default_item_name: buttonColor,
      // default_quantity: 1,
    };

    // Add the new item to the updatedeposite array
    this.updatedeposite.push(newItem);
  }

  // Update the grid to reflect the changes
  this.gridApi.setRowData(this.updatedeposite);
},

  
      deleteItem(data) {
        const index = this.updatedeposite.indexOf(data);
        if (index > -1) {
        
          const updatedDeposite = [...this.updatedeposite];
          updatedDeposite.splice(index, 1);
          this.updatedeposite = updatedDeposite;
        }
      
        this.gridApi.setRowData(this.updatedeposite);
      },
  
      onGridReady(params) {
        this.gridApi = params.api;
        this.columnApi = params.columnApi;
        // this.gridApi.sizeColumnsToFit();
      },






      clearSignature() {
      this.signaturePad.clear();
      this.signatureData = '';
      this.previewSignature = '';
    },
    saveSignature() {
      if (this.signaturePad.isEmpty()) {
        // Handle empty signature error
        return;
      }

      // Get the signature data URL from Signature Pad
      this.signatureData = this.signaturePad.toDataURL();

      console.log('Signature Data:', this.signatureData);

      // Send signature data to the backend for verification and storage
      axios.post('/api/v1/create_signature/', { signature_data: this.signatureData })
        .then(response => {
          console.log(response.data.message);
          // Handle success
          this.previewSignature = this.signatureData; // Show the saved signature preview
        })
        .catch(error => {
          console.error(error.response.data.error);
          // Handle error
        });
    },
  













    },
  };
  </script>

  
  