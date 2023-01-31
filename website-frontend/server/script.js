const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const fs = require('fs');

app.use(express.static('client'));
app.unsubscribe(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

const reportFolderPath = 'files/report1.pdf'
const programFolderPath = 'files/program1.json'
app.get('/report:reportID',function(req,res) {
    console.log('single file');
     
    // Download function provided by express
    res.download(reportFolderPath, function(err) {
        if(err) {
            console.log(err);
        }
        else{
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
});


app.listen(8090)
console.log('Server started at http://127.0.0.1:8090');