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
* nmea --> csv (all rows)

* csv: extract some seesential row ($GNGSA ?) and clean

* csv (cleaned) -->kml with Extruded Path: LineString (and Polygons?) (Opaque blue walls with white outline, values showed on plot)

* 最終的には、LineString の plot ではなくて、各地点で直方体のbinを作る(ヒストグラム的な)