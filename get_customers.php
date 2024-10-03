<?php
// Database configuration
$servername = "localhost";
$username = "root";
$password = "sql0114!";
$dbname = "restaurant mangement";

// Create a new MySQLi instance
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Query to get customers from the database
$sql = "SELECT * FROM customer";
$result = $conn->query($sql);

// Display customers in the HTML table
if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        echo "<tr>";
        echo "<td>" . $row["customer_id"] . "</td>";
        echo "<td>" . $row["customer_name"] . "</td>";
        echo "<td>" . $row["customer_contact"] . "</td>";
        echo "</tr>";
    }
}

// Close the database connection
$conn->close();
?>
