<html>
<head>
        <title>MOVEABLE CAM</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link href="https://fonts.googleapis.com/css2?family=Yusei+Magic&display=swap"
        rel="stylesheet">
	<style>
		body{
			font-family: 'Yusei Magic', sans-serif;
			text-align: center;
		}
		h1{
			margin-top:50px;
		}
		button{
			border: 2px solid black;
			background-color: #EFF8F5;
			font-family: 'Yusei Magic', sans-serif;
			border-radius: 8px;
			padding: 8px 10px;
			font-size:14px;
		}
		button:hover{
			background-color:white;
		}
		.contents{
			margin-top:40px;
			font-size:13px;
		}
		.bottom{
			font-size:12px;
		}
	</style>
</head>
<body bgcolor="#EFF8F5">
        <h1>MOVEABLE CAM</h1>
        <p>
                <p>- activation -</p>
                <form method="get" action="pjServer.php">
                        <button type="submit" name="GO">GO</button>
	        	<button type="submit" name="COME">COME</button>
	        	<button type="submit" name="STOP">STOP</button>
                </form>
        </p>
	<div class="contents">
		select button to move your camera:<br><br>
		"GO" to make it go back.<br>
		"COME" to make it come to you.<br>
		"STOP" to stop its movement.<br><br>
		---<br><br>
	</div>
	<div class="bottom">
		IAB2 final project<br>
		created by. Hyeonjin Kim<br>
		contact: peaceful1@snu.ac.kr
	</div>
	<p>
        <?php
        $setmode3 = shell_exec("/usr/local/bin/gpio -g mode 3 out");
        $setmode4 = shell_exec("/usr/local/bin/gpio -g mode 4 out");
        $setmode5 = shell_exec("/usr/local/bin/gpio -g mode 5 out");
        $setmode6 = shell_exec("/usr/local/bin/gpio -g mode 6 out");

        if(isset($_GET['GO'])){
                $gpio_on=shell_exec("/usr/local/bin/gpio -g write 3 0");
                $gpio_on=shell_exec("/usr/local/bin/gpio -g write 6 0");
                $gpio_on=shell_exec("/usr/local/bin/gpio -g write 4 1");
                $gpio_on=shell_exec("/usr/local/bin/gpio -g write 5 1");
        }
        else if(isset($_GET['COME'])){
                $gpio_on=shell_exec("/usr/local/bin/gpio -g write 3 1");
                $gpio_on=shell_exec("/usr/local/bin/gpio -g write 6 1");
                $gpio_on=shell_exec("/usr/local/bin/gpio -g write 4 0");
                $gpio_on=shell_exec("/usr/local/bin/gpio -g write 5 0");
        }
        else if(isset($_GET['STOP'])){
                $gpio_on=shell_exec("/usr/local/bin/gpio -g write 3 0");
                $gpio_on=shell_exec("/usr/local/bin/gpio -g write 6 0");
                $gpio_on=shell_exec("/usr/local/bin/gpio -g write 4 0");
                $gpio_on=shell_exec("/usr/local/bin/gpio -g write 5 0");
        }
        ?>
</body>
</html>
