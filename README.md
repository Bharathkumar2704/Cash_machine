# Cash_machine


## Time Complexity:

1. Loading coins: The load_coins method has a time complexity of O(1) since it directly updates the coin counts in the self.coins dictionary.
2. Exchanging coins: The exchange method has a time complexity of O(n), where n is the number of distinct coin denominations. It iterates through the coin values, performs a while loop to find the maximum number of coins that can be used, and updates the remaining amount. The number of iterations depends on the number of coin denominations.
3. Printing machine status: The print_machine_status method has a time complexity of O(m), where m is the number of non-zero coin and note counts. It iterates through the coin and note dictionaries to construct the formatted status string.

## OOPs Concepts Used:

1. Encapsulation: The CashMachine class encapsulates the data (coin and note counts) and related functionality (loading coins, exchanging amounts, and printing machine status) within the class.
2. Abstraction: The class provides high-level methods (load_coins, exchange, print_machine_status, process_commands) to interact with the cash machine, abstracting the underlying implementation details.
3. Static Method: The process_commands method is decorated with @staticmethod, indicating that it is a static method. It can be called on the class itself without requiring an instance of the class.

## Optimization:

1. The optimized version of the code mainly focuses on code readability and adherence to best practices.
2. Minor optimizations include caching the sorted coin values to avoid sorting repeatedly during the exchange process.
3. The print_machine_status method directly accesses the coin and note counts from their respective dictionaries instead of iterating over all items, reducing unnecessary iterations.

## Work Flow

### 1. Class: CashMachine

Description: This class represents a cash machine and contains methods to load coins, exchange amounts, and print the machine status.

### 2. Variables:

coins: A dictionary that stores the counts of different coin denominations. The keys are Decimal objects representing the coin values, and the values are integers representing the number of coins.
banknotes: A dictionary that stores the counts of different banknote denominations. The keys are integers representing the banknote values, and the values are integers representing the number of banknotes.

### 3. Methods:

1) __init__(self)

Description: The initialization method of the CashMachine class.
Functionality: Initializes the coins and banknotes dictionaries with default values (0 count for each denomination).

2) load_coins(self, number_of_coins, coin_type)

Description: Loads coins into the cash machine.
Parameters:
number_of_coins: An integer representing the number of coins to be loaded.
coin_type: The denomination of the coins as a Decimal object or integer.
Functionality: Increases the count of the specified coin type in the coins dictionary by the given number of coins.

3) exchange(self, amount)

Description: Exchanges an amount into the available coins.
Parameters:
amount: The amount to be exchanged as a Decimal object or integer.
Returns: A list of coins used for the exchange, or an empty list if the exchange is not possible.
Functionality: Iterates through the coin denominations in ascending order and tries to use the maximum number of coins to match the requested amount. Updates the coin counts in the coins dictionary accordingly.

4) print_machine_status(self, notes)

Description: Prints the current status of the coins and notes in the cash machine.
Parameters:
notes: A dictionary representing the counts of different banknote denominations.
Returns: A formatted string representing the machine status.
Functionality: Constructs formatted strings for the coin and note counts using list comprehensions and joins them into a single string.

5) process_commands(input_file)

Description: Processes commands from an input file and performs corresponding actions.
Parameters:
input_file: The path to the input file containing commands.
Functionality: Reads each line from the input file, identifies the command type ("LOAD" or "EXCHANGE"), and performs the appropriate action. Calls the relevant methods and prints the results.

### 4. Static Method:
The process_commands method is decorated with @staticmethod to indicate that it is a static method of the CashMachine class. It can be called on the class itself without requiring an instance of the class.

### 5. Main Execution:
The if __name__ == '__main__' block is responsible for executing the code when the script is run directly. It calls the process_commands method with the input file path ("input.txt").


## 4. Cloud:
To access the S3 service, the code initializes an S3 client and resource object using the boto3.client and boto3.resource methods, respectively. The script then demonstrates the download capability of S3 by using the S3 client's download_file method. It retrieves the file input.txt from the specified S3 bucket (cashmachine1) and saves it locally as input.txt.the script demonstrates the upload capability of S3 by utilizing the S3 resource's upload_file method. It uploads the generated output file (output.txt) to the same S3 bucket.
