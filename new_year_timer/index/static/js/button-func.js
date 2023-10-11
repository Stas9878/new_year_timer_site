function checkParams() {
    var name = $('#wish').val();
    if(name.length != 0) {
        $('#sub').removeAttr('disabled');
    } else {
        $('#sub').attr('disabled', 'disabled');
    }
}