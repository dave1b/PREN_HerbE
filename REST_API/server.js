// SocketConnection
var http = require('http').createServer(app);
var io = require('socket.io')(http);

io.on("connection", socket => {
   //either with send()
   socket.send("Hello!");

   // or with emit() and custom event names
   socket.emit("greetings", "Hey!", { "ms": "jane" }, Buffer.from([4, 3, 3, 1]));

   // handle the event sent with socket.send()
   socket.on("message", (data) => {
      console.log(data);
   });

   // handle the event sent with socket.emit()
   socket.on("salutations", (elem1, elem2, elem3) => {
      console.log(elem1, elem2, elem3);
   });
});

// REST-API
var MongoClient = require('mongodb').MongoClient;
var express = require('express');
var server = express();
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
var port = 8080


// Client requesting all users
server.get('/list', (req, res) => {
   const client = await mongoClient.connect(connectionString);
   const db = client.db('pren');
   const collection = db.collection('run');
   var query = { id: "1" };
   const result = await collection.find({ query }).toArray();
   res.json(result)
});

server.post('/updateRun', (req, res) => {
   const client = await mongoClient.connect(connectionString);
   const db = client.db('pren');
   const collection = db.collection('run');
   const queryFilter = { id: "1" }
   const result = await collection.updateOne(queryFilter, { $set: run });
   if (result) {
      res.send(result);
   } else {
      res.status(404);
   }
   res.end();
   return
});

var listener = server.listen(port);
console.log("Server running at port " + listener.address().port)

/*http.listen(process.env.PORT || port, function () {
   var host = http.address().address
   var port = http.address().port
   console.log('App listening at http://%s:%s', host, port)
});*/