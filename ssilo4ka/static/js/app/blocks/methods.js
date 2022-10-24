function blockActivity(uid){
    $.ajax({
    url:"{%url 'app:block-activity'%}",
    data:{
        "csrfmiddlewaretoken":"{{csrf_token}}",
        'uid':uid,
    },
    method:"POST",
    });
};
function updateTitle(uid,title){
    $.ajax({
    url:"{%url 'app:update-title'%}",
    data:{
        "csrfmiddlewaretoken":"{{csrf_token}}",
        'uid':uid,
        'title':title,
    },
    method:"POST",
    });
};
function updateURL(uid,url){
    if(/^(?:(?:(?:https?|ftp):)?\/\/)(?:\S+(?::\S*)?@)?(?:(?!(?:10|127)(?:\.\d{1,3}){3})(?!(?:169\.254|192\.168)(?:\.\d{1,3}){2})(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)(?:\.(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)*(?:\.(?:[a-z\u00a1-\uffff]{2,})).?)(?::\d{2,5})?(?:[/?#]\S*)?$/i.test( url )===true){
        document.getElementById('urlError').style.display='none';
        $.ajax({
        url:"{%url 'app:update-url'%}",
            data:{
                "csrfmiddlewaretoken":"{{csrf_token}}",
                'uid':uid,
                'url':url,
            },
            method:"POST",
        });
    }
    else if(url==''){
        document.getElementById('urlError').style.display='none';
    }
    else{
        document.getElementById('urlError').style.display='';
    }    
};


function deleteBlock(e){

    uid=e.id

    let undoHTML=`
    <bold><p>Блок удален. Хочешь его восстановить?</p></bold>
    <button>Да</button>
    <button onClick="hideUndo(this)" id="${uid}">X</button>
`      
    block=$('#block'+uid);
    blockContents=$('#blockContents'+uid);
    blockContents.animate({'opacity': '0'}, 400).promise().done(function(){
        blockContents.html(undoHTML);
        $(function () {
            block.animate({
            height: '60px'
            }, { duration: 500, queue: false });

            block.animate({
            'border-radius': '50px'
            }, { duration: 900, queue: false });
        })
        /* Spam animation to wait out before showing html */
        block.animate({'opacity':'1'},500).promise().done(function(){
            blockContents.animate({
                'opacity':1
            });
        });
    });
    

    $.ajax({
        method:'POST',
        url:"{% url 'app:delete-block'%}",
        data:{
            'csrfmiddlewaretoken':"{{csrf_token}}",
            'uid':e.id,
        },
    })

}

function hideUndo(e){
    block=$("#block"+e.id)
    block.html('');
    block.hide('slow');
}
