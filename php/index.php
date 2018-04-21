<!DOCTYPE html>
<html>
<head>
	<title>Old Music Website</title>
	<link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
	<script type="text/javascript" src="js/jquery-3.3.1.js"></script>
	<script type="text/javascript" src="js/bootstrap.min.js"></script>
</head>
<body>

<h1 class="text-center">OLD MUSIC WEBSITE</h1>

<div>


<div class="container">
	

  <!-- Nav tabs -->
  <ul class="nav nav-tabs" role="tablist">

<?php
  $i = 0;
  foreach (range('A', 'Z') as $char) {
    $i = $i + 1;
    ?>
      <li role="presentation" <?php if($i == 1){echo 'class="active"';} ?>><a href="#<?php echo $char; ?> " aria-controls="<?php echo $char; ?> " role="tab" data-toggle="tab"><?php echo $char; ?> </a></li>
    <?php
  }
?>
  </ul>



  <!-- Tab panes -->
  <div class="tab-content">
<?php
  $i = 0;
  foreach (range('A', 'Z') as $char) {
    $i = $i + 1;
    ?>

    <div role="tabpanel" class="tab-pane  <?php if($i == 1){echo 'active';} ?>" id="<?php echo $char; ?>">
    	

<?php

  include 'db_config.php';

  $sql = "SELECT id,title,size FROM songs WHERE title LIKE '$char%' ORDER BY title";
  
  $result = mysqli_query($con,$sql);

  $check_post = mysqli_num_rows($result);

  if ($check_post > 0) {

    while ($row = mysqli_fetch_assoc($result)) {
      $data[] = $row;
    }

?>

      <table class="table table-striped">
    		<tr>
    			<td>Title</td>
    			<td>Size</td>
    			<td>Play/Download</td>
    		</tr>



<?php 
foreach ($data as $key) {
?>
      	<tr>
    			<td><?php echo $key['title'] ?></td>
    			<td><?php echo $key['size'] ?></td>
    			<td><a href="player.php?id=<?php echo $key['id'] ?>">Details</a></td>
    		</tr>

<?php
}
?>


		</table>
    <?php
    } else {
      echo "Sorry song Not Available.";
    }
    ?>


    </div>
    <?php
  }
?>

  </div>

</div>


</div>

</body>
</html>