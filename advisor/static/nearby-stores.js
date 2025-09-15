document.addEventListener("DOMContentLoaded", function () {
    const mapMsg = document.getElementById("map-message");
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(success, error);
    } else {
        mapMsg.textContent = "Geolocation is not supported by your browser.";
    }

    function success(position) {
        const lat = position.coords.latitude;
        const lon = position.coords.longitude;

        const apiKey = '46df6f4c5bb74520ba117ea80d56fc7c'; // Your API Key
        const map = L.map('map').setView([lat, lon], 14);

        L.tileLayer(
            `https://maps.geoapify.com/v1/tile/osm-bright/{z}/{x}/{y}.png?apiKey=${apiKey}`,
            { attribution: '© OpenStreetMap, © Geoapify' }
        ).addTo(map);

        L.marker([lat, lon]).addTo(map)
            .bindPopup("You are here")
            .openPopup();

        const radius = 10000; // meters
        const category = 'shop.garden_centre';
        //const category=building.shopping
        const endpoint = `https://api.geoapify.com/v2/places?categories=${category}&filter=circle:${lon},${lat},${radius}&limit=10&apiKey=${apiKey}`;

        fetch(endpoint)
            .then(response => response.json())
            .then(data => {
                if (data.features.length === 0) {
                    mapMsg.textContent = 'No nearby plant stores found.';
                }
                data.features.forEach(place => {
                    const [x, y] = place.geometry.coordinates;
                    L.marker([y, x]).addTo(map)
                        .bindPopup(`<b>${place.properties.name || 'Unnamed Store'}</b><br>${place.properties.street || ''}`);
                });
            })
            .catch(() => {
                mapMsg.textContent = 'Failed to load nearby plant stores.';
            });
    }

    function error(err) {
        mapMsg.textContent = 'Unable to get your location.';
    }
});
