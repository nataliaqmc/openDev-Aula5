import gettext
import sys
import locale



gettext.bindtextdomain('cli', 'locale')
gettext.textdomain('cli')
_ = gettext.gettext
