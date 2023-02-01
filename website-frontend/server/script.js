const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const fs = require('fs');
const { response } = require('express');

app.use(express.static('client'));
app.unsubscribe(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

const reportFolderPath = 'files/reports/report1.pdf'
const programFolderPath = 'files/program/program1.json'
const flagReportFolderPath = 'files/data/flaggedReports.json'

app.get('/report/report1.pdf',function(req,res) {
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

app.post('/flagReport', (req, res)=>{
    try{
        info = req.body
        print(info)
        let reportNum = info.reportNum
        let reportDate = info.reportDate
        let reportReason = info.reportReason

        print(reportNum)
        print(reportDate)
        print(reportReason)

        if (!fs.existsSync(flagReportFolderPath)){
            fs.closeSync(fs.openSync(flagReportFolderPath, 'w'));
        }

        const file = fs.readFileSync(flagReportFolderPath)
        const data = {
            "reportNum": reportNum,
            "reportDate": reportDate,
            "reportReason": reportReason
        }

        if (file.length == 0){
            fs.writeFileSync(flagReportFolderPath, JSON.stringify([data]))
        }
        else{
            const json = JSON.parse(file.toString())
            json.push(data)
            fs.writeFileSync(flagReportFolderPath, JSON.stringify(json, null, 2))
            response.send("success")
        }

    }
    catch(e){
        response.send(e)
    }
});

app.listen(8090)
console.log('Server started at http://127.0.0.1:8090');