var fixmeTop = $('.fixme').offset().top;
$(window).scroll(function() {
    var currentScroll = $(window).scrollTop();
    if (currentScroll >= fixmeTop) {
        $('.fixme').css({
            position: 'fixed',
            top: '0',
            left: '0'
        });
    } else {
        $('.fixme').css({
            position: 'static'
        });
    }
});