import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute
import time

class SnowmanDrawer(Node):
    def __init__(self):
        super().__init__('snowman_drawer')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.teleport_client = self.create_client(TeleportAbsolute, '/turtle1/teleport_absolute')
        while not self.teleport_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for teleport service...')
        time.sleep(1)
        self.draw_snowman()
    
    def teleport(self, x, y, theta=0.0):
        request = TeleportAbsolute.Request()
        request.x = x
        request.y = y
        request.theta = theta
        self.teleport_client.call_async(request)
        time.sleep(0.5)
    
    def draw_circle(self, radius):
        twist = Twist()
        twist.linear.x = 1.0
        twist.angular.z = 1.0
        start_time = self.get_clock().now().to_msg().sec
        while self.get_clock().now().to_msg().sec - start_time < 6:
            self.publisher.publish(twist)
            time.sleep(0.1)
        twist.linear.x = 0.0
        twist.angular.z = 0.0
        self.publisher.publish(twist)
        time.sleep(0.5)

    def draw_snowman(self):
        # Alsó kör
        self.teleport(5.5, 4.0)
        self.draw_circle(2.0)
        
        # Középső kör
        self.teleport(5.5, 6.5)
        self.draw_circle(1.5)
        
        # Fej
        self.teleport(5.5, 8.5)
        self.draw_circle(1.0)
        
        # Szemek
        self.teleport(5.2, 9.2)
        self.draw_circle(0.1)
        self.teleport(5.8, 9.2)
        self.draw_circle(0.1)
        
        # Orr
        self.teleport(5.5, 8.9)
        self.draw_circle(0.15)
        
        self.get_logger().info('Snowman drawn!')

def main(args=None):
    rclpy.init(args=args)
    node = SnowmanDrawer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
