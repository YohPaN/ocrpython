const fs = require('fs');
const token = "eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJjYXJkdHJhZGVyLXByb2R1Y3Rpb24iLCJzdWIiOiJhcHA6NzEzMCIsImF1ZCI6ImFwcDo3MTMwIiwiZXhwIjo0ODQ2Mzg3MzE3LCJqdGkiOiI2OTI4NTBlNy1jNzQ2LTRhZWUtODY1Zi00MDllZTg0NTU0N2EiLCJpYXQiOjE2OTA3MTM3MTcsIm5hbWUiOiJWYXJ0dXMgQXBwIDIwMjMwNzMwMTA0MTU3In0.pymKhL_jZDO_oRuz38HTe1X6uM_E-WI5pJvfJJPsALnoj69c7FK74LF_whMr3i3W87J5P5FvTXn4fZv5sPFmwpd_vKSN3z7SjVvOrpWaog3PnT9iqYGCQSLROMBn4bcY-aHZfDsJ2vOgrfzmmJNk4dJM-QRqM3GDOuiEkXxpX0i9XI_Tjl0oS-xDLc56-kQBpw4u-3_TlZAMvvPbe7QzuF7KCxwuCJKKmboyUVWTh-BZiRDMlvH8ZvW47BwVWrRBOwYXUBx3bdBU1wp3s9mrTmnhR8wSh1U9uSLrG7sJZlEW5P4GjMr5eIQ22K5DkyvmZTdWph7LIvu24fttMvzsBQ"

const axios = require('axios');
const { resolve } = require('path');

async function myFunc() {
    try {
        const response = await axios.get('https://db.ygoprodeck.com/api/v7/cardinfo.php')
        return response.data.data
    } catch(error) {
        console.log(error)
    }
}

async function main() {
    const data = await myFunc()

    // Convert the JSON object to a JSON-formatted string
    console.log(data)

    // Write the JSON data to a file
    fs.writeFile('data.json', JSON.stringify(data), 'utf8', (err) => {
    if (err) {
        console.error('Error writing JSON file:', err);
    } else {
        console.log('JSON file has been written successfully.');
    }
    });
}

main()
