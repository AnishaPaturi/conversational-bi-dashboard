import axios from "axios";

function UploadCSV() {

  const handleUpload = async (event) => {

    const file = event.target.files[0];

    const formData = new FormData();

    formData.append("file", file);

    await axios.post("http://127.0.0.1:8000/upload", formData);

    alert("Dataset uploaded successfully!");
  };

  return (
    <div style={{ marginBottom: "20px" }}>
      <input type="file" onChange={handleUpload} />
    </div>
  );
}

export default UploadCSV;