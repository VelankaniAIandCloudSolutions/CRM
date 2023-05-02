<!-- <template>
    <div>
      <h1>Send Email</h1>
      <form @submit.prevent="sendEmail">
        <div>
          <label for="to">To:</label>
          <input type="email" id="to" v-model="to" required>
        </div>
        <div>
          <label for="subject">Subject:</label>
          <input type="text" id="subject" v-model="subject" required>
        </div>
        <div>
          <label for="message">Message:</label>
          <textarea id="message" v-model="message" required></textarea>
        </div>
        <button type="submit">Send</button>
      </form>
    </div>
  </template>
  
  <script>

  import axios from 'axios'
  export default {
    data() {
      return {
        to: '',
        subject: '',
        message: '',
      }
    },
    methods: {
      sendEmail() {
        const data = {
          to: this.to,
          subject: this.subject,
          message: this.message,
          tableHtml: '<table><thead><tr><th>Name</th><th>Age</th></tr></thead><tbody><tr><td>John Doe</td><td>30</td></tr><tr><td>Jane Smith</td><td>25</td></tr></tbody></table>'
        }
        axios.post('/api/v1/send_email/', data)
          .then(response => {
            console.log(response)
            // Show success message
            this.$router.push('/success/')
          })
          .catch(error => {
            console.log(error)
            // Show error message
          })
      }
    }
  }
  </script> -->