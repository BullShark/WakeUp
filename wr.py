import weechat

weechat.register('wr', 'BullShark and jtruant', '0.1', 'GPL3', 'Wakes the Room!', '', 'UTF-8')
server = weechat.buffer_get_string(weechat.current_buffer(), 'localvar_server')
channel = weechat.buffer_get_string(weechat.current_buffer(), 'localvar_channel')
infolist = weechat.infolist_get('irc_nick', '', server + ',' + channel) 
nicklist = ''
#while weechat.infolist_next(infolist):
#   nicklist += weechat.infolist_string(infolist, 'name')
#   nicklist += ' '

def wake_room(data, buffer, args):
   return weechat.WEECHAT_RC_OK

# hook prototype
#hook = weechat.hook_command(command, description, args, args_description,
#completion, callback, callback_data)
hook = weechat.hook_command("wakeroom", "Brings a dead IRC channel back to life!","","","","wake_room","")

weechat.command(weechat.current_buffer(), nicklist)
weechat.infolist_free(infolist)

