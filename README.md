# ロボシス2020
ロボットシステム学　課題２

# 概要
NBAのワシントン・ウィザーズの選手を教えてくれるプログラム。知りたい選手の背番号を入力すると、その選手の名前が出力される。当てはまらない背番号を入力すると、該当する選手はいないという旨を出力する。

# 動作環境
Ubuntu18.04

# 使用方法
　1．roscoreを入力
```bash
$ roscore
```
　2．一方の画面で入力できるようにする。
```bash
$ rosrun mypkg nba.py
```
　3．もう一方の画面で出力できるようにする。
```bash
$rostopic echo /result
```
　4．入力画面で知りたい選手の背番号を入力する。
 
　5．出力画面にその選手の名前がでる。

# デモ動画
https://www.youtube.com/watch?v=8ZXcsZjTJNk&feature=youtu.be

# ライセンス
GNU General Public License v3.0
