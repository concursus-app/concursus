<script lang="ts">
  import { onMount } from "svelte";

  onMount(() => {
    createFuzzBalls("fuzzballs");
  });

  const createFuzzBalls = (element) => {
    const fuzzballs = document.getElementById(element);

    for (let i = 0; i < 10; i++) {
      const fuzzball = document.createElement("div");

      fuzzball.style.position = "absolute";
      fuzzball.style.width = "7.5em";
      fuzzball.style.height = "7.5em";
      fuzzball.style.borderRadius = "100%";
      fuzzball.style.backgroundColor = "var(--text)";

      fuzzball.style.top = `${Math.random() * 80 + 5}vh`;
      fuzzball.style.left = `${Math.random() * 80 + 5}vw`;

      fuzzballs?.appendChild(fuzzball);
    }
  };
</script>

<div id="fuzzballs"></div>
<div id="blurry"></div>
<div id="parent">
  <div id="form-container">
    <h1>Create your Concursus.</h1>
    <form>
      <div id="left-fields">
        <div class="input-field">
          <label for="username">username</label>
          <input type="text" id="username" name="username" required />
        </div>
        <div class="input-field">
          <label for="username">username</label>
          <input type="text" id="username" name="username" required />
        </div>
        <div class="input-field">
          <input type="submit" value="CREATE ACCOUNT" />
        </div>
      </div>
      <div id="right-fields">
        <div class="input-field">
          <label for="username">username</label>
          <input type="text" id="username" name="username" required />
        </div>
        <div class="input-field">
          <label for="username">username</label>
          <input type="text" id="username" name="username" required />
        </div>
        <div class="input-field">
          <input type="button" value="LOGIN INSTEAD" />
        </div>
      </div>
    </form>
    <div id="divider-holder">
      <h2 id="divider">OR REGISTER WITH</h2>
    </div>
    <div id="alternative-methods"></div>
  </div>
</div>

<style>
  #fuzzballs {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;

    z-index: -2;
  }

  #blurry {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;

    backdrop-filter: blur(5em);
    z-index: -1;
  }

  #parent {
    height: calc(100vh - var(--navbar-height));
    width: 100%;

    display: flex;
    justify-content: center;
    align-items: center;
  }

  #form-container {
    width: 100%;
    background-color: rgba(from var(--mantle) r g b / 75%);

    padding: 2rem;
    box-sizing: border-box;
    border-radius: 25px;
  }

  #form-container h1 {
    margin: 0;
    font-size: 64px;
    font-weight: 600;
  }

  #divider-holder {
    display: flex;
    justify-content: center;
    align-items: center;
  }

  #divider {
    text-align: center;
    font-weight: 100;
    letter-spacing: 0.1em;
  }

  #divider-holder::before,
  #divider-holder::after {
    content: "";
    flex-grow: 1;
    height: 2px;
    background-color: var(--text);
  }

  #divider-holder::before {
    margin-right: 1rem;
  }

  #divider-holder::after {
    margin-left: 1rem;
  }

  form {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
  }

  form > div {
    flex-basis: 47.5%;
  }

  .input-field {
    display: inline-block;
    padding: 0.2em 1em 0.5em 1em;
    box-sizing: border-box;
    width: 100%;

    border-radius: 3em;
    background-color: var(--surface-0);
    margin: 1rem 0;

    height: 3em;
  }

  .input-field label {
    display: block;
    font-size: 1.2rem;
    font-weight: 100;
  }

  .input-field input {
    outline: none;
    border: none;
    display: block;
    line-height: 1.2em;
    font-size: 14pt;
    width: 100%;

    background-color: transparent;
    color: var(--text);
  }

  .input-field:has(input[type="submit"]) {
    background-color: var(--accent);
  }

  input[type="submit"],
  input[type="button"] {
    height: 100%;
    line-height: 2em;
    letter-spacing: 0.2em;
  }

  .input-field:has(input[type="button"]) {
    border: 2px solid var(--accent);
  }
</style>
