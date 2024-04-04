// banner.js
document.addEventListener("DOMContentLoaded", function() {
    var cerrarBoton = document.querySelector(".cerrar-anuncio");
    var banner = document.getElementById("bannerLateral");

    cerrarBoton.addEventListener("click", function() {
        banner.style.display = "none";
    });
});


document.addEventListener("DOMContentLoaded", function() {
    var cerrarBoton = document.querySelector(".cerrarBanner");
    var baner = document.getElementById("banner-inferior");

    cerrarBoton.addEventListener("click", function() {
        baner.style.display = "none";
    });
});