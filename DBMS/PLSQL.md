Certainly! Below are the PL/SQL blocks for the given problem statements:

### 1. Handling Attendance in Stud Table
```plsql
DECLARE
    v_roll_number Stud.Roll%TYPE;
    v_attendance Stud.Att%TYPE;
    v_status Stud.Status%TYPE;
BEGIN
    -- Accept Roll number from the user
    v_roll_number := &user_roll_number;

    -- Fetch attendance for the given roll number
    SELECT Att, Status
    INTO v_attendance, v_status
    FROM Stud
    WHERE Roll = v_roll_number;

    -- Check attendance and update status
    IF v_attendance < 75 THEN
        DBMS_OUTPUT.PUT_LINE('Term not granted');
        UPDATE Stud SET Status = 'D' WHERE Roll = v_roll_number;
    ELSE
        DBMS_OUTPUT.PUT_LINE('Term granted');
        UPDATE Stud SET Status = 'ND' WHERE Roll = v_roll_number;
    END IF;
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('Roll number not found in Stud table');
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('An error occurred: ' || SQLERRM);
END;
/
```

### 2. User-Defined Exception Handling for Account Master
```plsql
DECLARE
    v_current_balance NUMBER := 1000; -- Example: Initial balance in the account
    v_withdrawal_amount NUMBER := 1500; -- Example: Amount attempted to withdraw

    -- User-defined exception
    OVERDRAWN_EXCEPTION EXCEPTION;
    PRAGMA EXCEPTION_INIT(OVERDRAWN_EXCEPTION, -20001);

BEGIN
    -- Check if withdrawal amount is greater than the current balance
    IF v_withdrawal_amount > v_current_balance THEN
        -- Raise user-defined exception
        RAISE OVERDRAWN_EXCEPTION;
    ELSE
        -- Process the withdrawal
        v_current_balance := v_current_balance - v_withdrawal_amount;
        DBMS_OUTPUT.PUT_LINE('Withdrawal successful. Current balance: ' || v_current_balance);
    END IF;
EXCEPTION
    WHEN OVERDRAWN_EXCEPTION THEN
        DBMS_OUTPUT.PUT_LINE('Withdrawal amount exceeds current balance. Transaction failed.');
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('An error occurred: ' || SQLERRM);
END;
/
```

### 3. Handling Borrower and Fine Table with Exception Handling
```plsql
DECLARE
    v_roll_no Borrower.Roll_no%TYPE;
    v_book_name Borrower.Name_of_Book%TYPE;
    v_date_of_issue Borrower.Date_of_Issue%TYPE;
    v_status Borrower.Status%TYPE;
    v_fine_amt NUMBER;

    -- User-defined exception
    FINE_EXCEPTION EXCEPTION;
    PRAGMA EXCEPTION_INIT(FINE_EXCEPTION, -20002);

BEGIN
    -- Accept Roll number and Name of Book from the user
    v_roll_no := &user_roll_no;
    v_book_name := '&user_book_name';

    -- Fetch details from Borrower table
    SELECT Roll_no, Date_of_Issue, Status
    INTO v_roll_no, v_date_of_issue, v_status
    FROM Borrower
    WHERE Roll_no = v_roll_no AND Name_of_Book = v_book_name;

    -- Calculate fine amount based on the number of days
    v_fine_amt := CASE
        WHEN SYSDATE - v_date_of_issue BETWEEN 15 AND 30 THEN 5 * (SYSDATE - v_date_of_issue)
        WHEN SYSDATE - v_date_of_issue > 30 THEN 50 * (SYSDATE - v_date_of_issue)
        ELSE 0
    END;

    -- Check if fine condition is true and update tables accordingly
    IF v_fine_amt > 0 THEN
        -- Raise user-defined exception
        RAISE FINE_EXCEPTION;
    ELSE
        -- Update Borrower table
        UPDATE Borrower SET Status = 'R' WHERE Roll_no = v_roll_no AND Name_of_Book = v_book_name;

        -- Insert details into Fine table
        INSERT INTO Fine (Roll_no, Date, Amt) VALUES (v_roll_no, SYSDATE, v_fine_amt);
        DBMS_OUTPUT.PUT_LINE('Book submitted successfully. Fine amount: ' || v_fine_amt);
    END IF;
EXCEPTION
    WHEN FINE_EXCEPTION THEN
        DBMS_OUTPUT.PUT_LINE('Fine amount exceeds the allowed limit. Book cannot be submitted.');
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('Borrower details not found.');
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('An error occurred: ' || SQLERRM);
END;
/
```

These PL/SQL blocks address the specified requirements, including control structures and exception handling. Make sure to adapt them based on your actual database structure and requirements.