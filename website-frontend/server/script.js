const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const fs = require('fs');
const { response } = require('express');

app.use(express.static('client'));
app.unsubscribe(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.disable('etag');

app.use(bodyParser.urlencoded({ extended: false }));

const programFolderPath = 'files/program/program1.json'
const reportFolderPath = "data/flaggedReports.json"
const loadReports = JSON.parse(fs.readFileSync(reportFolderPath));
const folderPath = 'files/reports/'

const saveData = (file) => {
    const finished = (error) => {
        if (error) {
            console.log(error);
        }
    };
    const jsonData = JSON.stringify(loadReports, null, 2);
    fs.writeFile(file, jsonData, finished);
}

app.get('/reportDownload', (req,res) => {
    try{
        console.log(req.query.id)
        res.setHeader('Last-Modified', (new Date()).toUTCString());
        let path = folderPath + req.query.id;
        res.download(path, (err) =>{
            if(err) {
                console.log(err);
                console.log('Error downloading file');
                res.status(500).send('Error downloading file');
            }
        });
    }
    catch(e){
        // console.log(e)
        res.status(500).send("error")
    }
})

app.get('/program_download', function(req, res){
    console.log('downloading program');
    res.setHeader('Last-Modified', (new Date()).toUTCString());
    res.download(programFolderPath,function(err) {
        if(err) {
            console.log(err);
            console.log('Error downloading file');
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

app.post('/flagReport', (req, res) => {
    try{
        info = req.body
        console.log("passed")
        console.log(info)
        let reportReason = info.reportReason
    
        const data = {
            reportDate: reportDate,
            reportReason: reportReason
        };
        console.log("here")

        console.log(data)

        for (let i=0; i<loadReports.length; i++){
            const obj = loadReports[i];
            if (obj.reportNum == reportNum){
                obj.reviews.push(data)
                x = parseInt(obj.reportCounter )
                x += 1
                obj.reportCounter = x.toString()
                saveData(reportFolderPath)
                res.send("success")
                return;
            }
        }
    }
    catch(e){
        res.send(e)
    }
});

app.get('/reportList', (req, res) => {
    const reportList = [];
    try {
        for (const report of loadReports){
            reportList.push({Name: report.reportNum, TimesReported: report.reportCounter})
        }
        console.log(reportList)
        res.send(reportList)
    }
    catch(e){
        res.send(e)
    }
    /*if (reportList.length != 0){
        res.send(200).json(reportList);
    }
    else{
        res.send(204).json({});
    }*/
});

app.get('/reportReasons', (req, res) => {
    const reportReasons = [];
    const reportNum = req.query.reportNum;
    try{
        for (const report of loadReports){
            if (report.reportNum == reportNum){
                reportReasons.push({Reasons: report.reviews})
            }
        }
        console.log(reportReasons)
        res.send(reportReasons)
    }
    catch(e){
        res.send(e)
    }
});



app.listen(8090)
console.log('Server started at http://127.0.0.1:8090');