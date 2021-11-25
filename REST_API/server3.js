var express = require('express');
var app = express();
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27016/";


// Client requesting all users
/*app.get('/listUsers', function (req, res) {
   //data = JSON.parse( data );
   console.log("hello");
   // fs.readFile( __dirname + "/" + "users.json", 'utf8', function (err, data) {
   //    console.log( data );
   //    res.end( data );
   //});
});*/
/*
// Client requesting a specific user
app.get('/:id', function (req, res) {
   
});
 // example request: http://127.0.0.1:8080/2 and

// Client adding new User
app.post('/addUser', function (req, res) {

   var myObjec = JSON.parse(req);
   console.log(myObjec)
   console.log("PostRequest")
   var run = [
      { name: 'John', address: 'Highway 71'},
      { name: 'Peter', address: 'Lowstreet 4'},
      { name: 'Amy', address: 'Apple st 652'},
      { name: 'Hannah', address: 'Mountain 21'},
      { name: 'Michael', address: 'Valley 345'},
      { name: 'Sandy', address: 'Ocean blvd 2'},
      { name: 'Betty', address: 'Green Grass 1'},
      { name: 'Richard', address: 'Sky st 331'},
      { name: 'Susan', address: 'One way 98'},
      { name: 'Vicky', address: 'Yellow Garden 2'},
      { name: 'Ben', address: 'Park Lane 38'},
      { name: 'William', address: 'Central st 954'},
      { name: 'Chuck', address: 'Main Road 989'},
      { name: 'Viola', address: 'Sideway 1633'}
    ];
    console.log(run)

   MongoClient.connect(url, function(err, db) {
      if (err) throw err;
      var dbo = db.db("prenn");
      dbo.collection("runs").insertMany(run, function(err, res) {
         if (err) throw err;
         
         db.close();
      });
      });
}); 
   

var server = app.listen(8080, function () {
   //var host = "prenh21-dbrunner.enterpriselab.ch"
   var host = server.address().address;
   var port = server.address().port;
   console.log("Example app listening at http://%s:%s", host, port)
});
*/