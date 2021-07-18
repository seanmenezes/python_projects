# stack implementation in python
# summary
# add item on top of the stack - browsing_session.append()
# remove item on top of the stack - browsing_session.pop()
# if not browsing_session if stack is not empty
# get item on top of the stack - browsing_session[-1]
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
print('popping')
last = browsing_session.pop()
print(last)
print('after popping')
print(browsing_session)
print("redirect",browsing_session[-1])

if not browsing_session:
    print("disable")

