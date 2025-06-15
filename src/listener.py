# src/picar_pkg/picar_pkg/listener.py

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ListenerNode(Node):
    """토픽을 구독하여 메시지를 로깅하는 노드"""
    def __init__(self):
        super().__init__('minimal_listener')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        # ★★★ 의도된 실수 1: Pylint가 싫어하는 매우 긴 한 줄의 코드
        self.get_logger().info('I heard an incredibly important and detailed message from the talker node, and the content of that message is exactly as follows: "%s"' % msg.data)
        
        # ★★★ 의도된 실수 2: Pylint가 싫어하는 대문자 변수명 (상수가 아닌데)
        MY_VARIABLE = 10
        self.get_logger().info(f'Just a test variable: {MY_VARIABLE}')


def main(args=None):
    rclpy.init(args=args)
    minimal_listener = ListenerNode()
    rclpy.spin(minimal_listener)
    minimal_listener.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
