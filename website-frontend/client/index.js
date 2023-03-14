//downloadSoftwareWin function
const downloadSoftwareWin = document.getElementById("downloadSoftware-win")
downloadSoftwareWin.addEventListener("click", async function(event){
    try{
        //fetch request to download the program
      const response = await fetch('/program_download-win');
    } catch(e) {
      alert(e);
    }
  });

//downloadSoftwareMac function
const downloadSoftwareMac = document.getElementById("downloadSoftware-mac")
downloadSoftwareMac.addEventListener("click", async function(event){
    try{
      const response = await fetch('/program_download-mac');
    } catch(e) {
      alert(e);
    }
  });

//route function
const route = (event) => {
    event = event || window.event;
    event.preventDefault();
    window.history.pushState({}, '', event.target.href);
    changeLocation();
};

//array of routes
const routes = [
    {
        path: '/reportReasons/:reportName',
        getView: (params) => reportReasonsPopup(params)
    },
    {
        path: '/viewReports',
        getView: (params) => viewReportsPage()
    }
];

//changeLocation function
const changeLocation = async () => {
    document.getElementById('uploadForm').style.display= 'none'; 
    const path = window.location.pathname;
    
    //splits URL by /'s
    const routePathSegments = path.split('/').slice(1);

    if (routePathSegments.length > 1) {
        const params = routePathSegments[1]
        for (let i = 0; i < routes.length; i++) {
            
            const routePath = routes[i].path;

            const pathSegments = routePath.split('/').slice(1);

            if ((pathSegments[0] === routePathSegments[0]) && (pathSegments.length === routePathSegments.length)) {
                if (pathSegments[0] === 'reportReasons') {
                    const reasonsDiv = document.getElementById('listOfForms');
                    //calls function to create html for flagged reasons table
                    const reportReasons = reportReasonsPopup(params);
                    reportReasons.then(data => (reasonsDiv.innerHTML = data));
                } 
            }
        }
    } else {
        const contentDiv = document.getElementById('reportsPageContent');
        for (let j = 0; j < routes.length; j++) {
            if (routes[j].path === path) {
                const routeView = routes[j].getView();
                routeView.then(data => (contentDiv.innerHTML = data));
                window.scrollTo(0, 0);
            }
        }
    }
};

window.onpopstate = changeLocation;
window.route = route;

changeLocation();

// Define different templates

async function viewReportsPage(){
    try{
        // fetch request to get all reports
        const response = await fetch('/reportList')
        const data = await response.json();
        document.getElementById('homepage').style.display='none'; document.getElementById('softwarePage').style.display='none'; document.getElementById('reportsPage').style.display='block';

        const html = allReports(data);
        return html;

    }
    catch(e){
        alert(e)
    }
}

async function reportReasonsPopup(reportName){
    try{
        // fetch request to get all reasons for a report being flagged
        const response = await fetch('/reportReasons/' + reportName);
        if (response.status === 204){
            window.alert("Error, could not view reasons")
        }
        else{
            const data = await response.json()
            if (data.length === 0){
                const htmlPopup = noReasons();
                document.getElementById("listOfForms").style.display="block";
                return htmlPopup;
            }
            else {
                const htmlPopup = reportReasonsTable(data);
                document.getElementById("listOfForms").style.display="block";
                return htmlPopup;
            }
        }
    }
    catch(e){
        alert(e)
    }
}

// Functions to define how to load the data

// function to create html for all reports table
function allReports (data){
    let showReports = '';
    tableHeaders = `<table class="table">
        <th scope="col">Report Name</th>
        <th scope="col">Times Flagged</th>
        <th scope="col">Flag</th>
        <th scope="col">Download</th>`
    endTable = `</table>`
    

    showReports = tableHeaders;
    for(let i=0; i<data.length; i++){
        reportData = report(data[i]);
        showReports += reportData;
    }
    return showReports
}

