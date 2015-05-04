var AIS = (function() {

	// Farben fuer den Color Iterator
	var AISShipColors = ['#48AEFF', '#7FFFD4', '#C00054', '#87EF84', '#DBA7F8', '#EBC79E'];

	// Latitude und Logitude Grenzen des Kartenausschnitts
	var top = 50.759427;
	var bottom = 50.715809;
	var left = 7.089307;
	var right = 7.155004;

	// Hoehe und Breite des Kartenausschnitts in pixel
	var height = 800; // pixel
	var width = 766;

	// Aufloesung der Karte (Pixel pro Grad)
	var pixelPerLatitudeDegree =  height / (top - bottom);
	var pixelPerLongitudeDegree = width / (right - left);
	console.log('pixelPerLatitudeDegree:', pixelPerLatitudeDegree);
	console.log('pixelPerLongitudeDegree:', pixelPerLongitudeDegree);

	// Hoehe und Breite der Schiffe in pixel
	var shipHeight = 20;
	var shipWidth = 5;

	// Aufgabe 2
	var colorIterator = function(){
		// Gemeinsamer Color Index für alle zurückgegebenen Iteratoren
		var currentColorIndex = 0;

		return function next() {
			// Setze Index counter zurück, wenn am Ende angekommen
			if (currentColorIndex === AISShipColors.length) {
				currentColorIndex = 0;
			}
			return AISShipColors[currentColorIndex++];
		};
	};


	// Ship Konstruktor
	var Ship = function(mmsi, latitude, longitude, courseOverGround) {
		// Aufgabe 3
		this.mmsi = mmsi;
		this.latitude = latitude;
		this.longitude = longitude;
		this.courseOverGround = courseOverGround;
	};

	Ship.prototype.draw = function(canvas, color){
		// Aufgabe 6

		//     |
		//     .
		//    /|\
		//   / | \    ___2/3
		//  |  |  |
		//--|--.--| ------
		//  |  |  |
		//  |  |  |
		//  |-----|
		//     |
		//     |

		var ctx = canvas.getContext('2d');

		// Merke Canvas Zustand
		ctx.save();

		// Setze Füllfarbe
		ctx.fillStyle = color;

		// Errechne Position des Mittelspunkts, relativ zum Ursprung (in Pixel)
		var centerX = (this.longitude - left) * pixelPerLongitudeDegree;
		var centerY = (top - this.latitude) * pixelPerLatitudeDegree;

		// Verschiebe Ursprung zum Mittelpunkt
		ctx.translate(centerX, centerY);

		// Rotiere Canvas für richtige Ausrichtung des Schiffes
		var radians = (Math.PI / 180) * this.courseOverGround;
		ctx.rotate(radians);

		// Verschiebe Ursprung zurück
		ctx.translate(-centerX, -centerY);

		// Errechne relevante Positionen (Startpunkt: Linke untere Ecke)
		// Linke untere Ecke des Rechtecks
		var lowerLeftRectX = centerX - (shipWidth / 2); // Hälfte der Breite nach links
		var lowerLeftRectY = centerY + (shipHeight / 2); // Hälfte der Höhe nach unten

		// Linke obere Ecke des Rechtecks
		var upperLeftRectX = lowerLeftRectX; // X-Wert unverändert
		var upperLeftRectY = lowerLeftRectY - (shipHeight*2/3); // 2/3 der Schiffshöhe nach oben

		// Rechte obere Ecke des Rechtecks
		var upperRightRectX = upperLeftRectX + shipWidth; // Schiffsbreite nach rechts
		var upperRightRectY = upperLeftRectY;

		// Rechte untere Ecke des Rechtecks
		var lowerRightRectX = upperRightRectX;
		var lowerRightRectY = upperRightRectY + (shipHeight*2/3); // 2/3 der Schiffshöhe nach unten

		// Spitze
		var apexX = centerX; // Wie Mittelpunkt
		var apexY = centerY - (shipHeight / 2); // Vom Mittelpunkt Hälfte der Höhe nach oben

		// Zeichne
		ctx.beginPath();
		ctx.moveTo(lowerLeftRectX, lowerLeftRectY);
		ctx.lineTo(upperLeftRectX, upperLeftRectY);
		ctx.lineTo(apexX, apexY);
		ctx.lineTo(upperRightRectX, upperRightRectY);
		ctx.lineTo(lowerRightRectX, lowerRightRectY);
		ctx.closePath();
		ctx.fill(); // Ausfüllen
		ctx.stroke(); // Umranden

		// Setze Canvas Zustand zurück
		ctx.restore();
	};

	// ShipList Konstruktor
	var ShipList = function(){
		this.list = []; // initialisieren eines Arrays zum aufnehmen der Ship Objekte
	};

	ShipList.prototype.filter = function(filterFunction){
		// Aufgabe 4
		var filteredList = [];

		this.list.forEach(function(value, index, arr) {
			if (filterFunction(value) === true) {
				filteredList.push(value)
			}
		});

		this.list = filteredList;
	};

	// Laden der Daten und Zeichnen aller Schiffe auf das uebergebene Canvas
	var drawAllShips = function(canvas){

		// neue ShipList erstellen
		var currentShips = new AIS.ShipList();

		// fuer jeden Datensatz, ein Ship erstellen und in die ShipList legen
		for(var i = 0; i < AISData.length; i++){
			currentShips.list.push(new AIS.Ship(
					AISData[i].mmsi,
					AISData[i].latitude,
					AISData[i].longitude,
					AISData[i].courseOverGround));
		}

		// Filtern der Schiffe, die sich nicht auf dem Kartenausschnitt befinden
		currentShips.filter(function(ship){
			return ship.longitude >= left && ship.longitude <= right && ship.latitude >= bottom && ship.latitude <= top;
		});

		// neuen Color Iterator erstellen
		var colors = AIS.colorIterator();

		// alle Ships, mit jeweils der naechsten Farbe rendern
		for (var i = 0; i < currentShips.list.length; i++) {
			var ship = currentShips.list[i];
			ship.draw(canvas, colors());
		};
	};

	return {
		Ship : Ship,
		ShipList : ShipList,
		drawAllShips : drawAllShips,
		colorIterator : colorIterator
	};

})();

document.addEventListener("DOMContentLoaded", function() {
	var canvas = document.getElementById('map'); // get Element from the DOM

	// Aufgabe 5
	var img = new Image();

	// Registriere Event handler, der ausgeführt wird, sobald das Bild geladen ist
	img.addEventListener('load', function() {
  		canvas.getContext('2d').drawImage(img, 0, 0);
		AIS.drawAllShips(canvas);
	}, false);

	img.src = 'images/map.png';

	// Zeichnen sie zuerst die Karte (images/map.png) auf das canvas. Anschliessend, lassen Sie alle Schiffe auf die Karte zeichnen: AIS.drawAllShips(canvas);.

}, false);
