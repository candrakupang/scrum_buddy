
var Nasional = function() {
	return {

		// main function
		init : function(path) {
			
		
		
		
		peta = new Peta(); 
		peta.init();
		peta.setMapCenter(-4.3, 54.5, 6);
		
		var project = [];	
		var userStory = [];	
		$.ajax({
			url: '/scrum/getproject/',
			data: {id: 0},
			success: function (data) {							
				for (i = 0; i < Object.keys(data).length; i++) 
					project.push(data[i]);
				
				var row = $("<tr/>"); 
				$("#ProjectList").append(row);								
				row.append($("<td align='center'><b>Name</b></td>"));
				row.append($("<td align='center'><b>Status</b></td>"));

				setUserStory();
			}
		});
		
		
		function setUserStory(){
			for (i = 0; i < project.length; i++) 
			{
				var row = $("<tr/>"); 
				$("#ProjectList").append(row);								
				row.append($("<td align='left'>"+project[i].fields.name+"</td>"));
				row.append($("<td align='left'>"+project[i].fields.status+"</td>"));
			
		
				$.ajax({
					url: '/scrum/getstory/',
					data: {'id': project[i].pk},
					success: function (data) {															
						peta.addMarker(i,project,data);
					}
				});
			}
		}

		}
	}
}();
