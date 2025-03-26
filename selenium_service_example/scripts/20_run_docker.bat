docker run --name check_site --rm -it ^
    -e DB_HOST=bookaspace-production.caggdcgcgdrb.eu-central-1.rds.amazonaws.com ^
    -e DB=BookASpace ^
    -e USER=AndrewHr ^
    -e PASS=fsjidfj19_jfj11sh^
    -e CHROMEDRIVER_PATH=/usr/local/bin/chromedriver ^
    check_site
