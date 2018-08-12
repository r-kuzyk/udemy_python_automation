MENU_PROMPT = "Enter 'c' to create blog, 'l' to list blogs, 'r' to read, 'p' to create post, 'q' to quit"
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
    pass


def ask_read_blog():
    pass


def ask_create_post():
    pass