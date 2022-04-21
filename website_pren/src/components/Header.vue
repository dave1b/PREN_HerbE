<template>
  <header>
    <nav class="navbar navbar-dark bg-dark navbar-expand-lg">
      <div class="container-fluid">
           <router-link to="/" class="navbar-brand">
          <img
            src="../assets/herb-e.png"
            width="100"
            style="margin-top: -5px"
          />
           </router-link>
           <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item active-link" > 
              <router-link to="/" class="nav-link" style="margin-bottom: 5px"  v-bind:class="{'active':('Home' == this.$route.name)}">
              Herb-E
            </router-link>
            </li>
            <li class="nav-item active-link"> 
              <router-link to="/team" class="nav-link" style="margin-bottom: 5px" v-bind:class="{'active':('Team' == this.$route.name)}">
              Unser Team
            </router-link>
            </li>
            <li class="nav-item active-link"> 
              <router-link to="/construction" class="nav-link" style="margin-bottom: 5px" v-bind:class="{'active':('Construction' == this.$route.name)}">
              Konstruktion
            </router-link>
            </li>
            <li class="nav-item active-link"> 
              <router-link to="/sponsoren" class="nav-link" style="margin-bottom: 5px" v-bind:class="{'active':('Sponsoren' == this.$route.name)}">
              Sponsoren
            </router-link>
            </li>
          </ul>
        </div>
        
      </div>
    </nav>
  </header>
</template>

<script>
export default {
  name: "Header",
  data() {
    return {};
  },
  methods: {},
};
</script>

<style scoped>
li {
  margin-left: 10px
}
</style>