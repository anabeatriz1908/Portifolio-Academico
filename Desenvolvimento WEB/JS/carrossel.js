const progressCircle = document.querySelector(".autoplay-progress svg");
const progressContent = document.querySelector(".autoplay-progress span");
var swiper = new Swiper(".slide-content", {
    spaceBetween: 25,
    centeredSlides: 'true',
    loop: 'true',
    fade: 'true',
    autoplay: {
    delay: 2500,
    disableOnInteraction: false
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev"
    },

    on: {
        autoplayTimeLeft(s, time, progress) {
        progressCircle.style.setProperty("--progress", 1 - progress);
        progressContent.textContent = `${Math.ceil(time / 1000)}s`;
        }},

    breakpoints:{
        0: {
            slidesPerView: 1, 
        },

        520: {
            slidesPerView: 2, 
        },

        950: {
            slidesPerView: 3, 
        },
    },

    
});