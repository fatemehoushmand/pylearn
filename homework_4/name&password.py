import qrcode

# name =input('please enter your name: ')
img = qrcode.make(input('please enter your name: '))
img.save('my_first_qrcode.png')
# password = int(input('please enter your pass: '))
img2 = qrcode.make(int(input('please enter your pass: ')))
img2.save('my_second_qrcode.png')
