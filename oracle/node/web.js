var oracledb = require('oracledb');
var dbConfig = require('./dbConfig');
var express = require('express');
var path = require('path');
var bodyParser = require('body-parser');

oracledb.initOracleClient({ libDir: '/opt/oracle/instantclient_21_13' });

var app = express();
app.set('port', process.env.PORT || 3000); // 'Port'를 'port'로 수정
app.use(bodyParser.urlencoded({ extended: true })); // app.set() 대신 app.use() 사용

app.get('/dbTestSelect', function(req, res) { // seq를 res로 수정
    oracledb.getConnection(
        {
            user: dbConfig.user,
            password: dbConfig.password,
            connectString: dbConfig.connectString
        }, function(err, connection) {
            if (err) {
                console.error(err.message);
                return;
            }
            connection.execute(
                'SELECT * FROM usertbl', // 'select'를 'SELECT'로 수정
                function(err, result) {
                    if (err) {
                        console.error(err.message);
                        doRelease(connection, null, res); // res 전달
                        return;
                    }

                    console.log(result.rows);
                    doRelease(connection, result.rows, res); // res 전달
                }
            );

            function doRelease(connection, rowList, res) { // res 인자 추가
                connection.release(
                    function(err) {
                        if (err) {
                            console.error(err.message);
                        }
                        if (rowList) {
                            console.log('List size: ' + rowList.length);
                            res.send(rowList); // 응답 전송
                        }
                    }
                );
            }
        }
    );
});

app.all('*', function(req, res) {
    res.status(404).send('<h1>404 Not found</h1>'); // 400을 404로 수정
});

app.listen(app.get('port'), function() {
    console.log('3000 Port: server started~!');
});