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
	

	//$res=$con->query($sql);
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

echo "	
<link rel='stylesheet' media='screen and (min-device-width: 1400px)' href='style-900.1400.css'>
<link rel='stylesheet' media='screen and (max-device-width: 1280px)' href='style-800.1280.css'>
<link rel='stylesheet' media='screen and (max-device-width: 1279px)' href='style-less.css'>
<body>";
//start tile()
function tile($imgname,$md5,$path,$keywords) {

 echo "<div class='".$md5."'>
		<!-- create the tile -->

		<table id='tile'>
			<tr>
			 <th><a href='"."$imgname"."'><img src='".$imgname."'</a></th>
			</tr>
			<tr>
			 <td>
			  <!-- create subtable 1 for tile  -->
			  <table>
			   <tr>
			    <th><p>
				<div class='tooltip'>
				 ".basename($imgname)."
				 <span class='tooltiptext'>Image Name</span>
				</div>
				</p>
			    </th>
			   </tr>
                           <tr>
                            <td>
			     <!-- create subtable 2 for tile-->
                             <table>
                              <tr>
			       <th><hr></th>
			      </tr>
			      <tr>
			       <td><div class='tooltip'>
				<p id='id'>".$md5."</p>
			       <span class='tooltiptext'>
				Image ID
				</span>
				</div>
				</td>
			      </tr>
			      <tr>
			       <td><div class='tooltip'><a href='".$path." 'alt='".$path."'>Download</a><span class='tooltiptext'>Download</span></div></td>
			      </tr>
			      <tr>
			       <td><div class='tooltip'><p>"."Keywords (Hover for Keywords)"."</p><span class='tooltiptext'>".$keywords."</span></div></td>
			      </tr>
                             </table>
                             <!-- end create subtable 2 for tile -->
                            </td>
                           </tr>
			  </table>
			  <!-- end create subtable 1 for tile -->
			 </td>
			</tr>
		<!-- end create the tile -->
		</table>
		</div>";
}
//end function tile()

echo "<div style='width: 100%;'>";
//$con=mysqli_connect("localhost","carl","avalon","clips") or die ("db connect issues");
//sql data
$result=mysqli_query($con,$sql) or die ("query issues");

echo "<div class='row2'>";
while ( $row=mysqli_fetch_array($result) ) {
	tile($row[0],$row[3],$row[1],$row[2]);
}
echo "</div>";
echo "</div>";

	$mem=memory_get_usage();
	echo '<p id="DISC"> A product of Wisdom Technical Solutions, NoGuiLinux, (804) 845-4057, k.j.hirner.wisdom@gmail.com (client_browser: '.$browser['browser'].', mem_used:'.$mem.')</p>';
	echo "</table></td>";
	echo '</div>';
	}
	echo '</html>';
	}
?>

