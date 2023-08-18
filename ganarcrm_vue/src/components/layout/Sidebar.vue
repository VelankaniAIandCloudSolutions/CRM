
<template>
  <br>
  <br>
  <div class="sidebar">
    <div class="sidebar-brand">
      <a class="sidebar-item" href="/">
        <strong>CRM</strong>
      </a>
      <a role="button" class="sidebar-burger burger" aria-label="menu" aria-expanded="false" @click="toggleMenu" :class="{ 'is-active': isMenuActive }" data-target="sidebarMenu">
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>
    <div id="sidebarMenu" class="sidebar-menu" :class="{ 'is-active': isMenuActive }">
      <div class="sidebar-start">
        <template v-if="$store.state.isAuthenticated">
          <a class="sidebar-item" href="/dashboard">
            <span class="icon is-small">
              <i class="fas fa-tachometer-alt" style="margin-right:13px;"></i>
            </span>
            <span>Dashboard</span>
          </a>
          <div class="sidebar-item has-dropdown is-hoverable">
            <a class="sidebar-link">
              <span class="icon is-small">
                <i class="fas fa-user-friends" style="margin-right:13px;"></i>
              </span>
              <span>Leads</span>
            </a>
            <div class="sidebar-dropdown">
              <a class="sidebar-item" href="/dashboard/leads">
                All Leads
              </a>
            </div>
          </div>
          <div class="sidebar-item has-dropdown is-hoverable">
            <a class="sidebar-link">
              <span class="icon is-small">
                <i class="fas fa-users" style="margin-right:18px;"></i>
              </span>
              <span>Clients</span>
            </a>
            <div class="sidebar-dropdown">
              <a class="sidebar-item" href="/dashboard/clients">
                All Clients
              </a>
            </div>
          </div>
          <a class="sidebar-item" href="/dashboard/team">
            <span class="icon is-small">
              <i class="fas fa-users" style="margin-right:20px;"></i>
            </span>
            <span>Team</span>
          </a>
          <a class="sidebar-item" href="/dashboard/proposals">
            <span class="icon is-small">
              <i class="fas fa-file-alt" style="margin-right:13px;"></i>
            </span>
            <span>Proposal</span>
          </a>
          <div class="sidebar-item has-dropdown is-hoverable">
            <a class="sidebar-link">
              <span class="icon is-small">
                <i class="fas fa-file-invoice-dollar" style="margin-right:13px;"></i>
              </span>
              <span>Quotations</span>
            </a>
            <div class="sidebar-dropdown">
              <a class="sidebar-item" href="/dashboard/quotes">
                All Quotations
              </a>
              <a class="sidebar-item" href="/dashboard/accepted_quotes">
                Accepted Quotations
              </a>
              <a class="sidebar-item" href="/dashboard/rejected_quotes">
                Rejected Quotations
              </a>
            </div>
          </div>
        </template>
      </div>

      <div class="sidebar-end">
        <div class="sidebar-item">
          <div class="buttons">
            <template v-if="!$store.state.isAuthenticated">
              <a class="button is-success" href="/sign-up">
                <strong>Sign up</strong>
              </a>
              <a class="button is-light" href="/log-in">
                Log in
              </a>
            </template>

            <template v-else>
              <div class="sidebar-item has-dropdown is-hoverable">
                <a class="sidebar-link">
                  <span class="icon is-small">
                    <i class="fas fa-user" style="margin-right:13px;"></i>
                  </span>
                  <span>My Account</span>
                </a>
                <div class="sidebar-dropdown">
                  <a class="sidebar-item" href="/dashboard/my-account">
                    My Account
                  </a>
                 
                </div>
              </div>
            </template>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import router from '../../router';

export default {
  data() {
    return {
      isMenuActive: false
    };
  },
  computed: {
    isAuthenticated() {
      return this.$store.state.isAuthenticated;
    }
  },
  methods: {
    toggleMenu() {
      this.isMenuActive = !this.isMenuActive;
    },
    logout() {
      this.$store.dispatch("logout");
    }
  },
  components: { router }
};
</script>

<style>
.sidebar {
  width: 250px;
  height:700px;
  background-color: #212529;
  color: #fff;
  padding: 20px;
}

.sidebar-header {
  padding-bottom: 20px;
  border-bottom: 1px solid #fff;
}

.sidebar-title {
  margin: 0;
  font-size: 1.5rem;
}

.sidebar-menu {
  margin-top: 20px;
}

.sidebar-menu .sidebar-item {
  display: block;
  color: #fff;
  text-decoration: none;
  margin-bottom: 10px;
}

.sidebar-menu .sidebar-item .icon {
  margin-right: 13px;
}

.sidebar-menu .sidebar-dropdown {
  display: none;
  margin-left: 20px;
}

.sidebar-menu .sidebar-dropdown .sidebar-item {
  margin-bottom: 5px;
}

.sidebar-menu .sidebar-item:hover,
.sidebar-menu .sidebar-dropdown:hover {
  background-color: #ffffff;
  color: #1f1f1f;
}

.sidebar-menu .sidebar-link {
  color: #ffffff;
}

.sidebar-menu .sidebar-link:hover {
  color: #1f1f1f;
}

.sidebar-menu .is-active .sidebar-dropdown,
.sidebar-menu .is-active .sidebar-dropdown .sidebar-item {
  display: block;
}

.content {
  flex: 1;
  padding: 20px;
  overflow-y: auto;
}
</style>