/* Functions */

        /* Redirect */
        

        
        function updateTime(i){
            time=i.value;
            alert('y');
            $.ajax({
                method:'POST',
                url:"{%url 'app:redirect-update-time' %}",
                data:{
                    'csrfmiddlewaretoken':'{{csrf_token}}',
                    'time':time,
                },
            })
        }

        function updateDate(i){
            date=i.val();
            $.ajax({
                method:'POST',
                url:"{%url 'app:redirect-update-date' %}",
                data:{
                    'csrfmiddlewaretoken':'{{csrf_token}}',
                    'time':date,
                },
            })
        }

        function updateTimezone(i){
            date=i.val();
            $.ajax({
                method:'POST',
                url:"{%url 'app:redirect-update-date' %}",
                data:{
                    'csrfmiddlewaretoken':'{{csrf_token}}',
                    'time':date,
                },
            })
        }
        

        