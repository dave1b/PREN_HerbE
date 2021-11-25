var express = require('express');
var app = express();

// Client requesting all users
app.get('/listUsers', function (req, res) {
   
   console.log("hello world")
   res.end()
})

var server = app.listen(8080, function () {
    var host = "prenh21-dbrunner.enterpriselab.ch"
    //var host = server.address().address
    var port = server.address().port
    console.log("Example app listening at http://%s:%s", host, port)
 })