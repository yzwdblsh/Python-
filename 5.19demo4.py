while True:

    def IDCard(info_dict=None):
        name = input("请输入姓名：")

        phone = input("请输入电话号码：")

        email = input("请输入邮箱：")

        info_dict[name] = {'电话': phone, '邮箱': email}
        return info_dict


    saved_dict = {}

    while True:
        saved_dict = IDCard(saved_dict)
        more = input("是否继续输入信息？(是/否): ")
        if more.lower() == '否':
            break

    # 打印保存的字典
    print("保存的名片:", saved_dict)
