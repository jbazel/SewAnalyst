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
//const FolderPath = 'files/reports/report1.pdf'

const saveData = (file) => {
    const finished = (error) => {
        if (error) {
            console.log(error);
        }
    };
    const jsonData = JSON.stringify(loadReports, null, 2);
    fs.writeFile(file, jsonData, finished);
}

app.get('/reportDownload/:reportName', (req,res) => {
    try{
        /*const reportNum = req.query.reportNum;
        console.log(reportNum)
        const reportFolderPath = `files/reports/report${reportNum}.pdf`;
        console.log(reportFolderPath)*/
        console.log(req.params.reportName)
        FolderPath = `files/reports/${req.params.reportName}.pdf`
        console.log(FolderPath)
        
        res.setHeader('Last-Modified', (new Date()).toUTCString());
        res.download(FolderPath, (err) =>{
            if(err) {
                console.log(err);
                console.log('Error downloading file');
                res.status(500).send('Error downloading file');
            }
        });
    }
    catch(e){
        console.log(e)
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

app.post('/flagReport/:reportName', (req, res) => {
    try{
        info = req.body
        const reportName = req.params.reportName;
        const reportReason = info.reason;
    
        let reportDate = new Date().toLocaleString()
        reportDate = reportDate.split(",")[0]
        const data = {
            reportDate: reportDate,
            reportReason: reportReason
        };

        console.log(data)

        for (let i=0; i<loadReports.length; i++){
            const obj = loadReports[i];
            if (obj.reportName == reportName){
                obj.reviews.push(data)
                x = parseInt(obj.reportCounter )
                x += 1
                obj.reportCounter = x.toString()
                saveData(reportFolderPath)
                res.redirect("http://127.0.0.1:8090")
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
            reportList.push({Name: report.reportName, TimesReported: report.reportCounter})
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

app.get('/reportReasons/:reportName', (req, res) => {
    console.log("yay")
    //const reportReasons = [];
    const reportNum = req.params.reportName;
    console.log(reportNum)
    try{
        for (const report of loadReports){
            if (report.reportName == reportNum){
                reportReasons = report.reviews
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