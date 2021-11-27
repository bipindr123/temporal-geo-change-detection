    // Require client library and private key.
    var ee = require('@google/earthengine');
    var privateKey = require('./privatekey.json');
  
    // Initialize client library and run analysis.
    var runAnalysis = function() {
      ee.initialize(null, null, function() {
        // ... run analysis ...
        // console.log(ee);
      }, function(e) {
        console.error('Initialization error: ' + e);
      });
    };
  
    // Authenticate using a service account.
    ee.data.authenticateViaPrivateKey(privateKey, runAnalysis, function(e) {
      console.error('Authentication error: ' + e);
    });

const http = require('http');

const hostname = '127.0.0.1';
const port = 3001;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  // res.end();
  console.log(typeof(ee));
  res.end(JSON.stringify(ee));
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});