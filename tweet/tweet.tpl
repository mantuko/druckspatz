<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<html xmlns="http://www.w3.org/1999/xhtml" lang="en">
	<head>
		<meta charset="utf-8" />
		<style type="text/css">
			body {
				width: 5cm;
				font-family: "Helvetica", "Verdana", sans-serif;
				font-size: 13px;
    			-webkit-transform: rotate(180deg);
			}
			.clear {
				clear: both;
				padding-top: 1px;
				padding-right: 3px;
				margin-bottom: 3px;
				padding-bottom: 3px;
			}
			.info {
				float: left;
				margin-top: 4px;
			}
			#info_text {
				margin: 0 0 0 4px;
			}
			#name {
				font-size: 1.1em;
			}
			#user_name, #date {
			}
  		</style>
		<title>Druckspatz - Tweet</title>
	</head>
	<body>
		<div>
			<div id="avatar" class="info">
				<img src="{{avatar}}" width="45px" height="45px" />
			</div>
			<div id="info_text" class="info">
				<strong id="name">{{name}}</strong><br>
				<span id="user_name">{{screen_name}}</span><br>
				<span id="date">{{date}}</span>
			</div>   
		</div>
		<div class="clear">
			<p>{{tweet}}</p>
		</div>
	</body>
</html>