def build_username(first, last, year=""):
    username = first.lower() + "." + last.lower()
    if year != "":
        username = username + str(year)

    return username

print(build_username("Aysel", "Mammadova"))       
print(build_username("Kamran", "Aliyev", 2005))
