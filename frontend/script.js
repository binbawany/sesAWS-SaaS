async function uploadCSV() {
    const file = document.getElementById("fileInput").files[0];
    const formData = new FormData();
    formData.append("file", file);
    await fetch("http://localhost:8000/upload", {
      method: "POST",
      body: formData
    });
  }
  
  async function sendEmail() {
    const formData = new FormData();
    formData.append("name", document.getElementById("name").value);
    formData.append("email", document.getElementById("email").value);
    await fetch("http://<EC2-IP>:8000/send-email", {
      method: "POST",
      body: formData
    });
  }