<template>
  <nav class="navbar is-dark" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <a class="navbar-item" href="/">
        <strong>CRM</strong>
      </a>
      <a
        role="button"
        class="navbar-burger burger"
        aria-label="menu"
        aria-expanded="false"
        @click="toggleMenu"
        :class="{ 'is-active': isMenuActive }"
        data-target="navbarMenu"
      >
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>

    <div id="navbarMenu" class="navbar-menu" :class="{ 'is-active': isMenuActive }">
      <div class="navbar-start">
        <template v-if="$store.state.isAuthenticated">
          <a class="navbar-item" href="/dashboard">
            <span class="icon is-small">
              <i class="fas fa-tachometer-alt" style="margin-right:13px;"></i>
            </span>
            <span>Dashboard</span>
          </a>
          <a class="navbar-item" href="/dashboard/leads">
            <span class="icon is-small">
              <i class="fas fa-user-friends" style="margin-right:13px; color:white;"></i>
            </span>
            <span style="color:white;">Leads</span>
          </a>
          <a class="navbar-item" href="/dashboard/clients">
            <span class="icon is-small">
              <i class="fas fa-users" style="margin-right:18px;color:white;"></i>
            </span>
            <span style="color:white;">Clients</span>
          </a>
          <a class="navbar-item" href="/dashboard/team">
            <span class="icon is-small">
              <i class="fas fa-users" style="margin-right:20px;"></i>
            </span>
            <span>Team</span>
          </a>
          <a class="navbar-item" href="/dashboard/proposals">
            <span class="icon is-small">
              <i class="fas fa-file-alt" style="margin-right:13px;"></i>
            </span>
            <span>Proposal</span>
          </a>
          <div class="navbar-item has-dropdown is-hoverable">
            <a class="navbar-link">
              <span class="icon is-small">
                <i class="fas fa-file-invoice-dollar" style="margin-right:13px;"></i>
              </span>
              <span>Quotations</span>
            </a>
            <div class="navbar-dropdown">
              <a class="navbar-item" href="/dashboard/quotes">
                All Quotations
              </a>
              <a class="navbar-item" href="/dashboard/accepted_quotes">
                Accepted Quotations
              </a>
              <a class="navbar-item" href="/dashboard/rejected_quotes">
                Rejected Quotations
              </a>
            </div>
          </div>
        </template>
      </div>

      <div class="navbar-end">
        <div class="navbar-item">
          <div class="buttons">
            <template v-if="!$store.state.isAuthenticated">
              <router-link to="/sign-up" class="button is-success"><strong>Sign up</strong></router-link>
              <router-link to="/log-in" class="button is-light">Log in</router-link>
            </template>

            <template v-else>
              <div class="navbar-item">
                <router-link to="/dashboard/my-account" class="navbar-item" style="color:white;">My Account</router-link>
              </div>
            </template>
          </div>
        </div>
      </div>
    </div>
  </nav>
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
.navbar {
  background-color: #1f1f1f;
  color: #ffffff;
  font-size: 1.2rem;
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 100;
}

.navbar-item {
  font-size: 1.2rem;
  margin: 0 0.5rem;
}

/* .navbar-item:hover {
  background-color: transparent;
  color: #ffffff;
}

.navbar-link {
  color: #ffffff;
}

.navbar-link:hover {
  color: #ffffff;
} */

.navbar-dropdown {
  background-color: #ffffff;
  border-radius: 0.25rem;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
}

.navbar-burger {
  border: none;
  background-color: transparent;
  cursor: pointer;
  color: #ffffff;
  position: relative;
  z-index: 2;
}

.navbar-burger span {
  background-color: #ffffff;
  display: block;
  height: 0.2rem;
  margin: 0.4rem 0;
  transition: transform 0.2s ease-out;
  width: 1.5rem;
}

.navbar-burger span:first-child {
  transform-origin: top-left;
}

.navbar-burger span:last-child {
  transform-origin: bottom-left;
}

.navbar-burger.is-active span:first-child {
  transform: rotate(45deg) translate(0.4rem, 0.4rem);
}

.navbar-burger.is-active span:nth-child(2) {
  opacity: 0;
}

.navbar-burger.is-active span:last-child {
  transform: rotate(-45deg) translate(0.4rem, -0.4rem);
}

@media screen and (max-width: 768px) {
  .navbar-item {
    margin: 0.5rem 0;
  }

  .navbar-menu {
    background-color: #1f1f1f;
    position: fixed;
    top: 56px;
    left: 0;
    right: 0;
    z-index: 100;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    transform: translateY(-100%);
    transition: transform 0.2s ease-out;
  }

  .navbar-menu.is-active {
    transform: translateY(0);
  }

  .navbar-dropdown {
    position: static;
    box-shadow: none;
  }
}
</style>












































