import boto3
from decimal import Decimal

s3_client = boto3.client(
    's3',
    aws_access_key_id='AKIA2X4ZQCXUJWN3YW5',
    aws_secret_access_key='LsyHqaP4leF3H5J9C+AbX8v3OgtdzSMsOXlycPr',
    region_name='eu-west-2'
)

s3_resource = boto3.resource(
    's3',
    aws_access_key_id='AKIA2X4ZQCXUJWN3YW5',
    aws_secret_access_key='LsyHqaP4leF3H5J9C+AbX8v3OgtdzSMsOXlycPr',
    region_name='eu-west-2'
)

bucket_name = 'cashmachine1'
file_path = 'input.txt'
object_name = 'input.txt'
local_file_path = 'input.txt'

s3_client.download_file(bucket_name, object_name, local_file_path)

class CashMachine:
    def __init__(self):
        self.coins = {Decimal("0.2"): 0, Decimal("0.5"): 0, 1: 0, 2: 0}
        self.banknotes = {5: 0, 10: 0, 20: 0}

    def load_coins(self, number_of_coins, coin_type):
        if coin_type in self.coins:
            self.coins[coin_type] += number_of_coins

    def exchange(self, amount):
        coins_to_use = []
        remaining_amount = amount
        coin_values = sorted(self.coins.keys())
        for coin_value in coin_values:
            coin_count = self.coins[coin_value]
            while coin_count > 0 and remaining_amount >= coin_value:
                coins_to_use.append(coin_value)
                remaining_amount -= coin_value
                coin_count -= 1
        if remaining_amount == 0:
            for coin in coins_to_use:
                self.coins[coin] -= 1
            return coins_to_use
        else:
            return []

    def print_machine_status(self, notes):
        coin_counts = [f"{self.coins[coin]} {coin}£" for coin in self.coins if self.coins[coin] > 0]
        formatted_notes = [f"{notes[note]} {note}£" for note in notes if notes[note] > 0]
        return ', '.join(coin_counts + formatted_notes)

    @staticmethod
    def process_commands(input_file, output_file):
        cash_machine = CashMachine()
        notes = {5: 0, 10: 0, 20: 0}
        output_lines = []
        with open(input_file, 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith("LOAD"):
                    _, number_of_items, item_type = line.split()
                    number_of_items = int(number_of_items)
                    item_type = Decimal(item_type)
                    cash_machine.load_coins(number_of_items, item_type)
                    result = cash_machine.print_machine_status(notes)
                    print(f"> {line}\n= {result}")
                    output_lines.append(f"> {line}\n= {result}")
                elif line.startswith("EXCHANGE"):
                    _, amount = line.split()
                    amount = Decimal(amount)
                    coins_used = cash_machine.exchange(amount)
                    if coins_used:
                        coin_counts = [f"{coins_used.count(coin)} {coin}£" for coin in set(coins_used)]
                        output_lines.append(f"> {line}\n< {', '.join(coin_counts)}")
                        print(f"> {line}\n< {', '.join(coin_counts)}")
                        if amount in notes:
                            notes[amount] += 1
                    else:
                        print(f"> {line}\n< CANNOT EXCHANGE")
                        output_lines.append(f"> {line}\n< CANNOT EXCHANGE")
                    result = cash_machine.print_machine_status(notes)
                    output_lines.append(f"= {result}")

        with open(output_file, 'w') as file:
            print(f"= {result}")
            file.write('\n'.join(output_lines))


if __name__ == '__main__':
    CashMachine.process_commands("input.txt", "output.txt")
    
file_path = 'output.txt'
object_name = 'output.txt'
    
s3_resource.meta.client.upload_file(file_path, bucket_name, object_name)

