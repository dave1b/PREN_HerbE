<template>
  <footer>
    <div class="middle">
      <div class="container">
        <div class="row">
          <div class="col-sm">
            <h7>Team 40 - HSLU - PREN 2022</h7>
            <ul style="list-style: none">
              <li>Dave Brunner</li>
              <li>Rachel Sprecher</li>
              <li>Emanuel Wyer</li>
              <li>Philip Seiler</li>
              <li>Tomas Prajzler</li>
              <li>Denis Saric</li>
            </ul>
          </div>
          <div class="col-sm">
            <h7>Social Media</h7>
            <div class="">
              <a
                class="footer-btn"
                href="https://www.youtube.com/channel/UCtmv4LU7WXBFtNVOQaqm8TQ"
              >
                <i class="fab fa-youtube"></i>
              </a>
              <a
                class="footer-btn"
                href="https://www.instagram.com/sportteam_bbzg_w_sursee/"
              >
                <i class="fab fa-instagram"></i>
              </a>
              <a
                class="footer-btn"
                href="https://www.linkedin.com/in/dave-b-a7a158199"
              >
                <i class="fab fa-linkedin-in"></i>
              </a>
              <a class="footer-btn" href="mailto:dave.brunner@protonmail.ch">
                <i class="fa-solid fa-envelope"></i>
              </a>
            </div>
          </div>
          <div class="col-sm">
            <h7>Hochschule</h7>
            <div>
              <img src="../assets/hslu_logo.svg" style="padding-top: 15px" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: "Footer",
  data() {
    return {};
  },
  methods: {},
};
</script>

<style scoped>
h7 {
  font-size: larger;
  font-weight: bold;
  text-decoration: underline 2px;
  text-underline-offset: 5px;
}
</style>