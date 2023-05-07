$(document).ready(function () {
  function Carousel1__onTranslated() {
    $(".carousel-1 > .owl-carousel").trigger("play.owl.autoplay");
    $(".carousel-1").attr("data-carousel-1-autoplay-status", "Y");
  }

  // 모바일일 때 초기화
  function updateCarouselImages() {
    if ($(window).width() < 768) {
      $('.owl-carousel .item img').each(function () {
        $(this).attr('src', $(this).data('src-mobile'));
      });
    } else {
      $('.owl-carousel .item img').each(function () {
        $(this).attr('src', $(this).data('src-desktop'));
      });
    }
  }

  function Carousel1__onInitialized() {
    updateCarouselImages();
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
    onInitialized: Carousel1__onInitialized,
  });

  $(".carousel-1 .play").on("click", function () {
    $(".carousel-1 > .owl-carousel").trigger("play.owl.autoplay");
    $(".carousel-1").attr("data-carousel-1-autoplay-status", "Y");
  });

  $(".carousel-1 .stop").on("click", function () {
    $(".carousel-1 > .owl-carousel").trigger("stop.owl.autoplay");
    $(".carousel-1").attr("data-carousel-1-autoplay-status", "N");
  });

  // 창 크기가 변경될 때마다 이미지 업데이트
  $(window).resize(function () {
    updateCarouselImages();
  });
});
