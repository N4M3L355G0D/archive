<html>
<?php
 $refresh=10;
?>
<meta http-equiv="refresh" content="<?php echo $refresh; ?>" >
<body>
<center>
 <div>
  <h1>System Status</h1>
  <h4>Page Refresh: <?php echo $refresh; ?> Sec</h4>
 </div>
</center>
<hr>
<div>
 <pre>
  <?php
   $a=shell_exec("acpi");
   $b=shell_exec("date");
   $c=shell_exec("ip addr");
   $d=shell_exec("nmcli dev wifi");
   $e=shell_exec("free -h");
   $f=shell_exec("top -bn1 | grep 'Cpu' | awk '{print $3;}'");
   $g=shell_exec("iostat");
   echo $a."<br>";
   echo $b."<br>";
   echo $c."<br>";
   echo $d."<br>";
   echo $e."<br>";
   echo 'CPU USEAGE<br>'.$f."<br>";
   echo $g."<br>";
  ?>
 </pre>
</div>


</body>
</html>
