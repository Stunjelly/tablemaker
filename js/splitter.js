
function getRulerLoc (rulerID) {
	return ($('#ruler'+rulerID).position().top);
}

function setRulerLoc (rulerID, Loc) {
	if ($('#ruler'+rulerID).css('top', Loc)){
		return(true);
	}else {
		return(false);
	}
}

function getRulers() {
	return [$('#ruler1').position().top,$('#ruler2').position().top, $('#ruler3').position().top]
}

function setRulers(ruler1, ruler2, ruler3) {
	$('#ruler1').css('top', ruler1);
	$('#ruler2').css('top', ruler2);
	$('#ruler3').css('top', ruler3);
}

function setPage (page){
	$('#page').attr('src',page);
}

$(document).ready(function () {
	$('.ruler').each(function () {
		$(this).mousedown(function(e){
			e.preventDefault();

			var mousey = $(this).position().top;
			$ruler = $(this);
			$(document).mousemove(function(e) {
				if (e.pageY < $('#wrapper').height()){
					$ruler.css('top', e.pageY);	
				}
			});
		});
		$(this).mouseup(function() {
			$(document).unbind('mousemove');
		});
	});

});


