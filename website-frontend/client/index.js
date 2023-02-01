

// function downloadFunction(){
//     alert("Are you really sure?");
// }

const downloadReport = document.getElementById("getReport")
downloadReport.addEventListener("click",async(event) => {
    try{
        console.log("Download button clicked")
        const response = await fetch('/report/report1.pdf')
    }
    catch(err){
        console.log(err)
    }
});

const downloadSoftware = document.getElementById("downloadSoftware")
downloadSoftware.addEventListener("click", async function(event){
    try{
      const response = await fetch('/program_download');
    } catch(e) {
      alert(e);
    }
  });

const flagReport = document.getElementById('flagReportForm')
flagReport.addEventListener('submit', async function(event){
    try{
        console.log("Here")
        reportNum = flagReport.elements.namedItem('InputReportNumber').value
        console.log(reportNum)
        reportDate = flagReport.elements.namedItem('InputDateOfSubmission').value
        console.log(reportDate)
        reportReason = flagReport.elements.namedItem('InputReason').value
        console.log(reportReason)
        const reportData = {reportNum: reportNum, reportDate: reportDate, reportReason: reportReason}
        const response = await fetch('http://127.0.0.1:8090/flagReport',{
            method: 'POST',
            headers:{'Content-Type':'application/json'},
            body: JSON.stringify(reportData),
        })
        if (response.status === 204){
            console.log(response)
            window.alert("Error, could not flag report")
        }
        else{
            const data = await response.text()

            flagReport.elements.namedItem('InputReportNumber').value = ''
            reportDate = flagReport.elements.namedItem('InputDateOfSubmission').value = ''
            reportReason = flagReport.elements.namedItem('InputReason').value = ''

            window.alert(data);
        }
    }
    catch(e){
        alert(e)
    }
});


