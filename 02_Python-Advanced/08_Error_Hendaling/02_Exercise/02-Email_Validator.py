class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


VALID_DOMAINS = ["org", "com", "org", "bg"]
line = input()

while line != "End":
    email = line
    if "@" not in email:
        raise NameTooShortError("Email must contain @")
        break
    name, domain = email.split("@")
    mail_host, net_domain = domain.split(".")
    if len(name) < 5:
        raise NameTooShortError("Name must be more than 4 characters")
        break

    if net_domain not in VALID_DOMAINS:
        raise NameTooShortError(f"Domain must be one of the folowing: {', '.join(VALID_DOMAINS)}")
        break

    print("Email is valid")
    line = input()