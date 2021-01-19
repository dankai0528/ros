#!/usr/bin/env python
## coding: UTF-8
import rospy
from std_msgs.msg import String

def ROC():
    rospy.init_node('nba')
    pub = rospy.Publisher('result', String, queue_size=10)
    rate = rospy.Rate(5)
    while not rospy.is_shutdown():
        print("知りたいウィザーズの選手の背番号は？")

        key = input()
        if key == '3':
            name = 'Bradley Beal'
        elif key == '4':
            name = 'Russell Westbrook'
        elif key == '5':
            name = 'Cassius Winston'
        elif key == '6':
            name = 'Troy Brown Jr.'
        elif key == '8':
            name = 'Rui Hachimura'
        elif key == '9':
            name = 'Deni Avdija'
        elif key == '12':
            name = 'Jerome Robinson'
        elif key == '13':
            name = 'Thomas Bryant'
        elif key == '14':
            name = 'Ish Smith'
        elif key == '15':
            name = 'Robin Lopez'
        elif key == '16':
            name = 'Anthony Gill'
        elif key == '17':
            name = 'Isaac Bonga'
        elif key == '19':
            name = 'Raul Neto'
        elif key == '21':
            name = 'Moritz Wagner'
        elif key == '24':
            name = 'Garrison Mathews'
        elif key == '42':
            name = 'Davis Bertans'
        else:
            print("その背番号の選手はいません。")
            name = 'x'
        pub.publish(name)
        rate.sleep()

    if __name__ == '__main__':
        try:
            ROC()
        except rospy.ROSInterruptException: pass
