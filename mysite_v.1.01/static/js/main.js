$(function(){
	$("#wizard").steps({
        headerTag: "h4",
        bodyTag: "section",
        transitionEffect: "fade",
        enableAllSteps: true,
        transitionEffectSpeed: 500,
        labels: {
            next: "Next",
            previous: "Back"
        },
        onStepChanging: function (event, currentIndex, newIndex) { 
            if ( newIndex === 1 ) {
                $('.steps ul').addClass('step-2');
                $('.actions ul li:nth-child(2)').addClass('step-2');
                $('.actions ul li:nth-child(2) a').html('Book Now');
            } else {
                $('.steps ul').removeClass('step-2');
                $('.actions ul li:nth-child(2)').removeClass('step-2');
                $('.actions ul li:nth-child(2) a').html('Next');
            }
            if ( newIndex === 2 ) {
                $('.steps ul').addClass('step-3');
                $('.actions ul').addClass('step-last');
                $('.actions ul li').hide();
            } else {
                $('.steps ul').removeClass('step-3');
            }
            return true; 
        }
    });

    // Custome Jquery Step Button
    $('.forward').click(function(){
    	$("#wizard").steps('next');
    })
    $('.backward').click(function(){
        $("#wizard").steps('previous');
    })

    // Date Picker
    var dp = $('#dp').datepicker().data('datepicker');
    dp.selectDate(new Date());

    // Select Dropdown
    $('html').click(function() {
        $('.select .dropdown').hide(); 
    });
    $('.select').click(function(event){
        event.stopPropagation();
    });
    $('.select .select-control').click(function(){
        $('.select .dropdown').toggle();
    })    
    var textInit = $('.select .dropdown li:first-child').attr('rel');
    $('.select-control').text(textInit);
    $('.select .dropdown li').click(function(){
        $('.select .dropdown').toggle();
        var text = $(this).attr('rel');
        $(this).parent().prev().find('div').text(text);
    })
})
