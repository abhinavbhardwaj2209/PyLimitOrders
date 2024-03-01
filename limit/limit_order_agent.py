from trading_framework.execution_client import ExecutionClient
from trading_framework.price_listener import PriceListener
import sys
import os

# Get the directory path containing the module file
# module_dir = "/Users/abhinavbhardwaj/Desktop/Project/PyLimitOrders"
# Add the directory to the Python path
# sys.path.append(module_dir)

class LimitOrderAgent(PriceListener):

    # def __init__(self, execution_client: ExecutionClient) -> None:
    #     super().__init__()
    #     self.execution_client = execution_client
    #     self.orders = []

    # def on_price_tick(self, product_id: str, price: float):
    #     # Implement logic to check if the price is below $100 and execute buy order
    #     if product_id == 'IBM' and price < 100:
    #         self.add_order(True, 'IBM', 1000, 100)

    #     # Check if any held orders can be executed
    #     self.execute_orders(product_id, price)

    # def add_order(self, is_buy: bool, product_id: str, amount: int, limit_price: float):
    #     order = {'is_buy': is_buy, 'product_id': product_id, 'amount': amount, 'limit_price': limit_price}
    #     self.orders.append(order)

    # def execute_orders(self, product_id: str, current_price: float):
    #     executed_orders = []
    #     for order in self.orders:
    #         if order['product_id'] == product_id and current_price >= order['limit_price']:
    #             try:
    #                 if order['is_buy']:
    #                     self.execution_client.buy(order['product_id'], order['amount'])
    #                 else:
    #                     self.execution_client.sell(order['product_id'], order['amount'])
    #                 executed_orders.append(order)
    #             except Exception as e:
    #                 print(f"Failed to execute order: {e}")

    #     # Remove executed orders
    #     for executed_order in executed_orders:
    #         self.orders.remove(executed_order)


    def __init__(self, execution_client: ExecutionClient):
        self.execution_client = execution_client
        self.orders = []

    def price_tick(self, product_id, price):
        for order in self.orders:
            if order['product_id'] == product_id:
                try:
                    if order['type'] == 'buy' and price <= order['limit']:
                        self.execution_client.buy(product_id, order['amount'])
                        self.orders.remove(order)
                    elif order['type'] == 'sell' and price >= order['limit']:
                        self.execution_client.sell(product_id, order['amount'])
                        self.orders.remove(order)
                except Exception as e:
                    print(f"Failed to execute order: {e}")

    def add_order(self, order_type, product_id, amount, limit):
        self.orders.append({
            'type': order_type,
            'product_id': product_id,
            'amount': amount,
            'limit': limit
        })
