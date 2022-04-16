# Fire Alarm
Supplies
- ESP8266 NodeMCU x 1
- Flame Sensor x 1
- MQ2 Smoke Sensor x 1
- Jumper cables
- Breadboard

### Environment Setup
Connect the NodeMCU with Power Supply.  
Provide Wifi with given Credentials.  

# FIRE ALARM SYSTEM SETUP
![image](https://user-images.githubusercontent.com/58547392/162053442-6ade2656-c305-4e15-a093-86ec1596679b.png)

# VIDEO LINK:
Part1:
https://drive.google.com/file/d/1tXmzTGrdy4QsYJSJ6KGYUhSOk_rmQR76/view?usp=sharing \
Part2:
https://drive.google.com/file/d/1aLFdjgRMifjsO5URJTRmNAkVEUaaAyxI/view?usp=sharing


### Working of the Code
Since code already flashed in the microcontroller hence It will sense data from the sensors and send It to spreadsheet through the Internet and update the spreadsheet in real time, Afterwards from spreadsheet we will send it to Firebase server and through that we will be showing on the WebApp and triggering Alarm.

## Installation


Create/Activate virtual environment

```sh
pip install virtualenv
virtualenv myproject
(go to myproject) \Scripts\activate
```

Installing Dajngo

```sh
pip install django
```

Clone Github Project


Install Dependencies
```sh
(go to requirements directory) pip install -r requirements.txt
```

## Run Project
```sh
 python manage.py runserver
```


