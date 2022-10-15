theme=document.getElementById(profile.theme.title);
alert(theme);

$('#avatar-form-ajax').submit(function(e){
    e.preventDefault();
    $form = $(this)
    var formData = new FormData(this);
    $.ajax({
        url: window.location.pathname,
        type: 'POST',
        data: formData,
        success: function (response) {
            $('.error').remove();
        },
        cache: false,
        contentType: false,
        processData: false
    });
});

$('#select-image').on('click',function(){
    document.getElementById('avatar-form').click();
});
$('#avatar-form').on('change',function(){
    document.getElementById('submit-image').click();
})
$('#delete-avatar').on('click',function(){
    $.ajax({
        url:"{%url 'link:delete-avatar'%}",
        data:{
            'csrfmiddlewaretoken':"{{csrf_token}}",
        },
        method:'POST',
        success:function(){
            document.getElementById('avatar').remove();
        }
    });
});

$('#theme').on('click',function(){
    document.getElementById('theme')
    theme=document.querySelector('input[name="theme"]:checked').value;
    checked=theme;
    document.getElementById(theme).style="width:130px;height:240px;transition:width 0.2s;transition:height 0.2s;"
});

