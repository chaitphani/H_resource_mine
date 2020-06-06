(function($) {
    "use strict";

    $(document).on('ready', function() {
		
	/* Header scroll on fixed */
	
	var NavBar = $('nav.navbar');
    var didScroll;
    var lastScrollTop = 0;
    var navbarHeight = NavBar.outerHeight();
    $(document).ready(function(event) {
        didScroll = true;
    });
    $(window).scroll(function(event) {
        didScroll = true;
    });
    setInterval(function() {
        if (didScroll) {
            hasScrolled();
            didScroll = false;
        }
    }, 100);

    function hasScrolled() {
        var st = $(document).scrollTop();
        if (st + $(window).height() < $(document).height()) {
            NavBar.addClass('fixed-header');
            if (st == 0) {
                NavBar.removeClass('fixed-header');
            }
        }
        lastScrollTop = st;
    }


        /* ==================================================
            # Smooth Scroll
         ===============================================*/
        $("body").scrollspy({
            target: ".navbar-collapse",
            offset: 200
        });
        $('a.smooth-menu').on('click', function(event) {
            var $anchor = $(this);
            var headerH = '75';
            $('html, body').stop().animate({
                scrollTop: $($anchor.attr('href')).offset().top - headerH + "px"
            }, 1500, 'easeInOutExpo');
            event.preventDefault();
        });
		
		
		
		$('[data-toggle="tooltip"]').tooltip();
		
		$('[data-toggle="popover"]').popover();
		
		$(".owl-carousel").owlCarousel({
		    center: true,
		    items:2,
		    lazyLoad:true,
		    loop:true,
		    margin:40,
		    autoplay:true,
		    dots:true,
		    smartSpeed:800,
		    autoplayTimeout:3500,
		    autoplayHoverPause:false
		});
		
	
    $(window).on ('load', function (){ // makes sure the whole site is loaded
		
		$('#loader').delay(100).fadeOut('slow');
		$('#loader-wrapper').delay(500).fadeOut('slow');
		$('body').delay(500).css({'overflow':'visible'});
		
		AOS.init({
          duration: 1000,
		  disable: 'mobile',
          mirror: true
        });


    });

    }); // end document ready function
})(jQuery); // End jQuery


$(function () {
	$('#contact-form').on('submit', function (e) {
			console.log("baasss")
		if (!e.isDefaultPrevented()) {
			console.log("Sasas")
			var re = /^(("[\w-\s]+")|([\w-]+(?:\.[\w-]+)*)|("[\w-\s]+")([\w-]+(?:\.[\w-]+)*))(@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$)|(@\[?((25[0-5]\.|2[0-4][0-9]\.|1[0-9]{2}\.|[0-9]{1,2}\.))((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\.){2}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\]?$)/;
			var emailFormat = re.test($("#form_email").val());// this return result in boolean type
			if (emailFormat) {
				$('#alert_message').css({ 'display': 'none' })
				var url = "contact.php";
				$.ajax({
					type: "POST",
					url: url,
					data: $(this).serialize(),
					success: function (data) {
						var messageAlert = 'alert-' + data.type;
						var messageText = data.message;
						var alertBox = '<div class="alert ' + messageAlert + ' alert-dismissable"><button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>' + messageText + '</div>';
						if (messageAlert && messageText) {
							$('#contact-form').find('.messages').html(alertBox);
							$('#contact-form')[0].reset();
						}
					}
				});
			}
			else {
				$('#alert_message').css({ 'display': 'block' });
				$('#form_email').focus();
				return false;
			}
			return false;
		}
	})
});
