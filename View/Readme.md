This folder contains the view elements of application.
-----------------------------------------------------

Point domain to index.html using nginx \
Point domain/api to 127.0.0.1:8000(Django server) using nginx


### Folder structure: ###
* Css folder contains all stylesheet elements.
* Scss folder contains Scss components
* js folder contains all javascript files.
* config folder contains config files for nginx

### Scss ###
To use scss first install ruby-sass package( * sudo apt install ruby-sass * / * sudo pacman -S ruby-sass* ). Then run * sass --watch Scss/master.scss:Css/master.css *
