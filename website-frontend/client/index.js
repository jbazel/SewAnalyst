const { response } = require("express");
var bodyParser = require('body-parser');  
var urlencodedParser = bodyParser.urlencoded({ extended: false })  

function downloadFunction(){
    alert("Are you really sure?");
}

const downloadReport = document.getElementById("getReport")
downloadReport.addEventListener("click", async(event) => {
    try{
        console.log("Download button clicked")
        const response = await fetch('http://127.0.0.1:8090/report/report1.pdf')
    }
    catch(err){
        console.log(err)
    }
});

const downloadSoftware = document.getElementById("getSoftware")
downloadSoftware.addEventListener("click", async(event) => {
    try{
        console.log("Download button clicked")
        const response = await fetch('http://127.0.0.1:8090/single')
    }
    catch(err){
        console.log(err)
    }
    });





