const { response } = require("express");
var bodyParser = require('body-parser');  
var urlencodedParser = bodyParser.urlencoded({ extended: false })  

// function downloadFunction(){
//     alert("Are you really sure?");
// }

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

let downloadSoftware = document.getElementById("downloadSoftware")
downloadSoftware.addEventListener("click", async function(event){
    try{
      let response = await fetch('http://127.0.0.1:8090/program_download');
    } catch(e) {
      alert(e);
    }
  });


