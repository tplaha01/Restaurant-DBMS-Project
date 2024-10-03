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

// Get form data
$name = $_POST['customer_name'];
$contact = $_POST['customer_contact'];

// Insert the new customer into the database
$sql = "INSERT INTO customer (customer_name, customer_contact) VALUES ('$name', '$contact')";
if ($conn->query($sql) === true) {
    // Success message
    echo "Customer added successfully.";
} else {
    // Error message
    echo "Error: " . $sql . "<br>" . $conn->error;
}

// Close the database connection
$conn->close();
?>
