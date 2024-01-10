## Flask
> Topic of Focus, Babel

Flask-Babel is an extension to Flask that adds i18n and l10n support to any Flask application with the help of babel, pytz and its own copy of speaklater. It has built-in support for date formatting including timezones, as well as a very simple and friendly interface to gettext translations.

### Installation

```pip install Flask-Babel```


### Config

```
from flask import Flask
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

```