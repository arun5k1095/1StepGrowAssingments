import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("Employee_data.xlsx")
# print(df)

"""
Compare the average salary and total sales across different
departments and regions. Identify which department and region perform
the best in terms of these metrics.
"""

grouped_data = df.groupby(["department", "region"])
grouped_avg_sal = grouped_data["salary"].mean()
grouped_avg_sal = grouped_avg_sal.reset_index()
# print(grouped_avg_sal)

dept_sal_data = grouped_avg_sal.groupby(["department"])["salary"].max().reset_index()
print(dept_sal_data)
max_sal = dept_sal_data["salary"].max().round(0)
# print(max_sal)
max_sal_data = grouped_avg_sal.loc[grouped_avg_sal["salary"].round(0) == max_sal]
print("Department having max salary is: \n" , max_sal_data)
#
grouped_total_sales = grouped_data["sales"].sum().reset_index()
print(grouped_total_sales)

dept_sales_data = grouped_total_sales.groupby(["department"])["sales"].max().reset_index()
max_sales = dept_sales_data["sales"].max().round(0)
max_sales_data = grouped_total_sales.loc[grouped_total_sales["sales"].round(0) == max_sales]
print("Department having max sales is: \n" , max_sales_data)
#
#

"""
Identify the top 5 employees with the highest sales and the top 5
employees with the highest salaries.
Are the highest earners also the top performers in terms of sales?
"""
top_emp_sales = df.sort_values(by='sales', ascending=False).head(5)
top_emp_salary = df.sort_values(by='salary', ascending=False).head(5)
print("Top 5 employees with highest sales: \n", top_emp_sales[["employee_id","employee_name","sales"]])
print("Top 5 employees with highest salary: \n", top_emp_salary[["employee_id","employee_name","salary"]])
top_emp_sales_salary = pd.merge(top_emp_salary, top_emp_sales, on='employee_id', how='inner' )
if len(top_emp_sales_salary)== 0:
    print("There are no employee who are highest earners and also top performers in terms of sales")
else:
    print("Employee who are highest earners and also top performers in terms of sales")
    print(top_emp_sales_salary)


"""
Analyze the relationship between an employee's experience and their
salary. 
"""
emp_exp = df[["employee_id","salary","experience"]]
corr = emp_exp.corr()
print("Correlation matrix between experience and salary")
print(corr)

"""
Investigate the correlation between experience and sales performance.
Does more experience lead to better sales figures?
"""
emp_sale = df[["employee_id","experience","sales"]]
corr = emp_sale.corr()
print("Correlation between employee experience and sales:")
print(corr)

"""
The distribution of sales across departments.
"""
dept_sales = df.groupby("department")["sales"].sum().reset_index()
print(dept_sales)
dept_sales.plot(kind="bar", x="department", y="sales",legend=True)
plt.title("Department wise Sales")
plt.show()

"""
The relationship between experience and salary.
"""
exp_salary = df.groupby("experience")["salary"].sum().reset_index()
print(exp_salary)
exp_salary.plot(kind='scatter', x="experience", y="salary")
plt.title("Salary vs Experience")
plt.show()

"""
The comparison of average salaries across regions or departments.
"""
reg_sal = df.groupby("region")["salary"].mean().reset_index()
print(reg_sal)
reg_sal.plot(kind='line', x="region", y="salary")
plt.title("Region wise average salary")
plt.show()