const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('sync-mysql');
const env = require('dotenv').config({ path: "../../.env" });

const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

var connection = new mysql({
    host: process.env.host,
    user: process.env.user,
    port: process.env.port,
    password: process.env.password,
    database: process.env.database
});

app.get('/Hello', (req, res) => {
    res.send('Hello World!!');
});




// select all rows from st_info table
app.get('/select', (req, res) => {
    let result = connection.query('select * from user');
    res.send(result);
    console.log(result);
});



app.get('/selectQuery', (req, res) => {
    let result = connection.query('select * from user where userid=?', [id]);
    res.send(result);
    console.log(result);
});



app.post('/insert', (req, res) => {
    const { id, pw} = req.body;
    console.log(id)
    const result = connection.query("insert into user values (?, ?)",
        [id, pw]);
        res.redirect('/selectQuery?id='+req.body.id);
})


module.exports = app;

