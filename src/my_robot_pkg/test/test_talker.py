# src/picar_pkg/test/test_talker.py

import unittest
import rclpy
from std_msgs.msg import String
from picar_pkg.talker import TalkerNode # talker.py에서 TalkerNode를 가져옵니다.

class TestTalkerNode(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        rclpy.init()

    @classmethod
def tearDownClass(cls):
        rclpy.shutdown()

    def test_published_message_content(self):
        """발행된 메시지의 내용이 'Hello World'로 시작하는지 테스트합니다."""
        talker_node = TalkerNode()
        
        # 테스트를 위한 임시 구독자 생성
        received_msgs = []
        def sub_callback(msg):
            received_msgs.append(msg)

        test_subscriber = talker_node.create_subscription(String, 'topic', sub_callback, 1)
        
        # 잠시 노드를 실행하여 메시지가 발행되도록 함
        rclpy.spin_once(talker_node, timeout_sec=1.0)

        # 노드 정리
        talker_node.destroy_node()

        # 받은 메시지가 있는지, 그리고 내용이 올바른지 확인
        self.assertGreater(len(received_msgs), 0, "메시지를 받지 못했습니다.")
        
        # ★★★ 이 부분이 '테스트의 핵심'입니다.
        # 'Hello World'로 시작하는지 검사하지만, talker.py는 'Wrong Message'를 보내므로 실패할 것입니다.
        self.assertTrue(
            received_msgs[0].data.startswith('Hello World'),
            f"예상치 못한 메시지 수신: {received_msgs[0].data}"
        )
