#
# Copyright (C) 2012 Christopher Lemire <christopher.lemire@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
# Brings a dead channel back to life!
# 
# Use with caution where acceptable.
# This script is effective at bringing my channel back to life.
# Create alias /wakeup if you like.
#
# History at:
#   https://github.com/BullShark/WakeUp
#


import weechat

if weechat.register('wakeup', 'BullShark and Dr_Krieger', '1.0', 'GPL3', 'Wakes the Room!', '', 'UTF-8'):
  weechat.hook_command("wakeup", "Brings a dead IRC channel back to life!","","","","wake_room","")

def wake_room(data, buffer, args):
  server = weechat.buffer_get_string(weechat.current_buffer(), 'localvar_server')
  channel = weechat.buffer_get_string(weechat.current_buffer(), 'localvar_channel')
  infolist = weechat.infolist_get('irc_nick', '', server + ',' + channel)
  nicklist = ''
  while weechat.infolist_next(infolist):
    nicklist += weechat.infolist_string(infolist, 'name')
    nicklist += ' '
  weechat.command(weechat.current_buffer(), nicklist)
  weechat.infolist_free(infolist)
  return weechat.WEECHAT_RC_OK
