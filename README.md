# TurtleBot3 Haritalama ve Otonom Navigasyon Projesi

Bu proje, TurtleBot3 robotunun simülasyon ortamında haritasının çıkarılması ve ardından bu harita üzerinde belirlenen noktalara otonom olarak gitmesi üzerine kurgulanmıştır.

---

## Projeyi Hazırlarken Uygulanan Adımlar (Haritalama Aşaması)

Bu bölüm, projenin altyapısını oluşturmak için benim tarafımdan gerçekleştirilen SLAM adımlarını içerir. Sistemin çalışması için bu adımların tekrar edilmesine gerek yoktur.

### 1. Simülasyon ve SLAM Dünyası
Öncelikle Gazebo dünyası ve haritalama (SLAM) düğümü başlatılmıştır:

```bash
roslaunch turtlebot3_gazebo turtlebot3_world.launch
roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping
```

### 2. Manuel Haritalama
Klavye kontrolü (teleop) kullanılarak robot simülasyon içerisinde gezdirilmiş ve çevre haritası oluşturulmuştur:

```bash
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
```

### 3. Haritanın Kaydedilmesi
Oluşturulan harita, navigasyon aşamasında kullanılmak üzere kaydedilmiştir:

```bash
rosrun map_server map_saver -f cerezs_map
```

---

## Proje Çalıştırma Adımları

Projeyi test etmek için indirilen klasörün içerisine girin, boş bir alana sağ tıklayarak **"Terminalde Aç" (Open in Terminal)** deyin ve aşağıdaki adımları sırayla 3 farklı terminalde uygulayın.

### ADIM 1: Simülasyonun Başlatılması (1. Terminal)
Gazebo simülasyon ortamını başlatmak için:

```bash
roslaunch turtlebot3_gazebo turtlebot3_world.launch
```

### ADIM 2: Navigasyon ve Hazır Haritanın Yüklenmesi (2. Terminal)
Kayıtlı haritayı yüklemek ve RViz arayüzünü açmak için yeni bir terminalde şunu çalıştırın:

```bash
roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$(pwd)/cerezs_map.yaml
```

**ÖNEMLİ UYARI:** RViz açıldıktan sonra üst menüde bulunan **"2D Pose Estimate"** butonuna tıklayın. Robotun haritadaki gerçek konumunu ve yönünü farenizle işaretleyerek lazerlerin (yeşil noktalar) siyah duvar çizgilerine tam oturmasını sağlayın.

### ADIM 3: Otonom Görevin Başlatılması (3. Terminal)
Hizalama işlemi tamamlandıktan sonra robotu hedeflere göndermek için son terminalde python kodunu çalıştırın:

```bash
python3 cerezs_bot.py
```
