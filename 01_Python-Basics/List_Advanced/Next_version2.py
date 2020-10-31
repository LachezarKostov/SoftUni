old_version = input().split(".")

old_version = int("".join(old_version))+1

new_version = (".".join(str(old_version)))

print(new_version)