# Druckspatz
This is initially used to print tweets via a little thermor printer in an exhibition. It's running on a raspberry pi with Python 3.5.2. Using [TwitterAPI](https://github.com/geduldig/TwitterAPI) to access twitter's api. It then generates a tweet.html file with Jinja2 2.8 as  template engine. From this a pdf is generated using PDFKit 0.5 which is a python wrapper for wkhtmltopdf 0.9.9. The resulting PDF is then printed via  the lpr command.

[Driver for Thermo Printer](https://github.com/klirichek/zj-58)

[Tutorial to get Thermoprinter running](http://scruss.com/blog/2015/07/12/thermal-printer-driver-for-cups-linux-and-raspberry-pi-zj-58/)


# Usage
python3 druckspatz.py '#tag' <searchTerm ...>.

If no search terms are given the script terminates.

# Example
python3 druckspatz.py ‘#muffins’ ‘#butterMuffins’ butterMuffins