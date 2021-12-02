
var url = "mongodb://localhost:27016/";
var port = 8080

var express = require('express');
var app = express();
var MongoClient = require('mongodb').MongoClient;
app.use(express.urlencoded({ extended: false }));
var io = require("socket.io")(port);


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
   console.log("get: list")
   res.send(getLatestRunFromDB())
});

app.post('/updateRun', (req, res) => {
   console.log("post: udpateRun")
   updateRunInDB(req.body)
   res.send('Message received')
   console.log(req.body)
});

var server = app.listen(port, function () {
   //var host = "prenh21-dbrunner.enterpriselab.ch"
   var host = server.address().address;
   var port = server.address().port;
   console.log("Example app listening at http://%s:%s", host, port)
});


function updateRunInDB(run) {
   MongoClient.connect(url, function (err, db) {
      if (err) throw err;
      var dbo = db.db("pren");
      var query = { id: "1" };
      dbo.collection("run").updateOne(updateDocWhere, { $set: run }, function (err, res) {
         if (err) throw err;
         console.log("1 document inserted");
         db.close();
      });
   });
   return
};

function getLatestRunFromDB() {
   MongoClient.connect(url, function (err, db) {
      if (err) throw err;
      var dbo = db.db("pren");
      var query = { id: "1" };
      dbo.collection("run").find(query).toArray(function (err, result) {
         if (err) throw err;
         db.close();
         console.log(result);
         return (result)
      });
   });
}

