var renderer, scene, camera, pointLight, spotLight;

var fieldWidth = 300, fieldHeight = 200;

var blocoLargura, blocoAltura, blocoProfundidade, paddleQuality;
var bloco1DirY = 0, bloco2DirY = 0, blocoVelocidade = 3;


var bola, bloco1, bloco2;
var bolaDirX = 1, bolaDirY = 1, bolaVelocidade = 2;

var score1 = 0, score2 = 0, maxScore = 7;

// Nivel de dificuldade do oponente
var difficulty = 0.2;


function setup()
{
	document.getElementById("winnerBoard").innerHTML = "First to " + maxScore + " wins!";
	
	score1 = 0;
	score2 = 0;
	
	cria_cenario();
	
	draw();
}

function cria_cenario()
{
	// tamanho do enquadramento da cena
	var WIDTH = 640,
	  HEIGHT = 360;

	// atributos da camera
	var VIEW_ANGLE = 50,
	  ASPECT = WIDTH / HEIGHT,
	  NEAR = 0.1,
	  FAR = 10000;

	var c = document.getElementById("gameCanvas");

	//Renderização com WebGL
	renderer = new THREE.WebGLRenderer();
	camera =
	  new THREE.PerspectiveCamera(
		VIEW_ANGLE,
		ASPECT,
		NEAR,
		FAR);

	scene = new THREE.Scene();

	scene.add(camera);
	
	camera.position.z = 320;
	
	renderer.setSize(WIDTH, HEIGHT);

	c.appendChild(renderer.domElement);

	var planeWidth = fieldWidth,
		planeHeight = fieldHeight,
		planeQuality = 10;
		
	var bloco1Material =
	  new THREE.MeshLambertMaterial(
		{
		  color: 0x1B32C0
		});
	var bloco2Material =
	  new THREE.MeshLambertMaterial(
		{
		  color: 0xFF4045
		});
	var planeMaterial =
	  new THREE.MeshLambertMaterial(
		{
		  color: 0x4BD121
		});
	var tableMaterial =
	  new THREE.MeshLambertMaterial(
		{
		  color: 0x111111
		});

	var groundMaterial =
	  new THREE.MeshLambertMaterial(
		{
		  color: 0x2F2FAC
		});
		
		
	var plane = new THREE.Mesh(

	  new THREE.PlaneGeometry(
		planeWidth * 0.95,	
		planeHeight,
		planeQuality,
		planeQuality),

	  planeMaterial);
	  
	scene.add(plane);
	plane.receiveShadow = true;	
	
	var table = new THREE.Mesh(

	  new THREE.CubeGeometry(
		planeWidth * 1.05,	
		planeHeight * 1.03,
		100,				
		planeQuality,
		planeQuality,
		1),

	  tableMaterial);
	table.position.z = -51;	
	scene.add(table);
	table.receiveShadow = true;	
		
	var radius = 5,
		segments = 6,
		rings = 6;
		
	var sphereMaterial =
	  new THREE.MeshLambertMaterial(
		{
		  color: 0xD43001
		});
		
	bola = new THREE.Mesh(

	  new THREE.SphereGeometry(
		radius,
		segments,
		rings),

	  sphereMaterial);

	scene.add(bola);
	
	bola.position.x = 0;
	bola.position.y = 0;

	bola.position.z = radius;
	bola.receiveShadow = true;
    bola.castShadow = true;
	
	blocoLargura = 10;
	blocoAltura = 30;
	blocoProfundidade = 10;
	paddleQuality = 1;
		
	bloco1 = new THREE.Mesh(

	  new THREE.CubeGeometry(
		blocoLargura,
		blocoAltura,
		blocoProfundidade,
		paddleQuality,
		paddleQuality,
		paddleQuality),

	  bloco1Material);

	scene.add(bloco1);
	bloco1.receiveShadow = true;
    bloco1.castShadow = true;
	
	bloco2 = new THREE.Mesh(

	  new THREE.CubeGeometry(
		blocoLargura,
		blocoAltura,
		blocoProfundidade,
		paddleQuality,
		paddleQuality,
		paddleQuality),

	  bloco2Material);
	  
	scene.add(bloco2);
	bloco2.receiveShadow = true;
    bloco2.castShadow = true;	
	
	bloco1.position.x = -fieldWidth/2 + blocoLargura;
	bloco2.position.x = fieldWidth/2 - blocoLargura;
	
	bloco1.position.z = blocoProfundidade;
	bloco2.position.z = blocoProfundidade;
		
	var ground = new THREE.Mesh(

	  new THREE.CubeGeometry( 
	  1000, 
	  1000, 
	  3, 
	  1, 
	  1,
	  1 ),

	  groundMaterial);

	ground.position.z = -132;
	ground.receiveShadow = true;	
	scene.add(ground);		
		
	//Cria os focos de iluminação
	pointLight =
	  new THREE.PointLight(0xF8D898);


	pointLight.position.x = -1000;
	pointLight.position.y = 0;
	pointLight.position.z = 1000;
	pointLight.intensity = 2.9;
	pointLight.distance = 10000;
	scene.add(pointLight);
		

    spotLight = new THREE.SpotLight(0xF8D898);
    spotLight.position.set(0, 0, 460);
    spotLight.intensity = 1.5;
    spotLight.castShadow = true;
    scene.add(spotLight);
	
	renderer.shadowMapEnabled = true;		
}

function draw()
{	
	renderer.render(scene, camera);

	requestAnimationFrame(draw);
	
	bola_Interacao();
	blocoInteracao();
	cameraInteracao();
	jogador_blocoMove();
	oponente_blocoMove();
}

