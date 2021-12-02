// Require client library and private key.
var ee = require('@google/earthengine');
var privateKey = require('./privatekey.json');
var selected1 = null;

// Initialize client library and run analysis.
var runAnalysis = function() {
  ee.initialize(null, null, function() {
    // ... run analysis ...
    // console.log(ee);
    var country = 'Bolivia'; // selected country (e.g. Bolivia)
    var cc = ee.Number(10); // canopy cover percentage (e.g. 10%)
    // minimum forest size in pixels (e.g. 6 pixels, approximately 0.5 ha in this example)
    var pixels = ee.Number(15);
    // minimum mapping area for tree loss (usually same as the minimum forest area)
    var lossPixels = ee.Number(6);
    // Load country features from Large Scale International Boundary (LSIB) dataset.
    var countries = ee.FeatureCollection('USDOS/LSIB_SIMPLE/2017');
    // console.log(countries);
 
    var selected = countries.filter(ee.Filter.eq('country_na', ee.String(
      country)));
    selected1 = selected;
    console.log(selected.features);
   
        // Center the map to the selected country.
    // Map.centerObject(selected, 14);
   
  }, function(e) {
    console.error('Initialization error: ' + e);
  });
};

// Authenticate using a service account.
ee.data.authenticateViaPrivateKey(privateKey, runAnalysis, function(e) {
  console.error('Authentication error: ' + e);
});

const http = require('http');
const { rejects } = require('assert');

const hostname = '127.0.0.1';
const port = 3001;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  // res.end();
  // console.log(typeof(ee));
  // res.end(JSON.stringify(ee));
  res.end(JSON.stringify(selected1));
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});