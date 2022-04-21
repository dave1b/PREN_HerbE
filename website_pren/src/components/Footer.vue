<template>
  <footer>
    <div class="middle">
      <div class="container">
        <div class="row">
          <div class="col-sm">
            <h7>Team 40 - HSLU - PREN 2022</h7>
            <ul style="list-style: none">
              <li>Tim Christen</li>
              <li>Dave Brunner</li>
              <li>Tomas Prajzler</li>
              <li>Denis Saric</li>
              <li>Philip Seiler</li>
              <li>Rachel Sprecher</li>
              <li>Emanuel Wyer</li>
            </ul>
          </div>
          <div class="col-sm">
            <h7>Social Media</h7>
            <div class="">
              <a
                class="footer-btn"
                href="https://www.youtube.com/c/HochschuleLuzern-HSLU"
                target="_blank"
              >
                <i class="fab fa-youtube"></i>
              </a>
              <a
                class="footer-btn"
                href="https://www.instagram.com/hslu_luzern/"
              >
                <i class="fab fa-instagram"></i>
              </a>
              <a
                class="footer-btn"
                href="https://www.linkedin.com/school/hslu-hochschule-luzern/"
                target="_blank"
              >
                <i class="fab fa-linkedin-in"></i>
              </a>
              <a class="footer-btn" href="mailto:dave.brunner@stud.hslu.ch">
                <i class="fa-solid fa-envelope"></i>
              </a>
            </div>
          </div>
          <div class="col-sm">
            <h7>Hochschule</h7>
            <div>
            <a href="https://www.hslu.ch/de-ch/" style="text-decoration: none;" target="_blank">
              <img src="../assets/hslu_logo.svg" style="padding-top: 15px" />
            </a>
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