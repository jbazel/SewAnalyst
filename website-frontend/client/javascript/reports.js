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
        let action = ' action = "/reportDownload"';
        let input = '<input type = "hidden" name = "id" value =' + object.Name + '></>'
        let id = ' id =' + object.Name + ';'
        let method = 'method = "GET"'

        tr.innerHTML = '<td><form' + id + method + action + '>' + ' <button type="submit">' + 'Report ' + object.Name + '</button>'+input+'</form>' + '</td>' +
          '<td>' + colourTriangle(object.TimesReported) + object.TimesReported + '</td>' +
          '<td>' + '<button onclick="openList()"><img src="http://clipart-library.com/data_images/81597.png" style="width:50px; height:50px"></button>' + '</td>' +
          '<td>' + '<button type="button" class="btn" id="reportbutton" onclick="openForm()">  REPORT</button>' + '</td>';
        table.appendChild(tr);
    });
}

function colourTriangle(TimesReported){
    if (+TimesReported == 0){
        return '<img id="alerts" src="../Green alert.jpg">';
    }
    else if (+TimesReported <= 5){
        return '<img id="alerts" src="../Yellow alert.jpg" >';
    }
    else{
        return '<img id="alerts" src="../Red alert.jpg" >';
    }
}


//this element doesnt actually exist rn but having the same issues as with downloading report / flagging report of it knowing which report we are relating to
const viewReasons = document.getElementById('listOfForms')
viewReasons.addEventListener('submit', async function(event){
    try{
        event.preventDefault()
        //this won't work rn but the basis is there
        const reportNumber = viewReasons.elements.namedItem('InputReportNumber').value
        const response = await fetch('/viewReasons?' + new URLSearchParams({reportNum: reportNumber}))
        if (response.status === 204){
            window.alert("Error, could not view reasons")
        }
        else{
            const data = await response.json()
            window.alert(data);
        }
    }
    catch(e){
        alert(e)
    }
})