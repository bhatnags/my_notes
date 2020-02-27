"""

Created on Thu Feb 20 20:56:32 2020

@author: Saumya Bhatnagar (bhatnags@tcd.ie)

Time complexity of the algorithm:
O(n^2) < Time Complexity < O(n)


How the algorithm works:
    Intuition:
        for every calendar day when the seller comes,
        customer should buy only if the seller offers min price
        (as compared to the sellers who offered to sale in last 30 days)

    This is done as:
        for every calendar day when the seller comes,
        the price that the seller is offering is compared with the previous sellers
        who could sell in the last 30 days

    Also keeping in mind that:
        initially the customer is provided with 10 bread loaves
        1 loaf is consumed per day
        all the breads (initially provided or bought) should be eaten up by the end of the calendar
        if two sellers offer the same price, consider the seller (if possible) who has already sold some
        max bread that a seller sells should be at max 30
        if no bread is needed to buy, or should a case come when stale bread has to be consumed, return None

"""


















'''
Method to calculate bread loaves from different sellers which could minimize the cost
Tells how much bread to buy from each of the sellers
Input:
    total_days, an integer, the number of days in the calendar until the free bread arrives
    sellers, a list of pairs of integers (day, price). Each pair represents one bread seller
    The day is how many days from the start until the seller arrives
    The price is the price to buy each loaf of bread from this seller, in pennies
Output:
    purchases, a list of integers of the same length as sellers. Each integer is how many
    loaves you should buy from each seller
    Or None, if there is no solution that does not force your family to eat stale bread at some point
'''
def calculate_purchasing_plan(total_days, sellers):

    # fresh bread lasts for 30 days 
    # max qty that can be bought per seller = 30
    max_qty = 30     
    
    # initial quantity of bread loaves provided
    # 10 fresh loaves at the beginning of the calendar
    initial_quantity = 10  
    
    # bread loaves needed from sellers, 
    # initialized to list of zero
    qty_needed_lst = [0]*len(sellers)  
    
    if total_days<=initial_quantity:
        #print('end of calendar, get a bunch of free bread')
        return None

    if not sellers:
        #print('no sellers to provide meal')
        return None

    if sellers[0][0]>initial_quantity:
        #print('first seller should visit before the initial quantity gets finished')        
        return None
    else:
        # quantity remaining after consuming, till the first seller arives
        remaining_qty = initial_quantity-sellers[0][0]
    
    # Time Complexity O(n)
    for s in range(1, len(sellers)-1):
        if immediate_diff_stale(sellers, s, max_qty):
            #print('consecutive seller arrival took more than 30 days, possibility to eat stale')
            return None
    
    slr_price_lst, slr_day_lst, idxs = cheapest_seller_last_30_days(sellers, max_qty, qty_needed_lst, slr_price_lst=[], slr_day_lst=[])

    # O(n)
    for s in range(len(sellers)-1):
        qty_needed_lst = get_qty_needed(sellers, idxs, slr_day_lst, s, remaining_qty, qty_needed_lst, max_qty, total_days)
            
    # sort for last day
    # at the end of calendar, no bread bought should be left on hand
    last_day = len(sellers)-1
    qty_needed_lst = get_qty_needed(sellers, idxs, slr_day_lst, last_day, remaining_qty, qty_needed_lst, max_qty, total_days)
    
    if sum(qty_needed_lst)>0:
        return qty_needed_lst

    return None
    

# assign the quantity of bread loaves needed per seller 
# based on the remaining amount of bread loaves left from the initial given quantity
def assign_based_on_initial_remaining(sellers, total_days, remaining_qty, qty_needed_lst, idx, s):

    try:
        remaining_diff = min(sellers[s+1][0], total_days)-sellers[s][0]

    except IndexError:
        remaining_diff = total_days-sellers[s][0]

    if remaining_qty>0 and remaining_diff>remaining_qty:
        qty_needed_lst[idx] += remaining_diff-remaining_qty

    elif remaining_qty>0 and remaining_diff<remaining_qty:
        remaining_qty = remaining_qty-remaining_diff

    else:
        qty_needed_lst[idx] += remaining_diff

    return qty_needed_lst, remaining_qty


