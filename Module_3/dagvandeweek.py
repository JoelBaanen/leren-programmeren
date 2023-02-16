vraag = input('welke dag is het?')
week_list = ['ma','di','wo','do','vr','za','zo']
while vraag != week_list[0]:
    print(week_list[0])
    week_list.pop(0)

