function scrollIntoView(e) {
    const scrollTo = document.querySelector(e);
    scrollTo.scrollIntoView({ behavior: "smooth" });
  }

  const navbarMenu = document.querySelector(".menu2");
  navbarMenu.addEventListener("click", e => {
    const link = e.target.dataset.link;
    if (link == null) {
      return;
    }
  
    console.log(e.target.dataset.link);
    scrollIntoView(link);
  });