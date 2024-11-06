# create database bank_atm;
use bank_atm;
# accounts table for storing account details
CREATE TABLE accounts (
    account_id INT AUTO_INCREMENT PRIMARY KEY,
    account_number VARCHAR(20) NOT NULL UNIQUE,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100),
    balance DECIMAL(15, 2) NOT NULL DEFAULT 0.00,
    created_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
# authenticattion table is used to store card data and is used while transactions
CREATE TABLE authentication (
    auth_id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT NOT NULL,
    pin VARCHAR(6) NOT NULL,
    card_number VARCHAR(20) NOT NULL UNIQUE,
    expiration_date DATE NOT NULL,
    cvv VARCHAR(3) NOT NULL,
    FOREIGN KEY (account_id) REFERENCES Accounts(account_id) ON DELETE CASCADE
);
# login_credits table stores userid and password for first step login
CREATE TABLE login_credits (
	account_id INT NOT NULL,
    userid VARCHAR(20) NOT NULL UNIQUE,
    pass VARCHAR(20) CHECK(0<length(pass)<20) NOT NULL,
	FOREIGN KEY (account_id) REFERENCES Accounts(account_id) ON DELETE CASCADE
);
drop table login_credits;
-- Inserting account data for multiple users
INSERT INTO Accounts (account_number, first_name, last_name, balance)
VALUES 
    ('1234567890', 'John', 'Doe', 1500.00),
    ('9876543210', 'Jane', 'Smith', 2300.50),
    ('4567891230', 'Alice', 'Brown', 4500.75),
    ('6789012345', 'Bob', 'Jones', 1200.25),
    ('1122334455', 'Charlie', 'Davis', 5600.60);
-- Inserting authentication data for the accounts
INSERT INTO Authentication (account_id, pin, card_number, expiration_date, cvv)
VALUES 
    (1, '123456', '9876543210123456', '2025-12-31', '123'),  -- For account 1
    (2, '234567', '1234567890123456', '2026-11-30', '234'),  -- For account 2
    (3, '345678', '2345678901234567', '2027-10-31', '345'),  -- For account 3
    (4, '456789', '3456789012345678', '2025-09-30', '456'),  -- For account 4
    (5, '567890', '4567890123456789', '2028-08-31', '567');  -- For account 5
    
-- Inserting login credentials for the users in the login_credits table

INSERT INTO login_credits (account_id, userid, pass)
VALUES 
    (1, 'johndoe', 'password123'),    -- For account 1 (John Doe)
    (2, 'janesmith', 'securepass234'), -- For account 2 (Jane Smith)
    (3, 'alicebrown', 'mypassword456'), -- For account 3 (Alice Brown)
    (4, 'bobjones', 'password7890'),   -- For account 4 (Bob Jones)
    (5, 'charliedavis', 'charlie@01'); -- For account 5 (Charlie Davis)

select * from accounts;
select * from authentication;
select * from login_credits;