// Define your MapBox access token
mapboxgl.accessToken = 'YOUR_MAPBOX_ACCESS_TOKEN';

// Function to create and configure a MapBox map
function createMap(containerId, style, center, zoom, geojsonData) {
    var map = new mapboxgl.Map({
        container: containerId,
        style: style,
        center: center,
        zoom: zoom
    });

    map.on('load', function () {
        map.addSource('points', {
            type: 'geojson',
            data: geojsonData
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
            }
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

        // Function to handle layer selection
        function handleLayerChange() {
            var selectedLayer = document.querySelector('input[name="layer"]:checked').value;

            // Show/hide layers based on selection
            for (var layer in layerStyles) {
                if (layer === selectedLayer) {
                    map.setLayoutProperty(layer, 'visibility', 'visible');
                } else {
                    map.setLayoutProperty(layer, 'visibility', 'none');
                }
            }
        }

        // Add event listener for radio buttons
        document.querySelectorAll('input[name="layer"]').forEach(function(radio) {
            radio.addEventListener('change', function() {
                handleLayerChange();
            });
        });
    });
}

// Example usage
createMap('map1', 'mapbox://styles/mapbox/streets-v11', [-73.9857, 40.7484], 10, 'data1.geojson');
