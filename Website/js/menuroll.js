$(document).ready(function(){  
  
    //When mouse rolls over  
    $("mli").mouseover(function(){  
        $(this).stop().animate({height:'150px'},{queue:false, duration:600, easing: 'easeOutBounce'})  
    });
    

    //When mouse is removed  
    $("mli").mouseout(function(){  
        $(this).stop().animate({height:'1px'},{queue:false, duration:600, easing: 'easeOutBounce'})  
    });  
  
});  