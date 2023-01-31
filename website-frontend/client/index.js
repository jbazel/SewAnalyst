

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


