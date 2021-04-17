#!/bin/bash
rm -r data
rm -r tmp

mkdir data
COUNTRY='ES'
for year in $(seq 1975 2019); do
    mkdir tmp
    if [ $year -lt 2009 ]; then
        wget "https://ine.es/ftp/microdatos/mnp_defun/datos defuncio${year:2:4}.zip"
        7z x "datos defuncio${year:2:4}.zip" -o./tmp
        mv tmp/* data/DEF$COUNTRY$year
    else
        prefix=""
        if [ $year -lt 2012 ]; then prefix="/sin"; fi
        wget "https://ine.es/ftp/microdatos/mnp_defun$prefix/datos_$year.zip"
        if [ $year -eq 2014 ]; then
            7z x "datos_$year.zip" -o./tmp
            7z x "tmp/datos_defunciones_ nivel_ educativo14.zip" -o./tmp
            mv "tmp/Anonimizado Defunciones nivel educativo sin causaA2014.TXT" data/DEF$COUNTRY$year
        else 
            7z x "datos_$year.zip" -o./tmp
            if [ $year -eq 2019 ]; then
                mv "tmp/DEFUNsincm.ANONIMI.A2019.ESTPR.txt" data/DEF$COUNTRY$year
            else
                mv tmp/* data/DEF$COUNTRY$year
            fi
        fi
    fi

    rm *.zip
    rm -r tmp
done