// function to create html for each report in the table (each row)
function report (data){
    let name = data.Name;
    let nameSub = name.substring(0, name.length-4);
    const report = `<tr>
    <td>${nameSub}</td>
    <td><button id="downloadButton"><a href="/reportReasons/${data.Name}" onclick="route()">${colourTriangle(data.TimesReported)} ${data.TimesReported}</a></button></td>
    <td><button type="button" class="btn" id="downloadButton" onclick="generateForm('${data.Name}')"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-flag-fill" viewBox="0 0 16 16">
    <path d="M14.778.085A.5.5 0 0 1 15 .5V8a.5.5 0 0 1-.314.464L14.5 8l.186.464-.003.001-.006.003-.023.009a12.435 12.435 0 0 1-.397.15c-.264.095-.631.223-1.047.35-.816.252-1.879.523-2.71.523-.847 0-1.548-.28-2.158-.525l-.028-.01C7.68 8.71 7.14 8.5 6.5 8.5c-.7 0-1.638.23-2.437.477A19.626 19.626 0 0 0 3 9.342V15.5a.5.5 0 0 1-1 0V.5a.5.5 0 0 1 1 0v.282c.226-.079.496-.17.79-.26C4.606.272 5.67 0 6.5 0c.84 0 1.524.277 2.121.519l.043.018C9.286.788 9.828 1 10.5 1c.7 0 1.638-.23 2.437-.477a19.587 19.587 0 0 0 1.349-.476l.019-.007.004-.002h.001"/>
  </svg></button></td>
    <td><form id = "getReport" action="/reportDownload/${data.Name}" method = "GET"><button id="downloadButton" type="submit"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-file-earmark-arrow-down-fill" viewBox="0 0 16 16">
    <path d="M9.293 0H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V4.707A1 1 0 0 0 13.707 4L10 .293A1 1 0 0 0 9.293 0zM9.5 3.5v-2l3 3h-2a1 1 0 0 1-1-1zm-1 4v3.793l1.146-1.147a.5.5 0 0 1 .708.708l-2 2a.5.5 0 0 1-.708 0l-2-2a.5.5 0 0 1 .708-.708L7.5 11.293V7.5a.5.5 0 0 1 1 0z"/>
  </svg></button></form></td>`
    return report;    
}


//function to choose the correct colur of triangle for the number of times a report has been flagged
function colourTriangle(TimesReported){
    if (+TimesReported == 0){
        return '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-exclamation-triangle-fill" id="greenWarning" viewBox="0 0 16 16"><path d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/></svg>';
    }
    else if (+TimesReported <= 5){
        return '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-exclamation-triangle-fill" id="yellowWarning" viewBox="0 0 16 16"><path d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/></svg>';
    }
    else{
        return '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-exclamation-triangle-fill" id="redWarning" viewBox="0 0 16 16"><path d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/></svg>';
    }
}

// function to show the reasons for flagging a report in a table
function reportReasonsTable(data){
    let showReportReasons = '';
    tableHeaders2 = `<table class="table table2">
    <th class="col-2" scope="col">Flagging date</th>
    <th class="col-6"scope="col">Reason for Flagging</th>`
    endTable2 = `</table>`

    showReportReasons = tableHeaders2;

    buttonToClose = `<div id="centering"><button type="button" id="buttonClosingFlagPage" onclick="closeList()"> CLOSE</button></div>`

    for(let i=0; i<data.length; i++){
        showReportReasons += reportReason(data[i]);
    }
    showReportReasons += buttonToClose;
    return showReportReasons
}

//function for each row of the report reasons table
function reportReason(data){
    const reportReason = `<tr>
    <td>${data.reportDate}</td>
    <td>${data.reportReason}</td>`
    return reportReason;
}

// function to generate popup for submitting a form of flagging a report
function generateForm(data) {
    console.log("generate form")
    let flagReporthtml=``;
    flagReporthtml += `<form style="text-align: center" class="formContainer" method="POST" action="/flagReport/${data}">
                <div class="mb-3">
                    <label for="InputReason" class="form-label" style="color: white; font-weight:500;"><b>Reason for Reporting</b> </label>
                    <texarea name="Text1"><input type="text" placeholder="Enter Reason" class="form-control" id="InputReason" name="reason" required></texarea>
                </div>
                <input type="checkbox" class="form-check-input" id="checkbox">
                <label class="form-check-label" for="agree" style="color:white; padding-bottom:2%;"> I confirm that I am being truthful</label> <br>
                <button type="submit" class="btn" id="flagReportBtn" onclick="if(!this.form.checkbox.checked){alert('Please confirm that you are being truthful before submission.');return false}"> SUBMIT</button>
                <button type="button" class="btn cancel" onclick="closeForm()"> CLOSE</button>`

    let reasonsDiv2 = document.getElementById('flagReportFormBox');
    reasonsDiv2.style.display='block';
    reasonsDiv2.innerHTML = flagReporthtml;
    
}

function noReasons(){
    console.log("no reasons")
    const noReasons = `<div id="centering"><div id="noreason"><col><p> No reasons to show</p><button type="button" id="buttonClosingFlagPage" onclick="closenoReasons()"> CLOSE</button></col></div></div>`
    return noReasons;

}

// closing certain popups
function closenoReasons() {
    document.getElementById("noreason").style.display="none";
}

function closeList() {
    document.getElementById("listOfForms").style.display="none";
}

function closeForm() {
    document.getElementById("flagReportFormBox").style.display="none";
}

function openUploadReportPopup() {
    document.getElementById('uploadForm').style.display='flex';
    document.getElementById('homepage').style.display='none'; 
    document.getElementById('softwarePage').style.display='none';
    document.getElementById('reportsPage').style.display='none';
    
}

function closeUploads() {
    document.getElementById('uploadForm').style.display='none';
     document.getElementById('homepage').style.display='flex'; 
    document.getElementById('softwarePage').style.display='none';
    document.getElementById('reportsPage').style.display='none';
}

