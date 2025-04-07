<script lang="ts">
  import Navbar from "../components/navbar.svelte";
  import "../app.css";

  let { children } = $props();
</script>

<svelte:head>
  <title>Concursus</title>
</svelte:head>

<main>
  <Navbar />
  {@render children()}
</main>

<style lang="css">
  main {
    width: 70vw;

    margin: 0 auto;
  }
</style>
