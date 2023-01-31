const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const fs = require('fs');

app.use(express.static('client'));
app.unsubscribe(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

const folderPath = 'files/report1.pdf'

app.get('/single',function(req,res) {
    console.log('single file');
     
    // Download function provided by express
    res.download(folderPath, function(err) {
        if(err) {
            console.log(err);
        }
        else{
            console.log('File sent');
        }
    })
})



app.listen(8090)
console.log('Server started at http://127.0.0.1:8090');