from flight import Flight

'''
Python Code to implement a heap with general comparison function
'''
# class PriorityQueueBase:
#     # ”””Abstractbaseclassforapriorityqueue.”””
#     class Item:
#     # ”””Lightweightcompositetostorepriorityqueueitems.”””
#         __slots__ = '_key' , '_value'

#         def __init__(self,k,v):
#             self._key = k
#             self._value=v

#         def __lt__ (self,other):
#             return self._key<other._key #compare itemsbasedontheirkeys

#     def is_empty(self): #concretemethodassumingabstract len
#     # ”””ReturnTrueifthepriorityqueueisempty.”””
#         return len(self)==0

class Heap():
    '''
    Class to implement a heap with general comparison function

    '''
    def __len__(self):
        return len(self.arr)

    def is_empty(self):
        return len(self) == 0
   
    def _parent(self, j):
        return (j-1)//2

    def _left(self, j):
        return 2*j+1

    def _right(self, j):
        return 2*j+2
    
    def _has_left(self, j):
        return self._left(j)<len(self.arr) #indexbeyondendof list?
 
    def _has_right(self, j):
        return self._right(j)<len(self.arr) #indexbeyondendof list?

    def _swap(self, i, j):
    #Swap the elements at indices i and j of array
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j>0 and self.comparator(self.arr[j],self.arr[parent]):
            self._swap(j,parent)
            self._upheap(parent) #recuratpositionofparent

    def _downheap(self, j):
        if self._has_left(j):
            left=self._left(j)
            small_child=left #althoughrightmaybesmaller
            if self._has_right(j):
                right=self._right(j)
                if self.comparator(self.arr[right],self.arr[left]):
                    small_child=right
            if self.comparator(self.arr[small_child],self.arr[j]):
                self._swap(j, small_child)
                self._downheap(small_child)
    
    def __init__(self, comparison_function, init_array):
        '''
        Arguments:
            comparison_function : function : A function that takes in two arguments and returns a boolean value
            init_array : List[Any] : The initial array to be inserted into the heap
        Returns:
            None
        Description:
            Initializes a heap with a comparison function
            Details of Comparison Function:
                The comparison function should take in two arguments and return a boolean value
                If the comparison function returns True, it means that the first argument is to be considered smaller than the second argument
                If the comparison function returns False, it means that the first argument is to be considered greater than or equal to the second argument
        Time Complexity:
            O(n) where n is the number of elements in init_array
        '''
        
        # Write your code here
        self.arr = []
        self.comparator = comparison_function
        self.size = 0
        for x in init_array:
            self.insert(x)
        pass
        
    def insert(self,value):
        '''
        Arguments:
            value : Any : The value to be inserted into the heap
        Returns:
            None
        Description:
            Inserts a value into the heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here
        self.size +=1
        self.arr.append(value)
        self._upheap(len(self.arr)-1)
        pass
    
    def extract(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value extracted from the top of heap
        Description:
            Extracts the value from the top of heap, i.e. removes it from heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here
        if self.size == 0:
            return None
            
        item = self.arr[0] #andremove itfromthelist;
        self._swap(0, len(self.arr)-1) #putminimumitemattheend
        self.arr.pop()
        self.size -= 1
        self._downheap(0) #thenfixnewroot
        return item
    
    def top(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value at the top of heap
        Description:
            Returns the value at the top of heap
        Time Complexity:
            O(1)
        '''
        
        # Write your code here
        if self.size == 0:
            return None
        else :
            return self.arr[0]
        
class Queue:
    """A simple Queue implementation using a list."""
    def __init__(self):
        self.items = []
    
    def append(self, item):
        """Add item to end of queue."""
        self.items.append(item)
    
    def popleft(self):
        """Remove and return item from front of queue."""
        if not self.items:
            return None
        return self.items.pop(0)
    
    def __bool__(self):
        """Return True if queue has items."""
        return bool(self.items)

