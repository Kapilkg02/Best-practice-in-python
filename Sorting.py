import pandas as pd
new_data = pd.read_excel("D:\Car_sales.xlsx", sheet_name="car")

# proc sort command
new_sort = new_data.sort_values("Sales_in_thousands",ascending=True )
new_sort2 = new_data.sort_values("Sales_in_thousands",ascending= True, "Price_in_thousands",ascending = False)
#sorting dataset ;; one ascending and one descending;
sorted_data = new_data.sort_values(by=["Sales_in_thousands","Horsepower"],ascending= [False,True], na_position= "first")
sorted_data = new_data.sort_values(["Sales_in_thousands","Model"],ascending= [False,True])

sorted_data=sorted_data[["Sales_in_thousands","Horsepower","Manufacturer"]]
sorted_data