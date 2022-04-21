<template>
  <div class="center-container">
    <h1>Team 40</h1>
    <p>
      User Team besteht aus Studenten von den Departementen
      <b>Informatik</b> und <b>Technik & Architektur</b> Gemeinsam haben wir
      während 2 Semestern im Modul Produktentwicklung (PREN) zusammen am Herb-E
      gearbeitet.
    </p>
    <div>
      <div class="container">
        <div class="row">
          <h3>Informatik</h3>
          <div class="col-sm">
            <img
              src="../assets/faceImages/dave.jpg"
              alt="image of Dave"
              class="img-thumbnail mx-auto d-block"
            />
            <h5 class="nameHeading">Dave Brunner</h5>
          </div>
          <div class="col-sm">
            <img
              src="../assets/faceImages/denis.jpg"
              alt="image of Denis"
              class="img-thumbnail mx-auto d-block"
            />
            <h5 class="nameHeading">Denis Saric</h5>
          </div>
        </div>
        <div class="row">
          <h3>Elektrotechnik</h3>
          <div class="col-sm">
            <img
              src="../assets/faceImages/tim.jpg"
              alt="image of Tim"
              class="img-thumbnail mx-auto d-block"
            />
            <h5 class="nameHeading">Tim Christen</h5>
          </div>
          <div class="col-sm">
            <img
              src="../assets/faceImages/tomas.jpg"
              alt="image of Tomas"
              class="img-thumbnail mx-auto d-block"
            />
            <h5 class="nameHeading">Tomas Prajzler</h5>
          </div>
          <div class="col-sm">
            <img
              src="../assets/faceImages/emanuel.jpg"
              alt="image of Emanuel"
              class="img-thumbnail mx-auto d-block"
            />
            <h5 class="nameHeading">Emanuel Wyer</h5>
          </div>
        </div>
        <div class="row">
          <div class="col-sm">
          <h3>Maschinenbau</h3>
            <img
              src="../assets/faceImages/philip.jpg"
              alt="image of Philip"
              class="img-thumbnail mx-auto d-block"
            />
            <h5 class="nameHeading">Philip Seiler</h5>
          </div>
          <div class="col-sm">
          <h3>Digital Engineering </h3>
            <img
              src="../assets/faceImages/rachel.jpg"
              alt="image of Rachel"
              class="img-thumbnail mx-auto d-block"
            />
            <h5 class="nameHeading">Rachel Sprecher</h5>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "TeamInfo",
  created() {},
};
</script>
<style scoped>
.nameHeading {
  text-align: center;
}
div .row {
  margin-bottom: 30px;
}
</style>