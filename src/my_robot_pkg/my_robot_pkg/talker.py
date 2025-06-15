# src/picar_pkg/picar_pkg/talker.py

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TalkerNode(Node):
    """메시지를 주기적으로 발행하는 노드"""
    def __init__(self):
        super().__init__('minimal_talker')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # 0.5초
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        # ★★★ 의도된 실수: 테스트는 'Hello World'를 기대하지만, 'Wrong Message'를 보냅니다.
        msg.data = f'Wrong Message: {self.i}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    minimal_talker = TalkerNode()
    rclpy.spin(minimal_talker)
    minimal_talker.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
