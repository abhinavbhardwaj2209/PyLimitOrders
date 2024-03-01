# import sys
# import os

# # Get the directory path containing the module file
# module_dir = "/Users/abhinavbhardwaj/Desktop/Project/PyLimitOrders"
# sys.path.append(module_dir)


import unittest
from limit.limit_order_agent import LimitOrderAgent
from unittest.mock import MagicMock


class TestLimitOrderAgent(unittest.TestCase):
    def setUp(self):
        # Create a mock execution client
        self.execution_client = MagicMock()
        # Initialize the LimitOrderAgent with the mock execution client
        self.agent = LimitOrderAgent(self.execution_client)

    def test_buy_order_execution(self):
        # Test buying 1000 shares of IBM when price drops below $100
        self.agent.price_tick('IBM', 99)
        self.execution_client.buy('IBM', 1000)
        # print("\n test case test_buy_order_execution pass successfully")

    def test_sell_order_execution(self):
        # Test executing sell order for IBM
        self.agent.add_order('sell', 'IBM', 500, 120)
        self.agent.price_tick('IBM', 120)
        self.execution_client.sell('IBM', 500)

    def test_add_order(self):
        # Test adding buy order for Apple
        self.agent.add_order('buy', 'AAPL', 200, 150)
        self.assertEqual(len(self.agent.orders), 1)
        self.assertEqual(self.agent.orders[0]['type'], 'buy')
        self.assertEqual(self.agent.orders[0]['product_id'], 'AAPL')
        self.assertEqual(self.agent.orders[0]['amount'], 200)
        self.assertEqual(self.agent.orders[0]['limit'], 150)

    # def test_limit_order_agent(self):
    #     execution_client = MagicMock()
    #     limit_order_agent = LimitOrderAgent(execution_client)

    #     # Simulate price ticks to trigger buy order
    #     limit_order_agent.on_price_tick('IBM', 99)
    #     self.assertEqual(len(limit_order_agent.orders), 1)

    #     # Simulate price ticks to trigger order execution
    #     limit_order_agent.on_price_tick('IBM', 101)
    #     execution_client.buy.assert_called_once_with('IBM', 1000)
    #     self.assertEqual(len(limit_order_agent.orders), 0)

if __name__ == '__main__':
    unittest.main()



