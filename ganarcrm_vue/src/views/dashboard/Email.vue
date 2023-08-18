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
















  
<!-- <script>
  import { reactive } from 'vue';
  import axios from 'axios';

  export default {
    name: 'AddProposal',

    data() {
      return {
        form: [
          {
            name: '',
            company: '',
            phone: '',
            city: '',
            date: '',
            start_time: '',
            end_time: '',
            event: '',
            setup: '',
            venue: '',
            attendance: '',
            rate: '',
            package: '',
            buffet: 0,
            addition: 0,
            menu: 0,
          },
        ],
        packages: [], // Populate with your package data
        buffets: [], // Populate with your buffet data
        additions: [], // Populate with your addition data
        menus: [], // Store menus for each form row
      };
    },
    methods: {
      addRow() {
        this.form.push({
          name: '',
          company: '',
          phone: '',
          city: '',
          date: '',
          start_time: '',
          end_time: '',
          event: '',
          setup: '',
          venue: '',
          attendance: '',
          rate: '',
          package: 0,
          buffet: 0,
          addition: 0,
          menu: 0,
        });
      },
      removeRow(index) {
        if (this.form.length > 1) {
          this.form.splice(index, 1);
        }
      },
      submitForm() {
        this.$store.commit('setIsLoading', true);

        const proposal = {
          proposals: this.form.map((item) => ({
            ...item,
            menu: item.menu.map((menuItem) => ({ soup: menuItem.soup })),
          })),
        };

        axios
          .post('/api/v1/create_proposal/', proposal)
          .then((response) => {
            this.$router.push('/dashboard/proposals');
          })
          .catch((error) => {
            console.log(error);
          })
          .finally(() => {
            this.$store.commit('setIsLoading', false);
          });
      },

       fetchMenus() {
        const buffetId = document.getElementById('buffet').value;
        const additionId = document.getElementById('addition').value;

        axios
          .get(`/api/v1/get_menu?buffet=${buffetId}&addition=${additionId}`)
          .then((response) => {
            this.menus = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
      },
      
      buffetField() {
        const buffetId = document.getElementById('buffet').value;
        window.location = "/?buffet=" + buffetId;
      },
      additionField() {
        const additionId = document.getElementById('addition').value;
        const buffet = this.getQueryParameter('buffet');
        const url = "/?buffet=" + encodeURIComponent(buffet) + "&addition=" + additionId;
        window.location = url;
      },
      getQueryParameter(parameterName) {
        const queryString = window.location.search.substring(1);
        const parameters = queryString.split('&');
        for (let i = 0; i < parameters.length; i++) {
          const parameter = parameters[i].split('=');
          if (parameter[0] === parameterName) {
            return decodeURIComponent(parameter[1]);
          }
        }
        return null;
      },
    },
    mounted() {
      const buffetId = this.getQueryParameter('buffet');
      const additionId = this.getQueryParameter('addition');

      document.getElementById('buffet').value = buffetId;
      document.getElementById('addition').value = additionId;

      this.fetchMenus(); // Fetch the menu data on component mount
    },
  };
</script> -->