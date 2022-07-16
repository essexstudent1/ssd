# README File

### _How to run the code using Codio:_

1. Go to the Codio box at: [https://codio.co.uk/kpeuhkurinen/ssd](https://codio.co.uk/kpeuhkurinen/ssd)
2. Open Terminal and pull the latest code:
   - git pull origin
   - cd django01/ssd
   - python3 manage.py makemigrations
   - python3 manage.py migrate
   - Run server: python3 manage.py runserver 0.0.0.0:8000
3. Open a browser and surf to: [https://freddieblue-romanpablo-8000.codio-box.uk/](https://freddieblue-romanpablo-8000.codio-box.uk/)
### _How the website works:_

When accessing the website a login and register option is available, as well as additional information (who runs it, what the organisation provides). The registration process requires an email, password (including confirmation), full name, address, and a security question that only the user knows the answer to. For an already existing user, the login requires the email provided and password. It then asks the user for the answer to the security question that was selected in the registration process. The password is hashed and salted for security purposes. 

### _Differences:_

**Functionalities:**

The web application initially aimed to include the following functionalities:
- The website will:
  - Provide latest cybersecurity news, alerts, allowing subscriptions.
  - Allow organisations to register, report, and manage security incidents.
  - Allow individuals to register, report, and manage GDPR breaches.

Due to tight schedules, this web application did not include all functionalities. As a result, functionalities such as: alerting users for new breaches and for users to manage them  have been excluded and postponed. It is currently a website specifically for allowing users/organisations to register, login, and view/report data breaches.

**2FA:**

Instead of using an one-time-password (OTP) as a 2FA security method as mentioned in the design document, a security question was used as an additional authorisation process when logging in. This was due to complications which shortened the period of time left for finalising the assessment.


### _Future Features:_

- For a higher level and an additional layer of security, it is strongly recommended that a 2FA method is integrated into the login process. One secure method of achieving a 2FA approach is the use of OTPs (Eldefrawy, et. al., 2011). These can be either sent to a mobile device via SMS or an application scanning a QR code such as Google Authenticator.

- As discussed in the design document, the web application will allow users/organisations to manage the reported GDPR breaches and security incidents, and alert them about newly reported breaches.

### _References:_

Eldefrawy, M. H., Alghathbar, K. & Khan, M. K. (2011) ‘OTP-Based Two-Factor Authentication Using Mobile Phones’, _2011 Eighth International Conference on Information Technology: New Generations_. Las Vegas, Nevada, USA. 11-13 April New York: IEEE. 327-331.
 
 
