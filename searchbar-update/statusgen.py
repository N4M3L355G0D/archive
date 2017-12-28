def gen(state="running"):
    if state =="running":
        html="""<html>
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
</html>"""
    if state == "done":
        html="""<html>
        <meta http-equiv="refresh" content="10">
	<body>
		<center><h1>Done</h1></center>
                <center><p>
                <?php
                 system('date');
                 echo "<br>";
                 system('ps -ax | grep -w "python3 tree.py" | grep -v "grep"');
                ?>
                </p></center>
                <br>
                <center><a href="update.php">Return to Update Page.</a></center>
                <center><a href="index.php">Go to Search Page.</a></center>
	</body>
</html>"""
    ofile=open("status.php","w")
    ofile.write(html)
    ofile.close()

