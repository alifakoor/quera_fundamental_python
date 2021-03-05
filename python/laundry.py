n, m = map(int, input().split())
towls = [0] * n
techi = ['no assign'] * m
end = False
result = ''
while (not end):
    command = input()
    if command == 'put an end to my misery':
        # end = True
        break
    else:
        command = command.split()
        tech_guy = int(command[0])-1
        if command[1] == 'track':
            towl_number = int(command[2])-1
            techi[tech_guy] = towl_number
        elif command[1] == 'dry':
            if techi[tech_guy] == 'no assign':
                result += 'no towel has been assigned to me. \n'
            else:
                degree_dry = int(command[2])
                degree_towl = towls[techi[tech_guy]]
                if degree_dry > degree_towl:
                    towls[techi[tech_guy]] = 0
                else:
                    towls[techi[tech_guy]] = degree_towl - degree_dry
        elif command[1] == 'give':
            if techi[tech_guy] == 'no assign':
                result += 'no towel has been assigned to me. \n'
            else: 
                if towls[techi[tech_guy]] == 0:
                    result += 'ok \n'
                    towls[techi[tech_guy]] = 10
                else:
                    result += 'impossible \n'
        else:
            if techi[tech_guy] == 'no assign':
                result += 'no towel has been assigned to me. \n'
            else:
                result += str(towls[techi[tech_guy]])
print(result)
