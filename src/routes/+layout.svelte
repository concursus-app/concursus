<script lang="ts">
  import Navbar from "../components/navbar.svelte";
  // import main.js
  import "../main.js";

  let { children } = $props();
</script>

<main>
  <Navbar />
  {@render children()}
</main>

<style lang="css">
  main {
    width: 75vw;

    margin: 0 auto;
  }
</style>
