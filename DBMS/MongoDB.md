Sure, here are MongoDB queries to address the given problem statement:

### 1. Create Database DYPIEMR
```javascript
use DYPIEMR;
```

### 2. Create following Collections Teachers(Tname,dno,dname,experience,salary,date_of_joining ) Students(Sname,roll_no,class)
```javascript
db.createCollection("Teachers");
db.createCollection("Students");
```

### 3. Find the information about all teachers
```javascript
db.Teachers.find({});
```

### 4. Find the information about all teachers of computer department
```javascript
db.Teachers.find({ dname: "Computer" });
```

### 5. Find the information about all teachers of computer, IT, and E&TC department
```javascript
db.Teachers.find({ dname: { $in: ["Computer", "IT", "E&TC"] } });
```

### 6. Find the information about all teachers of computer, IT, and E&TC department having salary greater than or equal to 10000/-
```javascript
db.Teachers.find({
  dname: { $in: ["Computer", "IT", "E&TC"] },
  salary: { $gte: 10000 }
});
```

### 7. Find the student information having roll_no = 2 or Sname=xyz
```javascript
db.Students.find({ $or: [{ roll_no: 2 }, { Sname: "xyz" }] });
```

### 8. Update the experience of teacher-praveen to 10 years, if the entry is not available in the database, consider the entry as a new entry.
```javascript
db.Teachers.update(
  { Tname: "praveen" },
  { $set: { experience: 10 } },
  { upsert: true }
);
```

### 9. Update the department of all the teachers working in IT department to COMP
```javascript
db.Teachers.update(
  { dname: "IT" },
  { $set: { dname: "COMP" } },
  { multi: true }
);
```

### 10. Find the teachers' names and their experience from the teachers collection
```javascript
db.Teachers.find({}, { Tname: 1, experience: 1, _id: 0 });
```

### 11. Using Save() method insert one entry in the department collection
```javascript
db.Department.save({
  dno: 101,
  dname: "Mechanical",
  hod: "John Doe"
});
```

### 12. Using Save() method change the department of teacher praveen to IT
```javascript
db.Teachers.save({ Tname: "praveen", dname: "IT" });
```

### 13. Delete all the documents from teachers collection having IT dept.
```javascript
db.Teachers.remove({ dname: "IT" });
```

### 14. Display with pretty() method, the first 3 documents in the teachers collection in ascending order
```javascript
db.Teachers.find().sort({ _id: 1 }).limit(3).pretty();
```

These queries should help you perform various CRUD operations and retrieve the required information from MongoDB. Adjust the queries based on your specific data structure and requirements.