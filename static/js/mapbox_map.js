// Mapbox access token
var token = 'pk.eyJ1IjoibGVlbHVtMSIsImEiOiJjamFzNHM0cmo0bmduMnFwbHh0MXNweW5jIn0.1fUr70BuY4Kk4BERLB5Pkg';
mapboxgl.accessToken = token;

//Zoom out
function zoomOut(){
  map.flyTo({center: [-61.5, 10.5], zoom: 8});
};

//Map Preview
function setMapPreview() {
  var bounds = map.getBounds().toArray();
  bounds = [bounds[0][0], bounds[0][1], bounds[1][0], bounds[1][1]];

  // The size of the desired map.
  var size = [80, 80];

  // Calculate a zoom level and centerpoint for this map.
  var vp = geoViewport.viewport(bounds, size, 0, 24, 512); //viewport(bounds, dimensions, minzoom, maxzoom, tileSize)

  // Construct a static map url
  // https://www.mapbox.com/developers/api/static/
  document.getElementById('basemenu').src =
    'https://api.mapbox.com/styles/v1/mapbox/' + styles[1] + '/static/' +
    vp.center.join(',') + ',' + vp.zoom + ',' +
    map.getBearing() + ',' + map.getPitch() + '/' +
    size.join('x') + '?' +
    'attribution=false&logo=false&access_token=' + token
}

var styles = ['basic-v9', 'satellite-v9']

//Initialize map object
var map = new mapboxgl.Map({
  container: 'map',
  style: 'mapbox://styles/mapbox/' + styles[0],
  center: [-61.5, 10.5],
  zoom: 8
});

//Scale
var scale = new mapboxgl.ScaleControl({
    maxWidth: 100,
    unit: 'metric'
});
map.addControl(scale);


//Navigation
var nav = new mapboxgl.NavigationControl();
map.addControl(nav, 'top-left');


//Geolocation control
map.addControl(new mapboxgl.GeolocateControl({
    positionOptions: {
        enableHighAccuracy: true
    },
    trackUserLocation: true
}), 'top-left');

var previewUpdate

map.on('render', function() {
  clearTimeout(previewUpdate)
  previewUpdate = setTimeout(setMapPreview, 100)
});

function switchBase() {
  styles.push( styles.shift() )
  map.setStyle('mapbox://styles/mapbox/' + styles[0])
  var buts = document.getElementsByClassName("main-layer")
  for (var i = 0; i < buts.length; i++) {
    buts[i].classList.remove("active");
  }
};

// //Mouse coordinates
// map.on('mousemove', function (e) {
//     document.getElementById('coords').innerHTML = JSON.stringify(e.lngLat);
// });

// //Remove mouse coordinates on leave
// $( "#map" ).mouseleave(function() {
//   $( "#coords" ).html("");
// });
