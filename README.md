# TurtleBot3 Haritalama ve Otonom Navigasyon Projesi

Bu ödev kapsamında, TurtleBot3 robotuyla Gazebo ortamında haritalama yapılmış ve bu harita kullanılarak belirlenen noktalara otonom gidiş senaryosu uygulanmıştır. Proje, hazır haritanın yüklenmesi ve hedeflere gidişi sağlayan Python kodunun çalıştırılması olmak üzere iki ana kısımdan oluşmaktadır.

---

## Projenin Hazırlık Aşaması (Haritalama)

Aşağıdaki komutlar projenin temelini oluşturan haritayı (SLAM) çıkarmak için kullanılmıştır. Harita dosyaları klasörde mevcut olduğu için **bu kısmın tekrar çalıştırılmasına gerek yoktur.**

### Simülasyonun ve haritalamanın açılması:
```bash
roslaunch turtlebot3_gazebo turtlebot3_world.launch
roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping
```

### Robotun gezdirilip haritanın kaydedilmesi:
```bash
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
rosrun map_server map_saver -f cerezs_map
```

---

## Çalıştırma Talimatları

Projeyi çalıştırmak için indirilen klasörün içine girip terminali orada açın (Open in Terminal). Ardından 3 ayrı terminalde şu adımları izleyin:

### 1. Terminal: Simülasyon
```bash
roslaunch turtlebot3_gazebo turtlebot3_world.launch
```

### 2. Terminal: Navigasyon ve Harita
```bash
roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$(pwd)/cerezs_map.yaml
```
**UYARI:** RViz açılınca üstteki "2D Pose Estimate" butonuyla robotun haritadaki yerini el ile gösterip hizalama yapmayı unutmayın.

### 3. Terminal: Otonom Kodun Çalıştırılması
Hizalama bittikten sonra robotu harekete geçirmek için şu komutu girin:
```bash
python3 cerezs_bot.py
```
