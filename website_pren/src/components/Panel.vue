<template>
  <h1>Hello There</h1>
  <h1>{{ count }}</h1>
  <div>
    <button type="button" class="btn btn-primary" v-on:click="increment()" >{{btnName}}</button>
  </div>
  <div v-html="btnName"></div>

</template>

<script>
export default {
  name: "Panel",
  data() {
    return {
      count: 1,
      btnName: "Lets go and count!"
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

<style scoped>
h1 {
  color: red;
}
</style>
