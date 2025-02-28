<div id="navbar">
  <a>concursus</a>
  <a>about</a>
  <a>explore</a>
  <a>contact</a>
</div>

<style lang="css">
  #navbar {
    display: flex;
    justify-content: space-between;
    width: 100%;
  }

  #navbar a {
    text-decoration: none;
    font-size: 1.2rem;
    color: var(--primary);

    transition-duration: 200ms;
    padding: 1rem 0rem;
    font-weight: 600;
  }

  #navbar > a:first-child {
    color: var(--accent);
  }

  #navbar a:hover {
    color: var(--text);

    transition-duration: 200ms;
  }
</style>
