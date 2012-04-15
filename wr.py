import weechat

weechat.register('wr', 'BullShark and jtruant', '0.1', 'GPL3', 'Wakes the Room!', '', 'UTF-8')

def wake_room():
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
hook = weechat.hook_command("wakeroom", "Brings a dead IRC channel back to life!","","","","wake_room","")
