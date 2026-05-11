import rclpy
from rclpy.node import Node

class BasicNode(Node):
    def __init__(self):
        super().__init__("basic")
        self.get_logger().info("Hello World")
        # ROS timer functionality : “Execute this function  every X seconds”
        self.create_timer(1, self.print_callback)

        self.counter = 0
    
    def print_callback(self) -> None:
        self.get_logger().info(f"{self.counter=}")
        self.counter +=1
        
    
def main(args=None):
    rclpy.init(args=args)
    node = BasicNode()
    rclpy.spin(node) # optional : required if we want the node to stay alive 
    rclpy.shutdown()


if __name__ == "__main__":
    main()