function bola_Interacao()
{

	if (bola.position.x <= -fieldWidth/2)
	{	
		// CPU scores
		score2++;

		document.getElementById("scores").innerHTML = score1 + "-" + score2;

		reinicia_jogo(2);
		placar_partida();	
	}
	

	if (bola.position.x >= fieldWidth/2)
	{	

		score1++;

		document.getElementById("scores").innerHTML = score1 + "-" + score2;

		reinicia_jogo(1);
		placar_partida();	
	}
	

	if (bola.position.y <= -fieldHeight/2)
	{
		bolaDirY = -bolaDirY;
	}	

	if (bola.position.y >= fieldHeight/2)
	{
		bolaDirY = -bolaDirY;
	}
	

	bola.position.x += bolaDirX * bolaVelocidade;
	bola.position.y += bolaDirY * bolaVelocidade;
	
	
	if (bolaDirY > bolaVelocidade * 2)
	{
		bolaDirY = bolaVelocidade * 2;
	}
	else if (bolaDirY < -bolaVelocidade * 2)
	{
		bolaDirY = -bolaVelocidade * 2;
	}
}


function oponente_blocoMove()
{
	bloco2DirY = (bola.position.y - bloco2.position.y) * difficulty;
	
	if (Math.abs(bloco2DirY) <= blocoVelocidade)
	{	
		bloco2.position.y += bloco2DirY;
	}
	else
	{
		if (bloco2DirY > blocoVelocidade)
		{
			bloco2.position.y += blocoVelocidade;
		}
		else if (bloco2DirY < -blocoVelocidade)
		{
			bloco2.position.y -= blocoVelocidade;
		}
	}
	
	bloco2.scale.y += (1 - bloco2.scale.y) * 0.2;	
}


function jogador_blocoMove()
{
	if (Key.isDown(Key.A))		
	{
		if (bloco1.position.y < fieldHeight * 0.45)
		{
			bloco1DirY = blocoVelocidade * 0.5;
		}
		else
		{
			bloco1DirY = 0;
			bloco1.scale.z += (10 - bloco1.scale.z) * 0.2;
		}
	}	

	else if (Key.isDown(Key.D))
	{
		if (bloco1.position.y > -fieldHeight * 0.45)
		{
			bloco1DirY = -blocoVelocidade * 0.5;
		}
		else
		{
			bloco1DirY = 0;
			bloco1.scale.z += (10 - bloco1.scale.z) * 0.2;
		}
	}
	else
	{
		bloco1DirY = 0;
	}
	
	bloco1.scale.y += (1 - bloco1.scale.y) * 0.2;	
	bloco1.scale.z += (1 - bloco1.scale.z) * 0.2;	
	bloco1.position.y += bloco1DirY;
}

function cameraInteracao()
{
	spotLight.position.x = bola.position.x * 2;
	spotLight.position.y = bola.position.y * 2;
	
	camera.position.x = bloco1.position.x - 100;
	camera.position.y += (bloco1.position.y - camera.position.y) * 0.05;
	camera.position.z = bloco1.position.z + 100 + 0.04 * (-bola.position.x + bloco1.position.x);
	
	camera.rotation.x = -0.01 * (bola.position.y) * Math.PI/180;
	camera.rotation.y = -60 * Math.PI/180;
	camera.rotation.z = -90 * Math.PI/180;
}

function blocoInteracao()
{
	if (bola.position.x <= bloco1.position.x + blocoLargura
	&&  bola.position.x >= bloco1.position.x)
	{
		if (bola.position.y <= bloco1.position.y + blocoAltura/2
		&&  bola.position.y >= bloco1.position.y - blocoAltura/2)
		{
			if (bolaDirX < 0)
			{

				bloco1.scale.y = 15;

				bolaDirX = -bolaDirX;
				bolaDirY -= bloco1DirY * 0.7;
			}
		}
	}
	
	
	if (bola.position.x <= bloco2.position.x + blocoLargura
	&&  bola.position.x >= bloco2.position.x)
	{
		if (bola.position.y <= bloco2.position.y + blocoAltura/2
		&&  bola.position.y >= bloco2.position.y - blocoAltura/2)
		{
			if (bolaDirX > 0)
			{
				bloco2.scale.y = 15;	

				bolaDirX = -bolaDirX;
				bolaDirY -= bloco2DirY * 0.7;
			}
		}
	}
}

function reinicia_jogo(loser)
{
	bola.position.x = 0;
	bola.position.y = 0;
	
	if (loser == 1)
	{
		bolaDirX = -1;
	}
	else
	{
		bolaDirX = 1;
	}
	
	bolaDirY = 1;
}

var bounceTime = 0;

function placar_partida()
{
	if (score1 >= maxScore)
	{
	
		bolaVelocidade = 0;
	
		document.getElementById("scores").innerHTML = "Jogador Ganhou!";		
		document.getElementById("winnerBoard").innerHTML = "F5 Para Jogar Novamente";
	
		bounceTime++;
		bloco1.position.z = Math.sin(bounceTime * 0.1) * 10;
	
		bloco1.scale.z = 2 + Math.abs(Math.sin(bounceTime * 0.1)) * 10;
		bloco1.scale.y = 2 + Math.abs(Math.sin(bounceTime * 0.05)) * 10;
	}
	
	else if (score2 >= maxScore)
	{
	
		bolaVelocidade = 0;
	
		document.getElementById("scores").innerHTML = "Oponente Ganhou!";
		document.getElementById("winnerBoard").innerHTML = "F5 Para Jogar Novamente";
	
		bounceTime++;
		bloco2.position.z = Math.sin(bounceTime * 0.1) * 10;
	
		bloco2.scale.z = 2 + Math.abs(Math.sin(bounceTime * 0.1)) * 10;
		bloco2.scale.y = 2 + Math.abs(Math.sin(bounceTime * 0.05)) * 10;
	}
}