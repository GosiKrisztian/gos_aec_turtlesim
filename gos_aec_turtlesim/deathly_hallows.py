import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math
import time

class DeathlyHallowsDrawer(Node):
    def __init__(self):
        super().__init__('deathly_hallows_drawer')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        time.sleep(2)  

    def move_turtle(self, linear, angular, duration):
        twist = Twist()
        twist.linear.x = linear
        twist.angular.z = angular
        start_time = time.time()
        while time.time() - start_time < duration:
            self.publisher_.publish(twist)
            time.sleep(0.1)
        twist.linear.x = 0.0
        twist.angular.z = 0.0
        self.publisher_.publish(twist)

    def turn_turtle(self, angle):
        twist = Twist()
        twist.angular.z = 1.0 if angle > 0 else -1.0  
        target_time = abs(angle) / 1.0  
        start_time = time.time()

        while time.time() - start_time < target_time:
            self.publisher_.publish(twist)
            time.sleep(0.1)

        

    def draw_circle(self, radius, speed=1.0):
        circumference = 2 * math.pi * radius
        duration = circumference / speed
        self.move_turtle(speed, speed / radius, duration)

    def draw_triangle(self, side_length):
        for _ in range(3):
            self.move_turtle(2.0, 0.0, side_length / 2.0)
            self.turn_turtle(math.pi * 2 / 3)
    
    def draw_vertical_line(self, length):
        self.turn_turtle(85 * math.pi / 180)  
        self.move_turtle(1.732, 0.0, length / 2.0)
    
    def draw_deathly_hallows(self):
        side_length = 4.0  
        radius = side_length / math.sqrt(3) / 2  
        
        
        self.draw_triangle(side_length)
        
        
        self.move_turtle(1.610, 0.0, radius)  
        self.draw_circle(radius, speed=1.5)
        
        
        self.draw_vertical_line(side_length)
        
    def run(self):
        self.draw_deathly_hallows()
        self.get_logger().info("Halál ereklyéi szimbólum kész!")


def main(args=None):
    rclpy.init(args=args)
    drawer = DeathlyHallowsDrawer()
    drawer.run()
    drawer.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

