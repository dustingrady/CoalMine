# Coal Mine
![Canary Image](https://i.imgur.com/JRsJ8Q1.png)

Coal Mine is a tool that checks various VPN/ service providers [Canary notices](https://en.wikipedia.org/wiki/Warrant_canary) and reports any changes that have been found back to the user.

---

**Supported Platforms**:
- Linux
- Windows
- Mac

---

**Supported VPNs/ service providers**:
- [Nord](https://nordvpn.com/)
- [VPNSecure](https://www.vpnsecure.me/)
- [SlickVPN](https://www.slickvpn.com/)
- [IVPN](https://www.ivpn.net/)
- [Proxy.sh](https://proxy.sh/)
- [Proton](https://protonvpn.com/)
- [Spyoff](https://www.spyoff.com/)
- [Azire](https://www.azirevpn.com/)
- [Liquid](https://www.liquidvpn.com/)
- [Ace](https://www.acevpn.com/)
- [Cloudflare](https://www.cloudflare.com/)
- [VPNHT](https://vpn.ht/)

---

**To run** (I'll streamline this at some point):
- Clone project
- Install dependencies
- Add _canary.py_ to a cronjob or scheduled task (notes below)
---

**Example Usage**:
>python canary.py -nord

>python canary.py -proton

>python canary.py -proxy.sh

---

**Notification Examples** (hopefully you never see these):

**Linux**:

![Linux Alert](https://i.imgur.com/FVpYt66.png)


**Windows**:

![Windows Alert](https://i.imgur.com/12P3WGv.png)


**Mac**:

![Mac Alert](https://i.imgur.com/DGNhLVh.png)

---

**Notes on adding as chronjob**:

Because cronjobs use a different DISPLAY variable by default, you may not see the notifications displayed.

In this case, you will need to export your current env vars using [this method](https://askubuntu.com/questions/978382/how-can-i-show-notify-send-messages-triggered-by-crontab) so that cron can display the notifications properly.

For a list of supported environments, [click here](https://github.com/pa4080/cron-gui-launcher#supportedtested-desktop-environments).

---


**Potential Enhancements**:
- Multi-flag support
- PGP signature support

---


[![paypal](https://i.imgur.com/wsX84nD.png)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=W2FJJJAM7EESC&item_name=Development+efforts/+coffee+fund&currency_code=USD&source=url)