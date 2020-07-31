$(window).on('resize', function () {
    if ($(window).width() < 575) {
        $('div.align-items-end').removeClass('h-100').addClass('h-25 py-cus')
    }
});

$(window).ready(
    function () {
        if ($(window).width() <= 992){
            $('li.dropdown').removeClass('v-divider');
            $('div.align-items-end').removeClass('h-100').addClass('h-25 py-cus');
        }
    }
);