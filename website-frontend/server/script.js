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

const programFolderPath_win = 'files/program/SewAnalyst-win.zip'
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
        FolderPath = `files/reports/${req.params.reportName}`
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
    res.download(programFolderPath_win,function(err) {
        if(err) {
            console.log(err);
            console.log('Error downloading file');
        }
    })
})



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

app.post('/upload', function(req, res) {
    let sampleFile;
    let uploadPath;
  
    if (!req.files || Object.keys(req.files).length === 0) {
      return res.status(400).send('No files were uploaded.');
    }
  
    // The name of the input field (i.e. "sampleFile") is used to retrieve the uploaded file
    sampleFile = req.files.sampleFile;
    uploadPath = 'files/reports/' + sampleFile.name;

    updateJsonfile(sampleFile.name)
  
    // Use the mv() method to place the file somewhere on your server
    sampleFile.mv(uploadPath, function(err) {
      if (err)
        return res.status(500).send(err);

      
      res.status(200).redirect('http://127.0.0.1:8090');
    });
  });

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
}



app.listen(8090)
console.log('Server started at http://127.0.0.1:8090');