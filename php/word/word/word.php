<html>
<head>
	<title>Word</title>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>

	<?php if ( $_GET['refresh'] == "Inf. Refresh"): $re=0; ?>
	<form method="get" action=''>
		<input type="submit" name="refresh" value="Stop Refreshing" formenctype="application/x-www-form-urlencoded">
	</form>
	<?php endif; ?>

	<?php if ( $_GET['refresh'] == "Inf. Refresh" ): ?>
	<meta http-equiv="refresh" content="1" />
	
	<?php else: $refresh=0 ; ?> 
		<form method="get" action=''>
			<input type="submit" name="refresh" value="Single Refresh">
		</form>
		<form method="get" action="word.php">
			<input type="submit" name="refresh" value="Inf. Refresh" formenctype="application/x-www-form-urlencoded">
		</form>

	<?php endif;?>
	<link rel="stylesheet" content="text/css" href="datecode.css">
</head>
<body>
	<! get the date >
	<?php
		$date=exec("date +H%HM%MS%S-mm%mdd%dyy%Y;");
		
		$seed=exec('python3 seed.py');
		$rand=exec('python3 rand.py');
		$sha512=exec("echo '".$date.$seed.$rand."' | sha512sum | cut -f1 -d' ' ;");
		$sec=exec("date +%S;");
		$file="/dev/shm/datecode.txt";
		//uncomment the line below and comment the line above if issues occur
		//$file=$_SERVER['DOCUMENT_ROOT'].'middle/php/'.'datecode.txt';
		$handle = fopen($file,'w+') or die('cannot open file');
		$data="date: $date\n"."sha512: $sha512\n";
		fwrite($handle,$data);
	?>
	<div style="width:100%;">
	<center>
	<h1>The Datecode SHA512 Random Key Generator</h1>
	<table>
		<tr>
			<th>
			<p>
			<?php if (( $sec % 2 ) == 0 ): $odd=0 ; ?>
			*
			<?php endif; ?>
			Datecode
			<?php if (( $sec % 2 ) == 0 ): $odd=0 ; ?>
			*
			<?php endif; ?>
			</p>
			</th>

			<th><p>
			<?php if (( $sec % 2 ) != 0): $odd=1 ; ?>
			*
			<?php endif; ?>
			sha512 key
			<?php if (( $sec % 2 ) != 0): $odd=1 ; ?>
			*
			<?php endif; ?>
			</p>
			<th>Download</th>
		</tr>
		<tr>
		<td>
			<! step into php code and determine if sec is odd or even >
			<?php if ( ($sec % 2) == 0 ) { ?>
			<! if sec is even, then underline the datecode >
			<strong><?php echo $date; ?></strong>	
			<! else display the datecode not underlined >
			<?php } else { echo $date; } ?>
		</td>
		<td>
			<?php if (( $sec % 2 ) != 0 ): $odd=1; ?>
			<strong>
			<?php endif; ?>
			<p><?php echo $sha512; ?></p>
			<?php if (( $sec % 2 ) != 0 ): $odd=1; ?>
			</strong>
			<?php endif; ?>

		</td>
			<td><a href=<?php echo $file;?> download>Download</a>
		</tr>
	</table>
	</center>
	</div>

</body>
</html>
