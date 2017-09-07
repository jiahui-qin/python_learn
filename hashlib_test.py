db = {
    'michael': 'cfeabd61deae09348d7969f5f5cda033',
    'bob': 'e2cc770e507e9a3802440ef8b869067b',
    'alice': 'df2cda8ca01e9b68220f43db60ebc1c7'
}
import hashlib
def login(user, password):
    md5 = hashlib.md5()
    newline=password+user+'fuckyou'
    md5.update(newline . encode('utf-8'))
    if user in db: ##dict的使用方法不是很熟悉
    ##检验一个字典里是否有一个key的两种方法
    ##第一个是用 in 来判断
    ##第二个是用 get 方法来判断
        if db[user] == md5.hexdigest():
            print('pass')
        else:
            print('error password')
    else:
        print('error user')

login('michael', '123456')

# ##先计算salt之后的md5
# def register(username, password):
#     md5 = hashlib.md5()
#     newline = password+username+'fuckyou'
#     md5.update(newline . encode('utf-8'))
#     return(md5.hexdigest())
# print(register('michael','123456'))
# print(register('bob' , '88888'))
# print(register('alice','password'))