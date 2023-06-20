SELECT Count(EMPLOYEE_ID) AS Count_employee , 
ROUND(AVG(SALARY), 1) AS Avg_salary FROM employees
WHERE DEPARTMENT_ID = 90; 