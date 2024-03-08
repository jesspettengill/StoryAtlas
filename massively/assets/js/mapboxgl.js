// Define your MapBox map
mapboxgl.accessToken = 'YOUR_MAPBOX_ACCESS_TOKEN';
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11',
    center: [longitude, latitude], // Center coordinates
    zoom: 10 // Initial zoom level
});

// Load and add your GeoJSON data to the map
map.on('load', function () {
    map.addSource('points', {
        type: 'geojson',
        data: 'your_geojson_data.geojson' // Path to your GeoJSON file
    });

    // Define styles for each layer
    var layerStyles = {
        Layer1: {
            'circle-color': 'blue',
            'circle-radius': 6
        },
        Layer2: {
            'circle-color': 'red',
            'circle-radius': 6
        },
        // Add more layers and styles as needed
    };

    // Add a layer for each layer in the GeoJSON data
    for (var layer in layerStyles) {
        map.addLayer({
            'id': layer,
            'type': 'circle',
            'source': 'points',
            'filter': ['==', 'layer', layer],
            'paint': layerStyles[layer]
        });
    }

    // Add a temporal slider control
    var slider = document.getElementById('slider');
    slider.addEventListener('input', function(e) {
        var time = parseInt(e.target.value);
        // Update the time filter for each layer
        for (var layer in layerStyles) {
            map.setFilter(layer, ['<=', 'time', time]);
        }
    });
});

// Update the slider's max value based on the maximum time in the dataset
function setSliderMaxValue(maxTime) {
    var slider = document.getElementById('slider');
    slider.max = maxTime;
}
