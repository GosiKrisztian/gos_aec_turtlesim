import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math
import time

class ViolinKeyDrawer(Node):
    def __init__(self):
        super().__init__('violinkulcs_rajzolo')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        time.sleep(1)  # Publisher aktiválására vár
        self.draw_violin_key()

    def draw_violin_key(self):
        # Twist üzenet létrehozása MINDEN mezővel
        vel_msg = Twist()
        vel_msg.linear.x = 0.0  # Explicit float
        vel_msg.linear.y = 0.0
        vel_msg.linear.z = 0.0
        vel_msg.angular.x = 0.0
        vel_msg.angular.y = 0.0
        vel_msg.angular.z = 0.0  # Alapértelmezett float

        # Példa: Violinkulcs spiráljának rajzolása
        for _ in range(2):
            # Előrehaladás
            vel_msg.linear.x = 2.0  # Sebesség
            vel_msg.angular.z = 0.0
            self.publisher.publish(vel_msg)
            time.sleep(1.0)
            
            # Fordulás balra (90 fok)
            vel_msg.linear.x = 0.0
            vel_msg.angular.z = math.pi / 2  # 1.5708 rad = 90°
            self.publisher.publish(vel_msg)
            time.sleep(1.0)

def main(args=None):
    rclpy.init(args=args)
    node = ViolinKeyDrawer()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
