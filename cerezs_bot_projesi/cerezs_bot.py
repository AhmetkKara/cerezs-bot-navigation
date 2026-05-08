#!/usr/bin/env python3
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def hedefe_git(x, y, w=1.0):
    # Move_base (Navigasyon) sunucusuna bağlanıyoruz
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()

    # Hedef noktası için ayarları yapıyoruz
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    
    # Koordinatları atıyoruz
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.orientation.w = w # Yönelim

    rospy.loginfo(f"Cerezs Bot hedefe ilerliyor -> X: {x}, Y: {y}")
    client.send_goal(goal)
    
    # Robotun hedefe varmasını bekliyoruz
    client.wait_for_result()
    return client.get_result()

if __name__ == '__main__':
    try:
        # ROS Düğümünü başlatıyoruz
        rospy.init_node('cerezs_bot_node')
        
        # Format: (X_değeri, Y_değeri)
        hedefler = [
            (1.74,-0.0161),   # 1. Hedef: 2. direğin üstü
            (-0.0265,1.91),  # 2. Hedef: 4. direğin solu
            (-1.84,0.453), # 3. Hedef: 7 ve 8. direğin alt/ara kısmı
            (-0.0173,-2.01),   # 4. Hedef: 6. direğin sağı
            (0.544,0.481)   # 5. Hedef: 1, 2, 4, 5 direklerinin orta noktası
        ]

        # Listedeki her bir hedef için döngü başlatıyoruz
        for i, (x, y) in enumerate(hedefler):
            rospy.loginfo(f"--- Cerezs Bot Hedef {i+1}'e Gidiyor ---")
            hedefe_git(x, y)
            rospy.loginfo(f"--- Hedef {i+1} Tamamlandı! ---")
            
            # Bir sonraki hedefe geçmeden önce 2 saniye dinlen
            rospy.sleep(2) 
        
        rospy.loginfo("TEBRİKLER! Cerezs Bot tüm hedeflere başarıyla ulaştı ve görevi bitirdi.")
        
    except rospy.ROSInterruptException:
        rospy.loginfo("Görev kullanıcı tarafından iptal edildi.")
