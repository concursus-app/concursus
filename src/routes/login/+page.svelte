<script lang="ts">
  import { onMount } from "svelte";
  import type { PageProps } from "./$types";

  let { data, form }: PageProps = $props();

  onMount(() => {
    const circles = document.getElementById("circles");
    const colors = ["var(--primary)", "var(--secondary)", "var(--accent)"];

    for (let i = 0; i < 10; i++) {
      const circle = document.createElement("div");
      circle.style.width = `${Math.random() * 5 + 2}rem`;
      circle.style.height = circle.style.width;
      circle.style.backgroundColor =
        colors[Math.floor(Math.random() * colors.length)];
      circle.style.position = "absolute";
      circle.style.top = `${Math.random() * 60 + 10}vh`;
      circle.style.left = `${Math.random() * 60 + 10}vw`;
      circle.style.borderRadius = "100%";

      circles?.appendChild(circle);
    }
  });
</script>

<div id="circles"></div>
<div id="parent-container">
  <div id="form-container">
    <h1>Log In</h1>
    <form id="login-form" method="POST">
      <input name="email" type="email" placeholder="E-Mail" />
      <input name="password" type="password" placeholder="Password" />
      <button>Log in</button>
    </form>
  </div>
</div>

{#if form?.success}
  <p>Skibidi</p>
{/if}

<style>
  #circles {
    width: 100%;
    height: 100vh;
    position: absolute;

    top: 0;
    left: 0;
    z-index: -2;
  }

  #parent-container {
    height: 100%;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    position: absolute;
    top: 0;
    left: 0;
    pointer-events: none;
    backdrop-filter: blur(50px);
    z-index: -2;
  }

  #form-container {
    display: flex;
    flex-direction: column;

    width: 35%;
    margin: 0 auto;

    padding: 2rem;
    border-radius: 1rem;

    border: 2px solid var(--text);
    box-shadow: 0px 0px 40px 20px rgba(from var(--text) r g b / 10%);
    pointer-events: auto;
  }

  #form-container h1 {
    padding: 0;
    margin: 1rem 0;

    text-align: center;
  }

  form {
    display: flex;
    flex-direction: column;
  }

  form > input {
    margin: 0.5rem 0;
    padding: 0.5rem 0.5rem;
    border-radius: 0.5rem;

    box-sizing: border-box;

    background-color: var(--background);
    color: var(--text);
    border: 1px solid var(--text);
  }

  form button {
    padding: 1rem;
    margin: 1rem 0;

    background-color: var(--accent);
    color: var(--text);
    border: none;

    cursor: pointer;
  }

  @media (max-width: 767px) {
    #form-container {
      width: 90%;
      padding: 1rem;
    }
  }
</style>