class Planner:
    def __init__(self, flights):
        """The Planner

        Args:
            flights (List[Flight]): A list of information of all the flights (objects of class Flight)
        """
        self.no_of_city = 0
        
        # Determine the number of cities
        for flight in flights:
            self.no_of_city = max(self.no_of_city, flight.start_city, flight.end_city)
        
        # Create adjacency list for graph representation 
        self.city = [[] for _ in range(self.no_of_city + 1)]
        for flight in flights:
            self.city[flight.start_city].append(flight)

    def _reconstruct_path(self, parent, end_flight):
        """Helper method to reconstruct path from parent references"""
        path = []
        current = end_flight
        while current is not None:
            path.append(current)
            current = parent.get(current)
        return path[::-1]  # Reverse to get correct order

    def least_flights_earliest_route(self, start_city, end_city, t1, t2):
        queue = Queue()
        queue.append((start_city, t1-20, 0, None))  # city, arrival_time, flight_count, last_flight
        best_arrival = {start_city: (0, 0, None)}  # city: (arrival_time, flight_count, last_flight)
        parent = {}  # Flight -> previous Flight mapping
        temp_count = float('inf')
        ans_flight = None
        
        while queue:
            current_city, arrival_time, flight_count, last_flight = queue.popleft()

            if current_city == end_city and last_flight and best_arrival[end_city][2] and best_arrival[end_city][2].arrival_time <= t2:
                if temp_count > flight_count:
                    ans_flight = last_flight
                    temp_count = flight_count
                elif temp_count == flight_count:
                    if ans_flight is None or ans_flight.arrival_time >= arrival_time:
                        ans_flight = last_flight

                continue

            for flight in self.city[current_city]:
                if flight.departure_time >= t1 and flight.arrival_time <= t2 and flight.departure_time >= arrival_time + 20:
                    new_arrival_time = flight.arrival_time
                    new_flight_count = flight_count + 1

                    if (flight.end_city not in best_arrival or
                        (new_arrival_time < best_arrival[flight.end_city][0] or
                        (new_arrival_time == best_arrival[flight.end_city][0] and new_flight_count < best_arrival[flight.end_city][1]))):
                        best_arrival[flight.end_city] = (new_arrival_time, new_flight_count, flight)
                        parent[flight] = last_flight
                        queue.append((flight.end_city, new_arrival_time, new_flight_count, flight))

        if ans_flight:
            return self._reconstruct_path(parent, ans_flight)
        return []

    def cheapest_route(self, start_city, end_city, t1, t2):
        def compare_cost(a, b):
            return a[0] < b[0]  # Compare based on total_cost

        pq = Heap(compare_cost, [])
        pq.insert((0, start_city, t1-20, None))  # (cost, city, arrival_time, last_flight)
        
        best_cost = {city: float('inf') for city in range(0, self.no_of_city + 3)}
        best_cost[start_city] = 0
        parent = {}  # Flight -> previous Flight mapping
        temp_cost = 1e10
        ans_flight = None

        while not pq.is_empty():
            total_cost, current_city, arrival_time, last_flight = pq.extract()

            if current_city == end_city and arrival_time <= t2:
                if temp_cost > total_cost:
                    ans_flight = last_flight
                    temp_cost = total_cost
                continue

            for flight in self.city[current_city]:
                if flight.departure_time >= t1 and flight.arrival_time <= t2 and flight.departure_time >= arrival_time + 20:
                    new_cost = total_cost + flight.fare
                    new_arrival_time = flight.arrival_time

                    if new_cost < best_cost[flight.end_city]:
                        best_cost[flight.end_city] = new_cost
                        parent[flight] = last_flight
                        pq.insert((new_cost, flight.end_city, new_arrival_time, flight))

        if ans_flight:
            return self._reconstruct_path(parent, ans_flight)
        return []

    def least_flights_cheapest_route(self, start_city, end_city, t1, t2):
        def compare_flights_cost(a, b):
            if a[0] != b[0]:  # First compare flight count
                return a[0] < b[0]
            return a[1] < b[1]  # If flight counts are equal, compare cost

        pq = Heap(compare_flights_cost, [])
        pq.insert((0, 0, start_city, None))  # (flight_count, cost, city, last_flight)
        
        best_state = {start_city: (0, 0, None)}  # city: (cost_so_far, flight_count, last_flight)
        parent = {}  # Flight -> previous Flight mapping
        
        while not pq.is_empty():
            flight_count, total_cost, current_city, last_flight = pq.extract()

            if current_city == end_city and last_flight and last_flight.arrival_time <= t2:
                return self._reconstruct_path(parent, last_flight)

            for flight in self.city[current_city]:
                if flight.departure_time >= t1 and flight.arrival_time <= t2 and (last_flight is None or flight.departure_time >= last_flight.arrival_time + 20):
                    new_cost = total_cost + flight.fare
                    new_flight_count = flight_count + 1

                    if (flight.end_city not in best_state or 
                        new_flight_count < best_state[flight.end_city][1] or 
                        (new_flight_count == best_state[flight.end_city][1] and new_cost < best_state[flight.end_city][0])):
                        best_state[flight.end_city] = (new_cost, new_flight_count, flight)
                        parent[flight] = last_flight
                        pq.insert((new_flight_count, new_cost, flight.end_city, flight))

        return []