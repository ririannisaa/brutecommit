import os

# Number of days you want to make commits
for i in range(0, 365*1 + 0):
    d = str(i) + ' day ago'
    # Open a text file and modify it
    with open('bot.txt', 'a') as file:
        file.write(d)
    # Add bot.txt to staging area
    os.system('git add bot.txt')
    # Commit it
    mydate = str(i) + ' day ago'
    os.system('git commit --date="' + mydate + '" -m "first commit"')
    os.system('git commit --date="' + d + '" -m "second commit"')

# push the commit to github
os.system('git add .')
os.system('git commit -am "last commit"')
os.system('git push -u origin main')
