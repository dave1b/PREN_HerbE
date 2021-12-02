
var url = "mongodb://localhost:27016/";
var port = 8080

var express = require('express');
var app = express();

var http = require('http').createServer(app);
var io = require('socket.io')(http);


var MongoClient = require('mongodb').MongoClient;
app.use(express.urlencoded({ extended: false }));



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


// Client requesting all users
app.get('/list', (req, res) => {
   
   MongoClient.connect(url, function (err, db) {
      if (err) throw err;
      var dbo = db.db("pren");
      var query = { id: "1" };
      dbo.collection("run").find(query).toArray(function (err, result) {
         if (err) throw err;
         res.end(JSON.stringify(result[0]))
         db.close();
      });
   });
   /*
   console.log("get: list")
   var json = getLatestRunFromDB()
   console.log(json)
   res.end(json)*/
});

app.post('/updateRun', (req, res) => {
   console.log("post: udpateRun")
   updateRunInDB(req.body)
   res.send('Message received')
   console.log(req.body)
});




function updateRunInDB(run) {
   MongoClient.connect(url, function (err, db) {
      if (err) throw err;
      var dbo = db.db("pren");
      var query = { id: "1" };
      dbo.collection("run").updateOne(query, { $set: run }, function (err, res) {
         if (err) throw err;
         console.log("1 document inserted");
         db.close();
      });
   });
   return
};

function getLatestRunFromDB() {
   var json = ""
   MongoClient.connect(url, function (err, db) {
      if (err) throw err;
      var dbo = db.db("pren");
      var query = { id: "1" };
      dbo.collection("run").find(query).toArray(function (err, result) {
         if (err) throw err;
         json = result[0]
         console.log(json)
         db.close();
      });
   });
   //console.log(json)
   return (json)
}




http.listen(process.env.PORT || port, function() {
   var host = http.address().address
   var port = http.address().port
   console.log('App listening at http://%s:%s', host, port)
 });