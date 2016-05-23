#!/bin/bash

if [[ "$(ls /usr/bin/)" == *pluma* ]]; 
then
      gsettings set org.mate.pluma active-plugins "['docinfo', 'time', 'modelines', 'filebrowser']"
      gsettings set org.mate.pluma auto-detected-encodings "['UTF-8', 'WINDOWS-1251', 'CURRENT', 'ISO-8859-15', 'UTF-16']"
      gsettings set org.mate.pluma auto-indent "true"
      gsettings set org.mate.pluma auto-save "true"
      gsettings set org.mate.pluma bracket-matching "true"
      gsettings set org.mate.pluma color-scheme "oblivion"
      gsettings set org.mate.pluma display-line-numbers "true"
      gsettings set org.mate.pluma display-right-margin "true"
      gsettings set org.mate.pluma editor-font "Monospace 10"
      gsettings set org.mate.pluma highlight-current-line "true"
      gsettings set org.mate.pluma insert-spaces "true"
      gsettings set org.mate.pluma use-default-font "false"
      gsettings set org.mate.pluma wrap-mode "GTK_WRAP_NONE"
else
      echo "Pluma не найдено."
fi

sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo /etc/init.d/gunicorn restart
