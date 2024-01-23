




var $grid = $('.isotope-items').isotope({
    itemSelector: '.all',
});


$('.isotope-select').on('change', function () {
    var filterValue = this.value;
    $grid.isotope({ filter: filterValue });
});
  