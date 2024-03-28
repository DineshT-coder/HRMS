
CREATE DATABASE EmployeeInformation;
use EmployeeInformation;

CREATE TABLE Employee(
EmployeeID int primary key not null Identity(1,1),
FirstName varchar(255),
LastName varchar(255),
DateOfBirth date,
HireOfDate date,
Email varchar(255),
PhoneNumber varchar(50),
DepartmentID int,
Position varchar(255),
ManagerID int 
);
alter table Employee add foreign key(DepartmentID) references Department(DepartmentID);
alter table Employee add foreign key(ManagerID) references Employee(EmployeeID);


CREATE TABLE Department(
DepartmentID int primary key not null Identity(1,1),
DepartmentName VARCHAR(255)
);

insert into Department(DepartmentName)values('hr');
select * from department;

CREATE TABLE salary(
SalaryID int primary key not null Identity(1,1),
EmployeeID int,
foreign key (EmployeeID) references Employee(EmployeeID) on delete cascade,
Salary int
);

insert into salary(Salary) VALUES(1111);
SELECT * FROM salary;


CREATE TABLE Project(
    ProjectID INT PRIMARY KEY Identity(1,1),
    EmployeeID int,
    foreign key (EmployeeID) references Employee(EmployeeID) on delete cascade,
    DepartmentID INT,
    foreign key (DepartmentID) references Department(DepartmentID) on delete cascade,
    ProjectName VARCHAR(100),
    StartDate DATE,
    EndDate DATE,
    Budget INT,
	Status varchar(120)
);

select * from salary;

CREATE TABLE Qualification(
    QualificationID INT PRIMARY KEY Identity(1,1),
    EmployeeID int,
    Degree VARCHAR(150),
    GraduationYear INT,
    Institute VARCHAR(150),
    foreign key (EmployeeID) references Employee(EmployeeID) on delete cascade
);

CREATE TABLE Address(
AddressID INT PRIMARY KEY Identity(1,1),
Employee_ref_ID INT,
country_id INT,
state_id INT,
city_id INT,
street varchar(100),
zipcode varchar(100),
FOREIGN KEY(Employee_ref_ID) REFERENCES Employee(EmployeeID) ON DELETE CASCADE,
FOREIGN KEY(country_id) REFERENCES Country(country_id) on delete cascade ,
FOREIGN KEY(state_id) REFERENCES State(state_id) on delete cascade,
FOREIGN KEY(city_id) REFERENCES City(city_id) on delete cascade
);

CREATE TABLE Country(
country_id int primary key Identity(1,1),
countryName varchar(150)
);

CREATE TABLE City(
city_id int primary key Identity(1,1),
city_name varchar(150));

create table State(
state_id int primary key Identity(1,1),
state_name varchar(150));


select * from employee;
select * from department;
select * from qualification;
select * from salary;
select * from project;
select * from address;
select * from country;
select * from city;
select * from state;

create table Users(
id int not null Identity(1,1),
username varchar(100),
password varchar(100));

delete from employee;
delete from salary;
delete from department;
delete from address;
delete from Qualification;
delete from project;
delete from country;
delete from city;
delete from state;


DBCC CHECKIDENT ('employee', RESEED, 0);
DBCC CHECKIDENT ('department', RESEED, 0);
DBCC CHECKIDENT ('salary', RESEED, 0);
DBCC CHECKIDENT ('project', RESEED, 0);
DBCC CHECKIDENT ('address', RESEED, 0);
DBCC CHECKIDENT ('country', RESEED, 0);
DBCC CHECKIDENT ('state', RESEED, 0);
DBCC CHECKIDENT ('city', RESEED, 0);
DBCC CHECKIDENT ('qualification', RESEED, 0);