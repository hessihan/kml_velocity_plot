# NMEA to KML: Velocity Visualization
Plot velocity as height of path in kml from nmea data

## 目的
GPS nmea ファイル (緯度, 経度, 速度)をデータクリーニング。
KMLを用いてGoogle Earth上に3Dプロット(x=緯度, y=経度, z=速度)。
* 最終目標: nmeaファイル内のデータを用いて3Dプロットするkmlファイルを作ること。(kmlファイルはダブルクリックすればGoogle Earthに飛ぶ。)

## Descriptions
kml  
https://developers.google.com/kml/documentation/kml_tut  
nmea  
http://aprs.gids.nl/nmea/  


## デザイン
* nmea --> csv (python pandas)

* csv --> some 3d plots in kml with Path (and Polygons?)