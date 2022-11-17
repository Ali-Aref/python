(function($){
    "use strict";
    $(window).on('load', function(){
        $('.preloader').fadeOut(1000);
    });
    
    $(document).ready(function() {
        // lightcase 
        $('a[data-rel^=lightcase]').lightcase();

        // sticky menu
        var fixed_top = $(".header-section");
        $(window).on('scroll', function(){
            if( $(this).scrollTop() > 400 ){  
                fixed_top.addClass("animated fadeInDown menu-fixed");
            }
            else{
                fixed_top.removeClass("animated fadeInDown menu-fixed");
            }
        });


        // search cart option
        $(document).on('click','.cart-option i',function(){
            $(".cart-option").toggleClass("open");
        });
        $(document).on('click','.search i, .search-close',function(){
            $(".search-input").toggleClass("open");
        });

        $(document).on('click','.bar-area>span, .sidemenubar',function(){
            $(".sidemenubar").toggleClass("open");
        });

        // mobile menu responsive
        $(document).on('click','.header-bar',function(){
            $(".header-bar").toggleClass("close");
            $(".primary-menu").toggleClass("open");
        });

        //mobile drodown menu display
        $('.main-menu ul li a, .shop-menu li a').on('click', function(e) {
            var element = $(this).parent('li');
            if (element.hasClass('open')) {
                element.removeClass('open');
                element.find('li').removeClass('open');
                element.find('ul').slideUp(1000,"swing");
            }
            else {
                element.addClass('open');
                element.children('ul').slideDown(1000,"swing");
                element.siblings('li').children('ul').slideUp(1000,"swing");
                element.siblings('li').removeClass('open');
                element.siblings('li').find('li').removeClass('open');
                element.siblings('li').find('ul').slideUp(1000,"swing");
            }
        });

        // Header Section Menu Part
        $("ul li ul").parent("li").addClass("menu-item-has-children");
        $(".shop-menu>li .shop-submenu").parent("li").children("a").addClass("dd-icon-down");

        // drop down menu width overflow problem fix
        $('ul').parent().on('hover', function() {
            var menu = $(this).find("ul");
            var menupos = $(menu).offset();
            if (menupos.left + menu.width() > $(window).width()) {
                var newpos = -$(menu).width();
                menu.css({ left: newpos });    
            }
        });
        


        // banner slider
        var swiper = new Swiper('.banner-slider', {
            slidesPerView: 1,
            spaceBetween: 0,
            autoplay: {
                delay: 5000,
                disableOnInteraction: false,
            },
            pagination: {
                el: '.banner-pagination',
                clickable: true,
            },
            loop: true,
        });

        //Testimonial Slider
        var swiper = new Swiper('.testimonial-slider', {
            slidesPerView: 2,
            spaceBetween: 0,
            autoplay: {
                delay: 2000,
                disableOnInteraction: false,
            },
            pagination: {
                el: '.testimonial-pagination',
                clickable: true,
            },
            breakpoints: {
                767: {
                    slidesPerView: 1,
                },
            },
            loop: true,
        });

        // sponsor section
        var swiper = new Swiper('.sponsor-slider', {
            slidesPerView: 6,
            spaceBetween: 10,
            autoplay: {
                delay: 5000,
                disableOnInteraction: false,
            },
            breakpoints: {
                992: {
                    slidesPerView: 3,
                },
                576: {
                    slidesPerView: 2,
                },
                420: {
                    slidesPerView: 1,
                },
            },
            loop: true,
        });

        // post-thumb-slider section
        var swiper = new Swiper('.post-thumb-slider', {
            slidesPerView: 1,
            autoplay: {
                delay: 5000,
                disableOnInteraction: false,
            },
            navigation: {
                nextEl: '.post-thumb-slider-next',
                prevEl: '.post-thumb-slider-prev',
            },
            loop: true,
        });

        // product view mode change js
        $(function() {
            $('.product-view-mode').on('click', 'a', function (e) {
                e.preventDefault();
                var shopProductWrap = $('.shop-product-wrap');
                var viewMode = $(this).data('target');
                $('.product-view-mode a').removeClass('active');
                $(this).addClass('active');
                shopProductWrap.removeClass('grid list').addClass(viewMode);
            });
        });

        // counter up start
        $('.count').counterUp({
            delay: 10,
            time: 2500
        });

        // model option start here
        $(function() {
            $('.view-modal').on('click', function () {
                $('.modal').addClass('show');
            });
            $('.close').on('click', function () {
                $('.modal').removeClass('show');
            });
        });

        // shop cart + - start here
        var CartPlusMinus = $('.cart-plus-minus');
        CartPlusMinus.prepend('<div class="dec qtybutton">-</div>');
        CartPlusMinus.append('<div class="inc qtybutton">+</div>');
        $(".qtybutton").on("click", function() {
            var $button = $(this);
            var oldValue = $button.parent().find("input").val();
            if ($button.text() === "+") {
                var newVal = parseFloat(oldValue) + 1;
            } else {
                if (oldValue > 0) {
                    var newVal = parseFloat(oldValue) - 1;
                } else {
                    newVal = 1;
                }
            }
            $button.parent().find("input").val(newVal);
        });

        // shop single pro slider
        $(function() {
            var galleryThumbs = new Swiper('.pro-single-thumbs', {
                spaceBetween: 10,
                slidesPerView: 5,
                loop: true,
                freeMode: true,
                loopedSlides: 5,
                watchSlidesVisibility: true,
                watchSlidesProgress: true,
                breakpoints: {
                    420: {
                        slidesPerView: 3,
                    },
                },
            });
            var galleryTop = new Swiper('.pro-single-top', {
                spaceBetween: 10,
                loop:true,
                loopedSlides: 5,
                thumbs: {
                    swiper: galleryThumbs,
                },
                navigation: {
                    nextEl: '.pro-single-next',
                    prevEl: '.pro-single-prev',
                },
            });
        });

        //Review Tabs
        $('ul.review-nav').on('click', 'li', function (e) {
            e.preventDefault();
            var reviewContent = $('.review-content');
            var viewRev = $(this).data('target');
            $('ul.review-nav li').removeClass('active');
            $(this).addClass('active');
            reviewContent.removeClass('review-content-show description-show').addClass(viewRev);
        });


        //  Isotope
        $(window).on('load',function() { 
            var $grid = $('.grid').isotope({
                itemSelector: '.port-item',
                masonry: {
                    columnWidth: 0
                }
            });
            var filterFns = {
                numberGreaterThan50: function() {
                    var number = $(this).find('.number').text();
                    return parseInt( number, 10 ) > 50;
                },
                ium: function() {
                    var name = $(this).find('.name').text();
                    return name.match( /ium$/ );
                }
            };
            $('.port-filter').on( 'click', 'li', function() {
                var filterValue = $( this ).attr('data-filter');
                filterValue = filterFns[ filterValue ] || filterValue;
                $grid.isotope({ filter: filterValue });
            });
            $('.port-filter').each( function( i, buttonGroup ) {
                var $buttonGroup = $( buttonGroup );
                    $buttonGroup.on( 'click', 'li', function() {
                    $buttonGroup.find('.active').removeClass('active');
                    $( this ).addClass('active');
                });
            });
        });

        // scroll up start here
        $(function(){
            $(window).scroll(function(){
                if ($(this).scrollTop() > 300) {
                    $('.scrollToTop').css({'bottom':'8%', 'opacity':'1','transition':'all .5s ease'});
                } else {
                    $('.scrollToTop').css({'bottom':'-30%', 'opacity':'0','transition':'all .5s ease'})
                }
            });
            //Click event to scroll to top
            $('.scrollToTop').on('click', function(){
                $('html, body').animate({scrollTop : 0},500);
                return false;
            });
        });
        $(function(){
            if ('.transparent-header') {
                $(".transparent-header").parent("body").addClass("marketp");
                $('.marketp>.banner').css({'padding-top': '208px'});
            }
        });
    });
}(jQuery));