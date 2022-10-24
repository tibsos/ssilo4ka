/* Redirect */

function redirectInit(el){
            
    uid=el.id;

    fun=$("#activeFunction"+uid)
    contents=$('#activeFunctionContents'+uid)
    
    /* Set the redirect icon to unclickable */

    /* Fade out previous content */
    fun.html('');

    /* Fade in new content */
    html=`
    <div class='contents' id='contents${uid}' style="opacity:0;">
        <h4 class="title">Works!</h4>
        <div class="content" id="content${uid}">
            <p>Explanation</p>
            <button onClick=createRedirectLink(this) id="${uid}">Confirm</button>
        </div>
    </div>
    `

    fun.animate({height: '200px'},{ duration: 500 });
    fun.html(html);
    $("#contents"+uid).animate({opacity:0},500);
    $("#contents"+uid).animate({opacity:1},1000);
}

function viewRedirect(el){
    uid=el.id;

    fun=$("#activeFunction"+uid)
    contents=$('#activeFunctionContents'+uid)
    
    /* Set the redirect icon to unclickable */

    /* Fade out previous content */
    fun.html('');   
    end_date=$('#redirectDate').value;
    alert(end_date)
    end_time=$('#redirectTime').val()
    timezone=$('#redirectTimezone').val()

    /* Fade in new content */
    html=`
    <div class='countdown'>
        <div id="countdown">
    </div>
    <div class='form'>
        <input type="date" id="date" value='${end_date}'>
        <input type="time" id="time" value='${emd_time}' onChange="updateTime(this)">
        <select id="tz" name="tz" >
            <option value="saab">Saab</option>
            <option value="fiat">Fiat</option>
            <option value="+3" selected>UTC +3 | Московское время</option>
            <option value="audi">Audi</option>
        </select>
    </div>
    `

    fun.animate({height: '200px'},{ duration: 500 });
    fun.html(html);
    $("#contents"+uid).animate({opacity:0},500);
    $("#contents"+uid).animate({opacity:1},1000);
}
        



        