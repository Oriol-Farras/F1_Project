document.addEventListener("DOMContentLoaded", function () {
    console.log("Página cargada correctamente");

    const navbarLinks = document.querySelectorAll(".nav-link");

    navbarLinks.forEach(link => {
        link.addEventListener("click", function () {
            navbarLinks.forEach(l => l.classList.remove("active"));
            this.classList.add("active");
        });
    });
});
