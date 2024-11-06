function BotonMeGusta(button) {
    button.classList.toggle("clicked");

    for (let i = 0; i < 10; i++) {
      const particle = document.createElement("span");
      particle.classList.add("particle");
      particle.style.top = Math.random() * 100 + "%";
      particle.style.left = Math.random() * 100 + "%";
      document.body.appendChild(particle);

      setTimeout(() => {
        particle.remove();
      }, 1000);
    }
  }