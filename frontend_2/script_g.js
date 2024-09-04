$(document).ready(function () {
    $(window).scroll(function () {
        
        if (this.scrollY > 20) {
            $('.navbar').addClass("sticky");
        } else {
            $('.navbar').removeClass("sticky");
        }
        if (this.scrollY > 500) {
            $('.scroll-up-btn').addClass("show");
        } else {
            $('.scroll-up-btn').removeClass("show");
        }
    });
    document.getElementById('farmersHeavenBtn').addEventListener('click', function() {
        window.location.href = 'farmers_heaven_g.html';
    });
    document.getElementById('farmers_heaven.html').addEventListener('click',function() {
        window.location.href='plant_disease_prediction_g.html';
    })

    $('.scroll-up-btn').click(function () {
        $('html').animate({ scrollTop: 0 });
        
        $('html').css("scrollBehavior", "auto");
    });

    $('.navbar .menu li a').click(function () {
        
        $('html').css("scrollBehavior", "smooth");
    });

    
    $('.menu-btn').click(function () {
        $('.navbar .menu').toggleClass("active");
        $('.menu-btn i').toggleClass("active");
    });

    var typed = new Typed(".typing", {
        strings: ["AI Driven", "Crop Disease Prediction", "FoodTech","Management system"],
        typeSpeed: 100,
        backSpeed: 60,
        loop: true
    });

    var typed = new Typed(".typing-2", {
        strings: ["AI Driven", "Crop Disease Prediction", "FoodTech", "Management system"],
        typeSpeed: 100,
        backSpeed: 60,
        loop: true
    });



    

});
