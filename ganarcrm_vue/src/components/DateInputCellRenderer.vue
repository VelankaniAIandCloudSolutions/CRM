<!-- <template>
  <input type="date" :value="dateValue" @input="onDateInput" />
</template>

<script>
export default {
  props: {
    value: String, // The 'scheduled_date' data passed from the grid
  },
  data() {
    return {
      dateValue: this.value || '', // Initialize the dateValue with the passed value (if any)
    };
  },
  methods: {
    onDateInput(event) {
      // Update the 'dateValue' when the user inputs a new date
      this.dateValue = event.target.value;
      // Emit the 'input' event to send the updated date to the grid
      this.$emit('input', this.dateValue);
    },
  },
};
</script> -->
