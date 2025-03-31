const express = require('express');
const bodyParser = require('body-parser');
const pool = require('../../conf/pool')
const XMLHttpRequest = require("xhr2");
const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));


app.get('/Hello', (req, res) => {
    res.send('Hello World!!')
})


app.get("/getData", (req, res) => {
    const xhr = new XMLHttpRequest();
    xhr.open("GET", "http://localhost:5000/users");
    xhr.setRequestHeader("Content-Type", "application/json");
    const data = { id: req.body.id, name: req.body.name };

    xhr.send(JSON.stringify(data));

    xhr.onload = () => {
        if (xhr.status === 200) {
            console.log(res);
        } else {
            console.log(xhr.status, xhr.statusText);
        }
        res.send(xhr.response);
    };
})

app.post("/postData" , (req, res) => {
    const xhr = new XMLHttpRequest();
    console.log(req.body);
    xhr.open("POST", "http://localhost:5000/users");
    xhr.setRequestHeader("Content-Type", "application/json; charset=UTF-8");
    const data = { id: req.body.id, name: req.body.name };    
    xhr.send(JSON.stringify(data));    
    xhr.onload = () => {
        if (xhr.status === 200) {
            const res = JSON.parse(xhr.response);
            console.log(res);
        } else {
            console.log(xhr.status, xhr.statusText);
        }
        res.send(xhr.response);
    };    
})


app.post("/putData" , (req, res) => {
    const xhr = new XMLHttpRequest();
    console.log(req.body);
    xhr.open("PUT", "http://localhost:5000/users/" + req.body.id);
    xhr.setRequestHeader("Content-Type", "application/json; charset=UTF-8");
    const data = { id: req.body.id, name: req.body.name };    
    xhr.send(JSON.stringify(data));    
    xhr.onload = () => {
        if (xhr.status === 200) {
            const res = JSON.parse(xhr.response);
            console.log(res);
        } else {
            console.log(xhr.status, xhr.statusText);
        }
        res.send(xhr.response);
    };    
})

app.post("/deleteData" , (req, res) => {
    const xhr = new XMLHttpRequest();
    console.log(req.body);
    xhr.open("DELETE", "http://localhost:5000/users/" + req.body.id);
    xhr.setRequestHeader("Content-Type", "application/json; charset=UTF-8");  
    xhr.send();    
    xhr.onload = () => {
        if (xhr.status === 200) {
            const res = JSON.parse(xhr.response);
            console.log(res);
        } else {
            console.log(xhr.status, xhr.statusText);
        }
        res.send(xhr.response);
    };    
})

module.exports = app;