

// REST-API
var MongoClient = require('mongodb').MongoClient;
var express = require('express');
var bodyParser = require("body-parser");
var server = express();

require('dotenv').config()
server.use(bodyParser.json());
server.use(bodyParser.urlencoded({ extended: false }));
server.use((req, res, next) => {
   res.header('Access-Control-Allow-Origin', '*');
   res.header('Access-Control-Allow-Headers', '*');
   if (req.method === 'OPTIONS') {
      res.header('Access-Control-Allow-Methods', 'POST, GET');
      return res.status(200).json({});
   }
   next();
})

server.use(bodyParser.json());
server.use(express.urlencoded({ extended: false }));

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
var connectionString = "mongodb://localhost:27016/";


// Client requesting all users
server.get('/list', async (req, res) => {
   const client = await mongoClient.connect(connectionString);
   const db = client.db('pren');
   const collection = db.collection('run');
   var query = { id: "1" };
   const result = await collection.find({ query }).toArray();
   res.json(result)
});

server.post('/updateRun', async (req, res) => {
   const client = await mongoClient.connect(connectionString);
   const db = client.db('pren');
   const collection = db.collection('run');
   const queryFilter = { id: "1" }
   const run = req.body
   const result = await collection.updateOne(queryFilter, { $set: run });
   if (run.isFinisched == true) {
      const collection = db.collection('runArchive');
      await collection.insertOne(run);
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