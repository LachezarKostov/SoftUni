company_and_id = input()
company_with_id = {}

while company_and_id != "End":
    company, id = company_and_id.split(" -> ")

    if company not in company_with_id:
        company_with_id[company] = []

    if id not in company_with_id[company]:

        company_with_id[company].append(id)

    company_and_id = input()

sort_company = dict(sorted(company_with_id.items(), key=lambda x: (x[0])))

for company, ids in sort_company.items():
    print(company)
    for id in ids:
        print("--", id, end="\n")