
<!DOCTYPE html>

<html lang="en">

	<head>
	
		<script type="text/javascript" src="https://www.google.com/jsapi"></script>

		<script type="text/javascript">
		  google.load("visualization", "1",{packages: ['gauge']});
		</script>
		
		<script type="text/javascript">
			var gauge;
		    var gaugeData;
		    var gaugeOptions;
		    
		    function drawGauge() {
		      gaugeData = google.visualization.arrayToDataTable([
		        ['% Done'],
		        [10]
		      ]);
		    
		      gauge = new google.visualization.Gauge(document.getElementById('gauge'));
		      gaugeOptions = {
		          width: 300, height: 300,
		          min: 0,
		          max: 100,
		          yellowFrom: 50, yellowTo: 80,
		          redFrom: 0, redTo: 50,
		          greenFrom:80, greenTo:100,
		          minorTicks: 5,
		          //majorTicks: ['0','10','20','30','40','50','60','70','80','90','100']
		      };
		      gauge.draw(gaugeData, gaugeOptions);
		    }
		    google.setOnLoadCallback(drawGauge);
		</script>

		<script type="text/javascript">
			function printTextFile() {
				var filename = document.getElementById("files").value;

				elem = document.getElementById("textfile_out");
				

				elem.innerHTML = filename;
			}
		</script>

	</head>




	<body align="center"  bgcolor="#777766">
		
		<h1>
			Master Chief
		</h1>

		<h2>
			A webapp which compares the run time of different algorithms
		</h2>

		<p>
			This webapp is still underconstruction! check out <a href="https://github.com/Darkmer/masterchief">MasterChief</a> to see how the app is coming along
		</p>

		<div id="gauge" align='center'></div>


		<select id="files">
			<option value="index.php">index</option>
			<option value="guage.js">gauge</option>
			<option value="dbSetup.sql">database</option>
		</select>
		<button onclick="printTextFile()">Print It</button>
		
		<p id="textfile_out"> </p>
	</body>







</html>