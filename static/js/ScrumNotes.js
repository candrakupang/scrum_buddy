
	
		var pid;
		var notes = [];
		var mynote = {
				resizable: true,						
				availableThemes: [
				{ text: "Finish", value: "sticky-note-green-theme" },
				{ text: "On Progress", value: "sticky-note-blue-theme" },
				{ text: "New", value: "sticky-note-pink-theme" }],					
				defaultTheme: { text: "New", value: "sticky-note-pink-theme" },
				notePosition: { top: "120px", left: "50px" },
				noteDimension: { width: "200px", height: "100px" },
				noteText: "As ... I want ...",
				noteHeaderText: "header",	
				idUserStory: "0",
				status: "1",
		};
		
		 $(function () {
			$('#divStickyNotesContainer').coaStickyNote({				
				
			});		
		});


		$("tr.table").click(function() {
			var tableData = $(this).children("td").map(function() {
				return $(this).text();
			}).get();			
			window.location.href = "/scrum/board/"+$.trim(tableData[0]);
		});		
		
		function save(){
			var index = 1;
			var noteObject = $('#divStickyNotesContainer').data('coaStickyNote').getNoteBoxByIndex(index);
			var tmp;
			var array_tmp;
			while (noteObject != null) {					
				array_tmp = [];
				if (noteObject.data("coaStickyNote")["settings"]["status"] == "1") {
					tmp = noteObject.data("coaStickyNote")["settings"]["notePosition"]["top"];
					if (tmp.indexOf('.') != -1)
						tmp = tmp.substring(0, tmp.indexOf('.'))+"px";
					array_tmp.push(tmp);
					tmp = noteObject.data("coaStickyNote")["settings"]["notePosition"]["left"];
					if (tmp.indexOf('.') != -1)
						tmp = tmp.substring(0, tmp.indexOf('.'))+"px";
					array_tmp.push(tmp);
					tmp = noteObject.data("coaStickyNote")["settings"]["noteDimension"]["width"];
					if (tmp.indexOf('.') != -1)
						tmp = tmp.substring(0, tmp.indexOf('.'))+"px";
					array_tmp.push(tmp);					
					tmp = noteObject.data("coaStickyNote")["settings"]["noteDimension"]["height"];
					if (tmp.indexOf('.') != -1)
						tmp = tmp.substring(0, tmp.indexOf('.'))+"px";
					array_tmp.push(tmp);
					$.ajax({
						type: 'post',
						url: '/scrum/board/{{prj.id}}/',
						data: {
						text:noteObject.data("coaStickyNote")["settings"]["noteText"],
						header:noteObject.data("coaStickyNote")["settings"]["noteHeaderText"],
						top:array_tmp[0],
						left:array_tmp[1],
						width:array_tmp[2],
						heigth:array_tmp[3],
						theme:noteObject.data("coaStickyNote")["settings"]["defaultTheme"]["value"],
						id:noteObject.data("coaStickyNote")["settings"]["idUserStory"],
						csrfmiddlewaretoken: '{{ csrf_token }}'
					  },
					  success: function (response) {
							// none
					  }
					});
						
				}	
				index++;
				noteObject = $('#divStickyNotesContainer').data('coaStickyNote').getNoteBoxByIndex(index);
			} 			
			alert("data is saved");
			location.reload(); 
		}
				
		function del(){
			$("#cblist input:checked").each(function() {
				$.ajax({
						type: 'post',
						url: '/scrum/xstory/',
						data: {id: $(this).val(),csrfmiddlewaretoken: '{{ csrf_token }}'},
					  success: function (response) {
							
					  }
					});
			});		
			alert("data is deleted");location.reload();			
		}		
				
		function init(){
			{% if stories %}							
				{% for story in stories %}											
								
					var note = {
						resizable: true,						
						availableThemes: [				
						{ text: "Finish", value: "sticky-note-green-theme" },
						{ text: "On Progress", value: "sticky-note-blue-theme" },
						{ text: "New", value: "sticky-note-pink-theme" }],					
						defaultTheme: { text: "", value: "{{story.theme}}" },
						notePosition: { top: "{{story.top}}", left: "{{story.left}}" },
						noteDimension: { width: "{{story.width}}", height: "{{story.heigth}}" },
						noteText: "{{story.text}}",
						noteHeaderText: "{{story.header}}",	
						idUserStory: "{{story.id}}", 
						status: "0",
						onNoteBoxDraggingStop: function (note) {note.settings.status = "1";},
						onThemeSelectionChange: function (note) {note.settings.status = "1";},
						onNoteBoxResizeStop: function (note) {note.settings.status = "1";},
						onNoteBoxHeaderUpdate: function (note) {note.settings.status = "1";},
						onNoteBoxTextUpdate: function (note) {note.settings.status = "1";},
					};
					notes.push(note);
					$('#cblist').append('<input id="a1" type="checkbox" value="{{story.id}}" /> {{story.text}}<br />');					
				{% endfor %}		
				row = $("<tr/>"); 
				$("#ProjectDetails").append(row);								
				row.append($("<td bgcolor='#e6ffe6' align='left'>Total</td>"));
				row.append($("<td bgcolor='#e6ffe6' align='left'>"+notes.length+"</td>"));
				row = $("<tr/>"); 
				$("#ProjectDetails").append(row);
				row.append($("<td bgcolor='#e6ffe6' align='left'>New</td>"));
				row.append($("<td bgcolor='#e6ffe6' align='left'>"+notes.length+"</td>"));
				row = $("<tr/>"); 
				$("#ProjectDetails").append(row);
				row.append($("<td bgcolor='#e6ffe6' align='left'>On Progress</td>"));
				row.append($("<td bgcolor='#e6ffe6' align='left'>"+notes.length+"</td>"));
				row = $("<tr/>"); 
				$("#ProjectDetails").append(row);
				row.append($("<td bgcolor='#e6ffe6' align='left'>Finish</td>"));
				row.append($("<td bgcolor='#e6ffe6' align='left'>"+notes.length+"</td>"));
			{% endif %}						
			$("#init").click();						
			
		}				
