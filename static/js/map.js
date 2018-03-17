
var ScrumMap = function() {
	return {

		// main function
		init : function(path) {
			
			/**  Init Global variable  */
			var project = [];	
			var userStory = [];
			
			/**  Set geospatial initial data  */
			geospatial = new Geospatial(); 
			geospatial.init();
			geospatial.setMapCenter(-4.3, 54.5, 6);
			
			/**  Get project data  */
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
			
			
			/**  supply data to geospatial  */
			function setUserStory(){
				for (i = 0; i < project.length; i++) 
				{
					var row = $("<tr/>"); 
					$("#ProjectList").append(row);								
					row.append($("<td align='left'>"+project[i].fields.name+"</td>"));
					row.append($("<td align='left'>"+project[i].fields.status+"</td>"));
				
					/**  Get user story data  */
					$.ajax({
						url: '/scrum/getstory/',
						data: {'id': project[i].pk},
						success: function (data) {															
							geospatial.addMarker(i,project,data);
						}
					});
				}
			}

		}
	}
}();
