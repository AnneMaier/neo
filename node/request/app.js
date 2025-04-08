const express = require('express');
const CircularJSON = require('circular-json');
const request  = require('request');
const app = express(); 

app.get('/', (req, res) => {
    res.send("Web server started~!!");

})

app.get('/hello', (req, res) => {
    res.send({data : 'Hello World!'});
}) 

let option1 = 'http:/192.168.1.28:80000/hello';

app.get('rhello', function(req, res){
    request(option1, {json: true}, function(err, result, body){
        if (err){
            console.log(err);
        }
        console.log(body);
        res.send(CircularJSON.stringify(body));
    })
})

const data = JSON.stringify({ todo : 'Buy the milk - hwi'});


app.get('/data', function(req, res){
    res.send(data);
})

let option2 = 'http:/192.168.1.28:8000/data';

app.get('/rhello', function(req, res){
    request(option2, {json: true}, function(err, result, body){
        if (err){
            console.log(err);
        }
        console.log(body);
        res.send(CircularJSON.stringify(body));
    })
})


app.listen(8000, function(){
    console.log ("server is started~ Port : 8000");
})