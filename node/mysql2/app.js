const { connect } = require('http2');
var mysql = require('mysql2/promise');
const env = require('dotenv').config({ path: "../../.env" }); 

const db = async () => {
    try{
        let connection = await mysql.createConnection({
        
            host: process.env.host,
            user: process.env.user,
            port: process.env.port,
            password: process.env.password,
            database: process.env.databasehost
        })
        
        let [rows, fileds] = await connection.query('select * from st_info');
        console.log(rows);

        let data = {
            st_id: 202599,
            name: "Moon",
            dept: "Computer"
        };

        let insertId = data.st_id;

        // inset query
        [rows, fileds] = await connection.query("insert into st_info values ?", data);
        console.log("Data is inserted: " + insertId);
        [rows, fileds] = await connection.query("select * from st_info where ST_ID = ?", [insertId]);
        console.log(rows);

        // select * query for inserted data
        [rows, fileds] = await connection.query("select * from st_info where ST_ID = ?", [insertId]);
        console.log(rows);

        // update query
        [rows, fileds] = await connection.query("update st_info dept = ? where ST_ID = ?", ["Game", insertId]);
        console.log("Data is updated: " + insertId);
        [rows, fileds] = await connection.query("select * from st_info where ST_ID = ?", [insertId]);
        console.log(rows);

        // select * query for updated data
        [rows, fileds] = await connection.query("select * from st_info where ST_ID = ?", [insertId]);
        console.log(rows);

        // delete query
        [rows, fileds] = await connection.query("delete from st_info where ST_ID = ?", [insertId]);
        console.log("Data is deleted: " + insertId);
        [rows, fileds] = await connection.query("select * from st_info where ST_ID = ?", [insertId]);
        console.log(rows);

        // select * query for deleted data
        [rows, fileds] = await connection.query("select * from st_info where ST_ID = ?", [insertId]);
        console.log(rows);

    }catch(err){
        console.log(err);
    }
}

db();