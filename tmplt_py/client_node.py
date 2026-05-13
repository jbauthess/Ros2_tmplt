from functools import partial

import rclpy
from rclpy.node import Node

# message type used in this example.
# Custom message types can also be used
# to know all available interfaces:
# > ros2 interface list
# To know what contains a messages of type 'AddTwoInts'
# > ros2 interface show example_interfaces/srv/AddTwoInts
from example_interfaces.srv import AddTwoInts 

SERVICE_NAME = "add_two_ints"

class ClientNode(Node):
    def __init__(self):
        super().__init__("client")
        self.get_logger().info("client has started...")
 
        # listen on the "/counter" topic
        self._client = self.create_client(AddTwoInts, SERVICE_NAME)


    
    def call_add_two_ints(self, a:int, b:int) -> None:
        """ usually we name the client to server callback using the action it genrates
        """
        # wait for service used to be up and running
        while not self._client.wait_for_service(1.0):
            self.get_logger().warn(f"Waiting for service '{SERVICE_NAME}'")

        # create the request as expected by the server
        request = AddTwoInts.Request()
        request.a = a
        request.b = b
        # send the request to the server
        future = self._client.call_async(request)  # asynchroneous call here. For synchroneous call, use 'call()' instead

        # register a callback to process the server response
        # add_done_callback() taking only one argument, the function object
        # we can use 'partial' to pass additional arguments 
        future.add_done_callback(partial(self.add_two_ints_callback, request = request))

    
    def add_two_ints_callback(self, future:rclpy.Future, request:AddTwoInts.Request) -> None:
        response:AddTwoInts.Response = future.result()
        self.get_logger().info(f"{request.a} + {request.b} = {response.sum}")


    
def main(args=None):
    rclpy.init(args=args)
    node = ClientNode()
    node.call_add_two_ints(3, 8)
    rclpy.spin(node)

    # Non oop version
    # ---------------
    # node = rclpy.Node("name")
    # client = node.create_client(AddTwoInts, SERVICE_NAME)

    ## wait for the server to be up
    # while client.wait_for_service(1.0):
    #     node.get_logger().warn(f"Waiting for service '{SERVICE_NAME}'")

    ## create request
    # request = AddTwoInts.Request()
    # request.a = 3
    # request.b = 4

    ## send request
    # future = self._client.call_async(request)  # asynchroneous call here. For synchroneous call, use 'call()' instead

    ## required if we want the node to stay alive for a non oop version
    # rclpy.spin_until_future_complete(node, future) 
    ## log server response
    # node.get_logger().info(f"sum = {future.result()}")

        
    rclpy.shutdown()


if __name__ == "__main__":
    main()

    # Note : to test this code works:
    # > ros2 topic echo /counter