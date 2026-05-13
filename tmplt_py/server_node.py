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

class ServerNode(Node):
    def __init__(self):
        super().__init__("server")
        self.get_logger().info("server has started...")
 
        # listen on the "/counter" topic
        self._server = self.create_service(AddTwoInts, SERVICE_NAME, self._add_two_ints_callback)
    
    def _add_two_ints_callback(self, request:AddTwoInts.Request, response:AddTwoInts.Response) -> AddTwoInts.Response:
        """ usually we name the server callback using the action it genrates
        """
        response.sum = request.a + request.b
        self.get_logger().info(f"{request.a} + {request.b} = {response.sum}")
        return response

    
def main(args=None):
    rclpy.init(args=args)
    node = ServerNode()
    rclpy.spin(node) # optional : required if we want the node to stay alive
    rclpy.shutdown()


if __name__ == "__main__":
    main()

    # Note : to test this code works:
    # > ros2 topic echo /counter