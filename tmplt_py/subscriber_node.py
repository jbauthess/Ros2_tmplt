import rclpy
from rclpy.node import Node

# message type used in this example.
# Custom message types can also be used
# to know all available interfaces:
# > ros2 interface list
# To know what contains a messages of type 'String'
# > ros2 interface show example_interfaces/msg/String
from example_interfaces.msg import String 

TOPIC_NAME = "counter"

class SubscriberNode(Node):
    def __init__(self):
        super().__init__("subscriber")
        self.get_logger().info("subscriber has started...")
 
        # listen on the "/counter" topic
        self._subscriber = self.create_subscription(String, TOPIC_NAME, self.counter_callback, 10)
    
    def counter_callback(self, msg:String) -> None:
        """ usually we name the subscriber callback using the topic name from which it 
            processes data
        """
        self.get_logger().info(msg.data)

    
def main(args=None):
    rclpy.init(args=args)
    node = SubscriberNode()
    rclpy.spin(node) # optional : required if we want the node to stay alive
    rclpy.shutdown()


if __name__ == "__main__":
    main()

    # Note : to test this code works:
    # > ros2 topic echo /counter