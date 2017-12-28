<?php $html="
	<html>
	<body>
	<head>
		<title>
			McDonald's Work Schedule
		</title>
		<style>
			table { 
				border: solid black 2px;
			}
			tr,td,th {
				border: solid gray 1px;
			}
			div {
				padding: 4px;
			}
			.aria {
				position: relative;
				border: solid darkgray 1px;
				padding: 2px;
				width: 100%;
				display: block;
			}
			.aria hr {
			width: 100%;
			border: solid lightgray 1px;
			}
		</style>
	</head>
	<h1>Schedule Times</h1>
	<table>
		<tr>
			<th>Sunday</th>
			<th>Monday</th>
			<th>Tuesday</th>
			<th>Wednesday</th>
			<th>Thursday</th>
			<th>Friday</th>
			<th>Saturday</th>
		</tr>
		<tr>
			<td>".$_GET['sun']." </td>
			<td>".$_GET['mon']." </td>
			<td>".$_GET['tue']." </td>
			<td>".$_GET['wed']." </td>
			<td>".$_GET['thu']." </td>
			<td>".$_GET['fri']." </td>
			<td>".$_GET['sat']." </td>
		</tr>
	</table>
	</body>
	</html>
";
	if ($_GET['submit'] == 'Submit') {
		$filename="schedule.html";
		header("Content-type: text/plain");
		header("Content-Disposition: attachment; filename=$filename");
		print $html;
	}
	if ($_GET['submit'] == "Preview") {
		print($html);
		print("<a href='docgen.php?sun=".$_GET['sun']."&mon=".$_GET['mon']."&tue=".$_GET['tue']."&wed=".$_GET['wed']."&thu=".$_GET['thu']."&fri=".$_GET['fri']."&sat=".$_GET['sat']."&submit=Submit"."'>Download</a><br>");
		print("<a href='schedule.php'>Return</a>");
	}
?>

