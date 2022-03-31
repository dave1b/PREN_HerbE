// Initializing REST-API
var mongoClient = require('mongodb').MongoClient;
var express = require('express');
var server = express();
var bodyParser = require("body-parser");
server.use(bodyParser.json());
server.use(bodyParser.urlencoded({ extended: false }));

// Initializing Socket
var httpServer = require('http').Server(server);
const io = require("socket.io")(httpServer, {
   serveClient: false,
   cors: {    
      origin: "*",    
      methods: ["GET", "POST, PUT"]  
   }
});

// Reading .env variables
require('dotenv').config()
const API_KEY = process.env.SECRET_KEY;
const CONNECTION_STRING = "mongodb://localhost:27016/";

// Handling CORS-Restriction
server.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Headers', '*');
    if (req.method === 'OPTIONS') {
        res.header('Access-Control-Allow-Methods', 'POST, GET, PUT');
        return res.status(200).json({});
    }
    next();
})

// Client requesting all users
server.get('/api/v1/listRun', async (req, res) => {
   latestRun = await getLatestRun();
   res.json(latestRun);
});

// Update run
server.put('/api/v1/updateRun', async (req, res) => {
   const run = req.body;
   // Check validity of Key
   if (run.apiKey != API_KEY) {
      res.status(401);
      res.end();
      console.log("not authorized")
      return;
   }
   delete run["apiKey"];
   broadcastClients(run);
   // Write to DB
   const client = await mongoClient.connect(CONNECTION_STRING);
   const db = client.db('pren');
   const collection = db.collection('run');
   const queryFilter = { id: 1 }
   const result = await collection.updateOne(queryFilter, { $set: run });
   // Copy to Archive if end
   if (run.isFinished == true) {
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

// on initial socket connection
io.on('connection',async function(socket){
   var latestRun = await getLatestRun();
   broadcastClients(latestRun);
   // Whenever someone disconnects this piece of code executed
   socket.on('disconnect', function () {
   });
});

function broadcastClients(run) {
   io.emit('runUpdated', run);
}

async function getLatestRun() {
   const client = await mongoClient.connect(CONNECTION_STRING);
   const db = client.db('pren');
   const collection = db.collection('run');
   const queryFilter = { id: 1 };
   const result = await collection.find(queryFilter).toArray();
   return result[0];
}

var port = 8080
var listener = httpServer.listen(port);
console.log("Server running at port " + listener.address().port)