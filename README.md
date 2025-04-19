# Jeguvin-Python-Mysql-CRUD-Jegatheesh-M


# 🎓 Student Database Management System

A simple Python project using MySQL to manage student records via a command-line interface (CLI). It supports adding, updating, deleting, and viewing student details in a clean tabular format using the `tabulate` library.

---

## 📋 Overview

This project demonstrates how to connect a Python program to a MySQL database and perform basic CRUD (Create, Read, Update, Delete) operations.

You can:
- 🟢 Add a new student record
- ✏️ Update existing student details
- ❌ Delete a student record
- 📖 View all student records in a neat tablecd

---

## 🗄️ MySQL Database Structure

### Database: `Students`

### Table: `STD_Details`

```sql
CREATE DATABASE Students;

USE Students;

CREATE TABLE STD_Details (
    roll_no INT PRIMARY KEY,
    name VARCHAR(100),
    Department VARCHAR(100),
    Email VARCHAR(100)
);
