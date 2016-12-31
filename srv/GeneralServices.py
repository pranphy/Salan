#!/usr/bin/env python3

import gettext

def setLocale(locale='en'):
    gettext.bindtextdomain('messages','./i18n')
    gettext.textdomain('messages')

    lang = gettext.translation('messages','./i18n',languages=[locale])
    lang.install()
    print('locale changed')

