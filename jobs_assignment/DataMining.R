# 1. Import all 4 datasets provided in the previous question.

TableA <- read.csv("C://Users//bijno//Desktop//Data//TableA.csv")
TableB <- read.csv("C://Users//bijno//Desktop//Data//TableB.csv")
TableC <- read.csv("C://Users//bijno//Desktop//Data//TableC.csv")
TableD <- read.table("C://Users//bijno//Desktop//Data//TableD.xlsx")

  
# 2. Extract unique users for each month and calculate total number of bookings 
#  made by each, total amount spent in each month, total room nights stayed 
#  (status2) for each user for each month.


'
3. Merge these summarized datasets to create one dataframe such that you can see all these
summarized columns for each month side by side. Below is an example of the output:
Guest_id No_bookings.jan Total_room_nights.jan Total_amt.jan No_bookings.feb Total_room_nights.feb Total_amt.feb
1 3 8 6000 1 2 1800
2 NA NA NA 2 4 3000
4. Calculate Repeat Rate for the month February (If X customers had made the bookings in the
month of Jan 2017 (TableA), how many of them made them in Feb 2017 too. (TableB) too i.e Y) -
(Y/X*100)
5. For each city, give the top 3 revenue earning hotels over this time period. (Not separately for
Jan, Feb, Mar)
'