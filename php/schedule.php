<html>
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
	<body>
		<div class="aria">
			<div>
				<center><h1>Set Schedule Display<h1></center>
			</div>

		<div>
			<form action='docgen.php' method="get">
				<table>
					<div>
						<legend><h1>Set Schedule Times</h1></legend>
					</div>
					<div>
						<tr>
							<th>Sunday</th>
							<th>Monday</th>
							<th>Tuesday</th>
						</tr>
						<tr>
							<td><input type="text" name="sun" value=''></td>
							<td><input type="text" name="mon" value=''></td>
							<td><input type="text" name="wed" value=''></td>
						</tr>
					</div>	
				</table>
				<br>		
				<table>
					<div>
						<tr>
							<th>Wednesday</th>
							<th>Thursday</th>
							<th>Friday</th>
						</tr>
						<tr>
							<td><input type="text" name="tue" value=''></td>
							<td><input type="text" name="thu" value=''></td>
							<td><input type="text" name="fri" value=''></td>
						</tr>
					</div>
				</table>
				<br>
				<table>
					<div>
						<tr>
							<th>Saturday</th>
						</tr>
						<tr>
							<td><input type="text" name="sat" value=''></td>
						</tr>
					</div>
				</table>
				<br>	
				<input type="submit" name="submit" value="Preview" formenctype="application/x-www-form-urlencoded">
				<input type="submit" name="submit" value="Submit" formenctype="application/x-www-form-urlencoded">
			</form>
		</div>
		</div>
		</div>
		</div>
	</body>

</html>
