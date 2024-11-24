
# Flight Planner System  

## Overview  
This project simulates a flight planning system that selects optimal itineraries based on various traveler needs. It efficiently plans routes between cities, considering constraints such as connection times and flight costs.

## Features  
The system offers three route optimization goals:  
1. **Fewest Flights & Earliest Arrival**  
2. **Cheapest Trip**  
3. **Fewest Flights & Cheapest**  

## Core Classes & Methods  
### `Flight` Class  
Represents flight data: start city, end city, departure/arrival times, and fare.

### `Planner` Class  
- **Constructor**:  
  ```python  
  def __init__(self, flights):  
      # Initializes with a list of Flight objects  
  ```  
- **Route-finding methods**:  
  - **`least_flights_earliest_route(self, start_city, end_city, t1, t2)`**  
  - **`cheapest_route(self, start_city, end_city, t1, t2)`**  
  - **`least_flights_cheapest_route(self, start_city, end_city, t1, t2)`**  

## Constraints  
- **Cities**: Represented as integers from 1 to *n*.  
- **Flights**: Up to 100 flights can arrive or depart from any city.  
- **Connecting Flights**: Minimum gap of 20 minutes between consecutive flights at a city.  
- **Time Complexity**:  
  - `__init__`: O(m)  
  - `least_flights_earliest_route`: O(m)  
  - `cheapest_route`: O(m log m)  
  - `least_flights_cheapest_route`: O(m log m)  
