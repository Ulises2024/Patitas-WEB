mapboxgl.accessToken = 'pk.eyJ1IjoidWxtb3IiLCJhIjoiY2xpN2wzY2NiMHJvbDNlczVxZjFhbTU2ZCJ9.NOOM5PpRmdMaoZLlfyElwg';

// Crea una instancia del mapa
var map = new mapboxgl.Map({
  container: 'map', // ID del contenedor del mapa
  style: 'mapbox://styles/mapbox/streets-v11', // Estilo del mapa (puedes elegir otro)
  center: [-70.75248151796418, -33.51112012371187], // Coordenadas de ubicación inicial del mapa
  zoom: 12 // Nivel de zoom inicial
});

// Crea el marcador de Mapbox y establece la ubicación
var marker_tienda = new mapboxgl.Marker({ color: '#d317aa' })
  .setLngLat([-70.75248151796418, -33.51112012371187]) // Coordenadas de ubicación del marcador
  .addTo(map);

// Crea una etiqueta personalizada
var popup_tienda = new mapboxgl.Popup({ offset: 25 }).setText('Tienda Patitas');

// Asocia la etiqueta al marcador
marker_tienda.setPopup(popup_tienda);

// Crea el marcador de Mapbox y establece la ubicación
var marker_cliente = new mapboxgl.Marker({ color: '#d317aa' })
  .setLngLat([-70.77000481315878, -33.48593729407288]) // Coordenadas de ubicación del marcador -33.48593729407288, -70.77000481315878
  .addTo(map);

// Crea una etiqueta personalizada
var popup_cliente = new mapboxgl.Popup({ offset: 25 }).setText('Tienda Patitas');

// Asocia la etiqueta al marcador
marker_cliente.setPopup(popup_cliente);