 var map = L.mapbox.map('map', 'retornam.ionbikm0')
                .setView([37.545, -122.482], 10);
            var featureLayer = L.mapbox.featureLayer()
                .loadURL('jsoncoords.json')
                .addTo(map);