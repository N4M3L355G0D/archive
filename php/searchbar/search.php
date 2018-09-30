<?php
ini_set('memory_limit','512M');
$servername="127.0.0.1";
$username="carl";
$password="avalon";
$dbname="clips";
//$search_value=mysqli_real_escape_string($_POST["search"]);
$search_value=addslashes($_POST['search']);
$con=new mysqli($servername,$username,$password,$dbname);
if($con->connect_error){
    echo 'Connection Faild: '.$con->connect_error;
}
else{
	if ( strlen($search_value) < 2 ) {
		$searchPage="index.php";
		echo "Due to hardware and software constraints,<br>";
		echo "please keep searches to two (2) or<br> ";
		echo "more (> X) characters in length. Thank you! <br><br>";
		echo "Click the link below to <br>";
		echo "<a href='".$searchPage."'>Return to the Loca Search Page</a>";
	}
	else {
       	$sql="select * from clipart where keyword like \"%$search_value%\" or clipID='$search_value'";
	

	$res=$con->query($sql);
	$browser=get_browser(null,True);
	echo '<html>';
	if (preg_match('~MSIE|Internet Explorer~i', $_SERVER['HTTP_USER_AGENT']) || (strpos($_SERVER['HTTP_USER_AGENT'], 'Trident/7.0; rv:11.0') !== false)) {
		echo '<link rel="icon" href="loca.ico">'; 
	}
	else {
	echo '<link rel="icon" href="loca.png">';
	}
	echo '<link rel="stylesheet" type="text/css" href="common.css">';

	/*echo '<div id="DIV">';
	echo '<p id="DISC"> A product of Wisdom Technical Solutions, NoGuiLinux, (804) 845-4057, k.j.hirner.wisdom@gmail.com (client_browser: '.$browser['browser'].')</p>';
	echo '</div>';*/

	echo '<hr>';
	$logosize=getimagesize("loca.png");
	$logW=$logosize[0]/2;
	$logH=$logosize[1]/2;
	echo '<h1><center><a href="index.php"><img src="loca.png" style="width:'.$logW.'px;height:'.$logH.'px;"/></a></center></h1>';
	echo '<h2><center>';
	echo '<form action="search.php" method="POST">';
	echo '<input type="text" name="search" />';
	echo '<input type="submit" name="submit" value="Search" />';
	echo '</form>';
	echo '</center></h2>';
	echo '<div>';
	echo '<table style="width:100%;height:100%;text-overflow:scroll;">';
	echo '<tr>';
	echo '<th>IMG</th>';
	echo '<th>Download</th>';
	echo '<th>Keyword Entered</th>';
	echo '<th>Keyword</th>';
	echo '<th>ID</th>';
	echo '</tr>';
	while($row=$res->fetch_assoc()){
		echo '<tr>'; 
		$size = getimagesize($row["urlThumbNail"]);
		$width=$size[0]/5;
		$height=$size[1]/5;
		if (($height > 400) or ($width > 400)){
			$height=$size[1]/10;
			$width=$size[0]/10;
		}
		echo '<td>'.'<img src="'.$row["urlThumbNail"].'" alt="'.$row["urlThumbNail"].'" style="width:'.$width.'px;height:'.$height.'px;">'.'</td>';
		echo '<td>'.'<a href="'.$row["urlVector"].'" download>'.$row["urlVector"].'</a>'.'</td>';
		echo '<td>'.$search_value.'</td>';
		echo '<td>'.$row["keyword"].'</td>';
		echo '<td>'.$row["clipID"].'</td>';
		echo '</tr>';


	}       
	echo '</table>';
	echo '<hr>';
	echo '</div>';
	echo '<div id="DIV">';
	echo '<table style="width:100%;"><td>';
	$mem=memory_get_usage();
	echo '<p id="DISC"> A product of Wisdom Technical Solutions, NoGuiLinux, (804) 845-4057, k.j.hirner.wisdom@gmail.com (client_browser: '.$browser['browser'].', mem_used:'.$mem.')</p>';
	echo "</table></td>";
	echo '</div>';
	}
	echo '</html>';
	}
?>

