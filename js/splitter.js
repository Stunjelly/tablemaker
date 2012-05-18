
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
	rulers = [];
	counter= 1;
	$('.ruler').each(function(){
		rulers.push($('#ruler'+counter).position().top);
		counter++;
	});
	console.log(rulers);
	return (rulers);
}

function setRulers(rulers) {
	for (i=0;i<rulers.length;i++){
		$('#ruler'+(i+1)).css('top', rulers[i]);
	}
}

function setPage (page){
	$('#page').attr('src',page);
}

$(document).ready(function () {
	$('body').mousedown(function(e) {
		e.preventDefault();
	});
	
	
	$('.ruler').each(function () {
		$(this).css('width', '100%');
		$(this).mousedown(function(e){
			e.preventDefault();
			var mousey = $(this).position().top;
			$ruler = $(this);
			$(document).mousemove(function(e) {
				if (e.pageY < $('#wrapper').height()){
					$ruler.css('top', e.pageY);
					pyObj.handleMoved();
				}
			});
		});
		$(this).mouseup(function() {
			$(document).unbind('mousemove');
		});
	});

});


