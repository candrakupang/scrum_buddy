
function Peta() {
	// ********* Maps Variable
	var map,vlayer;
	var size = new OpenLayers.Size(20, 20); 
	var offset = new OpenLayers.Pixel(-(size.w / 2), -size.h);
	var iconred;
	var markers_red = new OpenLayers.Layer.Markers("User Story");
	var markers_blue = new OpenLayers.Layer.Markers("Sprint");
	

	// ********* Connection Global Variabel
	var  lonLat, road, aerial, osmlayer, hybrid, terrain;

	this.init = function() {
		
	map = new OpenLayers.Map('map', {
			projection : "EPSG:900913"
		});
		map.addControl(new OpenLayers.Control.LayerSwitcher());
		initBaseMap();
		map.addLayers([ road, aerial, hybrid,terrain, osmlayer ]);
		vlayer = new OpenLayers.Layer.Vector("Drawing Polygon", {
		    styleMap: new OpenLayers.StyleMap({
		        "default": new OpenLayers.Style({
		            strokeColor: "#ff0000",
		            strokeOpacity: .7,
		            strokeWidth: 1,
		            fillColor: "#ff0000",
		            fillOpacity: .1,
		            cursor: "pointer"
		        }),

		        "temporary": new OpenLayers.Style({
		            strokeColor: "#ffff33",
		            strokeOpacity: .9,
		            strokeWidth: 2,
		            fillColor: "#ffff33",
		            fillOpacity: .3,
		            cursor: "pointer"
		        }),
		        "select": new OpenLayers.Style({
		            strokeColor: "#0033ff",
		            strokeOpacity: .7,
		            strokeWidth: 2,
		            fillColor: "#0033ff",
		            fillOpacity: .4,
		            graphicZIndex: 2,
		            cursor: "pointer"
		        })
		  })
		});
        map.addLayer(vlayer);
        map.addControl(new OpenLayers.Control.EditingToolbar(vlayer));   
		map.addLayer(markers_blue);
		map.addLayer(markers_red);	

		iconred = new OpenLayers.Icon(OpenLayers.Util.getImageLocation("red.png"), size, offset);			
		iconblue = new OpenLayers.Icon(OpenLayers.Util.getImageLocation("blue.png"), size, offset);			
	}

	// private
	var initBaseMap = function() {
		osmlayer = new OpenLayers.Layer.OSM( "OSM Map");
		road = new OpenLayers.Layer.Google("Google Maps", {
			numZoomLevels : 20
		});

		aerial = new OpenLayers.Layer.Google("Google Satellite", {
			type : google.maps.MapTypeId.SATELLITE, numZoomLevels: 22
		});
		
		hybrid = new OpenLayers.Layer.Google(
			    "Google Hybrid",
			    {type: google.maps.MapTypeId.HYBRID, numZoomLevels: 20});
		
		terrain = new OpenLayers.Layer.Google(
			    "Google Terrain",
			    {type: google.maps.MapTypeId.TERRAIN, numZoomLevels: 20});
	}

	this.setMapCenter = function(lon, lat, zoom) {
		lonLat = new OpenLayers.LonLat(lon, lat).transform(
				new OpenLayers.Projection("EPSG:4326"), map
						.getProjectionObject());
		map.setCenter(lonLat, zoom);
	}

	
	this.addMarker = function(i,project,story) {	
		lonLat = new OpenLayers.LonLat(project[i].fields.longitude, project[i].fields.latitude).transform(
				new OpenLayers.Projection("EPSG:4326"), map.getProjectionObject());
		
		marker2 = new OpenLayers.Marker(lonLat, iconblue.clone());
		markers_blue.addMarker(marker2);
		
		marker = new OpenLayers.Marker(lonLat, iconred.clone());
		markers_red.addMarker(marker);
		
		markers_red.markers[i].events.register('mouseover', marker,	function(evt) {
			generateChart(story,project[i].fields.name);	
			generateTable(project[i]);
		});
		
		markers_red.markers[i].events.register('mousedown', marker,	function(evt) {
			window.location.href = "/scrum/board/" + project[i].pk;
		});
		
		markers_blue.markers[i].events.register('mousedown', marker,	function(evt) {
			window.location.href = "/scrum/sprint/" + project[i].pk;
		});
	}
	
	function generateTable(project) {
		$("#div2").show();
		$("#div3").hide();
		$('#ProjectDetails tr').remove();
		var row = $("<tr/>"); 
		$("#ProjectDetails").append(row);								
		row.append($("<td  align='left'>Name</td>"));
		row.append($("<td  align='left'>"+project.fields.name+"</td>"));
		var row = $("<tr/>"); 
		$("#ProjectDetails").append(row);								
		row.append($("<td  align='left'>Description</td>"));
		row.append($("<td  align='left'>"+project.fields.description+"</td>"));
		var row = $("<tr/>"); 
		$("#ProjectDetails").append(row);								
		row.append($("<td  align='left'>Address</td>"));
		row.append($("<td  align='left'>"+project.fields.address+"</td>"));
		var row = $("<tr/>"); 
		$("#ProjectDetails").append(row);								
		row.append($("<td align='left'>Status</td>"));
		row.append($("<td align='left'>"+project.fields.status+"</td>"));
	}
	
	function generateChart(story,projectName) {
		$("#div1").show();
		var ds;
		var finish=0,create=0,working=0;
		
		for (i = 0; i < story.length; i++){
			ds = [];
			if (story[i].fields.theme == "sticky-note-green-theme")
				finish++;
			else if (story[i].fields.theme == "sticky-note-blue-theme")
				create++;
			else 
				working++;
			
			$('#mytitle').html("Project : " + projectName);
			ds.push(finish);ds.push(working);ds.push(create);
			config.data.datasets.forEach(function(dataset) {dataset.data = ds;});				
			config.data.labels = ['Finish','On Progress','New'];
			myDoughnut.update();
		}	
	}	
}