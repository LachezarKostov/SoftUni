# You will be receiving lines with commands until you receive the "Log out" command.  There are four possible commands:
#
likes = {}
comments = {}

while True:
    command = input()
    if command == "Log out":
        break

    command = command.split(": ")
    username = command[1]
# "New follower: {username}":
# Add the username, to your records (with 0 likes and 0 comments). If person with the given username already exists ignore the line.
    if command[0] == "New follower":
        if username not in likes:
            likes[username] = 0
            comments[username] = 0
# "Like: {username}: {count}":
# If the username doesn't exist, add it to your records with the given count of likes.
# If the username exist, increase the count of likes with the given count.
    elif command[0] == "Like":
        new_likes = int(command[2])
        if username not in likes:
            likes[username] = 0
            comments[username] = 0
        likes[username] += new_likes
# "Comment: {username}":
# If the username doesn't exist, add it to your records with 1 comment.
# If the username exists, increase the count of commens with 1.
    elif command[0] == "Comment":
        if username not in likes:
            likes[username] = 0
            comments[username] = 0
        comments[username] += 1
# "Blocked: {username}":
    # Delete all records of the given username. If it doesn’t exist, print:
    #  "{Username} doesn't exist."
    elif command[0] == "Blocked":
        if username not in likes:
            print(f"{username} doesn't exist.")
        else:
            likes.pop(username)
            comments.pop(username)
# In the end, you have to print the count of followers,
# each follower with his/her likes and comments (the sum of likes and comments)
# sorted in descending order by the likes and then by their username in ascending order in the following format:
# {count} followers
# {username}: {likes+comments}
# {username}: {likes+comments}
# ...
likes = dict(sorted(likes.items(), key=lambda item: (-item[1], item[0])))
print(f"{len(likes)} followers")
for users, likes in likes.items():
    print(f"{users}: {likes+comments[users]}")