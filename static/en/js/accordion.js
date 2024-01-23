







// FOR FAQS
jQuery(document).ready(function($){
    
    var panels = $(".faq-ans").hide();

    panels.first().show();
    
     $(".faq-que").click(function(){

         var $this = $(this);

         panels.slideUp();
         $this.next().slideDown();
         
    });

});

// FOR ORDER LIST
jQuery(document).ready(function($){
    
    var panels = $(".orderlist-body").hide();

    panels.first().show();
    
     $(".orderlist-head").click(function(){

         var $this = $(this);

         panels.slideUp();
         $this.next().slideDown();
         
    });

});