import { useEffect, useState } from 'react'

function App() {

  const [records, setRecords] = useState([])
  const [selectedFile, setSelectedFile] = useState(null)

  const fetchRecords = () => {

    fetch("https://breathe-esg-prototype-u1yw.onrender.com/api/records/")
      .then(response => response.json())
      .then(data => {
        setRecords(data)
      })

  }

  useEffect(() => {
    fetchRecords()
  }, [])


  const approveRecord = (id) => {

    fetch(`https://breathe-esg-prototype-u1yw.onrender.com/api/approve/${id}/`, {
      method: 'POST'
    })
      .then(response => response.json())
      .then(data => {

        console.log(data)

        fetchRecords()

      })

  }


  const uploadCSV = () => {

    const formData = new FormData()

    formData.append('file', selectedFile)

    fetch("https://breathe-esg-prototype-u1yw.onrender.com/api/upload-csv/", {
      method: 'POST',
      body: formData
    })
      .then(response => response.json())
      .then(data => {

        console.log(data)

        fetchRecords()

      })

  }


  return (

    <div style={{ padding: "20px" }}>

      <h1>Breathe ESG Dashboard</h1>

      <div style={{ marginBottom: "20px" }}>

        <input
          type="file"
          onChange={(e) => setSelectedFile(e.target.files[0])}
        />

        <button onClick={uploadCSV}>
          Upload CSV
        </button>

      </div>

      <table border="1" cellPadding="10">

        <thead>

          <tr>
            <th>Source</th>
            <th>Activity</th>
            <th>Quantity</th>
            <th>Unit</th>
            <th>Scope</th>
            <th>Status</th>
            <th>Action</th>
          </tr>

        </thead>

        <tbody>

          {records.map(record => (

            <tr key={record.id}>

              <td>{record.source_type}</td>
              <td>{record.activity_type}</td>
              <td>{record.quantity}</td>
              <td>{record.unit}</td>
              <td>{record.scope}</td>
              <td>{record.review_status}</td>

              <td>

                {!record.locked ? (

                  <button
                    onClick={() => approveRecord(record.id)}
                  >
                    Approve
                  </button>

                ) : (
                  "Locked"
                )}

              </td>

            </tr>

          ))}

        </tbody>

      </table>

    </div>

  )

}

export default App