# XiaomiADBFastbootTools
Ceci est une alternative à l'outil Java, bien que sans interface graphique pour le moment, il permet de désinstaller les services MIUI de votre choix.

# Liste de Bloatware
La liste de bloatware cités dans main.py viennent du site : https://technastic.com/xiaomi-bloatware-list-miui/


# Préparation de l'exécution
Avant d'exécuter le script, assurez-vous que votre téléphone est connecté au PC via un câble USB, que le débogage USB est activé dans les paramètres et que vous avez autorisé votre PC à utiliser le débogage USB avec votre téléphone. Vous pouvez vérifier si votre téléphone est détecté en utilisant adb devices.
Dans mon cas, j'utilise Archlinux.
J'ai donc installé adb en utilisant : yay -S android-tools

# Activation du débogage USB dans MIUI
Pour activer le débogage USB dans MIUI, vous devez tout d'abord activer les options de développement. Pour ce faire, allez dans les paramètres > à propos du téléphone et cliquez 7 fois sur "MIUI version". Ensuite, revenez à la page principale des paramètres et allez dans les paramètres avancés. Faites défiler vers le bas et vous devriez voir les options de développement. Ouvrez les options développeur et faites défiler vers le bas jusqu'à l'option "débogage USB". Activez-la.

# Démarrage
Il suffit de télécharger le fichier depuis mon github, d'exécuter .sh sur votre distro Linux.

# Dans mon cas, ces services sont déjà désinstallés.
![image](https://github.com/ELEDANTEC/XiaomiADBFastbootTools/assets/134450385/cab88553-8af9-413d-80ff-d1335936cbd6)


Par ailleurs, il existe également un outil universel et graphique, open source, permettant de désinstaller les services, sans rooter son téléphone.
# [https://technastic.com/universal-android-debloater-best-bloatware-remover/] Le tutoriel de celui-ci
# (https://github.com/0x192/universal-android-debloater/releases) Sa source

La préparation de ce dernier se fait de la même façon, simplement il est compatible avec toute android ayant le débogage USB.

N'hésitez pas à me faire un retour sur mon portfolio ! 
