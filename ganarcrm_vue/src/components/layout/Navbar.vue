<template>
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item">
          <strong>Ganar CRM</strong>
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
                    <router-link to="/dashboard/my-account" class="navbar-item">My Account</router-link>
                    <!-- <router-link to="/profile" class="navbar-item">Profile</router-link> -->
                    <!-- <a class="navbar-item" @click="logout">Logout</a> -->
                  </div>
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
</style>




