<template>
  <div class="center-container">
    <div class="card">
      <div class="card-body">
        <h1 class="card-title">Aktuelle Informationen</h1>

        <div class="inCard-container">
          <table class="table table-dark table-striped ">
            <tbody>
              <tr>
                <td>Startzeitpunkt</td>
                <td>{{ startZeitDatum }}</td>
              </tr>
              <tr>
                <td>Laufzeit</td>
                <td>{{ laufzeit }}</td>
              </tr>
              <tr>
                <td>Distanz</td>
                <td>{{ distanz }} Meter</td>
              </tr>
              <tr>
                <td>Zustand</td>
                <td>{{ zustand }}</td>
              </tr>
              <tr>
                <td>Erkannte Pflanzenart</td>
                <td>{{ erkenntePflanze }}</td>
              </tr>
              <tr>
                <td>Position der gleichen Pflanze</td>
                <td>{{ positionDerGleichenPflanze }}</td>
              </tr>
            </tbody>
          </table>
        </div>
        <h3>Fortschritt von Herb-E</h3>
        <h4 style="float: left">| Start</h4>
        <h4 style="float: right"> Ende |</h4>
        <div class="progress" style="height: 20px; clear: both;">
          <div
            class="progress-bar"
            :class="{ 'progress-bar-striped progress-bar-animated bg-info': !finished, 'bg-success': finished  }"
            role="progressbar"
            :style="{ width: distanz + '%' }"
            aria-valuenow="25"
            aria-valuemin="0"
            aria-valuemax="100"
          ></div>
          <img src="../assets/herb-e_mirror.png" width="50" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { io } from "socket.io-client";
export default {
  name: "Panel",
  data() {
    return {
      socket: io("http://prenh21-dbrunner.enterpriselab.ch:8080", {
        transports: ["websocket"],
      }),
      timer: undefined,
      isConnected: false,
      startZeitDatum: "",
      startZeitStamp: null,
      endZeitStamp: null,
      laufzeit: "",
      distanz: "",
      zustand: "",
      erkenntePflanze: "",
      positionDerGleichenPflanze: "",
    };
  },
  methods: {
    start() {
      this.timer = setInterval(() => {
        this.updateLaufzeit(Date.now());
      }, 1000);
    },
    stop() {
      clearInterval(this.timer);
    },
    updateLaufzeit(zeitStamp) {
      var laufzeitInMilli = Math.floor(
        (zeitStamp - this.startZeitStamp) / 1000
      );
      this.laufzeit =
        Math.floor(laufzeitInMilli / 60).toString() +
        " Minuten " +
        (laufzeitInMilli % 60).toString() +
        " Sekunden";
    },
  },
  mounted() {
    this.socket.on("runUpdated", (run) => {
      this.startZeitDatum = run.dateTimeStamp;
      this.startZeitStamp = run.startTimeStamp;
      this.endZeitStamp = run.endTimeStamp;
      this.distanz = run.distance;
      this.zustand = run.state;
      this.erkenntePflanze = run.plantType;
      this.positionDerGleichenPflanze = run.plantMatchPosition;
      this.finished = run.isFinished;
      if (this.endZeitStamp > 0 && this.finished == true) {
        this.updateLaufzeit(this.endZeitStamp);
        this.stop();
      } else {
        this.updateLaufzeit(Date.now());
        if (this.timer == undefined) {
          this.start();
        }
      }
    }),
      this.socket.on("connect", () => {
        console.log("Successfully connected!");
      });
  },
  created() {},
};
</script>
<style scoped></style>