# when the min price seller is expected to sell more than the max quantity (30 breads)
# assign the extra bread loaves to the next min price seller 
# (within last 30 days, so it doesn't stale)
def assign_basis_extra(sellers, extra, qty_needed_lst, idxs, s, max_qty):
    idx = idxs[s]
    if sellers[s+1][0]-sellers[idx][0]>max_qty:
        day_diff = sellers[s+1][0]-sellers[idx][0]-max_qty
        extra = extra - day_diff

        if extra>0:
            qty_needed_lst[s] += day_diff
            qty_needed_lst[idx] += extra
        else:
            qty_needed_lst[s] += day_diff+extra
            
    else:
        qty_needed_lst[idx] += extra
        
    return qty_needed_lst, extra


# get the quantity needed to be bought from each seller
# knapsack
def get_qty_needed(sellers, idxs, slr_day_lst, s, remaining_qty, qty_needed_lst, max_qty, total_days):

    if sellers[s][0]<=total_days:
        idx = idxs[s]
        
        qty_needed_lst, remaining_qty = assign_based_on_initial_remaining(sellers, total_days, remaining_qty, qty_needed_lst, idx, s)

        while qty_needed_lst[idx]>max_qty:
            extra = qty_needed_lst[idx]-max_qty
            qty_needed_lst[idx]=max_qty
            spl, sdl, idxs = cheapest_seller_last_30_days(sellers, max_qty, qty_needed_lst)
            qty_needed_lst, extra = assign_basis_extra(sellers, extra, qty_needed_lst, idxs, s, max_qty)

    else:
        # end of calendar, ready for free bread
        qty_needed_lst[s]=0

    return qty_needed_lst


# for each seller day, 
# cheapest price offered by the sellers selling in last 30 days
# return lists 
def cheapest_seller_last_30_days(sellers, max_qty, qty_needed_lst, slr_price_lst=[], slr_day_lst=[]):

    idxs = [] # Indexes
    # better than O(nxn), since min_price_day_for_sellers uses break in for loop
    for slr in range(len(sellers)):
        min_price, min_price_day, s = min_price_day_for_seller(sellers, slr, qty_needed_lst, max_qty)
        slr_price_lst.append(min_price)
        slr_day_lst.append(min_price_day)
        idxs.append(s)
    return slr_price_lst, slr_day_lst, idxs


# cheapest seller in last 30 days
# price offered by the cheapest seller in last 30 days
# index of the seller offering thus, the cheapest price
def min_price_day_for_seller(sellers, slr, qty_needed_lst, max_qty):
    min_price = sellers[slr][1]
    min_price_day = sellers[slr][0]
    idx = slr
    
    # backtracking
    # better than O(n), since break is used
    # pool in from older bread sellersbnm
    for s in reversed(range(slr)):
        
        # reversed assuming the list of tuples is ordered
        if not seller_in_last_days(sellers, s, slr, max_qty):
            break
        
        elif qty_needed_lst[s]<max_qty:
            
            if min_price>sellers[s][1]:
                # check p2 and p1 and whichever is smaller
                min_price = sellers[s][1]
                min_price_day = sellers[s][0]
                idx = s
                
            elif min_price==sellers[s][1]:
                # in case of ties, consider where the seller has sold something
                if not qty_needed_lst[idx]:
                    min_price = sellers[s][1]
                    min_price_day = sellers[s][0]
                    idx = s
    return min_price, min_price_day, idx


# check for the seller at given index, 
# if the seller at another given index 
# was available to supply in last 30 days
def seller_in_last_days(sellers, idx1, idx2, max_qty=30):
    if sellers[idx2][0]-sellers[idx1][0]>=max_qty:
        return False
    return True


# check if the day difference between two consecutive suppliers is more than 30
def immediate_diff_stale(sellers, s, max_qty):
    if sellers[s+1][0]-sellers[s][0]>max_qty:
        return True
    else:
        return False



# Run the test case given in the problem statement
print(calculate_purchasing_plan(60, [(10,200), (15,100), (35,500), (50,30)]))







#################################################################################
######################## Run some more tests #########################################
#################################################################################

import unittest # Library to run unit tests

