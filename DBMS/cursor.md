Certainly! Below are the PL/SQL blocks for the given problem statements:

### 1. Implicit Cursor
```plsql
DECLARE
    -- Declare variables for the update and display messages
    v_inactive_count NUMBER;

BEGIN
    -- Activate inactive accounts
    UPDATE accounts
    SET status = 'Active'
    WHERE last_transaction_date < SYSDATE - 365;

    -- Get the number of rows affected by the update
    v_inactive_count := SQL%ROWCOUNT;

    -- Display message based on the number of rows affected
    IF v_inactive_count > 0 THEN
        DBMS_OUTPUT.PUT_LINE(v_inactive_count || ' accounts activated successfully.');
    ELSE
        DBMS_OUTPUT.PUT_LINE('No inactive accounts found.');
    END IF;
END;
/
```

### 2. Explicit Cursor
```plsql
DECLARE
    CURSOR emp_cursor IS
        SELECT E_no, Salary
        FROM EMP
        WHERE Salary < (SELECT AVG(Salary) FROM EMP);

    v_e_no emp.E_no%TYPE;
    v_salary emp.Salary%TYPE;
BEGIN
    -- Loop through employees and update salary
    FOR emp_rec IN emp_cursor LOOP
        v_e_no := emp_rec.E_no;
        v_salary := emp_rec.Salary * 1.10;

        -- Update salary in EMP table
        UPDATE EMP
        SET Salary = v_salary
        WHERE E_no = v_e_no;

        -- Insert record into increment_salary table
        INSERT INTO increment_salary (E_no, Salary)
        VALUES (v_e_no, v_salary);
    END FOR;
END;
/
```

### 3. Explicit Cursor with Parameterized Cursor
```plsql
DECLARE
    CURSOR stud_cursor (min_attendance NUMBER) IS
        SELECT roll, att
        FROM stud21
        WHERE att < min_attendance;

    v_roll stud21.roll%TYPE;
    v_att stud21.att%TYPE;

BEGIN
    -- Loop through students and update status
    FOR stud_rec IN stud_cursor(75) LOOP
        v_roll := stud_rec.roll;
        v_att := stud_rec.att;

        -- Update status in stud21 table
        UPDATE stud21
        SET status = 'D'
        WHERE roll = v_roll;

        -- Insert record into D_Stud table
        INSERT INTO D_Stud (roll, att)
        VALUES (v_roll, v_att);
    END FOR;
END;
/
```

### 4. Parameterized Cursor for Data Merge
```plsql
DECLARE
    CURSOR merge_cursor (table_name VARCHAR2) IS
        SELECT *
        FROM N_RollCall
        WHERE NOT EXISTS (SELECT 1 FROM O_RollCall WHERE N_RollCall.id = O_RollCall.id);

BEGIN
    -- Loop through records and merge data
    FOR merge_rec IN merge_cursor('N_RollCall') LOOP
        INSERT INTO O_RollCall VALUES merge_rec.*;
    END FOR;
END;
/
```

### 5. Explicit Cursor with Parameterized Cursor for Department Wise Average Salary
```plsql
DECLARE
    CURSOR dept_avg_cursor (d_no NUMBER) IS
        SELECT AVG(Salary) AS avg_salary
        FROM EMP
        WHERE d_no = dept_avg_cursor.d_no;

    v_d_no EMP.d_no%TYPE;
    v_avg_salary NUMBER;

BEGIN
    -- Loop through departments and insert average salary into dept_salary table
    FOR dept_rec IN (SELECT DISTINCT d_no FROM EMP) LOOP
        v_d_no := dept_rec.d_no;

        OPEN dept_avg_cursor(v_d_no);
        FETCH dept_avg_cursor INTO v_avg_salary;
        CLOSE dept_avg_cursor;

        INSERT INTO dept_salary (d_no, avg_salary)
        VALUES (v_d_no, v_avg_salary);
    END FOR;
END;
/
```

### 6. Explicit Cursor with Cursor FOR Loop for Student Detention
```plsql
DECLARE
    CURSOR stud_cursor IS
        SELECT roll, att
        FROM stud21
        WHERE att < 75;

BEGIN
    -- Loop through students and update status
    FOR stud_rec IN stud_cursor LOOP
        -- Update status in stud21 table
        UPDATE stud21
        SET status = 'D'
        WHERE roll = stud_rec.roll;

        -- Insert record into D_Stud table
        INSERT INTO D_Stud (roll, att)
        VALUES (stud_rec.roll, stud_rec.att);
    END FOR;
END;
/
```

These PL/SQL blocks should help you accomplish the specified tasks using both implicit and explicit cursors along with control structures and exception handling. Adjust the code as needed based on your database schema and requirements.
