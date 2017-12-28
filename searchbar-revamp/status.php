<html>
        <meta http-equiv="refresh" content="10">
	<body>
		<center><h1>Running</h1></center>
                <center><p>
                <?php
                 system('date');
                 echo "<br>";
                 system('ps -ax | grep -w "python3 tree.py" | grep -v "grep"');
                ?>
                </p></center>
	</body>
</html>