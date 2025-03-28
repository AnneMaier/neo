var express = require('express');
var mysql = require('mysql');
const env = require('dotenv').config({ path: "../../.env" });   
var app = express();

var connection = mysql.createConnection({
    host: process.env.NODE_MYSQL_HOST || "localhost",
    user: process.env.NODE_MYSQL_USER || "root",
    password: process.env.NODE_MYSQL_PASSWORD || "1234",
    database: process.env.NODE_MYSQL_DATABASE || "test"
});

connection.connect(function (err) {
    if (err){
        console.error("DB is connected!\n\n");

    }else{
        console.log("DB is not connected! Error: " + err + "\n\n");
    }
});

app.get('/', function (req, res) {
    connection.query('SELECT * FROM testdb', function (err, rows, fields) {
        connection.end();
        if (err) {
            res.send(rows);
            console.log("the solution is: ", rows);
        }else {
            console.log('error while performing Query.\n\n');
        }
    })
})

app.listen(8000, function () {
    console.log("Express server listening on port 8000 \n\n");
})