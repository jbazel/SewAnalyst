

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
flagReport.addEventListener('submit', async(event)=>{
    try{
        event.preventDefault()
        let reportNum = flagReport.elements.namedItem('InputReportNumber').value
        let reportDate = flagReport.elements.namedItem('InputDateOfSubmission').value
        let reportReason = flagReport.elements.namedItem('InputReason').value
        const reportData = {reportNum: reportNum, reportDate: reportDate, reportReason: reportReason}
        console.log(reportData)
        const response = await fetch('/flagReport',{
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


