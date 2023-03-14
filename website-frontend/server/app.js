//declaring everything that is needed for the server
const express = require('express');
const fileUpload = require('express-fileupload');
const app = express();
const bodyParser = require('body-parser');
const fs = require('fs');
const { response } = require('express');

app.use(express.static('client'));
app.unsubscribe(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.disable('etag');

app.use(bodyParser.urlencoded({ extended: false }));
app.use(fileUpload());

//declaring the paths for the files
const programFolderPath_win = 'files/program/SewAnalyst-win.zip'
const programFolderPath_mac = 'files/program/SewAnalyst-mac.zip'
const reportFolderPath = "data/flaggedReports.json"
const loadReports = JSON.parse(fs.readFileSync(reportFolderPath));

//function that saves the data to the json file
const saveData = (file) => {
    const finished = (error) => {
        if (error) {
            console.log(error);
        }
    };
    const jsonData = JSON.stringify(loadReports, null, 2);
    fs.writeFile(file, jsonData, finished);
}

//get request for downloading a report
app.get('/reportDownload/:reportName', (req,res) => {
    try{
        FolderPath = `files/reports/${req.params.reportName}`
        
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

//get request for downloading the program for windows
app.get('/program_download-win', function(req, res){
    console.log('downloading program');
    res.setHeader('Last-Modified', (new Date()).toUTCString());
    res.download(programFolderPath_win,function(err) {
        if(err) {
            console.log(err);
            console.log('Error downloading file');
        }
    })
})

//get request for donwloading the program for mac
app.get('/program_download-mac', function(req, res){
    res.setHeader('Last-Modified', (new Date()).toUTCString());
    res.download(programFolderPath_mac,function(err) {
        if(err) {
            console.log(err);
            console.log('Error downloading file');
        }
    })
})

//post request for flagging a report
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

//get request for getting the list of reports
app.get('/reportList', (req, res) => {
    const reportList = [];
    try {
        for (const report of loadReports){
            reportList.push({Name: report.reportName, TimesReported: report.reportCounter})
        }
        res.send(reportList)
    }
    catch(e){
        res.send(e)
    }
});

//get request for getting the reasons for a report being flagged
app.get('/reportReasons/:reportName', (req, res) => {
    const reportNum = req.params.reportName;
    try{
        for (const report of loadReports){
            if (report.reportName == reportNum){
                reportReasons = report.reviews
            }
        }
        res.send(reportReasons)
    }
    catch(e){
        res.send(e)
    }
});

//post request for uploading a report from clients computer to server
app.post('/upload', function(req, res) {
    let sampleFile;
    let uploadPath;
  
    if (!req.files || Object.keys(req.files).length === 0) {
      return res.status(400).send('No files were uploaded.');
    }
  
    sampleFile = req.files.sampleFile;
    uploadPath = 'files/reports/' + sampleFile.name;

    updateJsonfile(sampleFile.name)

    sampleFile.mv(uploadPath, function(err) {
      if (err)
        return res.status(500).send(err);

      
      res.status(200).redirect('http://127.0.0.1:8090');
    });
  });

//function that updates the json file with the new report
function updateJsonfile(reportName){
    let reportDate = new Date().toLocaleString()
    reportDate = reportDate.split(",")[0]
    const data = {
        reportName: reportName,
        dateOfReport: reportDate,
        reviews: [],
        reportCounter: "0"
    };
    loadReports.push(data);
    saveData(reportFolderPath);
};

module.exports=app;