import sys
import datetime
f = open('errors.txt','a')

clients = [{
    'id': 1,
    'phone': '+99200000001',
    'email': 'test@test.com',
},
{
    'id': 2,
    'phone': '+99200000002',
    'email': 'test@test.com',
}]

payments = [{
    'id': 23,
    'product': 'testBuy',
    'price': 100,
    'clientId': 1,
},
{
    'id': 24,
    'product': 'testBuy2',
    'price': 100,
    'clientId': 2,
}]

def sendMessage(client,payment):
    str = '\n Спасибо за заказ!!!\n Номер вашего заказа: {0}\n Продукт: {1}\n Стоимость: {2}'.format(payment['id'],payment['product'],payment['price'])
    print(str)
def messageForOperator(client,payment,type):
    print('\n Успех,\n Вы отправили уведомление с помощью {}\n Номер заказа: {}\n ID Клиента: {}\n Номер телефона: {}\n email-адресс: {}'.format(type,payment['id'],client['id'],client['phone'], client['email']))

def main():
    args = sys.argv
    helpMessage = 'Пожалуйста ознакомьтесь с флагом -help или -h '
    nowTime = str(datetime.datetime.now()) + '\n'
    if len(args) == 1:
        print(helpMessage + nowTime)
        return
    if args[1].lower()=='-help' or args[1].lower()=='-h':
        print('Пример для команды: Buy-Event.py -sms 23\n Buy-Event.py flag1 flag2\n flag1 \n Для отправки  СМС:\n -sms \n -s \n Для отправки email: \n -email \n -e \n flag2 \n Пренимает номер Заказа (Целые числа)')
        return
    if len(args) != 3:
        print(helpMessage + nowTime)
        f.write(helpMessage + nowTime)
        return
    else:
        flags = ['-sms','-s','-email','-e']
        flag1, flag2 = args[1],args[2]
        try: flag2 = int(flag2)
        except:
            f.write(helpMessage + '\nflag2 принимает целые числа ' + nowTime)
            print(helpMessage + '\nflag2 принимает целые числа ' + nowTime)
            return
        if flag1.lower() in flags:
            payment = list(filter(lambda x: x['id']==flag2, payments))
            if len(payment) != 1:
                f.write('Payment not found {}\n'.format(nowTime))
                print('Payment not found {}\n'.format(nowTime))
                return
            else:
                payment = payment[0]
                client = list(filter(lambda x: x['id']==payment['clientId'],clients))
                if len(client) != 1:
                    f.write('Client not found {}\n'.format(nowTime))
                    print('Client not found {}\n'.format(nowTime))
                    return
                client = client[0]
                sendMessage(client,payment)
                type = '0'
                if flag1[:2].lower() == '-s':
                    type = 'SMS'
                if flag1[:2].lower() == '-e':
                    type = 'email'
                print(flag1[:2].lower())
                messageForOperator(client,payment,type)
        else:
            print('Type not found. ' + helpMessage)

if __name__ == '__main__':
    main()
