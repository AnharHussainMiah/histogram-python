#Name:      histogram-python
#Author:    Ethan Dunford
#Email:     ethan@ethandunford.com
#Version:   1.0
#histogram
# take list
#output the count of how many times a item appears.

orginal = ['cat','dog','fish','cat']
unique = set(orginal)
for u in unique:
    counter = 0
    for o in orginal:
        if o == u:
            counter += 1
    print "%s appears %s times" % (u,counter)
