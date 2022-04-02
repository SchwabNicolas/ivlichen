window.addEventListener("load", function () {
    var locations = [
        ["test 1", 47.1219567396, 6.9147693738],
        ["test 2", 46.8182, 7.2275],
        ["test 3", 46.8182, 8.2275],
    ];

    var map = L.map('map').setView([46.8182, 8.2275], 8);

    for (var i = 0; i < locations.length; i++) {
        marker = new L.marker([locations[i][1], locations[i][2]])
        .bindPopup(locations[i][0])
        .addTo(map);
    }
    //var marker = L.marker([47.1219567396, 6.9147693738]).addTo(map)

    L.tileLayer('https://api.maptiler.com/maps/cadastre/256/{z}/{x}/{y}.png?key=JMZB74MQz61U6FKfnOEa',{
        attribution: "\u003ca href=\"https://www.maptiler.com/copyright/\" target=\"_blank\"\u003e\u0026copy; MapTiler\u003c/a\u003e \u003ca href=\"https://www.openstreetmap.org/copyright\" target=\"_blank\"\u003e\u0026copy; OpenStreetMap contributors\u003c/a\u003e",
    }).addTo(map);
});