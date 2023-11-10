import instaloader
import getpass

file = open("followers.txt", "r")
old_followers = []
for line in file:
    old_followers.append(line)
file.close

L = instaloader.Instaloader()
username = input("Enter your username: ")
pasword = input("Enter your pasword: ")

L.login(username, pasword)
print("you are login was seccessfuly")

profile = instaloader.Profile.from_username(L.context, "nasim_mhmadi")

new_followers = []
for follower in profile.get_followers():
    new_followers.append(follower)

for old_follower in old_followers:
    if old_follower not in new_followers:
        print(old_follower)

file = open("followers.txt", "w")
for follower in new_followers:
    file.write(follower + "\n")
file.close()