<template>
  <div class="center-container">
    <div class="card">
      <div class="card-body">
        <h1 class="card-title">Aktulle Informationen</h1>

        <div class="inCard-container">
          <table class="table table-success table-striped">
            <tbody>
              <tr>
                <td>Startzeitpunkt</td>
                <td>1</td>
              </tr>
              <tr>
                <td>Laufzeit</td>
                <td>1</td>
              </tr>
              <tr>
                <td>Distanz</td>
                <td>2</td>
              </tr>
              <tr>
                <td>Zustand</td>
                <td>3</td>
              </tr>
              <tr>
                <td>Erkannte Pflanzenart</td>
                <td>3</td>
              </tr>
              <tr>
                <td>Position der gleichen Pflanze</td>
                <td>3</td>
              </tr>
            </tbody>
          </table>
        </div>

        <a href="#" class="btn btn-primary">Go somewhere</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Panel",
  data() {
    return {
      count: 1,
      btnName: "Lets go and count!",
    };
  },
  methods: {
    increment() {
      this.count++;
    },
  },

  mounted() {
    this.count = 0;
  },
};
</script>

<style scoped></style>
