import weechat

if weechat.register('wr', 'BullShark and Dr_Krieger', '1.0', 'GPL3', 'Wakes the Room!', '', 'UTF-8'):
  weechat.hook_command("wr", "Brings a dead IRC channel back to life!","","","","wake_room","")

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
