<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<link rel="icon" href="loca.png">
<link rel="stylesheet" type="text/css" href="common.css">
<head>
    <title>Search</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
</head>
<body>
	<h1><center><img src="loca.png" /></center></h1>
	<h2><center>
	<form action="search.php" method="POST">
		<input type="text" name="search" />
		<input type="submit" name="submit" value="Search" />
	</form>
	</center></h2>

	<div id="DIV" style="bottom: 0; position: fixed;" >
	<table style="width:100%;"><td>
		<p id="DISC"> A product of Wisdom Technical Solutions, NoGuiLinux, (804) 845-4057, k.j.hirner.wisdom@gmail.com (client_browser: <?php echo get_browser(null,True)['browser'];$mem=memory_get_usage() ; echo ",mem_usage:".$mem; ?>)
		</p>
	</table></td>
	</div>
</body>
</html>
