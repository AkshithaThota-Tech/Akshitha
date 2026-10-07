def register_user(username,role="user",*permissions,**details):
    print(f"Username:{username}")
    print(f"Role:{role}")
    print(f"permissions:{permissions}")
    print(f"details:{details}")
register_user("Akshitha","Reading","writing","listening",)