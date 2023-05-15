import itchat

def send_message_to_group(message, group_name):
    itchat.auto_login()
    group = itchat.search_chatrooms(name=group_name)
    if group:
        group_username = group[0]['UserName']
        itchat.send(message, toUserName=group_username)
    else:
        print("未找到群聊：" + group_name)

if __name__ == '__main__':
    # 在这里填写你要发送的消息和微信群的名称
    message = "测试!"
    group_name = "微信群名称"

    send_message_to_group(message, group_name)
