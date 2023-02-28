const downloadSoftware = document.getElementById("downloadSoftware")
downloadSoftware.addEventListener("click", async function(event){
    try{
      const response = await fetch('/program_download');
    } catch(e) {
      alert(e);
    }
  });