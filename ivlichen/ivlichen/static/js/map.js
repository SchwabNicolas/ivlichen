window.addEventListener("load", function () {

    const locations = JSON.parse(document.getElementById('coordinates-data').textContent);
    console.log(locations)
    var map = L.map('map').setView([46.8182, 8.2275], 8);

    for (var i = 0; i < locations.length; i++) {
        marker = new L.marker(
        [locations[i][1], locations[i][2]])
        .bindPopup(locations[i][0])
        .addTo(map);
        circle = new L.circle(
        [locations[i][1], locations[i][2]],
        {radius: 100})
        .addTo(map);
    }

    L.tileLayer('https://api.maptiler.com/maps/streets/{z}/{x}/{y}.png?key=JMZB74MQz61U6FKfnOEa',{
        attribution: "\u003ca href=\"https://www.maptiler.com/copyright/\" target=\"_blank\"\u003e\u0026copy; MapTiler\u003c/a\u003e \u003ca href=\"https://www.openstreetmap.org/copyright\" target=\"_blank\"\u003e\u0026copy; OpenStreetMap contributors\u003c/a\u003e",
    }).addTo(map);
});