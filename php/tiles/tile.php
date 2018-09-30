<?php

//global scope spec info that will be modified later
echo "<html>
<style>
#tile {
width: 75%;
height: 25%;
border: solid black 1px;
}
#tile img {
width: 25%;
height; auto;
border: solid darkgray 3px;
}
p {
width: 100%;
overflow: hidden;
}
#id {
font-family: 'Courier New', courier ,monospace;
font-size: 20px;
}
.tooltip {
    position: relative;
    display: inline-block;
    border-bottom: 1px dotted black; /* If you want dots under the hoverable text */
}

/* Tooltip text */
.tooltip .tooltiptext {
    visibility: hidden;
    width: 500px;
    background-color: black;
    color: #fff;
    text-align: left;
    padding: 5px 0;
    border-radius: 6px;

    /* Position the tooltip text - see examples below! */
    position: float;
    z-index: 1;
}

/* Show the tooltip text when you mouse over the tooltip container */
.tooltip:hover .tooltiptext {
    visibility: visible;
}
.row2 {
 display: grid;
 grid-template-columns: 33% 66%;
 grid-gap: 10px;
}
* {
box-sizing: border-box;
}

</style>
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
$con=mysqli_connect("localhost","carl","avalon","clips") or die ("db connect issues");
//sql data
$result=mysqli_query($con,"select * from clipart where keyword like '%house%';") or die ("query issues");

echo "<div class='row2'>";
while ( $row=mysqli_fetch_array($result) ) {
	tile($row[0],$row[3],$row[1],$row[2]);
}
echo "</div>";
echo "</div>";
echo "
</body>
</html>

";
?>
