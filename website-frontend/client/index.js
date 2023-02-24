const downloadReport = document.getElementById('getReport');
downloadReport.addEventListener("submit", async(event)=>{
    try{
        event.preventDefault()
        const reportNumber = downloadReport.elements.namedItem('InputReportNumber').value;
        console.log("Download button clicked")
        console.log({reportNum: reportNumber})
        const response = await fetch('/reportDownload?' + new URLSearchParams({reportNum: reportNumber}))
        
        console.log(response)
        if (response.status === 204){
            alert('No report with that number')
        }
        else{
            //const data = await response.headers();
            //alert(data)
        }
    }
    catch(err){
        alert(err)
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


