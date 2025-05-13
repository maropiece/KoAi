// server.js
const express = require('express');
const mysql = require('mysql2');
const cors = require('cors');
const app = express();
const PORT = 3000;

app.use(cors());

// MySQL database connection
const db = mysql.createConnection({
  host: 'localhost',
  user: 'root',        // update if different
  password: 'Maram',        // update if set
  database: 'MochiScan' // change to your database name
});

db.connect((err) => {
  if (err) {
    console.error('MySQL connection error:', err);
    return;
  }
  console.log('Connected to MySQL database.');
});

// API endpoint to get all example products
app.get('/api/examples', (req, res) => {
  const sql = 'SELECT * FROM examples';
  db.query(sql, (err, results) => {
    if (err) {
      console.error('Error fetching data: ', err);
      return res.status(500).send('Error retrieving data');
    }
    res.json(results);
  });
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
