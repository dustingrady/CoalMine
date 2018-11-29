# Coal Mine
![Canary Image](https://i.imgur.com/Ulxjv05.png)

Coal Mine is a tool that checks various VPN providers [Canary notices](https://en.wikipedia.org/wiki/Warrant_canary) and reports any changes that have been found back to the user.

---

**Supported Platforms**:
- Linux
- Windows

---

**Supported VPNs**:
- Nord
- VPNSecure
- Lokun
- SlickVPN
- IVPN
- Proxy.sh

---

**To run** (I'll streamline this at some point):
- Clone project
- Install dependencies
- Add _canary.py_ to a cronjob or scheduled task (notes below)
---

**Usage Examples**:
>python canary.py -nord

>python canary.py -slickvpn

>python canary.py -proxy.sh

---

**Notification Examples** (hopefully you never see these):

**Linux**:

![Linux Alert](https://i.imgur.com/fdM5caR.png)


**Windows**:

![Windows Alert](https://i.imgur.com/ot59THn.png)

---

**Notes on adding as chronjob**:

Because cronjobs use a different DISPLAY variable by default, you may not see the notifications displayed.

In this case, you will need to export your current env vars using [this method](https://askubuntu.com/questions/978382/how-can-i-show-notify-send-messages-triggered-by-crontab) so that cron can display the notifications properly.

For a list of supported environments, [click here](https://github.com/pa4080/cron-gui-launcher#supportedtested-desktop-environments).


[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=W2FJJJAM7EESC&item_name=Development+efforts/+coffee+fund&currency_code=USD&source=url)
