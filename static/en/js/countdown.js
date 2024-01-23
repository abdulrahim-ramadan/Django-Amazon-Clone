


$('[data-countdown]').each(function () {
    
    var $this = $(this),
        finalDate = $(this).data('countdown');
    if (!$this.hasClass('countdown-full-format')) {
        $this.countdown(finalDate, function (event) {
            $this.html(event.strftime('<span class="countdown-time"><span>%D</span><small>days</small></span> <span class="countdown-time"><span>%H</span><small>hours</small></span> <span class="countdown-time"><span>%M</span><small>minutes</small></span> <span class="countdown-time"><span>%S</span><small>seconds</small></span>'));
        });
    } else {
        $this.countdown(finalDate, function (event) {
            $this.html(event.strftime('<span class="countdown-time"><span>%D</span><small>days</small></span> <span class="countdown-time"><span>%H</span><small>hours</small></span> <span class="countdown-time"><span>%M</span><small>minutes</small></span> <span class="countdown-time"><span>%S</span><small>seconds</small></span>'));
        });
    }
});