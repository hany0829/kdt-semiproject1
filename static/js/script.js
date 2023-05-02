$(document).ready(function () {
  function Carousel1__onTranslated() {
    $(".carousel-1 > .owl-carousel").trigger("play.owl.autoplay");
    $(".carousel-1").attr("data-carousel-1-autoplay-status", "Y");
  }

  $(".carousel-1 > .owl-carousel").owlCarousel({
    autoplay: true,
    autoplayTimeout: 2000,
    loop: true,
    margin: 0,
    nav: true,
    navText: [
      '<i class="fas fa-angle-left"></i>',
      '<i class="fas fa-angle-right"></i>',
    ],
    responsive: {
      0: {
        items: 1,
      },
    },
    autoplayHoverPause: false,
    onTranslated: Carousel1__onTranslated,
  });

  $(".carousel-1 .play").on("click", function () {
    $(".carousel-1 > .owl-carousel").trigger("play.owl.autoplay");
    $(".carousel-1").attr("data-carousel-1-autoplay-status", "Y");
  });

  $(".carousel-1 .stop").on("click", function () {
    $(".carousel-1 > .owl-carousel").trigger("stop.owl.autoplay");
    $(".carousel-1").attr("data-carousel-1-autoplay-status", "N");
  });
});
