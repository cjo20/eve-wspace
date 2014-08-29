#    Eve W-Space
#    Copyright (C) 2013  Andrew Austin and other contributors
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version. An additional term under section
#    7 of the GPL is included in the LICENSE file.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
from core.models import ConfigEntry
import random
import string
#defaults = [("TEST_SETTING", "BOB")]
defaults = [
        ("JABBER_FROM_JID", "announce@localhost"),
        ("JABBER_FROM_PASSWORD", ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(15))),
        ("JABBER_LOCAL_SPACE_CHAR", "_"),
        ("JABBER_LOCAL_DOMAIN", "localhost"),
        ("JABBER_LOCAL_ENABLED", "0"),
        ("SLACK_TOKEN", ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(24))),
        ("SLACK_SUBDOMAIN", "SLACK"),
        ]

def load_defaults():
    for setting in defaults:
        config = ConfigEntry.objects.get_or_create(name=setting[0], user=None)[0]
        config.value = setting[1]
        config.save()
