from blog import Blog

MENU_PROMPT = "Enter 'c' to create blog, 'l' to list blogs, 'r' to read, 'p' to create post, 'q' to quit"
POST_TEMPLATE = '''
--- {} ---

{}

    '''

blogs = dict() # blog_name : Blog object


def menu():
    # Show the user the available blogs
    # Let the user make a choice
    # Do something with that choice
    # Eventually exit

    print_blogs()
    selection = input(MENU_PROMPT)
    with selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)


def print_blogs():
    # Print the available blogs.items()
    for key, blog in blogs.items():
        print("- {}".format(blog))


def ask_create_blog():
    blog_title = input("Eneter blog title: ")
    blog_author = input("Enter blog author: ")
    blogs[blog_title] = Blog(blog_title, blog_author)


def ask_read_blog():
    blog_title = input("Eneter blog title: ")
    print_posts(blogs[blog_title])


def print_posts():
    for post in blog.posts:
        print_posts(post)


def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))


def ask_create_post():
    blog_title = input("Eneter blog title: ")
    post_title = input("Eneter post title: ")
    post_content =  input("Eneter post content: ")
    blogs[blog_title].create_post(post_title, post_content)
