const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const fs = require('fs');

app.use(express.static('client'));
app.unsubscribe(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

const reportFolderPath = 'files/reports/report1.pdf'
const programFolderPath = 'files/program/program1.json'
app.get('/report/report1.pdf',function(req,res) {
    console.log('single file');
     
    // Download function provided by express
    res.download(reportFolderPath, function(err) {
        if(err) {
            console.log(err);
        }
        else{
            app.download(reportFolderPath)
            console.log('File sent');
        }
    })
})

app.get('/program_download', function(req, res){
    console.log('downloading program');
    res.download(programFolderPath, function(err) {
        if(err) {
            console.log(err);
            console.log('Error downloading file');
        }
        else{
            app.download(programFolderPath)
            console.log('File sent');
        }
    })
})

app.post('/report_upload', function(req, res){
    console.log(req.body);
    fs.writeFile(reportFolderPath, req.body, function(err){
        if(err) {
            console.log(err);
        }
        else{
            console.log('File uploaded');
        }
    })
});

app.listen(8090)
console.log('Server started at http://127.0.0.1:8090');