<!-- <template>
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
</style> -->












<!-- <template>
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item">
          <strong> CRM </strong>
        </router-link>
        <button class="navbar-burger burger" @click="toggleMenu" :class="{ 'is-active': isMenuActive }">
          <span></span>
          <span></span>
          <span></span>
        </button>
      </div>
  
      <div class="navbar-menu" :class="{ 'is-active': isMenuActive }">
        <div class="navbar-start">
          <template v-if="$store.state.isAuthenticated">
            <router-link to="/dashboard/" class="navbar-item">Dashboard</router-link>
            <div class="navbar-item has-dropdown is-hoverable">
              <a class="navbar-link">
                Leads
              </a>
              <div class="navbar-dropdown">
                <router-link to="/dashboard/leads" class="navbar-item">All Leads</router-link>
              </div>
            </div>
            <div class="navbar-item has-dropdown is-hoverable">
              <a class="navbar-link">
                Clients
              </a>
              <div class="navbar-dropdown">
                <router-link to="/dashboard/clients" class="navbar-item">All Clients</router-link>
              </div>
            </div>
            <router-link to="/dashboard/team" class="navbar-item">Team</router-link>

            <router-link to='/dashboard/proposals' class="navbar-item">Proposal</router-link>

            <div class="navbar-item has-dropdown is-hoverable">
              <a class="navbar-link">
                Quotatons
              </a>
              <div class="navbar-dropdown">
                <router-link to="/dashboard/quotes" class="navbar-item">All Quotations</router-link>
                <router-link to="/dashboard/accepted_quotes" class="navbar-item">Accepted Quotations</router-link>
                <router-link to="/dashboard/rejected_quotes" class="navbar-item">Rejected Quotations</router-link>
                
              </div>
            </div>
          </template>
        </div>
  
        <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons">
              <template v-if="!$store.state.isAuthenticated">
                <router-link to="/sign-up" class="button is-success"><strong>Sign up</strong></router-link>
                <router-link to="/log-in" class="button is-light">Log in</router-link>
              </template>
  
              <template v-else>
                <div class="navbar-item has-dropdown is-hoverable">
                  <a class="navbar-link">
                    My account
                  </a>
                  <div class="navbar-dropdown">
                    <router-link to="/dashboard/my-account" class="navbar-item">My Account</router-link> -->
                    <!-- <router-link to="/profile" class="navbar-item">Profile</router-link> -->
                    <!-- <a class="navbar-item" @click="logout">Logout</a> -->
                  <!-- </div>
                </div>
              </template>
            </div>
          </div>
        </div>
      </div>
    </nav>
  </template> -->
  
  <!-- <script>
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
  
  <style >
    .navbar {
  background-color: #1f1f1f;
  color: #ffffff;
  font-size: 1.2rem;
}

.navbar-item {
  font-size: 1.2rem;
  margin: 0 0.5rem;
}

.navbar-item:hover {
  background-color: #ffffff;
  color: #1f1f1f;
}

.navbar-link {
  color: #ffffff;
}

.navbar-link:hover {
  color: #1f1f1f;
}

.navbar-dropdown {
  background-color: #ffffff;
  border-radius: 0.25rem;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
}

.navbar-burger {
  border: none;
  background-color: transparent;
  cursor: pointer;
}

.navbar-burger span {
  background-color: #ffffff;
  display: block;
  height: 0.2rem;
  margin: 0.4rem 0;
  transition: transform 0.2s ease-out;
  width: 1.5rem;
}

.navbar-burger span:first-child {
  transform-origin: top-left;
}

.navbar-burger span:last-child {
  transform-origin: bottom-left;
}

.navbar-burger.is-active span:first-child {
  transform: rotate(45deg) translate(0.4rem, 0.4rem);
}

.navbar-burger.is-active span:nth-child(2) {
  opacity: 0;
}

.navbar-burger.is-active span:last-child {
  transform: rotate(-45deg) translate(0.4rem, -0.4rem);
}

@media screen and (max-width: 768px) {
  .navbar-item {
    margin: 0.5rem 0;
  }
  
  .navbar-menu {
    background-color: #1f1f1f;
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    z-index: 10;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    transform: translateX(-100%);
    transition: transform 0.2s ease-out;
  }
  
  .navbar-menu.is-active {
    transform: translateX(0);
  }
  
  .navbar-dropdown {
    position: static;
    box-shadow: none;
  }
}
</style> -->




