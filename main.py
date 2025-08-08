# Oskar Bjerre Kristensen
# Computational Thinking with Python - Assignment 3

import numpy as np
import random
######### 
# Task 1
#########

### daily demand function
# Gets all the days from this function alone
def daily_demand(n):
    lambda_demand = 20  # Average daily demand (λ)
    demand = []
    for day in range(n):
        daily_units = np.random.poisson(lambda_demand)
        demand.append(daily_units)

    for days in range(len(demand)):
        print(f"Day {days + 1}: {demand[days]} units")

    return demand

def demand_analytics(demand):

    # Calculate statistics
    mean_demand = np.mean(demand)
    std_dev_demand = np.std(demand)
    fifth_percentile = np.percentile(demand, 5)
    ninety_fifth_percentile = np.percentile(demand, 95)
    
    # Print results
    print(f"Mean Daily Demand: {mean_demand}")
    print(f"Standard Deviation of Daily Demand: {std_dev_demand}")
    print(f"5th Percentile of Daily Demand: {fifth_percentile}")
    print(f"95th Percentile of Daily Demand: {ninety_fifth_percentile}")
    
    return demand

days = 30  # Number of days to simulate

# demand_analytics(daily_demand(days)) 
# Interpretation:
# Mean Daily Demand: 20.266666666666666
# Standard Deviation of Daily Demand: 4.545571715661543
# 5th Percentile of Daily Demand: 14.45
# 95th Percentile of Daily Demand: 28.549999999999997

# The mean daily demand is very close to the assumed demand of lambda = 20
# Standard deviation tells us that there is variablity of 4.5 in the daily demand
# On the 5th percentile we see that the worst days will only yield 14 units and on the opposite end
# we see that on the best days it is 28,5 units.


######### 
# Task 2
#########

def optimal_inventory_simulation(n_days, n_simulations, service_level):
    lambda_demand = 20  # Average daily demand (λ)
    
    # Store total monthly demand from each simulation
    monthly_demands = []
    
    for sim in range(n_simulations):
        # Set seed for reproducibility of this simulation
        np.random.seed(sim)
        
        # Generate demand for entire month and sum it up
        monthly_total = 0
        for day in range(n_days):
            daily_units = np.random.poisson(lambda_demand)
            monthly_total += daily_units
        
        # Store the total monthly demand for this simulation
        monthly_demands.append(monthly_total)
    
    # getting the mean monthly demand
    mean_monthly_demand = np.mean(monthly_demands)
    
    # Optimal inventory for 95% service level
    optimal_inventory = np.percentile(monthly_demands, service_level * 100)
    
    # Print results
    print(f"Average monthly demand: {mean_monthly_demand} units")
    print(f"Optimal inventory level (95% service): {optimal_inventory} units")


results = optimal_inventory_simulation(30, 1000, 0.95)


#######
# Task 3
#######
# User input for average daily demand
user_lambda = int(input("Enter the average daily demand (λ): "))

# Number of days
user_days = int(input("Enter the number of days to simulate: "))  # Number of days to simulate

# Number of simulations
user_simulations = int(input("Enter the number of simulations to run: "))  # Number of simulations

# Optimal service level
user_service_level = float(input("Enter the service level (as a decimal, e.g., 0.95 for 95%): "))  # Service level as a decimal





def optimal_inventory_simulation_2(n_days, n_simulations, service_level):
    lambda_demand = user_lambda  # Average daily demand (λ)
    
    # Store total monthly demand from each simulation
    monthly_demands = []
    
    for sim in range(n_simulations):
        # Set seed for reproducibility of this simulation
        np.random.seed(sim)
        
        # Generate demand for entire month and sum it up
        monthly_total = 0
        for day in range(n_days):
            daily_units = np.random.poisson(lambda_demand)
            monthly_total += daily_units
        
        # Store the total monthly demand for this simulation
        monthly_demands.append(monthly_total)
    
    # getting the mean monthly demand
    mean_monthly_demand = np.mean(monthly_demands)
    
    # Optimal inventory for 95% service level
    optimal_inventory = np.percentile(monthly_demands, service_level * 100)
    
    # Print results
    print(f"Average monthly demand: {mean_monthly_demand} units")
    print(f"Optimal inventory level ({service_level * 100}% service): {optimal_inventory} units")



results = optimal_inventory_simulation_2(user_days, user_simulations, user_service_level)


