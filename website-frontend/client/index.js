

const downloadSoftware = document.getElementById("downloadSoftware")
downloadSoftware.addEventListener("click", async function(event){
    try{
      const response = await fetch('/program_download');
    } catch(e) {
      alert(e);
    }
  });



/*function openForm() {
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
}*/

///////////////////
/////////////////////
/////////////////////////////
/////////////////////////////////

const route = (event) => {
    event = event || window.event;
    event.preventDefault();
    window.history.pushState({}, '', event.target.href);
    changeLocation();
};

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

//const baseRoutes = ["reportReasons, viewReports"];

const changeLocation = async () => {
    const path = window.location.pathname;
    
    const routePathSegments = path.split('/').slice(1);

    if (routePathSegments.length > 1) {
        const params = routePathSegments[1]
        //console.log("params in handle loc: "+params)
        for (let i = 0; i < routes.length; i++) {
            
            const routePath = routes[i].path;

            const pathSegments = routePath.split('/').slice(1);

            if ((pathSegments[0] === routePathSegments[0]) && (pathSegments.length === routePathSegments.length)) {
                if (pathSegments[0] === 'reportReasons') {
                    const reasonsDiv = document.getElementById('listOfForms');
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
        //console.log("here page")
        const response = await fetch('/reportList')
        const data = await response.json();
        // console.log(data)
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
        //this won't work rn but the basis is there
        //console.log("here reasons")
        const response = await fetch('/reportReasons/' + reportName);
        if (response.status === 204){
            window.alert("Error, could not view reasons")
        }
        else{
            const data = await response.json()
            //window.alert(data);
            if (data.length === 0){
                const htmlPopup = noReasons();
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

function allReports (data){
    let showReports = '';
    tableHeaders = `<table class="table">
        <th scope="col">Report Name</th>
        <th scope="col">Times Flagged</th>
        <th scope="col">Flag Report</th>`
    endTable = `</table>`
    

    showReports = tableHeaders;
    for(let i=0; i<data.length; i++){
        showReports += report(data[i]);
    }
    return showReports
}

function report (data){
    const report = `<tr>
    <td><form id = "getReport" action="/reportDownload/${data.Name}" method = "GET"><button id="togetform" type="submit">${data.Name}</button></form></td>
    <td><a href="/reportReasons/${data.Name}" onclick="route()"> ${colourTriangle(data.TimesReported)}${data.TimesReported}</a></td>
    <td><button type="button" class="btn" id="reportbutton" onclick="generateForm('${data.Name}')">REPORT</button></td>`
    return report;    
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

function reportReasonsTable(data){
    let showReportReasons = '';
    tableHeaders2 = `<table class="table table2">
    <th scope="col">Flagging date</th>
    <th scope="col">Reason for Flagging</th>`
    endTable2 = `</table>`

    showReportReasons = tableHeaders2;

    buttonToClose = `<button type="button" class="btn cancel2" onclick="closeList()"> CLOSE</button>`

    for(let i=0; i<data.length; i++){
        showReportReasons += reportReason(data[i]);
    }
    showReportReasons += buttonToClose;
    return showReportReasons
}

function reportReason(data){
    const reportReason = `<tr>
    <td>${data.reportDate}</td>
    <td>${data.reportReason}</td>`
    return reportReason;
}

function noReasons(){
    const noReasons = `<div id="noreason"><p> No reasons to show</p></div>`
    return noReasons;
    // needs to have a close button??
}

function closeList() {
    document.getElementById("listOfForms").style.display="none";
}

function generateForm(data) {
    console.log("generate form")
    let flagReporthtml=``;
    flagReporthtml += `<form style="text-align: center" class="formContainer" method="POST" action="/flagReport/${data}">
                <div class="mb-3">
                    <label for="InputReason" class="form-label" style="color: white; font-weight:500;"><b>Reason for Reporting</b> </label>
                    <texarea name="Text1" rows="5"><input type="text" placeholder="Enter Reason" class="form-control" id="InputReason" name="reason" required></texarea>
                </div>
                <input type="checkbox" class="form-check-input" id="Checkbox">
                <label class="form-check-label" for="Checkbox" style="color:white; padding-bottom:2%;"> I confirm that I am being truthful in my report</label> <br>
                <button type="submit" class="btn" id="flagReportBtn"> SUBMIT</button>
                <button type="button" class="btn cancel" onclick="closeForm()"> CLOSE</button>`

    let reasonsDiv2 = document.getElementById('flagReportFormBox');
    reasonsDiv2.style.display='block';
    reasonsDiv2.innerHTML = flagReporthtml;
    
}

function closeForm() {
    document.getElementById("flagReportFormBox").style.display="none";
}