docker run --name check_site --rm -it ^
    -e DB_HOST=test-production.caggdcgcgdrb.eu-central-1.rds.amazonaws.com ^
    -e DB=Test ^
    -e USER=user ^
    -e PASS=fsjidfj19_jfj11sh^
    -e CHROMEDRIVER_PATH=/usr/local/bin/chromedriver ^
    check_site
