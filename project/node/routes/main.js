const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('sync-mysql');
const env = require('dotenv').config({ path: "../../.env" });
const axios = require('axios');
const FastAPI = "http://192.168.1.28:3000"

const app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
const path = require('path');
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, '../public')); 
app.use('/graphs', express.static(path.join(__dirname, '../../api/graphs')));

var connection = new mysql({
    host: process.env.host,
    user: process.env.user,
    port: process.env.port,
    password: process.env.password,
    database: process.env.database
});

app.get('/Hello', (req, res) => {
    res.send('Hello World!!')
    
})


app.get('/viewAnalysis', async (req, res) => {
    const { eventDate } = req.query;
    try {
        const response = await axios(`${FastAPI}/LoanRankByDate?eventDate=${eventDate}`);
        const data = response.data;
        
        res.render('result', { data });
    } catch (error) {
        console.error(error);
        res.status(500).send('Error fetching data');
    }
    
})


// insert data to st_info table
app.get('/insert', (req, res) => {
    const { st_id, name, dept } = req.query;
    const result = connection.query("insert into st_info values (?, ?, ?)",
        [st_id, name, dept]);
        res.redirect('/select');
})


// select all rows from st_info table
app.get('/select', (req, res) => {
    let result = connection.query('select * from st_info');
    console.log(result);
    // res.send(result);
    res.writeHead(200);
    var template = `
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Result</title>
    </head>
    <body>
    <table border="1" margin:auto; text-align:center;>
        <tr>
            <th>ST_ID</th>
            <th>NAME</th>
            <th>DEPT</th>
        </tr>   
        `;
        for (var i=0; i<result.length; i++) {
        template += `
        <tr>
            <th>${result[i]['ST_ID']}</th>
            <th>${result[i]['NAME']}</th>
            <th>${result[i]['DEPT']}</th>
        </tr>
        `;
    }
    template += `
    </table>
    </body>
    </html>
    `;
    res.end(template);
})

// insert data to st_info table

module.exports = app;