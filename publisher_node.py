import rclpy
from rclpy.node import Node

# message type used in this example.
# Custom message types can also be used
# to know all available interfaces:
# > ros2 interface list
# To know what contains a messages of type 'String'
# > ros2 interface show example_interfaces/msg/String
from example_interfaces.msg import String 

class PublisherNode(Node):
    def __init__(self):
        super().__init__("publisher")
        self.get_logger().info("publisher has started...")
        # ROS timer functionality : “Execute this function every X seconds”
        self.create_timer(1, self.counter_callback)

        self._counter = 0
        # publish on the "/counter" topic
        self._publisher = self.create_publisher(String, "counter", 10)
    
    def counter_callback(self) -> None:
        """ usually we name the publisher callback using the topic name from which it 
            processes data
        """
        msg = String()
        msg.data = f"{self._counter=}"
        self._publisher.publish(msg)
        self._counter +=1
        
    
def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode()
    rclpy.spin(node) # optional : required if we want the node to stay alive
    rclpy.shutdown()


if __name__ == "__main__":
    main()

    # Note : to test this code works:
    # > ros2 topic echo /counter