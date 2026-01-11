# check if the post is talking about the given name

post = input("Enter your post: ")
name = input("Enter name that you want to check: ")

if(name.lower() in post.lower()):
    print("this post is talking about that name")
else:
    print("this post is not talking about that name ")