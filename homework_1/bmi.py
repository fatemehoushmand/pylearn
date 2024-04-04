kg = float(input('chamnd kg?'))
m = float(input('chand metr?'))


bmi= kg/(m**2)
print(bmi)


if bmi<18.5:
    print('under weight')
elif 18.5<bmi<24.9:
    print('normal weight')
elif 25<bmi<29.9:
    print('over weight')
elif 30<bmi<34.9:
    print('obesity')
elif 35<bmi<39.9:
    print('extreme obesity')