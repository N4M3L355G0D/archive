<!--<?php

if ($_POST['verify'] == "yes"){
 echo "updates will proceed!";	
};


?> -->
<html>
	<body>
		<center>
		<h1>Update Loca</h1>
		<hr>
		<form action="update.php" method="get">
			<br><br>
			<input type="submit" value="Update" name="submit" formenctype="application/x-www-form-urlencoded" >
		</form>
<?php

if ($_GET['submit'] == "Update"){
	exec("/usr/bin/python3 statusgen_wrap.py");
	exec("/usr/bin/python3 tree.py > /dev/null &");
	echo "<meta http-equiv='refresh' content='0;url=\"status.php\"'>";
};


?>
		<p>Warning: This may take more than 30 Minutes to complete.</p>
		</center>
	</body>
</html>
