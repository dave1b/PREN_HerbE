// REST-API
var mongoClient = require('mongodb').MongoClient;
var express = require('express');
var server = express();
var bodyParser = require("body-parser");
server.use(bodyParser.json());
server.use(bodyParser.urlencoded({ extended: false }));






require('dotenv').config()
const API_KEY = process.env.SECRET_KEY;
const CONNECTION_STRING = "mongodb://localhost:27016/";

//Handle CORS-Restriction
server.use((req, res, next) => {
   res.header('Access-Control-Allow-Origin', '*');
   res.header('Access-Control-Allow-Headers', '*');
   if (req.method === 'OPTIONS') {
      res.header('Access-Control-Allow-Methods', 'POST, GET');
      return res.status(200).json({});
   }
   next();
})


// Client requesting all users
server.get('/list', async (req, res) => {
   const client = await mongoClient.connect(CONNECTION_STRING);
   const db = client.db('pren');
   const collection = db.collection('run');
   const queryFilter = {id: "1"};
   const result = await collection.find(queryFilter).toArray();
   res.json(result)
});


// Update run
server.post('/updateRun', async (req, res) => {
   const run = req.body;

   // Check validity of Key
   if (run.apiKey != API_KEY) {
      res.status(401);
      res.end();
      console.log("not authorized")
      return;
   }
   // Write to DB
   const client = await mongoClient.connect(CONNECTION_STRING);
   const db = client.db('pren');
   const collection = db.collection('run');
   const queryFilter = { id: "1"  }
   const result = await collection.updateOne(queryFilter, { $set: run });
   // Copy to Archive if end
   if (run.isFinisched == true) {
      const collection2 = db.collection('runArchive');
      await collection2.insertOne(run);
   }
   if (result) {
       res.send(result);
   } else {
       res.status(404);
   }
   res.end();
   return
});

var port = 8080
var listener = server.listen(port);
console.log("Server running at port " + listener.address().port)


/*http.listen(process.env.PORT || port, function () {
   var host = http.address().address
   var port = http.address().port
   console.log('App listening at http://%s:%s', host, port)
});*/