$(document).ready(function() {
	console.log("listening!");
	
	// $("input[type='checkbox']").on("change", function() {
	// 	alert("Change to " + this.value);
	// });
	$("input[type='checkbox']").on('change', function(event) {
		console.log("i've been hit!");
		var hitID = event.target.id;
		
		if ($(this).is(":checked")) {
			console.log("checked");
			$.ajax({
				url: '/search.html',
				type: 'POST',
				data: { "strID": hitID, "state": "1" }
			});
		} else {
			console.log("unchecked");
			$.ajax({
				url: '/search/',
				type: 'POST',
				data: { "strID":hitID, "state":"0" },
				success : function(json) {
					console.log("gets here");
                	successFunc(json);
				},
				error : function(xhr, errmsg, err) {
					console.log("ERROR");
               		errorFunc(xhr,errmsg,err);
				}
			});
		}
	});

	function successFunc(json) {
	 	if (json.add == true){
	 		for (loc in json.locations){
	 			$("#list-data").append("<h1>"+loc.site_name+"</h1>");
	 		}
	 		
	 	}
	 
	}

	function errorFunc(xhr,errmsg,err){
		alert("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
	}
	// This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});





