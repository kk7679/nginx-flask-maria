FROM phpmyadmin/phpmyadmin
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y vim locales
RUN locale-gen ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LC_CTYPE ja_JP.UTF-8
RUN localedef -f UTF-8 -i ja_JP ja_JP.utf8
