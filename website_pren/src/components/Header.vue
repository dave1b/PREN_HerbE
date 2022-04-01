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
          &nbsp; &nbsp; Herb-E
           </router-link>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item active-link"> 
              <router-link to="/team" class="nav-link" style="margin-bottom: 5px">
              Team 40
            </router-link>
            </li>
            <li class="nav-item active-link"> 
              <router-link to="/team" class="nav-link" style="margin-bottom: 5px">
              Konstruktion
            </router-link>
            </li>
            <li class="nav-item active-link"> 
              <router-link to="/team" class="nav-link" style="margin-bottom: 5px">
              Sponsoren
            </router-link>
            </li>
          </ul>
        </div>
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