/**
 * Created by luca on 27/02/16.
 */
$(document).ready(function(){
    //dropdown changed
    $('#users').children().click(function(){
        $('#flatmate').value(this.value());
    });
});