

const downloadSoftware = document.getElementById("downloadSoftware")
downloadSoftware.addEventListener("click", async function(event){
    try{
      const response = await fetch('/program_download');
    } catch(e) {
      alert(e);
    }
  });



function openForm() {
    document.getElementById("flagReportFormBox").style.display="block";
}

function closeForm() {
    document.getElementById("flagReportFormBox").style.display="none";
}

function openList() {
    document.getElementById("listOfForms").style.display="block";
}
function closeList() {
    document.getElementById("listOfForms").style.display="none";
}


document.addEventListener('DOMContentLoaded', async function(event){
    try{
        console.log("clicked")
        //event.preventDefault();
        const response = await fetch('/reportList')
        if (response.status === 204){
            alert('No reports to display')
        }
        else{
            const data = await response.json()
            buildTable(data);
        }
    }
    catch(err){
        alert(err)
    }
});

function buildTable (data){
    const table = document.getElementById('reportTable');
    table.innerHTML = '';

    data.forEach(function(object) {
        const tr = document.createElement('tr');
        tr.innerHTML = '<td><form id = "getReport' + object.Name + '" action="/reportDownload" method = "GET"><button type="submit">' + 'Report ' + object.Name + '</button></form>' + '</td>' +
          '<td>' + colourTriangle(object.TimesReported) + object.TimesReported + '</td>' +
          '<td>' + '<button onclick="openList()"><img src="http://clipart-library.com/data_images/81597.png" style="width:50px; height:50px"></button>' + '</td>' +
          '<td>' + '<button type="button" class="btn" id="reportbutton" onclick="openForm()">  REPORT</button>' + '</td>';
        table.appendChild(tr);
    });
}

function colourTriangle(TimesReported){
    if (+TimesReported == 0){
        return '<img id="alerts" src="Green alert.jpg">';
    }
    else if (+TimesReported <= 5){
        return '<img id="alerts" src="Yellow alert.jpg" >';
    }
    else{
        return '<img id="alerts" src="Red alert.jpg" >';
    }
}

downloadReport.addEventListener("submit", async(event)=>{
    try{
        //event.preventDefault()
        console.log("working")
        /*const reportNumber = downloadReport.elements.namedItem('InputReportNumber').value;
        console.log("Download button clicked")
        console.log({reportNum: reportNumber})
        const response = await fetch('/reportDownload?' + new URLSearchParams({reportNum: reportNumber}))*/
        
        const response = await fetch('/reportDownload')
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

const flagReport = document.getElementById('formContainer')
flagReport.addEventListener('submit', async function(event){
    try{
        event.preventDefault()
        let reportReason = flagReport.elements.namedItem('InputReason').value
        const reportData = {reportReason: reportReason}
        console.log(reportData)
        const response = await fetch('/flagReport',{
            method: 'POST',
            headers:{'Content-Type':'application/json'},
            body: JSON.stringify(reportData),
        })
        if (response.status === 204){
            window.alert("Error, could not flag report")
        }
        else{
            const data = await response.text()

            reportReason = flagReport.elements.namedItem('InputReason').value = ''

            window.alert(data);
        }
    }
    catch(e){
        alert(e)
    }
});