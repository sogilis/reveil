# Installation des composants matériels

Ce document décris la liste des devices à installer dans les différentes configurations matérielles du réveil.

La version actuelle a été validée sur la version du noyau Linux 3.18.11+ sur les Raspberry Pi B et Raspberry Pi B+.

Avant toute chose il est important de mettre à jour le raspberry avec la commande **`sudo  rpi-update`** et redémarrer **`sudo reboot`**

Les étapes suivantes peuvent être déroulées dans n'importe quel ordre.


## Activation du bus I2C (inter integrated circuits)

L'I2C est utilisé pour piloter les afficheurs 7 segments. Sa mise en oeuvre est décrite dans le document : [I2C Configuration](hardware-i2c.md)


## Configuration de la clef wifi TP-Link TL-WN725N

Ce dongle n'est pas prévu initialement pour fonctionner sur Raspberry, mais des drivers ont été développés à cet effet. Néanmoins ces drivers sont dépendant de la version du noyau sur laquelle ils tournent, et peuvent devenir incompatible après une mise à jour du raspberry.

La procédure de configuration est donnée dans le document : [TP-Link TL-WN725N Wifi dongle configuration](hardware-wifi.md)


## Autres commandes utiles

* **`sudo raspi-config`** : Configuration du Raspberry.
* **`sudo dpkg-reconfigure tzdata`** : Reconfiguration de la time zone.
* **`dmesg`** : Affiche le journal de boot.
* **`sudo reboot`** : Redémarre le raspberry.