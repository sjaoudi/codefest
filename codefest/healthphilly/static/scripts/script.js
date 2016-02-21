$(function() {
	console.log("listening!");
	$("input[type='checkbox']").on("change", function() {
		alert("Change to " + this.value);
	});
	console.log("yo");
	$('test').on('change', function(event) {
		console.log("i've been hit!");
		var hitID = evt.target.id;
		
		if ($('#'+hitID).is(":checked")) {
			$.ajax({
				url: 'search',
				type: 'POST',
				data: { "strID":hitID, "state":"1" }
			});
		} else {
			$.ajax({
				url: 'search',
				type: 'POST',
				data: { "strID":hitID, "state":"0" }
			});
		}
	});

});





