<?php
#set the page tab icon 
#works on firefox and chrome, ie based browsers
$icon="loca.png";
if ( file_exists($icon) ) {
	echo "<link rel='icon' href='".$icon."'>";
}
#import css style sheets
echo "<link rel='stylesheet' type='text/css' href='searchbar.css'>";
echo "<link rel='stylesheet' type='text/css' href='common.css'>";
echo "<link rel='stylesheet' type='text/css' href='gridview.css'>";
echo "<link rel='stylesheet' type='text/css' media='screen and (min-device-width: 1400px)' href='gridview900.1400.css'>";
echo "<link rel='stylesheet' type='text/css' media='screen and (max-device-width: 1280px)' href='gridview800.1280.css'>";
echo "<link rel='stylesheet' type='text/css' media='screen and (max-device-width: 1279px)' href='gridview-less.css'>";

# set default index
$searchPage="index.php";
#set page memory limit
ini_set('memory_limit','512M');
#get db info set
$servername="127.0.0.1";
$username="carl";
$password="avalon";
$dbname="clips";

#search db value
$search_value=addslashes($_GET['search']);

$con=mysqli_connect($servername,$username,$password,$dbname) or die("could not connect to Database");
$offset=0;
$max=250;
if ( strlen($search_value) < 2 ) {
	//warn the user of too few characters
	echo "Due to hardware and software constraints,<br>";
	echo "please keep searches to two, or more, (2+),<br>";
	echo "characters in length. Thank you!<br><br>";
	echo "<a href='".$searchPage."'>Return to the Loca Search Page</a>";
} else {
	if (strcmp($_GET['page'],'') == 0 ){
		$offset=0;
	} else {
		$offset=$_GET['page'];
	}
	//set the query string for sql
	$sql="select * from clipart where keyword like '%".$search_value."%' or clipID='".$search_value."' order by clipID limit ".$max." offset ".$offset.";" ;

	$result=mysqli_query($con,$sql) or die ("there were some issues with that query");
	
	$logosize=getimagesize($icon);
	$logW=$logosize[0]/2;
	$logH=$logosize[1]/2;
	echo "<body>";
	echo "<div id='searchbar'>";
	echo "<div id='searchbarSub'>";
	echo "<h1><center><a href='".$searchPage."'><img src='".$icon."' style='width:".$logW."px;height:".$logH."px;' /></a></center></h1>";
	echo "<h2><center>";
	echo "<form action='search.php' method='get'>";
	echo "<input type='text' name='search' />";
	echo "<br>";
	echo "<input type='submit' name='submit' value='Search' />";
	echo "</form>";
	echo "</center></h2>";
	echo "<div style='background-color:lightgray;border: solid black 2px;'>";
	$offset=$offset+$max;
	if (!(  mysqli_num_rows($result) < $max )){
		echo "<div><a href='search.php?search=".$search_value."&submit=Search&page=".$offset."'>Next - ".$search_value."</a></div>";
	}
	$offset=$offset - ($max*2);
	if (!($offset < 0)){
		echo "<div><a href='search.php?search=".$search_value."&submit=Search&page=".$offset."'>Back - ".$search_value."</a></div>";
	}
	echo "</div>";
	echo "</div>";
	echo "</div>";
	echo "<div id='results'>";
	echo "</div>";
	echo "<div class='gridview'>"; 
//	echo "<div id='results'>";
//	echo "</div>";
	while ($row=mysqli_fetch_array($result)){
		echo "<div id='tile'>";
		echo "<div class='".$row[3]."'>";
		echo "<center>";
		echo "<p id='IDA'><strong>".$row[3].'</strong></p>';
		echo "<a href='".$row[0]."'><img id='DISPLAY' src='".$row[0]."'></a>";
		echo "<br>";
		//echo "<p id='IDA'><strong>ID:</strong>".$row[3].'</p>';
		echo "<a download='".basename($row[1])."' href='".$row[1]."'>Download</a>";
		echo "</center>";
		echo "</div>";
		echo "</div>";
	}
	echo "</div>";
	echo "<div id='DIV'>";
        $mem=memory_get_usage();
        echo '<p id="DISC"> A product of Wisdom Technical Solutions, NoGuiLinux, (804) 845-4057, k.j.hirner.wisdom@gmail.com (client_browser: '.$browser['browser'].', mem_used:'.$mem.')</p>';
        echo "</table></td>";
        echo '</div>';
}

?>