class TestCalculatePurchasingPlan(unittest.TestCase):

    # When total num of calendar days is less than 
    # the num of bread loaves already present
    def test_initial_quantity_is_sufficient_1(self):
        ret = calculate_purchasing_plan(5, [()]) # returns None
        self.assertIsNone(ret)

    def test_initial_quantity_is_sufficient_2(self):
        ret = calculate_purchasing_plan(10, [(10, 200)])
        self.assertIsNone(ret)

    def test_initial_quantity_is_sufficient_3(self):
        ret = calculate_purchasing_plan(5, [(10, 200), (20, 200)])
        self.assertIsNone(ret)

    def test_no_sellers_to_supply(self):
        ret = calculate_purchasing_plan(15, ())
        self.assertIsNone(ret)
        
    # when difference between two consecutive supply days
    # will force family to eat stale bread
    def test_num_days1(self):
        ret = calculate_purchasing_plan(15, [(15, 2)])
        self.assertIsNone(ret)

    def test_num_days2(self):
        ret = calculate_purchasing_plan(20, [(15, 200), (45, 200)])
        self.assertIsNone(ret)
        
    def test_immediate_diff_stale(self):
        ret = immediate_diff_stale([(15, 200), (50, 20)], 0, 30)
        self.assertTrue(ret)
        
        ret = immediate_diff_stale([(15, 20), (35, 200)], 0, 25)
        self.assertFalse(ret)
        
    def test_seller_in_last_days(self):
        sellers = [(15, 20), (50, 200), (70, 100), (75, 2)]
        ret = seller_in_last_days(sellers, 0, 2, 30)
        self.assertFalse(ret)

        ret = seller_in_last_days(sellers, 1, 3, 30)
        self.assertTrue(ret)

    def test_min_price_day_for_seller(self):
        sellers = [(15, 20), (50, 50), (70, 100), (75, 2)]
        qty_needed_lst = [0]*4
        
        self.assertEqual(min_price_day_for_seller(sellers, 0, qty_needed_lst, 30), (20,15,0))
        self.assertEqual(min_price_day_for_seller(sellers, 1, qty_needed_lst, 30), (50,50,1))
        self.assertEqual(min_price_day_for_seller(sellers, 2, qty_needed_lst, 30), (50,50,1))
        self.assertEqual(min_price_day_for_seller(sellers, 3, qty_needed_lst, 30), (2,75,3))

    def test_cheapest_seller_last_30_days(self):
        sellers = [(15, 20), (50, 50), (70, 100), (75, 2)]
        qty_needed_lst = [0]*4
        ret = cheapest_seller_last_30_days(sellers, 30, qty_needed_lst, slr_price_lst=[], slr_day_lst=[])
        
        self.assertIsNotNone(ret)
        self.assertEqual(len(ret[0]), 4)
        self.assertEqual(len(ret[1]), 4)
        

    def test_calculate_purchasing_plan1(self):
        ret = calculate_purchasing_plan(15, [(10, 20), (11, 200)])
        self.assertEqual(ret, [5, 0])

    def test_calculate_purchasing_plan2(self):
        ret = calculate_purchasing_plan(15, [(10, 200), (11, 20)])
        self.assertEqual(ret, [1, 4])

    def test_calculate_purchasing_plan3(self):
        ret = calculate_purchasing_plan(15, [(10, 200), (16, 20)])
        self.assertEqual(ret, [5, 0])
        
    # in case of ties
    def test_calculate_purchasing_plan4(self):
        ret = calculate_purchasing_plan(60, [(10,200), (15,100), (35,500), (50,500)])
        self.assertEqual(ret, [5, 30, 15, 0])

    def test_calculate_purchasing_plan5(self):
        ret = calculate_purchasing_plan(50, [(10,200), (15,100), (35,500), (50,30)])
        self.assertEqual(ret, [5, 30, 5, 0])
    
    def test_calculate_purchasing_plan6(self):
        ret = calculate_purchasing_plan(40, [(10,200), (15,100), (35,500), (50,30)])
        self.assertEqual(ret, [5, 25, 0, 0])

    def test_calculate_purchasing_plan7(self):
        ret = calculate_purchasing_plan(60, [(10,2), (15,100), (35,500), (50,30)])
        self.assertEqual(ret, [30, 5, 5, 10])

    def test_calculate_purchasing_plan8(self):
        ret = calculate_purchasing_plan(60, [(10,200), (15,100), (35,500), (50,30), (55,3)])
        self.assertEqual(ret, [5, 30, 5, 5, 5])

    def test_calculate_purchasing_plan9(self):
        ret = calculate_purchasing_plan(60, [(10,200), (15,100), (35,500), (50,30), (55,300)])
        self.assertEqual(ret, [5, 30, 5, 10, 0])

    def test_calculate_purchasing_plan10(self):
        ret = calculate_purchasing_plan(60, [(10,200), (15,10), (35,500), (50,30)])
        self.assertEqual(ret, [5, 30, 5, 10])

    def test_calculate_purchasing_plan11(self):
        ret = calculate_purchasing_plan(60, [(10,2), (15,100), (20,10), (35,500), (50,30)])
        self.assertEqual(ret, [30, 0, 10, 0, 10])


if __name__ == '__main__':
    unittest.main()


