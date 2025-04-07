<div id="navbar">
  <a href="/">CONCURSUS</a>
  <div id="lefty">
    <a>about</a>
    <a>explore</a>
    <a>contact</a>
  </div>
</div>

<style lang="css">
  #navbar {
    display: flex;
    justify-content: space-between;
    width: 100%;

    height: var(--navbar-height);
  }

  #navbar a {
    text-decoration: none;
    font-size: 1.2rem;
    color: var(--text);

    transition-duration: 200ms;
    padding: 1rem 0;
    cursor: pointer;

    letter-spacing: 0.2rem;
  }

  #navbar > a:first-child {
    color: var(--accent);
  }

  #navbar a:hover {
    color: var(--text);

    transition-duration: 200ms;
  }

  #lefty {
    flex-basis: 50%;

    display: flex;
    justify-content: space-between;
  }
</style>
